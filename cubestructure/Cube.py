from cubestructure.CubeElement import CubeElement
import json



class Cube():
    #static

    #dinamic
    def __init__(self,name:str=None,dims:[]=None):
        self.name = name
        self.dims = dims
        self.data = CubeElement()
        self.dimdict = {}
        for dim in self.dims:
            self.dimdict[dim.name] = dim

    def insertvalue(self,insertstatenment:{}=None):
        self.data.builddatatree(elements=insertstatenment['elements'],dimlist=self.dims,level=0,data=insertstatenment['data'])

    def getvalue(self,getstatenment:{}=None):
        #checking dimension element levels:
        for dimension in getstatenment['elements'].keys():
            for elem in getstatenment['elements'][dimension]:
                detail=self.dimdict[dimension].getdetail(elem)
                if detail != elem:
                    getstatenment['elements'][dimension].remove(elem)
                    getstatenment['elements'][dimension].append({elem:detail})
        return self.data.getvalue(elements=getstatenment['elements'],dimlist=self.dims,level=0,datakey=getstatenment['datakey'])
    def getmultiplevalue(self,getstatenment:{}=None):
        return self.data.getmultiplevalues(elements=getstatenment['elements'],dimlist=self.dims,level=0,datakey=getstatenment['datakey'])
    def cubetojson(self):
        return {
            'name':self.name,
            'data':self.data.getjson(self.dims,level=0)
        }



class Wrong_Cube():
    def __init__(self,name:str=None,dimsobj:[]=None):
        self.name = name
        self.dims = dimsobj
        self.dimnames = []
        for dim in self.dims:
            self.dimnames.append(dim.name)
        self.data = CubeElement()
        self.data = CubeElement()

    def insertvalue(self,insertstatenment:{}=None):
        #TODO What if one of the elements is consolidated?
        elem = self.data
        elements = insertstatenment['elements']
        for index in range(self.dimnames.keys()):
            if index != len(self.dimnames.keys()):
                nextelem = elements[self.dimnames[index]]
                elem = elem.get_insert(name=nextelem)
            else:
                elem.elist = insertstatenment['data']

    def getvalue(self,getstatenment:{}=None):
        #TODO logic to get consolidated element
        elements = getstatenment['elements']
        datakey = getstatenment['datakey']
        elem = self.data
        for index in range(self.dimnames.keys()):
            if index != len(self.dimnames.keys()):
                nextelem = elements[self.dimnames[index]]
                try:
                    elem = elem.get_get(name=nextelem)
                except KeyError:
                    return None
            else:
                try:
                    return elem.elist[datakey]
                except KeyError:
                    return None

