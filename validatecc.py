import re
import sys

uids=[input() for _ in range(int(input()))]

for uid in uids:
    isValid=False           
    if re.search(r"^[456]([\d]{15}|(\d{3})-(\d{4})-(\d{4})-(\d{4}))", uid):
        if not re.search(r"([\d])\1\1\1", uid.replace("-","")):
            isValid=True
    
    if isValid:
        print("Valid")
    else: 
        print("Invalid")
