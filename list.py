#List: #collections of data, ordered and changeable

courses = ["english","biology","technology"]
print(courses)

#Access item:
courses = ["english","biology","technology"]
print(courses[0])
print(courses[2])

#change item value:
courses = ["english","biology","technology"]
courses[0] = "french"
print(courses)

#loop through a list:
courses = ["english","biology","technology"]
for x in courses:
     print(x)
	 
#check item in the list:
if "biology" in courses:
    print("yes, biology is in the list" )
	
#to see the list length
courses = ["english","biology","technology"]
print(len(courses))

#add item at the end of the list:
courses = ["english","biology","technology"]
courses.append("algo")
print(courses)

#add item at a specified index:
courses = ["english","biology","technology","algo"]
courses.insert(2,"physic")
print(courses)

##remove item:

#remove() method : remove item
courses = ["english","biology","technology","algo"]
courses.remove("biology")

#pop() method: remove index
courses = ["english","biology","technology","algo"]
courses.pop(2) # or courses.pop(): the index is not specified, it removes the last item
print(courses)

#keyword del : remove specified index
del courses[0]
print(courses)
# if we want to delete the list completely : del courses
mycourses = courses
print(mycourses)
del mycourses
#print(mycourses) : i get an error because i have just deleted the list completely

#clear() method: to empty the list
courses.clear()
print(courses) # i get an empty list

#copy method:
courses = ["english","biology","technology","algo"]
mcourses = courses.copy()
print(mcourses)

#list() method:
mycourses = list(courses)
yourcourses = list(("Kirundi", "english","french","swahili","portugais"))
print(yourcourses)

#reverse() method
yourcourses.reverse()
print(yourcourses)

#count() method: returns the number of elements with the specified value
print(mycourses.count("english"))

#extend() method: add element of a list (or any iterable like tuple,set) to the end of current list
courses = ["english","biology","technology","algo"]
yourcourses = ["Kirundi", "english","french","swahili","portugais"]
courses.extend(yourcourses)
print(courses)

#index() method: return the index of the first element with the specified value
mycourses = list(("Kirundi", "english","french","swahili","portugais"))
print(mycourses.index("french"))









