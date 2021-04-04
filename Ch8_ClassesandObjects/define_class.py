#defining a class with methods

class MyClass(object):
    class_attribute = 'world'

    def my_method(self, param1):
        print('\nhello',param1)
        print("The object that called this method is:",self)
        self.instance_attribute = param1

my_instance = MyClass()

print("output of dir(my_instance):")
print(dir(my_instance))
my_instance.my_method('goodbye')

print(my_instance.instance_attribute)

print('dir(my_instance):')
print(dir(my_instance))
