import textwrap

def wrap(string, max_width):
    ans=[]
    for i in range(0,len(string),max_width):
        ans.append(string[i:i+max_width])     
    return "\n".join(ans)  ### joins the ans output in new line
##    return " ".join(ans) ## joins the ans output in one line with space" "

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
##  the inputs are  ABCDEFGHIJKLIMNOQRSTUVWXYZ

 ##   4    

### output is like 

  #  ABCD

   # EFGH

   #	IJKL

   # IMNO

   # QRST

   # UVWX

  #  YZ
