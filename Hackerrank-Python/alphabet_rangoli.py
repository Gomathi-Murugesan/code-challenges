def print_rangoli(size):
    all_alp="abcdefghijklmnopqrstuvwxyz"
    if size>1:
        alp=all_alp[0:size]
        rangoli_size=size+((size-1)*3)
        for i in range(size-1,-1,-1):
            j=(size-1)-i
            txt='-'+alp[i]+'-'
            if j>1:
                for side in range(1,j,1):
                    txt='-'+alp[side+i]+txt+alp[side+i]+'-'
            if j!=0:
                txt=alp[size-1]+txt+alp[size-1]
            print(txt.center(rangoli_size,'-'))
        for i in range(1,size,1):
            j=(size-1)-i
            txt='-'+alp[i]+'-'
            if j>1:
                for side in range(1,j,1):
                    txt='-'+alp[side+i]+txt+alp[side+i]+'-'
            if j!=0:
                txt=alp[size-1]+txt+alp[size-1]
            print(txt.center(rangoli_size,'-'))
    else:
        print(all_alp[0])
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

