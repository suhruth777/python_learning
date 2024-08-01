# Create a program that calculates the average grade of a student. The program should:

# 1.	Ask the user how many grades they want to input.
# 2.	Use a loop to get each grade from the user and store the grades in a list.
# 3.	Calculate the average grade.
# 4.	Print the average grade and a message indicating the letter grade based on the average (A, B, C, D, F)

entry_num = input("How many grades would you like to enter?: ")
grades = []
entry_num = int(entry_num)

for i in range(entry_num):
    grade = float(input("Enter a grade: "))
    grades.append(grade)

average_grade = sum(grades) / entry_num

if average_grade >= 90:
    letter_grade = 'A'
elif average_grade >= 80:
    letter_grade = 'B'
elif average_grade >= 70:
    letter_grade = 'C'
elif average_grade >= 60:
    letter_grade = 'D'
elif average_grade < 60:
    letter_grade = 'F'
else:
    print('Please enter a valid number')

print('This student average grade is:', average_grade)
