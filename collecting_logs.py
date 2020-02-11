    
b = 0
z = 0
with open("logs.txt") as f:    
    for i in f:
        if "png" in i:
            b = b +1
        elif "jpg" in i:
            z = z + 1
    print ("png" + " =", b)
    print ("jpg" + " =" , z)
            
            
