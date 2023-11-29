import os
print(os.path.expanduser('~'))
file_location=os.path.expanduser('~')
pvp_passkey = input('What is your Picovoice Access Key?')
file2 = open(file_location+"/Jimbot/Hotword/info.py", "w")
file2.write('pvp_passkey="'+pvp_passkey+'"')
file2.close()