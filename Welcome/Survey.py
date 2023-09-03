import os
print(os.path.expanduser('~'))
file_location=os.path.expanduser('~')
your_name = input('what is your name? ')
file1 = open(file_location+"/Jimbot/Welcome/info.py", "w") 
file1.write('your_name="'+your_name+'"')
file1.close()
