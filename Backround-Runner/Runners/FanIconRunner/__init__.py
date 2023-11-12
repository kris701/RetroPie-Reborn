from enum import Enum
import os
import subprocess
from gpiozero import CPUTemperature

from .FanIcons import FanIcons as FI

class FanIconRunner():
    IconName : str = "Fan"

    _currentState : FI = FI.Hide
    _fanIconMap : dict = {
            50 : FI.FanSpeed1,
            60 : FI.FanSpeed2,
            70 : FI.FanSpeed3,
            80 : FI.FanAlert
        }
    _fanSpeedMap : dict = {
            50 : 25,
            60 : 50,
            70 : 75,
            80 : 100
        }

    def Update(self, iconManager) -> None:
        currentTemp : float = self.GetCPUTemperature()
        self.SetFanSpeed(currentTemp)
        newState = FI.Hide
        for temp in self._fanIconMap:
            if temp > currentTemp:
                break;
            newState = self._fanIconMap[temp]
        if self._currentState != newState:
            self._currentState = newState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(newState, self.IconName)    
    
    def GetCPUTemperature(self) -> float:
        cpu = CPUTemperature()
        return cpu.temperature
    
    def SetFanSpeed(self, currentTemp : float):
        newSpeed = 0
        for temp, speed in self._fanSpeedMap:
            if temp > currentTemp:
                break
            newSpeed = speed
            
        # Set fan speed here
    