import generic as g
import re

hello	=	[]
g.fill_list(hello,r'\w',4)
y=''
y=y.join(hello)
newString='This is madhu cool guy you know'
l=re.search(f"{y}", newString)
print(len(l))
