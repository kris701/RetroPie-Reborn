from enum import Enum
import subprocess
import re

from ..BaseIconRunner import BaseIconRunner as BIR
from ...IconManager import IconManager as IM
from .PerformanceIcons import PerformanceIcons as PI

class PerformanceIconRunner(BIR):
    IconName : str = "Perf"
    _envCmd="vcgencmd get_throttled"
    
    _currentState : PI = PI.Hide

    def Update(self, iconManager : IM) -> None:
        checkState : PI = self.GetFrequencyState()
        if checkState != self._currentState:
            self._currentState = checkState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(checkState, self.IconName)     
    
    def GetFrequencyState(self) -> float:
        state = PI.Hide
        val=int(re.search("throttled=(0x\d+)", subprocess.check_output(self._envCmd.split()).decode().rstrip()).groups()[0], 16)
        freqCap : bool = bool(val & 0x02)
        throttled : bool = bool(val & 0x04)
        if freqCap:
            state = PI.Capped
        if throttled:
            state = PI.Throttled
        return state
    