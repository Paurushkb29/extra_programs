#Use map() and lambda functions to convert a list of temperatures (in Celsius) to Fahrenheit and Vice-Versa.

c_temperatures = [7, 50, 12, 22, 30]
f_temperatures = list(map(lambda c: round(c*9/5+32), c_temperatures)) # c to f
print(f_temperatures)
c_temperatures = list(map(lambda f: round((f - 32) * 5/9), f_temperatures)) # f to c
print(c_temperatures)

# def C_to_F():
#     c_temperatures = [7, 50, 12, 22, 30]
#     f_temperatures = list(map(lambda c: c*9/5+32, c_temperatures))
#     print(f_temperatures)

# def F_to_C():
#     f_temperatures = [44.6, 122.0, 53.6, 71.6, 86.0]
#     c_temperatures = list(map(lambda f: (f - 32) * 5/9, f_temperatures))
#     print(c_temperatures)

# C_to_F()
# F_to_C()

# Assertion
#assert f_temperatures == [44.6, 122.0, 53.6, 71.6, 86.0]

#In Python, the assert statement is used to check if a condition is true.
#In the provided code, the assert statement checks whether the list f_temperatures 
#matches the expected Fahrenheit temperatures [44.6, 122.0, 53.6, 71.6, 86.0].
