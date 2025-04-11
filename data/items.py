from data import Data

class items(Data): 

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
        with open("items.csv", "r") as file:
            readlines = file.readlines()
            for x in readlines:
                item_id,cuisine_tag,item_name,item_price,merchant_id = x.split(",")
                self.data[item_id] = {
                    "cuisine_tag": cuisine_tag,
                    "item_name": item_name,
                    "item_price": item_price,
                    "merchant_id": merchant_id
                }