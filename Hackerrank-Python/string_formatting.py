from decimal import *

def print_formatted(number):
    l=len(bin(number))-2
    for i in range(1,number+1,1):
        out=[]
        out.append(str(i).rjust(l,' '))
        oct_number=oct(i)
        out.append(str(oct_number[2:]).rjust(l,' '))
        hex_number=hex(i)
        out.append(str(hex_number[2:]).upper().rjust(l,' '))
        bin_number=bin(i)
        out.append(str(bin_number[2:]).rjust(l,' '))
        print (' '.join(out))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
