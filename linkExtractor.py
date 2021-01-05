#! python3

import re
import pyperclip

linksRegex = re.compile(r'''
 https?://[a-zA-Z0-9.-]{0,100}
 /?
 [a-zA-Z0-9.=/%?$#@*(){}-]{1,200}
 
 ''', re.VERBOSE)

randomData = pyperclip.paste()
mo = linksRegex.findall(randomData)

clearFormat = '\n'.join(mo) #it will make it in nice format

pyperclip.copy(clearFormat)  #your clipboard have been updated with the result of the program

print(clearFormat)