''' Some class exercise results '''
# Exercise questions: 
# https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/content/classes/exercisesclasses.html


class Triangle: # Exercise 1

    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        return False

print("\nExercise 1:")
my_triangle = Triangle(90,30,60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

class Songs: # Exercise 2
    def __init__(self, lyrics):
        self.lyrics = lyrics
        lyrics = []
    
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
print("\nExercise 2:")
happy_bday = Songs(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])

happy_bday.sing_me_a_song()     

class Lunch: # Exercise 3
    def __init__(self, menu):
        self.menu = menu
        menu = str

    def menu_price(self):
        if 'menu 1':
            print("Your choice: ", self.menu, "Price 12.00")
        elif 'menu 2':
            print("Your choice: ", self.menu, "Price 13.40")
        else:
            print("Error Input")

print("\nExercise 3:")
Paul = Lunch("menu 1")
Paul.menu_price()


class Point3D(object): # Exercise 4
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.x} {self.y} {self.z}'

print("\nExercise 4:")
my_point = Point3D(x=1,y=2,z=3)
print(my_point)