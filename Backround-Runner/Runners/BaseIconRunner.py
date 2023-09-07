from ..IconManager import IconManager as IM

class BaseIconRunner(object):
    IconName : str = "None"
    
    def Update(self, iconManager : IM) -> None:
        pass




