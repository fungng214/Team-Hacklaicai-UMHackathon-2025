from data import Data

class Transaction_Items(Data): 

    def __init__(self):
        self.data = {}
        self.read_file()
   
    def add(self, key, value):
        if key in self.data:
            raise ValueError("Item already exists in data")
        self.data[key] = value 
        
    
    def get(self, key):
        return key + key.values()
        
    def remove(self, item):
        if item in self.data:
            del self.data[item]
        else:
            raise ValueError("Item not found in data")  
    
    def duplicate(self, item):
        if item in self.data:
            self.data.append(item)
        else:
            raise ValueError("Item not found in data")
    
    def read_file(self):
        with open("keywords.csv", "r") as file:
            readlines = file.readlines()
            for x in readlines:
                index,order_id,item_id,merchant_id = x.split(",")
                self.data[order_id] = {
                    "index": index,
                    "item_id": item_id,
                    "merchant_id": merchant_id
                }