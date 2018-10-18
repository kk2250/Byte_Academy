import sqlite3
import os
import time

class Database:
	def __init__(self,database_name):
		self.connection = sqlite3.connect(database_name,check_same_thread=False)
		self.cursor = self.connection.cursor()
	def __enter__(self):
		return self
	def __exit__(self,type,value,traceback):
		if self.connection:
			self.connection.commit()
			self.cursor.close()
			self.connection.close()
		else:
			random_assignment = 1

    def add_class(subject,room,t_id,capacity,c_id):
        self.cursor.execute(
            """INSERT INTO Class(
                subject,
                room,
                t_id,
                capacity,
                c_id
            ) VALUES(
                {subject},
                {room},
                {t_id},
                {capacity},
                {c_id}
            );""".format(
                subject=subject,
                room=room,
                t_id=t_id,
                capacity=capacity,
                c_id=c_id
            )
            
            )
            
    def add_teacher(first,last,homeroom,subj,phone,age,email):
        cursor.execute(
            """INSERT INTO Teacher(
                first,
                last,
                homeroom,
                subj,
                phone,
                age,
                email
            ) VALUES(
                {first},
                {last},
                {homeroom},
                {subj},
                {phone},
                {age},
                {email}
            );""".format(
                first=first,
                last=last,
                homeroom=homeroom,
                subj=subj,
                phone=phone,
                age=age,
                email=email
            )
    
            )
    def add_student(first,last,gpa,homeroom,year,contact,absences):
        cursor.execute(
            """INSERT INTO Student(
                first,
                last,
                gpa,
                homeroom,
                year,
                contact
            ) VALUES(
                {first},
                {last},
                {gpa},
                {homeroom},
                {year},
                {contact}
            );""".format(
                first=first,
                last=last,
                gpa=gpa,
                homeroom=homeroom,
                year=year,
                contact=contact,
            )
    
            )
    def lookup_all(string):
        cursor.execute(
            """SELECT * FROM {string};""".format(
                string=string
            )
