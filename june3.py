def a1(n):
    for i in range(n+1):
        for j in range(n):
            print("*" , end = " ")
        print()

def a2(n):
    for i in range (n+1):
        for j in range (1,i+1):
            print( "*", end=" ")
        print()

def a3(n):
    for i in range (n+1):
        for j in range (1,i+1):
            print( j, end=" ")
        print()

def a4(n):
    for i in range (n+1):
        for j in range (1,i+1):
            print( i, end=" ")
        print()
        
def a5(n):
    for i in range (n,0,-1):
        for j in range (i):
            print ( "*", end=" ")
        print()
        
def a6(n):
    for i in range (n+1,1,-1):
        for j in range(1,i):
            print(j,end=" ")
        print()
    
def a7(n):
    for i in range (n):
        for a in range (n-i-1):
            print(" ", end= "")
        for b in range (i*2+1):
            print("*", end = "")
        for c in range (n-i-1):
            print(" ", end = "")
        print()
        
def a8(n):
    for i in range (n):
        for a in range (i):
            print(" ", end= "")
        for b in range (2*n - (i*2+1)):
            print("*", end = "")
        for c in range (i):
            print(" ", end = "")
        print()
        
def a9(n):
    for i in range (n):
        for j in range (n-i-1):
            print(" ", end ="")
        for j in range (2*i+1):
            print ("*", end="")
        for j in range (n-i-1):
            print(" ",end="")
        print()
    for i in range (n-1,-1,-1):
        for j in range (n-i-1):
            print (" ", end="")
        for j in range (2*i+1):
            print("*", end="")
        for j in range (n-i-1):
            print (" ", end="")
        print()
    
def a101(n):
    for i in range (1,n+1):
        for j in range (i):
            print("*", end="")
        print()
    for i in range (n-1,0,-1):
        for j in range (i):
            print("*",end="")
        print()
        
def a102(n):
    for i in range (2*n):
        s=i
        if i>n:
            s=2*n-i
        for j in range (s):
            print("*", end="")
        print()
        
def a11(n):
    for i in range (1,n+1):
        for j in range (i):
            if i%2==0:
                if j%2==0:
                    print("0", end="")
                else:
                    print("1", end="")
            else:
                if j%2==0:
                    print("1", end="")
                else:
                    print("0", end="")
        print()
        
        
def a12(n):
    for i in range (1,n+1):
        for j in range (1,i+1):
            print (j, end="")
        space=2*(n-i)
        print(" " * space, end="")
        for j in range (i,0,-1):
            print(j, end="")
        print()    
        
def a13(n):
    a=1
    for i in range (1,n+1):
        for j in range(i):
            print(a, end=" ")
            a+=1
        print()
        
def a14(n):
    for i in range (1,n+1):
        al=ord('A')
        for j in range (i):
            print(chr(al), end="")
            al+=1
        print()
        
def a15(n):
    for i in range (n,0,-1):
        al=ord('A')
        for j in range (i):
            print(chr(al), end="")
            al+=1
        print()
        
def a16(n):
    al=ord('A')
    for i in range (1,n+1):
        for j in range (i):
            print(chr(al), end="")
        al+=1
        print()
        
        
def a17(n):
    for i in range (1,n+1):
        for j in range (n-i):
            print(" ", end="")
        al=ord('A')
        for j in range (2*i-1):
            print(chr(al), end="")
            if (j<i-1): al+=1
            else: al-=1
        print()
      
def a18(n):
    for i in range (1,n+1):
        al=ord('E')
        for j in range(i,0,-1):
            print(chr(al-j+1),end="")
        print()
            
def a19(n):
    for i in range (n):
        for j in range (n-i):
            print("*", end="")
        for j in range (i*2):
            print(" ", end="")
        for j in range (n-i):
            print("*", end="")
        print()
    for i in range (n-1,-1,-1):
        for j in range (n-i):
            print("*", end="")
        for j in range (i*2):
            print(" ", end="")
        for j in range (n-i):
            print("*", end="")
        print()
        
def a20(n):
    for i in range (1,2*n+1):
        s=i
        if s<=n:
            s=i
        else: s=2*n-i
        for j in range(s):
            print("*", end="")
        for j in range (2*n-2*s):
            print(" ", end="")
        for j in range (s):
            print("*", end="")
        print()

def a21(n):
    for i in range (n):
        for j in range (n):
            if (i==0 or j==0 or i==n-1 or j==n-1) :
                print("*", end=" ")
            else: print(" ", end=" ")
        print()
        
def a22(n):
    for i in range (2*n-1):
        for j in range (2*n-1):
            top=i
            left=j
            bottom=(2*n-2)-i
            right=(2*n-2)-j
            print(n-min(top,left,bottom,right), end="")
        print()
            
    
    
        
n=int(input("enter the number"))
a22(n)


# abc=ord('A')
# print(chr(abc))
# abc+=1
# print(chr(abc))
