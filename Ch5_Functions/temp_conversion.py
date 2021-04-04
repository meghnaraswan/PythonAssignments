#temp conversion: C to F and F to C

def celsius_to_fahrenheit(celsius_float):
    '''Convert Celsius to Fahrenheit.'''
    return celsius_float * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit_float):
    '''Convert Fahrenheit to Celcius'''
    celsius_float = (fahrenheit_float - 32)/1.8
    return celsius_float

c_float = float(input("What is your temp in celsius? "))
f_float = celsius_to_fahrenheit(c_float)
print(c_float, "in celsius converts to", f_float, "in fahrenheit")
print()

f2_float = float(input("What is your temp in fahrenheit? "))
c2_float = fahrenheit_to_celsius(f2_float)

print(f2_float, "in fahrenheit converts to", c2_float, "in celsius")
print()
