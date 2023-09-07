from enum import Enum

from ..BaseIconRunner import BaseIconRunner as BIR
from ...IconManager import IconManager as IM
from .BluetoothIcons import BluetoothIcons as WI

class BluetoothIconRunner(BIR):
    IconName : str = "Bluetooth"
        
    def Update(self, iconManager : IM) -> None:
        pass 