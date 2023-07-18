lines=6  
i=1  
j=1  
while i<=lines: # this loop is used to print the lines  
    j=1  
    while j<=i:  # this loop is used to print lines  
        temp=i*j  
        print(temp, end='', flush=True)  
        print(" ", end='', flush=True)  
        j=j+1;  
    print("");  
    i=i+1;  