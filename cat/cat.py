import sys

try:
    file = sys.argv[1]

    try:
        f = open(file, 'r')

        print(f.read())
    except:        
        print(f'{file} not found')
except:
    print('No Argument')


