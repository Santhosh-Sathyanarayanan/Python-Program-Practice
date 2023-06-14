def check_multiples(num):
    if(num%3==0 and num%5==0):
        print("Zoom")
    elif(num%3==0):
        print("Zip")
    elif(num%5==0):
        print("Zap")
    else:
        print("Invalid")

check_multiples(30)