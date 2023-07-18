from platform import python_implementation, python_version_tuple

print(python_implementation())

for attribute in python_version_tuple():
    print(attribute)

# prints the version tuple line by line 
