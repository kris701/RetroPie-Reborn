from enum import Enum

from ..BaseIconRunner import BaseIconRunner as BIR
from ...IconManager import IconManager as IM
from .BatteryIcons import BatteryIcons as BI

class BatteryIconRunner(BIR):
    IconName : str = "Battery"
    _currentState : BI = BI.Battery10
    
    _chargeVoltage : float = 4.1
    _ChargevoltageMap : dict = {
            0: BI.Battery10,
            1: BI.Battery20,
            # ...
        }
    _voltageMap : dict = {
            0: BI.Battery10,
            1: BI.Battery20,
            # ...
        }
        
    def Update(self, iconManager : IM) -> None:
        checkState : BI = self.GetBatteryState()
        if checkState != self._currentState:
            self._currentState = checkState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(checkState, self.IconName)        

    def GetBatteryState(self) -> BI:
        voltage = self.GetBatteryVoltage()
        if voltage >= self._chargeVoltage:
            state : BI = BI.Battery10
            for v, s in self._ChargevoltageMap:
                state = s
                if voltage > v:
                    break    
        else:
            state : BI = BI.Battery10
            for v, s in self._voltageMap:
                state = s
                if voltage > v:
                    break    
                
        return state

    def GetBatteryVoltage(self) -> float:
        # insert ADC implementation here
        pass