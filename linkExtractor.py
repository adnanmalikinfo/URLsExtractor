#! python3
import re
import pyperclip

linksRegex = re.compile(r'''
 https?://[a-zA-Z0-9.-]{0,100}
 /?
 [a-zA-Z0-9./%?$#@*(){}-]{1,200}
 
 ''', re.VERBOSE)

randomData = pyperclip.paste()
mo = linksRegex.findall(randomData)

clearFormat = '\n'.join(mo)
pyperclip.copy(clearFormat)
print(clearFormat)