import os
import subprocess
from enum import Enum
import sys
from PIL import Image

class IconManager(object):
    PngviewPath : str = "/usr/local/bin/pngview"
    PngviewCall=[PngviewPath, "-d", "0", "-b", "0x0000", "-n", "-l", "15000", "-y", "0", "-x"]
    IconOffset : int = 24
    Resolution : int = 1024
    Margin : int = 5

    _currents : dict = {}
    _changed : bool = False

    def Update(self) -> None:
        if self._changed == False:
            return
        
        print("update")
        self._process.terminate()
        self._process.wait();
        
        images = []
        for name in self._currents:
            images.append(Image.open(self._currents[name]))
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
          new_im.paste(im, (x_offset,0))
          x_offset += im.size[0]

        new_im.save('temp.png')
            
        offset = self.Resolution - len(images) * (self.Margin + self.IconOffset)
        self._process = subprocess.Popen(self.PngviewCall + [str(offset), str("temp.png")])

        self._changed = False
    
    def AddIcon(self, icon, name : str) -> None:
        if str(icon) is "Hide":
            self.RemoveIcon(name)
        elif name not in self._currents:
            if os.path.exists(str(icon)):
                self._currents[name] = icon
                self._changed = True
        
    def RemoveIcon(self, name : str) -> None:
        if name in self._currents:
            self._currents.pop(name)
            self._changed = True
            
    def ClearIcons(self) -> None:
        for name in self._currents:
            self.RemoveIcon(name);
