from enum import Enum
import subprocess

from .DownloadingIcons import DownloadingIcons as DI

class DownloadingIconRunner():
    IconName : str = "Downloading"

    _cmd = "ifstat 0.5s 1 | awk 'NR==3 {print $1}'"

    _currentState : DI = DI.Hide
    def Update(self, iconManager) -> None:
        newState = DI.Hide
        downSpeed = self.GetDownloadSpeed()        
        if downSpeed > 500:
            newState = DI.Downloading
        if self._currentState != newState:
            self._currentState = newState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(newState, self.IconName)    
    
    def GetDownloadSpeed(self) -> float:
        try:
            downloaded_output = subprocess.check_output(self._cmd, shell=True, timeout=1)
            return float(downloaded_output)
        except Exception:
            return 0
    