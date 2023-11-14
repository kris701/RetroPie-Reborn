from enum import Enum
import subprocess
import re

from .UnderVoltageIcons import UnderVoltageIcons as UI

class UnderVoltageIconRunner():
    IconName : str = "Undervolt"
    _envCmd="vcgencmd get_throttled" 
    
    _currentState : UI = UI.Hide

    def Update(self, iconManager) -> None:
        checkState : UI = self.GetUnderVoltageState()
        if checkState != self._currentState:
            self._currentState = checkState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(checkState, self.IconName)     
    
    def GetUnderVoltageState(self) -> float:
        state = UI.Hide
        try:
            throttled_output = subprocess.check_output(self._envCmd, shell=True)
            throttled_binary = bin(int(throttled_output.split(b'=')[1], 0)) 
            if throttled_binary[0] == '1':
                state = UI.UnderVoltage
        except Exception:
            return state
        return state
    