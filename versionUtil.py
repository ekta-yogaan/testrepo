import platform

version_numbers = platform.python_version().split('.')

if (version_numbers[0] == '2'):
    print "version 2"
elif (version_numbers[0] == '3'):
    print("version 3")
