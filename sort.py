def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = False 
    is_heavy = False

    if volume >= 1000000 or width >= 150 or height >= 150 or length >= 150:
        is_bulky = True
    
    if mass >= 20:
        is_heavy = True

    if is_heavy and is_bulky:
        return "rejected"
    elif is_bulky or is_heavy:
        return "special"
    else:
        return "standard"
    
# standard not bulky, not heavy
print(sort(100, 100, 100, 10))  
# special bulky, not heavy
print(sort(200, 50, 50, 10)) 
# special not bulky, but heavy   
print(sort(100, 100, 100, 25)) 
 # reject bulky and heavy 
print(sort(200, 200, 200, 25)) 

