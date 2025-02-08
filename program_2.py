#Author: Michael Beaudet
#Title: Week 3 Program 2
#Date: 2/6/25

def categorize_age(age):
    ageCategory = "TBD"
    if age <= 1:
        ageCategory = "infant"
    elif age < 13:
        ageCategory = "child"
    elif age < 20:
        ageCategory = "teenager"
    else:
        ageCategory = "adult"

    return ageCategory

if __name__ == '__main__':
    age = float(input("Enter the person's age: "))

    ageBucket = categorize_age(age)
    print (ageBucket)