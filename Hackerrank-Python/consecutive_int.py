
#second method

#if __name__ == '__main__':
#    n = int(input())
#    output=[]
#    for i in range(n):
#        output.append(i+1)
#        output1=''.join(str(a) for a in output)
#    print(output1)



#one method
if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1),sep='')
    
