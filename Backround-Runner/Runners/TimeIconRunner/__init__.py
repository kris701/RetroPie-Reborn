from enum import Enum
from datetime import datetime
from .TimeIcons import TimeIcons as TI

class TimeIconRunner():
    _lastTime : str = "00:00"
    def Update(self, iconManager) -> None:
        now = datetime.now()
        time = now.strftime("%H:%M")
        if time != self._lastTime:
            self._lastTime = time
            iconManager.RemoveIcon("time_1");
            iconManager.RemoveIcon("time_2");
            iconManager.RemoveIcon("time_3");
            iconManager.RemoveIcon("time_4");
            iconManager.RemoveIcon("time_5");
            iconManager.AddIcon(self.GetIconFromString(time[0]), "time_1")
            iconManager.AddIcon(self.GetIconFromString(time[1]), "time_2")
            iconManager.AddIcon(TI.Seperator, "time_3")
            iconManager.AddIcon(self.GetIconFromString(time[3]), "time_4")
            iconManager.AddIcon(self.GetIconFromString(time[4]), "time_5")
    
    def GetIconFromString(self, character : str):
        if character == "0": return TI.Zero;
        if character == "1": return TI.One;
        if character == "2": return TI.Two;
        if character == "3": return TI.Three;
        if character == "4": return TI.Four;
        if character == "5": return TI.Five;
        if character == "6": return TI.Six;
        if character == "7": return TI.Seven;
        if character == "8": return TI.Eight;
        if character == "9": return TI.Nine;
    

    