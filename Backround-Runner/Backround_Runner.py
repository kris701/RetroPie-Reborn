import time

from .IconManager import IconManager as IM
from Runners.WifiIconRunner import WifiIconRunner as WIR
from Runners.BluetoothIconRunner import BluetoothIconRunner as BIR
from Runners.PerformanceIconRunner import PerformanceIconRunner as PIR
from Runners.BatteryIconRunner import BatteryIconRunner as BaIR
from Runners.FanIconRunner import FanIconRunner as FIR

iconManager : IM = IM()
wifiIconRunner : WIR = WIR()
bluetoothIconRunner : BIR = BIR()
performanceIconRunner : PIR = PIR()
batteryIconRunner : BaIR = BaIR()
fanIconRunner : FIR = FIR()

while True:
    wifiIconRunner.Update(iconManager)
    bluetoothIconRunner.Update(iconManager)
    performanceIconRunner.Update(iconManager)
    batteryIconRunner.Update(iconManager)
    fanIconRunner.Update(iconManager)

    time.sleep(1000)