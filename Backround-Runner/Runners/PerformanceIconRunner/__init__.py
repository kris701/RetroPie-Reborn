from enum import Enum

from ..BaseIconRunner import BaseIconRunner as BIR
from ...IconManager import IconManager as IM
from .PerformanceIcons import PerformanceIcons as WI

class PerformanceIconRunner(BIR):
    IconName : str = "Perf"
        
    def Update(self, iconManager : IM) -> None:
        pass 