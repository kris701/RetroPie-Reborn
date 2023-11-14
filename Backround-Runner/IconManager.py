import os
import subprocess
from enum import Enum

class IconManager(object):
    PngviewPath : str = "/usr/local/bin/pngview"
    PngviewCall=[PngviewPath, "-d", "0", "-b", "0x0000", "-n", "-l", "15000", "-y", "0", "-x"]
    IconOffset : int = 24
    Resolution : int = 1024
    Margin : int = 5

    _currents : dict = {}
    _processes : dict = {}
    _changed : bool = False

    def Update(self) -> None:
        if self._changed == False:
            return
        
        for name in self._processes:
            self._processes[name].kill()
            self._processes[name].wait();
        self._processes = {}

        counter : int = 1
        for name in self._currents:
            offset = self.Resolution - counter * (self.Margin + self.IconOffset)
            self._processes[name] = subprocess.Popen(self.PngviewCall + [str(offset), str(self._currents[name])])
            counter += 1

        self._changed = False
    
    def AddIcon(self, icon, name : str) -> None:
        print("update")
        print(name)
        if icon is "Hide":
            self.RemoveIcon(name)
        elif name not in self._processes:
            if os.path.exists(str(icon)):
                self._currents[name] = icon
                self._changed = True
        
    def RemoveIcon(self, name : str) -> None:
        if name in self._processes:
            self._processes.pop(name)
            self._changed = True
            
    def ClearIcons(self) -> None:
        for name in self._processes:
            self.RemoveIcon(name);
