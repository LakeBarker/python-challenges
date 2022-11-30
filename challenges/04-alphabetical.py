# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
string = "Berserk"

li = []
l = len(string)

for i in range (0,1):
    li.append(string[i])

for i in range(0,1):
    for j in range(0,1):
        if li[i]<li[j]:
            li[i],li[j]=li[j],li[i]
j=""

for i in range(0,1):
    j=j+li[i]

print(j)