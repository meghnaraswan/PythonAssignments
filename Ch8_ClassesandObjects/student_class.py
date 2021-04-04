class Student(object):

    def __init__(self, first = '',last='',id=0):
        self.first_name_str=first
        self.last_name_str=last
        self.id_int = id

    def __str__(self):
        return(self.first_name_str+' '+self.last_name_str+', ID:'+str(self.id_int))

stu1 = Student('Pete','Panther',12345)
print(stu1)
