from ...IconManager import IconStorage as IS

class PerformanceIcons(IS):
    OK = "..."
    UnderVoltage = "..."
    UnderVoltageAndFreqCap = "..."
    UnderVoltageAndThrottled = "..."
    UnderVoltageAndFreqCapAndThrottled = "..."
    FreqCap = "..."
    FreqCapAndThrottled = "..."
    Throttled = "..."

def GetIconFromValue(value : int) -> PerformanceIcons:

    # 0 = OK
    # 000 <- Undervoltage
    # ||<--- FreqCap
    # |<---- Throttled

    if value == 0:
        return PerformanceIcons.OK
    
    elif value == 001:
        return PerformanceIcons.UnderVoltage
    elif value == 010:
        return PerformanceIcons.FreqCap
    elif value == 100:
        return PerformanceIcons.Throttled

    elif value == 011:
        return PerformanceIcons.UnderVoltageAndFreqCap
    elif value == 111:
        return PerformanceIcons.UnderVoltageAndFreqCapAndThrottled
    elif value == 101:
        return PerformanceIcons.UnderVoltageAndThrottled
    
    elif value == 110:
        return PerformanceIcons.FreqCapAndThrottled



