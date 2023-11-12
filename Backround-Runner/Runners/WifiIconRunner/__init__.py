from enum import Enum

from .WifiIcons import WifiIcons as WI

class WifiIconRunner():
    IconName : str = "Wifi"
        
    _wifiCarrier = "/sys/class/net/wlan0/carrier" # 1 when wifi connected, 0 when disconnected and/or ifdown
    _wifiLinkmode = "/sys/class/net/wlan0/link_mode" # 1 when ifup, 0 when ifdown
    _currentState : WI = WI.Hide

    def Update(self, iconManager) -> None:
        checkState : WI = self.GetWifiState()
        if checkState != self._currentState:
            self._currentState = checkState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(checkState, self.IconName)        
    
    # From https://github.com/d-rez/gbz_overlay/blob/master/overlay.py#L107
    def GetWifiState(self) -> WI:
        new_wifi_state = WI.Hide
        try:
            f = open(self._wifiCarrier, "r")
            carrier_state = int(f.read().rstrip())
            f.close()
            if carrier_state == 1:
                # ifup and connected to AP
                new_wifi_state = WI.Connected
            elif carrier_state == 0:
                f = open(self._wifiLinkmode, "r")
                linkmode_state = int(f.read().rstrip())
                f.close()
                if linkmode_state == 1:
                    # ifup but not connected to any network
                    new_wifi_state = WI.Searching
                    # else - must be ifdown
      
        except IOError:
            pass
        
        return new_wifi_state
