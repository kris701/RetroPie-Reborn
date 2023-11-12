import os
import subprocess
from enum import Enum

class IconManager(object):
    PngviewPath : str = "/usr/local/bin/pngview"
    PngviewCall=[PngviewPath, "-d", "0", "-b", "0x0000", "-n", "-l", "15000", "-y", "0", "-x"]
    IconOffset : int = 24
    Resolution : int = 1024
    Margin : int = 5

    _processes : dict = {}
    
    def AddIcon(self, icon, name : str) -> None:
        if icon is "Hide":
            self.RemoveIcon(name)
        elif name not in self._processes:
            if os.path.exists(str(icon)):
                offset = self.Resolution - (self.Margin + self.IconOffset) - len(self._processes) * (self.Margin + self.IconOffset)
                self._processes[name] = subprocess.Popen(self.PngviewCall + [str(offset), str(icon)])
        
    def RemoveIcon(self, name : str) -> None:
        if name in self._processes:
            self._processes[name].kill()
            self._processes[name].wait();
            del self._processes[name]
            
    def ClearIcons(self) -> None:
        for name in self._processes:
            self.RemoveIcon(name);
