class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError(key)

    def set(self):
        if key in self.data:
            self.data[key] = value
        else:
            raise KeyError ('Error: Unexisting Key')

    
def add(self,key,value):
        if key not in self.data:
            self.data[key] = value
        else:
            raise KeyError("Such key exist")
