import os
print(os.path.expanduser('~'))
file_location=os.path.expanduser('~')
pvp_passkey = input('Access Key from https://picovoice.ai ')
file2 = open(file_location+"/Jimbot/Hotword/info.py", "w")
file2.write('pvp_passkey="'+pvp_passkey+'"')
file2.close()