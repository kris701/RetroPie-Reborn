from enum import Enum
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

from .BatteryIcons import BatteryIcons as BI

class BatteryIconRunner():
    IconName : str = "Battery"
    _currentState : BI = BI.Battery10
    _i2c = busio.I2C(board.SCL, board.SDA)
    _ads = ADS.ADS1015(_i2c)
    _chan = AnalogIn(_ads, ADS.P0)
    
    _chargeVoltage : float = 4.1
    _ChargevoltageMap : dict = {
            2:   BI.BatteryAlert,
            2.2: BI.Battery10,
            2.4: BI.Battery20,
            2.6: BI.Battery30,
            2.8: BI.Battery40,
            3:   BI.Battery50,
            3.2: BI.Battery60,
            3.4: BI.Battery70,
            3.6: BI.Battery80,
            3.8: BI.Battery90,
            4:   BI.Battery100,
        }
    _voltageMap : dict = {
            2:   BI.BatteryAlert,
            2.2: BI.Battery10,
            2.4: BI.Battery20,
            2.6: BI.Battery30,
            2.8: BI.Battery40,
            3:   BI.Battery50,
            3.2: BI.Battery60,
            3.4: BI.Battery70,
            3.6: BI.Battery80,
            3.8: BI.Battery90,
            4:   BI.Battery100,
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
            state : BI = BI.BatteryAlert
            for v, s in self._ChargevoltageMap:
                if voltage < v:
                    break   
                state = s
        else:
            state : BI = BI.BatteryAlert
            for v in self._voltageMap:
                if voltage < v:
                    break    
                state = self._voltageMap[v]
                
        return state

    def GetBatteryVoltage(self) -> float:
        return self._chan.voltage