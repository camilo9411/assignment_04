#Assignment #4

#Question 1)

class Rates:

    def __init__(self, first_name, last_name, year_of_birth, current_year):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__year_of_birth = int(year_of_birth)
        self.__current_year = int(current_year)
        self.age  = int(current_year - year_of_birth)
        self.max_bpm = int(220 - self.age)
        self.min_range_bpm = float(self.max_bpm * 0.5)
        self.max_range_bpm = float(self.max_bpm * 0.85)


    def get__first_name(self):
        return self.__firstname

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
        print("\nName: " + self.__first_name + " " + self.__last_name + ", Age: " + str(self.age))

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

Question_1()
    