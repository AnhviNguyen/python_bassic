import random
import math
from datetime import datetime
import pandas as pd


def area_and_perimeter():
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    print("Area: ", width* height)
    print("Perimeter: ", 2*(width + height))

def convert_cm_to_dm_and_inch():
    cm = float(input("Enter the length in cm: "))
    dm = cm / 10
    inch = cm / 2.54
    print(cm, "cm =", dm, "dm = ", round(inch, 2), "inch")

def check_digit_random_number():
    num = random.randint(0, 10000)
    print("Number is: ", num)
    return print(num, "has", len(str(num)),"digit")

def random_number():
    num = random.randint(-100, 100)
    print("Number is: ", num)
    print("Negative" if num < 0 else "Positive")
    print(num, "has", len(str(num)),"digit")

def nomalize_random():
    num = random.randint(10, 150)
    print("Number is: ", num)
    print("Nomalized:", round(float(num/150), 2))

def degree_and_radian():
    hour = int(input("Enter the hour: "))
    minute = int(input("Enter the minute: "))

    hour_angel = (360/12)*hour + (360/12/60)*minute
    minute_angel = (360/60)*minute
    angel = abs(hour_angel - minute_angel)
    print("angel: ", angel)
    print("radian: ", float(round((angel*2*3.14)/360, 2)))

def giai_phuong_trinh_bac_2():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    delta = b**2 - 4*a*c
    print("Calculate delta: b^2 - 4*a*c = ", delta)
    if delta < 0:
        print("because delta < 0 => No solution")
    elif delta == 0:
        print("because delta = 0 => has double solution =>  x = ", -b / (2 * a))
    else:
        print("because delta > 0 => has 2 solution")
        print("x1 = ", round((-b + delta**0.5) / (2 *a), 3))
        print("x2 = ", round((-b - delta**0.5) / (2 *a), 3))

def checkNumberInString():
    input_string = "Today is Sunday and we don't need to wake up at 6 am"
    num =0
    for index,i in enumerate(input_string):
        print("Position:", index) if i.isdigit() else ""
        if (i.isascii): num +=1
    print(num, "words in the string")

def student_profile():
    name = input("Enter your name: ")
    date = input ("Date of birth: ")
    sub1 = input("Name of Subject 1: ")
    mark1 = float(input("Mark of Subject 1: "))
    sub2 = input("Name of Subject 2: ")
    mark2 = float(input("Mark of Subject 2: "))
    sub3 = input("Name of Subject 3: ")
    mark3 = float(input("Mark of Subject 3: "))

    print("Student's name: ", name)
    print("Date of birth: ", date)
    print("Average mark: ", round(float(mark1+mark2+mark3)/3, 3))

def calculate_distance():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    
    euclidean_distance = round(math.sqrt(x**2 + y**2), 2)
    print("Euclidean distance from origin:", euclidean_distance)
    
    manhattan_distance = abs(x) + abs(y)
    print("Manhattan distance from origin:", manhattan_distance)
    
    dot_product = x * 0 + y * 0
    magnitude1 = sqrt(x**2 + y**2)
    magnitude2 = sqrt(0**2 + 0**2) 
    
    if magnitude1 != 0 and magnitude2 != 0:
        cosine_similarity = dot_product / (magnitude1 * magnitude2)
    else:
        cosine_similarity = 0.0 
    
    print("Cosine similarity with the origin:", cosine_similarity)


def covert_birth():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))

    try: 
        date_obj = datetime(year, month, day)
        print("Date:", date_obj.strftime("%A, %B %d, %Y"))
        print("Age: ", 2024- year)
    except ValueError:
        print("Invalid date")

def input_list():
    CustomerList = ['Join', 'Join', 'Marry', 'Marry', 'Marry']
    ProductList = ['Beer', 'Pork', 'Milk', 'Vegetable', 'Pork']
    QuantityList = ['2 Bottle', '1 kg', '5 Boxes', '2 Bunches', '3 Kg']

    #tao dataframe
    #download by terminal: pip3 install pandas
    #import
    df = pd.DataFrame({'Customer': CustomerList, 'Product': ProductList, 'Quantity':  QuantityList})
    print(df, "\n")

    #tach QuantityList thanh quantity va unit
    Quantity =[]
    Unit = []
    for i in QuantityList:
        Quantity.append(i.split(' ')[0])
        Unit.append(i.split(' ')[1])
    df = pd.DataFrame({'Customer': CustomerList, 'Product': ProductList, 'Quantity':  Quantity, 'Unit':  Unit})
    print(df)

    #tim Customer mua pork over 2 kg
    for index, quantity in enumerate(QuantityList):
        if int(quantity.split(' ')[0]) > 2 and quantity.split(' ')[1].lower() == 'kg':
            print("Customer:", CustomerList[index])












# check_digit_random_number()
# convert_cm_to_dm_and_inch()
# nomalize_random()
# degree_and_radian()
# giai_phuong_trinh_bac_2()
# checkNumberInString()
# covert_birth()
# input_list()
