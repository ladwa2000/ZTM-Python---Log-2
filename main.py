#Expressions and Statements

shares = int(input('Shares Run In: '))
isc = int(input('ISC: '))
perc_isc = (shares / isc) * 100

print(round(perc_isc, 2))

#NB: Anything after '=' is an 'expression' and an entire line of code is a 'statement'

#Augmented Assignment Operators

x = 100000

x += 200000
x -= 100000
x *= 2
x /= 10

print(x) #Use of augmented assingment operators return x = 40000.0 

#Strings

movement = 'The registered holder holds 40,000 shares'

print(movement) #Short string

desc = '''
The opening balance of this registered holder was 100,000 shares. 
They then bought an additional 200,000 shares, sold 100,000 shares, doubled and finally sold 1/10, resulting in their closing balance to be 40,000 shares to be held.
'''

print(desc) #Long string

#String Concatenation

print('Bank of New York ' + 'Nominees Limited')
#OR
print('Bank of New York' + ' ' + 'Nominees Limited')

#NB: Cannot concatenate a string to an integer, without converting 'int' to 'str', as it will return a TypeError

#Type Conversion

excel_general = float(input()) #Excel's 'General' formatting will change any integer to a floating point number
excel_number = int(excel_general) #Excel's 'Number' formatting will change any floating point number to an integer 

print(type(excel_number)) #Will return class 'int'

#Escape Sequences

id_fm = 'If we cannot determine who the fund manager\'s are for a particular fund, then we can try do so by doing the following: \n\t - we can look on LinkedIn \n\t - we can search the company\'s website'

print(id_fm) #Use of escape characters formats large text better and benefits more with higher grammatical usage

#Formatted Strings

reg_holder = 'Hargreaves Lansdown, stockbrokers (EO)'
amount = 13000

print(f'{reg_holder} holds {amount} shares.')
#OR
print('{} bought {} shares.'.format('Hargreaves Lansdown, stockbrokers (EO)', 2000))
#OR
print('{1} shares were bought by {0}.'.format('Hargreaves Lansdown, stockbrokers (EO)', 15000))
#OR
print('{0} lent {loan_shs} shares to {1}.'.format('Vidacos', 'Hargreaves Lansdown, stockbrokers (EO)', loan_shs = 15000)) #Positional arguments must come before named arguments

#String Indexes

tvr = '123456789' #Total Voting Rights

print(tvr[:]) #123456789
print(tvr[2:100]) #3456789
print(tvr[3:]) #456789
print(tvr[:7]) #1234567
print(tvr[2:6]) #3456
print(tvr[1:8:2]) #2468
print(tvr[-1:]) #9
print(tvr[:-4]) #12345
print(tvr[::-2]) #97531

#Immutability

#The above string, and any other strings for that matter, are immutable. We cannot assign a new value to an already assigned string, i.e. tvr[0] = 6. The only way we can is either by reassignment/creating a new string or concatenating an already assigned string, i.e. tvr = tvr + '6'