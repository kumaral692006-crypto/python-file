class person:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    def __add__(self,other):
        return self.first + " "+ other.last
p1=person("kumara","21")
p2=person("kd","24")
