import sys
sys.path.insert(0, '../')
import library

if __name__ == '__main__':
    strings=open('set.txt', 'r').read()
    strings=filter(None, strings.split('\n')) # delete empty strings
    for string in strings: 
        result = library.brute(string)
        decoded=False
        for i, r in enumerate(result):
            if library.is_printable(r):
                decoded=True
                print('%02x : %s' % (i, r.decode()))
        if decoded==True: 
            print('Result for %s \n' % string)
        decoded=False
