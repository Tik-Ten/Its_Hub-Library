"""
MIT License

Copyright (c) 2023 uǝ⊥ʞı⊥

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Its_Hub library.
This is a library with Other Libraries! (;
U Can Use This Library For Use Few Other Library. 4 Example:
Faker
CV2
Tkinter
TKHTMLVIEW
...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
My name is Farbod Parkhooi(Or you can call me Tik Ten)
This is Its_Hub doucuments: https://www.github.com/tik-ten/Its_Hub
This is my Github link: https://www.github.com/tik-ten
Thanks for use.
"""
def Return_error(error, exit_code, line): 
    print(f"""
_____________________________________________________________________________________
We have an error!                                                                   |
                                                                                    |
I think error it's:                                                                 |
{error}                                                                |
                                                                                    |
I think it's in line {line} of Its_Hub Library.                                         |
Now i quit with exit code: {exit_code}                                                        |
From Its_Hub library.                                                               |
____________________________________________________________________________________|
""")
    quit(exit_code)
def __version__():
    print("Its_Hub Library version is 0.1.0")
class Its_Hub():
    print("YOU USING ***Its_Hub*** LIBRARY FOR DO SOMETHING IN THIS CODE.")
    def Faker(target):
        try: from faker import Faker
        except ImportError: Return_error("import error. \nYou must install Faker library with: \npip3 install Faker", 0, 58)
        faker = Faker()
        try:
            if target == "first_name": return faker.first_name()
            elif target == "last_name": return faker.last_name()
            elif target == "name": return faker.name()
            elif target == "phone_number": return faker.phone_number()
            elif target == "address": return faker.address()
            elif target == "profile": return faker.profile()
            elif target == "job": return faker.job()
            elif target == "company": return faker.company()
            elif target == "website": return faker.website()
            elif target == "blood_group": return faker.blood_group()
        except AttributeError: Return_error("Attribute error. Your faker library has a problem.", 0, "61 -> 70")
    class Fake_profile():
        def __init__(self, Gender="M", Company=None, blood_group=None, website=None, username=None, name=None, sex=None, address=None, Job=None, mail=None):
            self.gender = Gender
            self.company = Company
            self.bg = blood_group
            self.website = website
            self.username = username
            self.name = name
            self.sex = sex
            self.address = address
            self.job = Job
            self.mail = mail
        def Create_profile(self):
            from faker import Faker
            faker = Faker()
            profile = faker.profile(sex=f"{self.gender}")
            del profile["ssn"]
            del profile["residence"]
            del profile["current_location"]
            del profile["birthdate"]
            if self.job != None: profile["job"] = self.job
            elif self.company != None: profile["company"] = self.company
            elif self.bg != None: profile["blood_group"] = self.bg
            elif self.website != None: profile["website"] = self.website
            elif self.username != None: profile["username"] = self.username
            elif self.name != None: profile["name"] = self.name
            elif self.sex != None: profile["sex"] = self.sex
            elif self.address != None: profile["address"] = self.address
            elif self.mail != None: profile["mail"] = self.mail
            result = list(profile.values())
            if self.website == None: result[3] = result[3][0]
            return result
        def Create_result(self, result):
            from tkinter import Tk, Frame, Label 
            from tkhtmlview import HTMLLabel
            root = Tk()
            label = HTMLLabel(root, html=f"""
____________________________________________
<br /> Created by <b>Tik Ten</b>
<br />Github: <b>Github.com/tik-ten</b> 
<h3> Information: </h3>
Job: <b>{result[0]}</b> <br />
Company: <b>{result[1]}</b> <br />
Blood group: <b>{result[2]}</b> <br />
Website: <b>{result[3]}</b> <br />
Username: <b>{result[4]}</b> <br />
Name: <b>{result[5]}</b> <br />
Sex: <b>{result[6]}</b> <br />
Address: <b>{result[7]}</b> <br />
Mail: <b>{result[8]}</b> <br /> 
____________________________________________
""")
            label.pack(pady=20, padx=20)
            root.resizable(False, False)
            root.geometry("400x500")
            root.title("Your fake profile is ready!")
            root.mainloop()
    class Mini():
        def Plus(number, plus):
            try: return number + int(plus)
            except: Return_error("Value error. Plus isn't int!", 0, 132)
        def Count(start_number, range_num):
            try: 
                start_number = int(start_number)
                range_num = int(range_num)
            except ValueError: Return_error("Value error. Start_number or range_num isn't int!", 0, 137)
            for i in range(range_num):
                start_number = start_number + 1
            return start_number
    class SQL():
        def __init__(self, Table_name, Table_Attributes, Database_address="", Database_name="database"):
            self.Table_name = Table_name
            self.Table_Attributes = Table_Attributes
            self.Address = Database_address
            self.Name = Database_name
        def Create_database(self):
            try: import sqlite3 as SQL
            except ImportError: Return_error("Import error. You must install sqlite3.", 0, 149)
            connect = SQL.connect(self.Address + self.Name + ".db")
            connect.close()
        def Create_Table(self):
            try: import sqlite3 as SQL
            except ImportError: Return_error("Import error. You must install sqlite3.", 0, 154)
            connect = SQL.connect(self.Address + self.Name + ".db")
            cursor = connect.cursor()
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.Table_name} ({self.Table_Attributes});""")
            connect.commit()
            connect.close()
        def Save_in_database(self, Attributes):
            try: import sqlite3 as SQL
            except ImportError: Return_error("Import error. You must install sqlite3.", 0, 162)
            connect = SQL.connect(self.Address + self.Name + ".db")
            cursor = connect.cursor()
            cursor.execute(f"""INSERT INTO {self.Table_name} ({self.Table_Attributes})
                            VALUES ({Attributes})""")
            connect.commit()
            connect.close()
        def Read_database(self, SELECT, WHERE=None):
            try: import sqlite3 as SQL
            except ImportError: Return_error("Import error. You must install sqlite3.", 0, 171)
            connect = SQL.connect(self.Address + self.Name + ".db")
            cursor = connect.cursor()
            cursor.execute(f"""SELECT {SELECT} FROM {self.Table_name} WHERE {WHERE};""")
            return str(cursor.fetchall()[0][0])
    class Computer_Vision():
        def Start_video(none, VideoCapture=0, Show=True, exit_button="q"):
            try: import cv2 as cv 
            except ImportError: Return_error("Import error.  You must install opencv library with: \npip install opencv-python", 0, 179)
            cap = cv.VideoCapture(VideoCapture)
            while True:
                _, frame = cap.read()

                if Show == True: cv.imshow("Its webcam video! from Its_Hub library.", frame)
                else: pass
                cv.waitKey(1)
                if cv.waitKey(1) & 0xFF == ord(exit_button): 
                    break
            cap.release() 
            cv.destroyAllWindows()
