import os
import sys

user = os.getlogin()
path = f'/home/{user}'

def find_file(filename):
    for root, dirs, files in os.walk(path):
        if filename in files:
            return os.path.join(root)
    return None
try:
    if __name__ == '__main__':
        filename = sys.argv[1]

        result = find_file(filename)

        if result:
            print(result)

        else:
            print(f'{filename} Not Found')

except:
    print('No Argument')
