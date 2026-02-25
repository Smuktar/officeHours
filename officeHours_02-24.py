print('Hello World')

age = 25

# Operators (+, -, *, /, %, **)
print(age+5)
print(age-5)
print(age*3)
print(age/4)
print(age%4)
print(age**2)

sentence = 'This is a sentence'
doYouLikeCottageCheese = "I don't like cottage cheese"

print(doYouLikeCottageCheese)

# Lists
selamsGradeInSchool = ['A', 'B', 'C', 'D', 'F']
print(selamsGradeInSchool)
selamsGradeInSchool.append('A+')
print(selamsGradeInSchool)

# Dictionary
student = {
    'name': 'Seli',
    'age': 20,
    'favoriteActivity': "Traveling",
    'favoriteSoda': 'nothing',
    'Grades': ['A+', 'A', "A+"]
}

print(student)
print(student['favoriteActivity'])
print(student['favoriteSoda'])

# For loops
for each in range(1, 11): print(each)

# shorthand for loop
for i in range(1,11): print(i)

for eachgrade in selamsGradeInSchool: print(eachgrade) 

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

numbers = [1, 57, 85, 32, 0]

total = 0
for num in numbers:
    total += num

print('The total sum of numbers is: ', total)

for i in range(5, 0, -1):
    print(i)

names = ['Colton', 'Qasmi', 'Mesganaw', 'Vasantha', 'Selam', 'Hima', 'Monika', 'Yamrot', 'Lucky']

for name in names:
    if len(name) >= 5:
        print(name)

for num in numbers:
    if num % 2 == 0:
        print(num, ' is even')
    else:
        print(num, 'is odd')

