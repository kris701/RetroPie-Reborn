import os
import subprocess
from enum import Enum

class IconManager(object):
    PngviewPath : str = "/usr/local/bin/pngview"
    PngviewCall=[PngviewPath, "-d", "0", "-b", "0x0000", "-n", "-l", "15000", "-y", "0", "-x"]
    IconOffset : int = 24
    Resolution : int = 500
    Margin : int = 5

    _processes : dict = {}
    
    def AddIcon(self, icon, name : str) -> None:
        print(name)
        if icon is "Hide":
            self.RemoveIcon(name)
        elif name not in self._processes:
            if os.path.exists(str(icon)):
                offset = self.Resolution - len(self._processes) * self.Margin
                self._processes[name] = subprocess.Popen(self.PngviewCall + [offset, str(icon)])
        
    def RemoveIcon(self, name : str) -> None:
        if name in self._processes:
            self._processes[name].kill()
            del self._processes[name]
            
    def ClearIcons(self) -> None:
        for name in self._processes:
            self.RemoveIcon(name);
