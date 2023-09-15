#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name,last_name)
        self.knowledge = []
    
    def learn(self,value):
        if not isinstance(value,str):
            raise Exception
        self.knowledge.append(value)