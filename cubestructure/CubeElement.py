#from CubeElement import CubeElement
import copy


class CubeElement():
    def __init__(self):
        self.elist = {}

    def getelem(self,elemnm):
        return self.elist[elemnm]
    def builddatatree(self,elements:{}=None,dimlist:[]=None,level:int=None,data:{}=None):
        if level != len(dimlist):
            if elements[dimlist[level]] in self.elist.keys():
                leaf = self.elist[elements[dimlist[level]]]
            else:
                leaf = CubeElement()
                self.elist[elements[dimlist[level]]] = leaf
            leaf.builddatatree(elements=elements,dimlist=dimlist,level=level+1,data=data)
        else:
            self.elist = data

    def getvalue(self,elements:{}=None,dimlist:[]=None,level:int=None,datakey:str=None):
        if level != len(dimlist):
            if type(elements[dimlist[level]]) != list:
                elements[dimlist[level]] = [elements[dimlist[level]]]
            value = 0
            for elem in elements[dimlist[level]]:
                try:
                    value+= self.elist[elem].getvalue(elements=elements,dimlist=dimlist,level=level+1,datakey=datakey)
                except KeyError:
                    pass
            return value
        else:
            return self.elist[datakey]

    def getmultiplevalues(self,elements:{}=None,dimlist:[]=None,level:int=None,datakey:str=None,rowdict:{}= {}):
        if level != len(dimlist):
            rowlist=[]
            for elem in elements[dimlist[level]]:
                tmprowdict = rowdict
                tmprowdict[dimlist[level]] = elem
                if elem in self.elist.keys():
                    tmprowdict=self.elist[elem].getmultiplevalues(elements=elements,dimlist=dimlist,level=level+1,datakey=datakey,rowdict=tmprowdict)
                    rowlist=rowlist + copy.deepcopy(tmprowdict)
            return rowlist
        else:
            tmprowdict = rowdict
            tmprowdict[datakey]=self.elist[datakey]
            return [tmprowdict]

    def getjson(self,dimlist:[]=None,level:int=None,rowdict:{}={}):
        if level != len(dimlist):
            rowlist=[]
            for key in self.elist.keys():
                tmprowdict = rowdict
                tmprowdict[dimlist[level]] = key
                tmprowlist=self.elist[key].getjson(dimlist=dimlist,level=level+1,rowdict=tmprowdict)
                rowlist=rowlist+copy.deepcopy(tmprowlist)
            return rowlist
        else:
            tmprowdict = rowdict
            tmprowdict['data']=self.elist
            return [tmprowdict]

class Wrong_CubeElement():
    def __init__(self):
        self.elist={}

    def get_insert(self,name:str=None):
        if name in self.elist.keys():
            return self.elist[name]
        else:
            new = CubeElement()
            self.elist[name] = new
            return new

    def get_get(self,name:str=None):
        return self.elist[name]