from platform import platform

print(platform()) #no argument, returns the OS version

print(platform(1)) #same as above

print(platform(0, 1)) #0 means system type and 1 means detailed version info is needed




print(platform(aliased = True, terse = False))

# aliased = True (or any non-zero value) means that the program can produce alternative undelying layer names instead of the common ones

# terse = True (or any non-zero value) may convince the funtion to present briefer results (if possible)
