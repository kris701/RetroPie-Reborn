from enum import Enum
import os
import subprocess
import statistics
from gpiozero import CPUTemperature
from RPi import GPIO

from .FanIcons import FanIcons as FI

class FanIconRunner():
    IconName : str = "Fan"

    _avgList : list = []
    _currentState : FI = FI.Hide
    _fanIconMap : dict = {
            70 : FI.Hide,
            75 : FI.FanSpeed1,
            80 : FI.FanSpeed2,
            85 : FI.FanAlert
        }
    _fanSpeedMap : dict = {
            70 : 0,
            75 : 50,
            80 : 75,
            85 : 100
        }

    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        self._pwm = GPIO.PWM(12, 100)
        self._pwm.start(0)

    def Update(self, iconManager) -> None:
        currentTemp : float = self.GetGetCPUTemperature()
        newState = FI.Hide
        for temp in self._fanIconMap:
            if temp > currentTemp:
                break;
            newState = self._fanIconMap[temp]
        self.SetFanSpeed(currentTemp)
        if self._currentState != newState:
            self._currentState = newState
            iconManager.RemoveIcon(self.IconName);
            iconManager.AddIcon(newState, self.IconName)    
    
    def SetFanSpeed(self, currentTemp : float):
        newSpeed : int = 0
        for temp in self._fanSpeedMap:
            if temp > currentTemp:
                break
            newSpeed = self._fanSpeedMap[temp]

        self._pwm.ChangeDutyCycle(newSpeed)
    
    def GetGetCPUTemperature(self) -> float:
        self._avgList.append(CPUTemperature().temperature)
        if len(self._avgList) > 5:
            self._avgList.pop(0)
        return statistics.mean(self._avgList)