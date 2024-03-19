class person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def getter(self):
        return self.__name,self.__age
    def setter(self,new_age): 
        if   new_age>0:
            self.__age=new_age
            return self.__age
        else:
            raise ValueError("age is always a non-negative number") 
a=person("tasu",20) 
print(a.getter())
print(a.setter(5))      