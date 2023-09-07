from enum import Enum

from ..BaseIconRunner import BaseIconRunner as BIR
from ...IconManager import IconManager as IM
from .BatteryIcons import BatteryIcons as WI

class BatteryIconRunner(BIR):
    IconName : str = "Battery"
        
    def Update(self, iconManager : IM) -> None:
        pass 