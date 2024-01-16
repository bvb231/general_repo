

class Tb_component:

    def __new__(self, name):
        self.name = name


    def __del__(self):
        print("Destructor")
