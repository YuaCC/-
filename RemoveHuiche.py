import time
import sys
import os
import re
sys.path.append(os.path.abspath("SO_site-packages"))
import pyperclip 
new_value = ""
old_value = ""
reg=re.compile(r"[\r\n]+")
while True:
    new_value = pyperclip.paste()
    if new_value != old_value:
        new_value=reg.sub(" ", new_value)
        pyperclip.copy(new_value)
        print(new_value)
        old_value=new_value
    time.sleep(0.1)