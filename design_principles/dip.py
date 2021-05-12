# Dependency Inversion Principle

"""
The Dependency Inversion Principle states that:

a). High level module should not depend on low level modules. Both should depend on abstractions
b). Abstractions should not depend on details. Details should depend on abstractions. 

E.g.

As shown in the below code we have a class Student that we use to create Student entities and a class TeamMemberships which 
holds memberships of different students into different teams.

Now we define a high-level class Analysis where we need to find out all students belonging to the RED team. 
"""

from enum import Enum
from abc import ABCMeta, abstractmethod

class Teams(Enum):
    BLUE_TEAM = 1
    RED_TEAM = 2
    GREEN_TEAM = 3

class Student:
    def __init__(self, name):
        self.name = name

class TeamMemberships:
    def __init__(self):
        self.team_memberships = []

    def add_team_memberships(self, student, team):
        self.team_memberships.append((student, team))

class Analysis:
    def __init__(self, team_student_memberships):
        memberships = team_student_memberships.team_memberships
        for members in memberships:
            if members[1] == Teams.RED_TEAM:
                print(f'{members[0].name} is in RED team')

student_1 = Student("Radek")
student_2 = Student("Tina")
student_3 = Student("Connor")

team_memberships = TeamMemberships()
team_memberships.add_team_memberships(student_1, Teams.BLUE_TEAM)
team_memberships.add_team_memberships(student_2, Teams.RED_TEAM)
team_memberships.add_team_memberships(student_3, Teams.GREEN_TEAM)

Analysis(team_memberships)
