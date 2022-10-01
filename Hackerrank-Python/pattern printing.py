def header(txt: str, width, filler='-'):
    return txt.center(width, filler)


if __name__ == "__main__":
    #N,M=int(input()),int(input()) #two separate inputs
    N,M=map(int, input().split(' ')) #split one input into two input values
    top_text='.|.'
    top_bottom = N//2
    middle= (N//2)+1
    for i in range(1,N,1):
        if (i%2)!=0:
            print(header(top_text*i, M))
    print(header('WELCOME', M))
    for i in range(N-1,0,-1):
        if (i%2)!=0:
            print(header(top_text*i, M))
