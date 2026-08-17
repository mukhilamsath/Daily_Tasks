score = float(input("Enter your score: "))

if score > 90:
    grade = "A"
elif score > 80:
    grade = "B"
elif score > 70:
    grade = "C"
else:
    grade = "D"

print(f"Score: {score}")
print(f"Grade: {grade}")