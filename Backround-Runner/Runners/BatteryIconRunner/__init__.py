from enum import Enum

from .BatteryIcons import BatteryIcons as BI

class BatteryIconRunner():
    IconName : str = "Battery"
    _currentState : BI = BI.Battery10
    
    _chargeVoltage : float = 4.1
    _ChargevoltageMap : dict = {
            0: BI.BatteryAlert,
            1: BI.Battery10,
            2: BI.Battery20,
            3: BI.Battery30,
            4: BI.Battery40,
            5: BI.Battery50,
            6: BI.Battery60,
            7: BI.Battery70,
            8: BI.Battery80,
            9: BI.Battery90,
            10: BI.Battery100,
        }
    _voltageMap : dict = {
            0: BI.BatteryAlert,
            1: BI.Battery10,
            2: BI.Battery20,
            3: BI.Battery30,
            4: BI.Battery40,
            5: BI.Battery50,
            6: BI.Battery60,
            7: BI.Battery70,
            8: BI.Battery80,
            9: BI.Battery90,
            10: BI.Battery100,
        }
        
    def Update(self, iconManager) -> None:
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
            for v in self._voltageMap:
                state = self._voltageMap[v]
                if voltage > v:
                    break    
                
        return state

    def GetBatteryVoltage(self) -> float:
        # insert ADC implementation here
        return 3