import datetime as dt
import math
selfinter = """
自我介紹
黃紹齊男生
真理大學資工
愛騎車寫程式
學分學分學分
"""


def upper():
    print("*"*26)
    print("*"*26)
    print("%s%s%s" % ("*"*6, "first program ", "*"*6))
    print("* this is the first test *")
    print(selfinter)


def BMI():
    year = int(input("Which year are you born?"))
    weight = int(input("Input your weight... "))
    tall = float(input("How tall are you?... "))
    print("*"*26)
    print("You are %d years old." % (dt.datetime.today().year-int(year)))
    print("And your BMI is %f" % (weight/math.pow(tall, 2)))


if __name__ == "__main__":
    upper()
    BMI()
    input("\n\npress enter to finish the program ")
