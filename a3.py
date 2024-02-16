A2a

import re
emailRegex=re.compile(r'''([a-zA-Z0-9._%+-]+ @[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''',re.VERBOSE)
matches=[]
text="xyz@gmail.com and abc_987@vvce.ac.in are the mail IDs."
for groups in emailRegex.findall(text):
    matches.append(groups[0])
print(matches)