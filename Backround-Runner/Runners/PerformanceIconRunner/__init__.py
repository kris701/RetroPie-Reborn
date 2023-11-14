from enum import Enum
import subprocess
import re

from .PerformanceIcons import PerformanceIcons as PI

class PerformanceIconRunner():
    IconName : str = "Perf"
    _envCmd="vcgencmd get_throttled"
    
    _currentState : PI = PI.Hide

    def Update(self, iconManager) -> None:
        checkState : PI = self.GetFrequencyState()
        if checkState != self._currentState:
            self._currentState = checkState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(checkState, self.IconName)     
    
    def GetFrequencyState(self) -> float:
        state = PI.Hide
        try:
            throttled_output = subprocess.check_output(self._envCmd, shell=True, timeout=1)
            throttled_binary = bin(int(throttled_output.split(b'=')[1], 0)) 
            if throttled_binary[1] == '1':
                state = PI.Capped
            if throttled_binary[2] == '1':
                state = PI.Throttled
        except Exception:
            return state
            
        return state
    