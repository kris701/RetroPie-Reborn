from enum import Enum
import subprocess
import re

from .UnderVoltageIcons import UnderVoltageIcons as UI

class UnderVoltageIconRunner():
    IconName : str = "Undervolt"
    _envCmd="vcgencmd get_throttled" 
    
    _currentState : UI = UI.Hide

    def Update(self, iconManager) -> None:
        checkState : UI = self.GetFrequencyState()
        if checkState != self._currentState:
            self._currentState = checkState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(checkState, self.IconName)     
    
    def GetFrequencyState(self) -> float:
        state = UI.Hide
        val=int(re.search("throttled=(0x\d+)", subprocess.check_output(self._envCmd.split()).decode().rstrip()).groups()[0], 16)
        underVoltaged : bool = bool(val & 0x01)
        if underVoltaged:
            state = UI.UnderVoltage
        return state
    