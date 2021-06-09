import re

zen="""Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implemention
is easy to explain,
it may be a good
idea.Namespaces
are one honking
great idea--let's
do more if those"""

m=re.findall("^If",zen,re.MULTILINE)
print(m)
