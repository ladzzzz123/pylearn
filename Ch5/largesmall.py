largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")

    if num == "done" : 
        break
        
    try:
        num = int(num)
        
        if smallest is None:
            smallest = num
            
        if largest is None:
            largest = num
        
        if num > largest:
            largest = num
        
        if num < smallest:
            smallest = num
        
    except: 
        print "Invalid input"
        
       
print "Maximum is", str(largest)
print "Minimum is", str(smallest)