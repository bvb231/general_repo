# Base test object that should be used to pass around 
# meta data 
#

class Tb_object:

    def __new__(self, name):
        self.name = name
