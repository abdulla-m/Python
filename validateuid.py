
import re
import sys

uids=[input() for _ in range(int(input()))]

for uid in uids:
    isvalid=False
    repeatingChars=False
    
    for c in uid:
        if uid.count(c) > 1:
            repeatingChars = True
            break
    if not repeatingChars:
        if len(uid)==10:
            if len(re.findall("[A-Z]",uid)) >= 2:
                if len(re.findall("[0-9]",uid)) >= 3:
                    if not re.search("[^a-zA-Z0-9]",uid):
                            isvalid=True
                            print("Ialid")

    if not isvalid:
        print("invalid")
