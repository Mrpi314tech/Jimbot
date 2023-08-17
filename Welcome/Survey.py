import os
print(os.path.expanduser('~'))
file_location=os.path.expanduser('~')
your_name = input('what is your name? ')
name='Jimbot'# what do you want the name of the robot to be?
city="blah"
api="blah" 
password=input('what do you want the password to be?' )
ask_for_password=input('do you want to be asked for the password? (True/False) ')
ip_for_kasa=" "
name_for_smart_device="pnumonoultramicroscopicsilicovolcanoconiosos"
file1 = open(file_location+"/Jimbot/Welcome/info.py", "w") 
file1.write('file_location="'+file_location+'"\nyour_name="'+your_name+'"\nname="'+name+'"\ncity="'+city+'"\napi="'+api+'"\npassword="'+password+'"\nask_for_password="'+ask_for_password+'"\nip_for_kasa="'+ip_for_kasa+'"\nname_for_smart_device="'+name_for_smart_device+'"')
file1.close()
