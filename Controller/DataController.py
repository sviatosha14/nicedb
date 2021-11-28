from cubestructure.Dimension import Dimension
from cubestructure.Cube import Cube

class DataController():
    def __init__(self):

        self.dimensions = Dimension('_dimensions_')
        self.dimensions.add('_dimensions_')
        self.dimensions_atrs = Dimension('_dimension_atrs_')
        self.dimensions_atrs.add('_object_link_')
        self.dimensions_cube = Cube('_dimensions_',['_dimensions_','_dimension_atrs_'])
        dimension_link ={
            'elements':{'_dimensions_':'_dimensions_','_dimension_atrs_':'_object_link_'},
            'data':{'value':self.dimensions}
        }
        self.dimensions_cube.insertvalue(dimension_link)

        dimensions_atrs_link={
            'elements':{'_dimensions_':'_dimension_atrs_','_dimension_atrs_':'_object_link_'},
            'data':{'value':self.dimensions_atrs}
        }
        self.dimensions_cube.insertvalue(dimensions_atrs_link)


        self._techdimension_objectlink_insert('_cubes_')
        self._techdimension_objectlink_insert('_roles_')
        self._techdimension_objectlink_insert('_users_')
        self._techdimension_objectlink_insert('_cube_atrs_')
        self.dimension_element_insert(dimname='_cube_atrs_',elname='_object_link_')
        self.cube_atrs = Cube('_cubes_',dims=['_cubes_','_cube_atrs_'])
        link = {
            'elements':{'_cubes_':'_cubes_','_cube_atrs_':'_object_link_'},
            'data':{'value':self.cube_atrs}
        }
        self.cube_atrs.insertvalue(link)

        link = {
            'elements':{'_cubes_':'_dimensions_','_cube_atrs_':'_object_link_'},
            'data':{'value':self.dimensions_cube}
        }

    def dimension_exist(self,dimname:str=None):
        return self.dimensions.exist(name=dimname)

    def _dimension_object_get(self,dimname:str=None):
        query = {
            'elements': {'_dimensions_': dimname, '_dimension_atrs_': 'object_link'},
            'datakey': 'value'
        }
        return self.dimensions_cube.getvalue(query)

    def dimension_element_exist(self,dimname:str=None,elname:str=None):
        # TODO Добавить логику ролей и юзеров
        if self.dimension_exist(dimname)==1:
            dim=self._dimension_object_get(dimname=dimname)
            return dim.exist(name=elname)
        else:
            raise Exception('dimension ' + dimname + ' does not exist')

    def dimension_element_insert(self,dimname:str=None,elname:str=None):
        # TODO Добавить логику ролей и юзеров
        dim:Dimension = self._dimension_object_get(dimname=dimname)
        dim.add(name=elname)


    def _techdimension_objectlink_insert(self,name:str=None):
        obj = Dimension(name)
        self.dimensions.add(name)
        link ={
            'elements': {'_dimensions_':name, '_dimension_atrs_': '_object_link_'},
            'data': {'value': obj}
        }
        self.dimensions_cube.insertvalue(link)


    def dimension_add(self,name:str=None):
        #TODO Добавить логику ролей и юзеров
        if self.dimensions.exist(name)==1:
            raise Exception('dimension ' + name + ' already exists')
        else:
            dim=Dimension(name=name)
            self.dimension_element_insert(dimname='_dimension_',elname=name)
            link = {
                'elements': {'_dimensions_': name, '_dimension_atrs_': '_object_link_'},
                'data': {'value': dim}
            }
            self.dimensions_cube.insertvalue(link)

    def cube_add(self,name:str=None,dims:[]=None):
        for dimname in dims:
            if self.dimension_exist(dimname=dimname)==0:
                raise Exception('Dimension ' + dimname + ' does not exist')
        if self.dimension_element_exist(dimname='_cubes_',elname=name) == 1:
            raise Exception('Cube ' + name + ' already exist')
        cube = Cube(name=name,dims=dims)
        self.dimension_element_insert(dimname='_cubes_',elname=name)
        link={
            'elements':{'_cubes_':name,'_cube_atrs_':'_object_link_'},
            'data':{'value':cube}
        }
        self.cube_atrs.insertvalue(link)

    def _cube_object_get(self,name:str=None):
        query = {
            'elements': {'_cubes_': name, '_cube_atrs_': 'object_link'},
            'datakey': 'value'
        }
        return self.cube_atrs.getvalue(query)

    def cube_exist(self,name:str=None):
        return self.dimension_element_exist(dimname='_cubes_',elname=name)

    def jcube_value_get(self,getstatenment:{}=None):
        #TODO Нужна логика создания куба т.к. нужен куб атрибутов измерения кубов
        if self.cube_exist(getstatenment['cubename'])==0:
            raise Exception('Cube ' + getstatenment['cubename'] + ' does not exist')
        for dim in getstatenment['elements'].keys():
            if self.dimension_element_exist(dimname=dim,elname=getstatenment['elements'][dim]) == 0:
                raise Exception('Element ' + getstatenment['elements'][dim] + ' does not exist')
        return self._cube_object_get(getstatenment['cubename']).getvalue(getstatenment)
