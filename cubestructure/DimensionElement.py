#from cubestructure.DimensionElement import DimensionElement

class DimensionElement():
    def __init__(self,name:str=None):
        self.name=name
        self.children= {}
    def childexist(self,name):
        if name in self.children.keys():
            return 1
        else:
            return 0
    def addchild(self,childelement=None):
        if self.childexist(childelement.name) == 0:
            raise Exception('Element '+childelement.name+ ' already appears as a child of '+self.name)
        else:
            self.children[childelement.name] = childelement

    def getchild(self,name:str=None):
        return self.children[name]

    def getallchild(self):
        return self.children.items()
