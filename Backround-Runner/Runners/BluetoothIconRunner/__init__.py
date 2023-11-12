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
            p1 = subprocess.Popen('hciconfig', stdout = subprocess.PIPE)
            p2 = subprocess.Popen(['awk', 'FNR == 3 {print tolower($1)}'], stdin = p1.stdout, stdout=subprocess.PIPE)
            state=p2.communicate()[0].decode().rstrip()
            if state == "up":
                new_bt_state = BI.Searching
        except IOError:
            pass

        if new_bt_state is BI.Searching:
            try:
                devices=os.listdir(self._bluetootDevicesDir)
                if len(devices) > 1:
                    new_bt_state = BI.Connected
            except OSError:
                pass
        
        return new_bt_state