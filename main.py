a = 100 - 23 #77 (int)
b = 47 // 7 #6 (int)
c = 68 % 9 #5 (int)
x = 3*4 #12 (int)
y = 2/4 #0.5 (float)
z = 18 + 4 #22 (int)
print(a, b, c, x, y, z)

print(bin(10)) #1010
print(int(bin(10), 2)) #10
print(int(0b1010)) #10 
print(int('0b1010', 2)) #10

bodmas = ((23 * 2) + 15 - 3) / 3 #19.333... (float)
print(bodmas)
print(int(bodmas)) #To give integer value 
print(round(bodmas)) #To give integer value 

#NB: When dividing data types, the output will return as a float for the most precise result as it does not round output to the nearest whole number, unless the use of round() and/or int() has been actioned

first_name = 'Ajay'
surname = 'Ladwa'
print(first_name + ' ' + surname) #Ajay Ladwa

d, e, f = 1, 5, 7
print(d) #1
print(e) #5
print(f) #7

g = h = i = 1966
print(g) #1966
print(h) #1966
print(i) #1966