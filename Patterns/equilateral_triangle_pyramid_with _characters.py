print("Print equilateral triangle Pyramid with characters : ")  
s = 5  
asciiValue = 65  
m = (2 * s) - 2  
for i in range(0, s):  
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1  
    for j in range(0, i + 1):  
        alphabate = chr(asciiValue)  
        print(alphabate, end=' ')
        asciiValue += 1  
    print()
    
    

    
    
#Output
    
#     Print equilateral triangle Pyramid with characters :
#         A 
#        B C 
#       D E F 
#      G H I J 
#     K L M N O
