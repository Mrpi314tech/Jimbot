import os
import new_words as aword
import new_com as acom
file_location=os.path.expanduser('~')
print('note: if using quotes, use single quotes')
nwordl=aword.word
ndefl=aword.defi
nwcoml=acom.word
nrunl=acom.com
file_location=os.path.expanduser('~')
qstn=input(" are you adding a command, music, words, website, or would you like to remove words? ")
qstn=qstn.lower()
if 'com' in qstn or 'Com' in qstn:
    kwordc=input("what is the keyword? (what do you want to say to run the command?)").lower()
    outputc=input("what command do you want to run?")
    outc='os.system("'+outputc+'")'
    nwcoml.append(kwordc.lower())
    nrunl.append(outputc)
    file1 = open(file_location+"/Jimbot/Python/new_com.py", "w")
    file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
    file1.close()
elif 'wor' in qstn or 'Wor' in qstn:
    kwordw=input("what is the keyword? (what do you want to say so that he says this?)").lower()
    outputw=input("what do you want him to say?")
    nwordl.append(kwordw.lower())
    ndefl.append(outputw)
    file1 = open(file_location+"/Jimbot/Python/new_words.py", "w")
    file1.write("word="+str(nwordl)+"\ndefi="+str(ndefl))
    file1.close()
elif 'mus' in qstn or 'Mus' in qstn:
    kwordc=input("what is the keyword? (what do you want to say to play the music?)").lower()
    outputc=input("what is the file location for the music and the name?")
    outc='xdg-open '+outputc+' &'
    nwcoml.append(kwordc)
    nrunl.append(outc)
    file1 = open(file_location+"/Jimbot/Python/new_com.py", "w")
    file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
    file1.close()
elif 'web' in qstn:
    kwordc=input("what is the keyword? (what do you want to say to open the website?)").lower()
    outputc=input("what is the url?")
    outc='os.system("'+outputc+'")'
    nwcoml.append(kwordc.lower())
    if 'http' in outputc:
        outputc='xdg-open '+outputc
    else:
        outputc='xdg-open http://'+outputc
    nrunl.append(outputc)
    file1 = open(file_location+"/Jimbot/Python/new_com.py", "w")
    file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
    file1.close()
elif 'rem' in qstn:
    print('here is a list of the words: ')
    seelist=0
    while True:
        try:
            print(nwordl[seelist]+" -- "+ndefl[seelist])
            seelist+=1
        except IndexError:
            break
    seelist=0
    while True:
        try:
            print(nwcoml[seelist]+" -- "+nrunl[seelist])
            seelist+=1
        except IndexError:
            break
    removew=input("what word/command are you removing? ")
    seelist=0
    while True:
        try:
            if nwordl[seelist]==removew:
                print(nwordl[seelist])
                nwordl.remove(nwordl[seelist])
                ndefl.remove(ndefl[seelist])
                file1 = open(file_location+"/Jimbot/Python/new_words.py", "w")
                file1.write("word="+str(nwordl)+"\ndefi="+str(ndefl))
                file1.close()
                break
            else:
                seelist+=1
        except IndexError:
            seelist=0
            while True:
                try:
                    if nwcoml[seelist]==removew:
                        nwcoml.remove(nwcoml[seelist])
                        nrunl.remove(nrunl[seelist])
                        file1 = open(file_location+"/Jimbot/Python/new_com.py", "w")
                        file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
                        file1.close()
                        break
                    else:
                        seelist+=1
                except IndexError:
                    print('word/command not found!')
                    break
            break
