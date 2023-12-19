import time

from IconManager import IconManager as IM
from Runners.WifiIconRunner import WifiIconRunner as WIR
from Runners.BluetoothIconRunner import BluetoothIconRunner as BIR
from Runners.PerformanceIconRunner import PerformanceIconRunner as PIR
from Runners.BatteryIconRunner import BatteryIconRunner as BaIR
from Runners.FanIconRunner import FanIconRunner as FIR
from Runners.UnderVoltageIconRunner import UnderVoltageIconRunner as UVIR
from Runners.DownloadingIconRunner import DownloadingIconRunner as DIR
from Runners.TimeIconRunner import TimeIconRunner as TIR

iconManager : IM = IM()
wifiIconRunner : WIR = WIR()
bluetoothIconRunner : BIR = BIR()
performanceIconRunner : PIR = PIR()
batteryIconRunner : BaIR = BaIR()
fanIconRunner : FIR = FIR()
underVoltageIconRunner : UVIR = UVIR()
downloadingIconRunner : DIR = DIR()
timeIconRunner : TIR = TIR()

while True:
    wifiIconRunner.Update(iconManager)
    bluetoothIconRunner.Update(iconManager)
    performanceIconRunner.Update(iconManager)
    batteryIconRunner.Update(iconManager)
    fanIconRunner.Update(iconManager)
    underVoltageIconRunner.Update(iconManager)
    downloadingIconRunner.Update(iconManager)
    timeIconRunner.Update(iconManager)
    
    iconManager.Update()

    time.sleep(2)