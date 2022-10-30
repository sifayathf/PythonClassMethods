class a:

    pass

class b:
    pass

a1=a()
b1=b()

class animal:
    pass

class tiger(animal):
    #attributes
    legs=4
    type="carnivores"

    def __init__(self,name):
        self.name = name

    def disp(self):
        print("{} is a Tiger.  It is a wild Animal, it has {} legs.".format(self.name,self.legs))


class lion(animal):
    legs=4
    type="carnivores"

class cheetah(animal):
    legs = 4
    type="carnivores"

class wolf(animal):
    legs = 4
    type = "carnivores"

class deer(animal):
    legs = 4
    type = "herbivores"

t1=tiger('namir')
t1.disp()


