# Write a program to print the student information for each departments
from itertools import groupby
from operator import itemgetter
  
# dictionary
students = [
    {'name': 'Tabish', 'roll_no': 1904197, 'branch': 'CSCE'},
    {'name': 'Tawana', 'roll_no': 1906228, 'branch': 'IT'},
    {'name': 'Akmal', 'roll_no': 1916432, 'branch': 'CSSE'},
    {'name': 'Mahmoud', 'roll_no': 1906196, 'branch': 'IT'},
    {'name': 'Azam', 'roll_no': 1905456, 'branch': 'CSE'},
    {'name': 'Mahdi', 'roll_no': 1909823, 'branch': 'CSE'},
    {'name': 'Kalam', 'roll_no': 1906789, 'branch': 'IT'},
    {'name': 'Manish', 'roll_no': 1919456, 'branch': 'CSSE'},
    {'name': 'Abi',    'roll_no': 1904332, 'branch': 'CSCE'}  
]
  
# Sort students data by branch key.
students = sorted(students, 
                  key = itemgetter('branch'))
  
# Display data grouped by branch
for key, value in groupby(students,key = itemgetter('branch')):
    print(key)
    for s in value:
        print("Name:", s['name'], ",Roll No: ", s['roll_no'])
