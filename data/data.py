from abc import ABC, abstractmethod 

class Data:
    def __init__(self):
        self.data = []
    
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def get(self, index):
        pass
    
    @abstractmethod
    def remove(self, item):
        pass
    
    @abstractmethod
    def duplicate(self, item):
        pass

    @abstractmethod
    def change(self, item, new_item):
        pass

    @abstractmethod
    def clear(self):
        pass
    
    @abstractmethod
    def read_file(self, file_path):
        pass
    @abstractmethod
    def write_file(self, file_path):
        pass
    
    

                

                

    
