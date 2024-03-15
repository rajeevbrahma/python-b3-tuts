
temp_mem_space = {}

from abc import ABC, abstractmethod

class DictCrudABC(ABC):
    
    @abstractmethod
    def create_table(self,table_name):
        pass

    @abstractmethod
    def create_doc(self,table_name,document):
        pass
    
    @abstractmethod
    def read_doc(self,table_name,doc_id):
        pass

    # @abstractmethod
    # def update_doc(self,table_name,doc_id,document):
    #     pass
    
    # @abstractmethod
    # def read_docs(self,table_name):
    #     pass

    # @abstractmethod
    # def delete_doc(self,table_name,doc_id):
    #     pass


class DictCrud(DictCrudABC):

    def __init__(self):
        self.data_space = temp_mem_space

    def create_table(self, table_name):
        self.data_space.update({table_name:{}}) 
        return True

    def create_doc(self, table_name, document):
        self.data_space[table_name].update({document["s.no"]:document})

    def read_doc(self, table_name, doc_id):
        pass


print (temp_mem_space)
dict_crud = DictCrud()
dict_crud.create_table("child_data")
print (temp_mem_space)
dict_crud.create_doc('child_data',{"s.no":1,"name":None,"age":None})
print (temp_mem_space)
dict_crud.create_doc('child_data',{"s.no":2,"name":None,"age":None})
print (temp_mem_space)