# Write a program to fill in a letter template given below with name and date.
# letter = '''
#     Dear <|Name|>,
#     You are selected!
#     <|Date|>
#     '''

name = input("Please enter your name: ")
date = input("Please enter the date: ")

print('''Dear {},
You are selected!
{}'''.format(name, date))


#but instead of using format function, we can use Fstring which came in Python3.6 onwards

print(f'''Dear {name},
You are selected!
{date}
''')

# OR we can also use replace funtion but it doesnt make that much of sense