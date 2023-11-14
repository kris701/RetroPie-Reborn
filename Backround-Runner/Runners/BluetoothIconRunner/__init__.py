from enum import Enum
import os
import subprocess

from .BluetoothIcons import BluetoothIcons as BI

class BluetoothIconRunner():
    IconName : str = "Bluetooth"
        
    _bluetootDevicesDir :str = "/sys/class/bluetooth"
    _currentState : BI = BI.Hide
    
    def Update(self, iconManager) -> None:
        checkState : BI = self.GetBluetoothState()
        if checkState != self._currentState:
            self._currentState = checkState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(checkState, self.IconName)    
    
    # From https://github.com/d-rez/gbz_overlay/blob/master/overlay.py#L143
    def GetBluetoothState(self) -> BI:
        new_bt_state : BI = BI.Hide
        try:
            stdoutdata = subprocess.getoutput("hcitool con")
            if "XX:XX:XX:XX:XX:XX" in stdoutdata.split():
                new_bt_state = BI.Connected
        except IOError:
            pass

        return new_bt_state