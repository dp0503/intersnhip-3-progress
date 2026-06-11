sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
average = total_marks / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "B+"
elif average >= 70:
    grade = "C+"
elif average >= 60:
    grade = "D+"
else:
    grade = "Fail..."

print(f"\nResults:")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average:.2f}")
print(f"Final Grade: {grade}")
