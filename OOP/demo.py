from pexpect import ExceptionPexpect


class Employee:

    def __init__(my, name):
        print(my)

    def sayMyName(self):
        print('my name is'+self.name)

try:
    emp1 = Employee('sadman')
    emp2 = Employee('shafin')
    lst = [1,2]
    print(lst[4])
    print(emp1.dept)

    emp2.sayMyName()


except AttributeError as exp:
    emp1.dept = 'cloud'
except ZeroDivisionError as zero:
    print(zero)
except Exception as e:
    print(e)

print(Employee)
print(emp2)
# print(emp1.dept)

# emp1.name = 'bla'

# print(emp1.name)
# print(emp2.name)

# emp1 = emp2

# emp1.name = 'hello'
# print(emp2.name)

# print(emp1)
# print(emp2)


