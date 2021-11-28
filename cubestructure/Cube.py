from cubestructure.CubeElement import CubeElement
import json

class Cube():
    #static

    #dinamic
    def __init__(self,name:str=None,dims:[]=None):
        self.name = name
        self.dims = dims
        self.data = CubeElement()

    def insertvalue(self,insertstatenment:{}=None):
        self.data.builddatatree(elements=insertstatenment['elements'],dimlist=self.dims,level=0,data=insertstatenment['data'])
    def getvalue(self,getstatenment:{}=None):
        return self.data.getvalue(elements=getstatenment['elements'],dimlist=self.dims,level=0,datakey=getstatenment['datakey'])
    def getmultiplevalue(self,getstatenment:{}=None):
        return self.data.getmultiplevalues(elements=getstatenment['elements'],dimlist=self.dims,level=0,datakey=getstatenment['datakey'])
    def cubetojson(self):
        return {
            'name':self.name,
            'data':self.data.getjson(self.dims,level=0)
        }


