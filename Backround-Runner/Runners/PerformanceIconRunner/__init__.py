from enum import Enum
import subprocess
import re

from ..BaseIconRunner import BaseIconRunner as BIR
from ...IconManager import IconManager as IM
from .PerformanceIcons import PerformanceIcons as PI

class PerformanceIconRunner(BIR):
    IconName : str = "Perf"
        
    _envCmd="vcgencmd get_throttled"
    _currentState : PI = PI.OK

    def Update(self, iconManager : IM) -> None:
        checkState : PI = self.GetEnvironmentState()
        if checkState != self._currentState:
            self._currentState = checkState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(checkState, self.IconName)    
    
    def GetEnvironmentState(self) -> PI:
        val=int(re.search("throttled=(0x\d+)", subprocess.check_output(self._envCmd.split()).decode().rstrip()).groups()[0], 16)
        underVoltaged : bool = bool(val & 0x01)
        freqCap : bool = bool(val & 0x02)
        throttled : bool = bool(val & 0x04)
        
        stateValue : int = 0
        if underVoltaged:
            stateValue += 1;
        if freqCap:
            stateValue += 10;
        if throttled:
            stateValue += 100;

        return PerformanceIcons.GetIconFromValue(stateValue)

    
        
        