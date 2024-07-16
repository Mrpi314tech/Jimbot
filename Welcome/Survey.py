import os
import Classy
print(os.path.expanduser('~'))
file_location=os.path.expanduser('~')
your_name = input('what is your name? ')
api_key = input('what is your OpenAI API key? ')
Classy.download()
file1 = open(file_location+"/Jimbot/Welcome/info.py", "w") 
file1.write('your_name="'+your_name+'"\n'+'api_key="'+api_key+'"')
file1.write('\npvp_passkey="'+pvp_passkey+'"')
file1.close()
