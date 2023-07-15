myString = "Doesn't"
print(myString)

mystring = 'doesn\'t'
print(mystring)
nextline = "line1 \nline2"
print(nextline)

sameline = "line 1 line 2"
print(sameline)
tabbed = "space1\tspace2\tspace3"
print(tabbed)
path = r"C:\Users\Milton.Omondi\OneDrive - LVCT Health\Documents"
print (path)

path2 = r'C:\Users\Milton.Omondi\OneDrive - LVCT Health\Documents\Zoom'
print (path2)

multiline = """\
    EPL Standings
    Team    Matches Played  Won Drawn   Lost    Point
    Arsenal     10  8       8   0       0       24
    Man City    10  10      1   0       9       3
    Madrid      10  6       4   1       1       13
"""
print(multiline)
quotes = ('Allan: "It was nice meeting you". '
         'Jane: "Same here"')
print(quotes)
print("My age" " is 102")

name1 = "Tonny"
name2 = "Uhuru"
name3 = "Abby Dani"
FullName = name1 + " " + name2 + " " + name3
print(FullName)

print("My name is", FullName)
# Access string characters
firstChar = FullName[0]
print("My name is starts with letter", firstChar)
secondChar = FullName [6]
print("My second name starts with letter", secondChar)
nameLength = len(FullName)
print(nameLength)
lastChar = FullName[nameLength-1]
print(lastChar)







