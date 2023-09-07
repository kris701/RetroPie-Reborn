import time

from .IconManager import IconManager as IM
from Runners.WifiIconRunner import WifiIconRunner as WIR
from Runners.BluetoothIconRunner import BluetoothIconRunner as BIR
from Runners.PerformanceIconRunner import PerformanceIconRunner as PIR
from Runners.BatteryIconManager import BatteryIconManager as BaIR

iconManager : IM = IM()
wifiIconRunner : WIR = WIR()
bluetoothIconRunner : BIR = BIR()
performanceIconRunner : PIR = PIR()
batteryIconRunner : BaIR = BaIR()

while True:
    wifiIconRunner.Update(iconManager)
    bluetoothIconRunner.Update(iconManager)
    performanceIconRunner.Update(iconManager)
    batteryIconRunner.Update(iconManager)

    time.sleep(1000)