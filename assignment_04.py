#Assignment #4
#Group #5
#Question 1)

class Rates:

    def __init__(self, first_name, last_name, year_of_birth, current_year):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__year_of_birth = int(year_of_birth)
        self.__current_year = int(current_year)
        self.age  = int(current_year - self.year_of_birth)
        self.max_bpm = int(220 - self.age)
        self.min_range_bpm = float(self.max_bpm * 0.5)
        self.max_range_bpm = float(self.max_bpm * 0.85)


    def get__first_name(self):
        return self.__first_name

    def set__first_name(self, first_name):
        self.__first_name = first_name
    
    first_name = property(get__first_name,set__first_name)

    def get__last_name(self):
        return self.__last_name

    def set__last_name(self, last_name):
        self.__last_name = last_name
    
    last_name = property(get__last_name,set__last_name)

    def get__year_of_birth(self):
        return self.__year_of_birth

    def set__year_of_birth(self, year_of_birth):
        self.__year_of_birth = year_of_birth
    
    year_of_birth = property(get__year_of_birth,set__year_of_birth)

    def get__current_year(self):
        return self.__current_year

    def set__current_year(self, current_year):
        self.__current_year = current_year

    current_year = property(get__current_year,set__current_year)

    def print_personal_information(self):
        print("\nName: " + self.first_name + " " + self.last_name + ", Age: " + str(self.age))

    def print_performance_info(self):
        print("Maximum BPM: " + str(self.max_bpm) + " bpm, Target Range: " 
            + str(self.min_range_bpm) + " bpm - " + str(self.max_range_bpm) + " bpm\n")


def Question_1():

    print("\n\t---------- Question #1 ----------\n")
    f_name = input("Enter your first name: ")
    l_name = input("Enter your lastname: ")
    year_birth = input("Enter your year of birth: ")
    currentyear = input("Enter current year: ")

    p1 = Rates(f_name, l_name, int(year_birth), int(currentyear))
    p1.print_personal_information()
    p1.print_performance_info()

#Calling function with exersise #1
Question_1()

#Question 2)
from datetime import datetime

class Profile:

    def __init__(self, first_name, last_name, gender, year_of_birth , month_of_birth, day_of_birth, height, weight):
        today = datetime.today()
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__year_of_birth = int(year_of_birth)
        self.__month_of_birth = month_of_birth
        self.__day_of_birth = day_of_birth
        self.__height = height
        self.__weight = weight
        self.age  = int(today.year - self.year_of_birth)
        self.max_bpm = int(220 - self.age)
        self.min_range_bpm = float(self.max_bpm * 0.5)
        self.max_range_bpm = float(self.max_bpm * 0.85)
        self.bmi = round((self.__weight *0.453592)/ (self.__height*0.0254 * self.__height*0.0254),4)

    
    def get__first_name(self):
        return self.__first_name

    def set__first_name(self, first_name):
        self.__first_name = first_name
    
    first_name = property(get__first_name,set__first_name)

    def get__last_name(self):
        return self.__last_name

    def set__last_name(self, last_name):
        self.__last_name = last_name
    
    last_name = property(get__last_name,set__last_name)

    def get__year_of_birth(self):
        return self.__year_of_birth

    def set__year_of_birth(self, year_of_birth):
        self.__year_of_birth = year_of_birth
    
    year_of_birth = property(get__year_of_birth,set__year_of_birth)
    
    def get__gender(self):
        return self.__gender

    def set__gender(self, gender):
        self.__gender = gender
    
    gender = property(get__gender,set__gender)

    def get__month_of_birth(self):
        return self.__month_of_birth

    def set__month_of_birth(self, month_of_birth):
        self.__month_of_birth = month_of_birth
    
    month_of_birth = property(get__month_of_birth,set__month_of_birth)

    def get__day_of_birth(self):
        return self.__day_of_birth

    def set__day_of_birth(self, day_of_birth):
        self.__day_of_birth = day_of_birth
    
    day_of_birth = property(get__day_of_birth,set__day_of_birth)

    def get__height(self):
        return self.__height

    def set__height(self, height):
        self.__height = height
    
    height = property(get__height,set__height)

    def get__weight(self):
        return self.__weight

    def set__weight(self, height):
        self.__height = height
    
    weight = property(get__weight,set__weight)

    def print_personal_information(self):

        print("\nName: " + self.first_name + " " + self.last_name + ", Age: " + str(self.age) + 
                ", Gender: "+ self.gender + ", Birthdate: " + str(self.year_of_birth) + "/" + str(self.month_of_birth) + "/" +
                str(self.day_of_birth) + ", Height: " + str(self.height) + "[inch], Weight: " + str(self.weight) + "[lb].")

    def print_performance_info(self):
        print("Maximum BPM: " + str(self.max_bpm) + " bpm, Target Range: " 
            + str(self.min_range_bpm) + " bpm - " + str(self.max_range_bpm) + " bpm, BMI: " + str(self.bmi) + "[kg]/[m^2]\n")

    
def Question2():
        
    print("\n\t---------- Question #2 ----------\n")
    f_name = input("Enter your first name: ")
    l_name = input("Enter your lastname: ")
    gender = input("Enter your gender: ")
    year_birth = input("Enter your year of birth: ")
    month_birth = input("Enter your month of birth: ")
    day_birth = input("Enter your day of birth: ")
    height = input("Enter yout height[Inches]: ")
    weight = input("Enter yout weight[Pounds]: ")


    p1 = Profile(f_name, l_name,gender, int(year_birth), int(month_birth), int(day_birth),float(height),float(weight))
    p1.print_personal_information()
    p1.print_performance_info()

#Calling function with exersise #2
Question2()