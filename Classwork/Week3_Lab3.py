#classes

def __init__(self, name):
        self._name = name
        
        
@proptery
        def name(self):
            return self._name
        
@name.setter
def name(self, new_name):
    self._name = new_name
    
    student1= Student('Ben')
    
    print(student1.name)
    student1.name = 'Benny'
    
    
    def outer_fn():
        def inner_fn():
            #body
            return inner_fn
        
        
def base_fn(func):
    print('Starting....')
    return func


#message function
def lowercaser_trans(func):
        def wrapper():
                func_to_process = func()
                lowercase_value = func_to_process.lower()
                return lowercase_value
        return wrapper
def name():
         username = input('Type username: ')
         return username
 username_lowercase = lowercase_trans(name)
 output = username_lowercase()
 print (output)

 

#
class strnValues:
        def__set_name-(self, owner, proptery_name):
        self._name = name
        def __get__(self, instance, owner:
                return instance._dict__.get(self.name) or 'Missing Value'
        def __set__(delf, instance, vlaue):
                if len(value)> 0 :
                        instance._dict__[self, _name]
                else:
                        raise ValueError(' Empty Field')
                        
        

class Student:
def __init__(self, name, program, location):
        self.name = name
        self.program = program        
        self.location = location
        
Student1 = Student()
Student1.setname ='Benny'
    
    
    