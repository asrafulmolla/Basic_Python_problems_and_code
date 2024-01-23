subject=["c","c++","python","java","android","toc"]
print(len(subject)) #list er size print korbe
subject.append("asraful") #list last e data added
print(subject)
subject.insert(3,"OS") #3 number index e "OS" add koebe.
print(subject)
subject.remove("asraful") #list theke "asraful" remove kore dibe
print(subject)
subject.sort() # A-Z,a-z & 1-..... akare sort korbe
print(subject)
subject.reverse() # list er item gula reverse akare print korbe
print(subject)
subject.pop() #last er item ta remove kore dibe
print(subject)
subject2=subject.copy() # subject vitore subject er item gula copy korbe
print(subject)
pos=subject.index("python") #list er item er position print korbe 
print(pos)
pos=subject.count("python")
print(pos) #item ta list e koy bar use kora hoyese ta print korbe
subject.clear() #list er item gula clear kore dibe
print(subject)