
# Variables in Python

first_name = 'Rancy'
last_name = 'Chepchirchir'
country = 'Kenya'
city = 'Nairobi'
age = 1050
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python', 'C++', 'JScript']
person_info = {
    'firstname':'Rancy', 
    'lastname':'Chepchirchir', 
    'country':'Kenya',
    'city':'Nairobi'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Rancy', 'Chepchirchir', 'Kenya', 1050, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)