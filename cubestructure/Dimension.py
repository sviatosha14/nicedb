from cubestructure.DimensionElement import DimensionElement
class Dimension():
    #static
    def CreateDim(name:str=None):
        return Dimension(name=name)

    #dinamic
    def __init__(self,name:str=None):
        self.name=name
        self.elements = {}
    def add(self,name:str=None):
        if self.exist(name) == 1:
            raise Exception('Element '+name+ ' already exist in '+self.name + ' dimension')
        else:
            self.elements[name] = DimensionElement(name)
    def exist(self,name:str=None):
        if name in self.elements.keys():
            return 1
        else:
            return 0
    def getelem(self,name:str=None):
        return self.elements[name]

    def addchild(self,name:str=None,childname:str=None):
        if self.exist(name) == 0:
            if self.exist(childname)==1 and self.getelem(name).childexist==0:
                self.getelem(name).addchild(self.getelem(childname))
            else:
                raise Exception('element ' + childname + ' does not exist or already appears as a child of ' + name )
        else:
            raise Exception('element ' + name + ' does not exist')
    def delete(self,name:str=None):
        del self.elements[name]

    def getchild(self,name:str=None):
        try:
            return self.elements[name].children.keys()
        except KeyError:
            raise Exception('Element ' + name + ' does not exist in ' + self.name)

    def getdetail(self,name:str=None):
        children = self.getchild(name)
        if children == []:
            return name
        else:
            detail = []
            for elem in children:
                detail.append(self.getdetail(name=elem))
        return detail


