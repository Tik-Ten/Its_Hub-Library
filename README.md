# Version: 0.1.6

<h1>Intro </h1>
<p>
Its_Hub library. <br />
This is a library with Other Libraries! (; <br />
U Can Use This Library For Use Few Other Libraries. 4 Example:
<b>
<ul>
    <li>Faker</li>
    <li>Tkinter</li>
    <li>CV2</li>
    <li>Tkhtmlview</li>
    <li>sqlite3 </li>
    <li>...</li>
</ul>
</b>

My name is Farbod Parkhooi(Or you can call me Tik Ten) <br />
This is my Github link: <a href="https://www.github.com/tik-ten/">`https://www.github.com/tik-ten/`</a> <br />
Thanks for use.<br />
</p>

# How to install
For download this library:
```git
>>> git clone https://github.com/Tik-Ten/Its_Hub.git
>>> cd Its_Hub
>>> pip install -r requirements.txt
>>> python setup.py <Your python libraries address>
>>> cd ...
>>> rmdir /s Its_Hub
```
example for python libraries address: <b>"C:/Users/Farbod Parkhooi/AppData/Local/Programs/Python/Python311/Lib" </b>
You must remove the Its_Hub directory to install other updates

# How to remove
To remove this app:
```git
>>> cd Its_Hub
>>> python remove.py <Your python libraries address>
```
example for python libraries address: <b>"C:/Users/Farbod Parkhooi/AppData/Local/Programs/Python/Python311/Lib" </b>

# Check
```Python
from Its_Hub import Its_Hub
Its_Hub.__version__()
# Output:
Its_Hub Library version is 0.0.9
```

# How to use ... library
<ul>
    <li><a href="#Faker">Faker</a></li>
    <li><a href="#Fake_profile">Fake_profile</a></li>
    <li><a href="#Mini">Mini</a></li>
    <li><a href="#SQL">SQL </a></li>
    <li><a href="#Computer_Vision">Computer_Vision </a></li>
    <li><a href="#Voice">Voice</a></li>
    <li><a href="#QR">QR</a></li>
    <li><a href="#Web">Web</a></li>
</ul>

<h2>Use Libraries </h2>
    For use Its_Hub you can use This:

```Python
from Its_Hub import Its_Hub
hub = Its_Hub()
````

# Faker
For use Faker:
```Python
Its_Hub.Faker(target="") # "first_name" or "last_name" or "name" or "phone_number" or "address" or "profile" or "job" or "Company" or "website" or "blood_group"

# You can print that:
print(Its_Hub.Faker(target="name"))
# and you can save that in a value
name = Its_Hub.Faker(target="name") 
```

# Fake_profile 
### Show a digital fake profile
```Python
profile = hub.Fake_profile() # You can customize job, company, name, and ...
profile.Create_result(profile.Create_profile()) 
```
output:

<img src="Files\out1.png">

### Create list of a fake profile
```Python
profile = hub.Fake_profile()
Profile_list = profile.Create_profile()
print(Profile_list)
```
# Mini
### Plus
You can use this function for num1 + num2 (:
```python
result = hub.Mini.Plus(number=8, plus=10)
print(ans)
```
### Count
You can count and plus with this function.
```Python
count_ans = hub.Mini.Count(0, 5)
print(count_ans)
```

# SQL
### Create_database
```Python
sql = hub.SQL("Users", "'Name', 'Email', 'Password'") # You must write Table_name and Table_Attributes and you can write the Database_address, and Database_name
sql.Create_database()
```

### Create_Table
```Python
sql = hub.SQL("Users", "'Name', 'Email', 'Password'") # You must write Table_name and Table_Attributes and you can write the Database_address, and Database_name
sql.Create_Table()
```

### Save_in_database
```Python
sql = hub.SQL("Users", "'Name', 'Email', 'Password'") # You must write Table_name and Table_Attributes and you can write the Database_address, and Database_name
sql.Save_in_database("'Farbod Parkhooi', 'your@email.com', 'Example@2023'")
```

### Read_database
```Python
sql = hub.SQL("Users", "'Name', 'Email', 'Password'") # You must write Table_name and Table_Attributes and you can write the Database_address, and Database_name
search_result = sql.Read_database("Email", "Name='Farbod Parkhooi'")
print(search_result)
```

# Computer_Vision
In this class, I use CV2 and CVZone to use a computer webcam.

### Start_Video
```Python
cv = hub.Computer_Vision()
cv.Start_video(VideoCapture=0, Show=True, exit_button="q")
```

### Detect Hand

```Python
cv = hub.Computer_Vision()
cv.Start_video(VideoCapture=0, Show=True, exit_button="q", Detect_Hands=True)
```
output: <br>
<img src="Files\out3.png" />

### Detect Faces
```Python
cv = hub.Computer_Vision()
cv.Start_video(VideoCapture=0, Show=True, exit_button="q", Detect_Faces=True)
```
output: <br>
<img src="Files\out4.png" />

### Detect Pose
```Python
cv = hub.Computer_Vision() 
cv.Start_video(VideoCapture=0, Show=True, exit_button="q", Detect_Pose=True)
```

# Voice

### Say
```Python
voice = hub.Voice("You text here", speed=125, gender="M") # for gender you can use F too
voice.Say()

# Also you can save the generated voice
voice.Say(save_voice=True, File_name="voice.mp3")
```

# QR

### Create_QR
```Python
qr = hub.QR()
qr.Create_QR(Data="https://www.github.com/tik-ten/Its_Hub/", name="qrcode.png")
```
output: <br>
<img src="Files\out5.png">

# Web

### Open_website
```Python
hub.Web.Open_website(URL="https://simple.wikipedia.org/w/index.php?title=User%3AFarbod_Parkhooi%2FIts_Hub_Library")
```

# Links
<ul>
    <li><a href="https://simple.wikipedia.org/w/index.php?title=User%3AFarbod_Parkhooi%2FIts_Hub_Library">Wikipedia</a></li>
    <li><a href="https://www.aparat.com/ImRick">Aparat</a></li>
</ul>  
