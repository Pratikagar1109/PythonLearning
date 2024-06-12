try:
    income=int(input("enter the income"))
    age=int(input("enter the age of the person"))
    risk=income/age
    print(age)
    print(risk)
except ZeroDivisionError:
    print("age zero not possible")
except ValueError:
    print("invalid value")