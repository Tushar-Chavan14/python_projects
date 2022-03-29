def milage(speed):
    if speed <= 10:
        print(" the milage of car is 30 kmpl")
    elif speed>10 and speed <=20:
        print("the milage of the vechile is 40 kmpl")
    elif speed>20 and speed <=30:
        print("the milage of the vechile is 35 kmpl")
    elif speed>30:
        print("the milage of the vechile is 32 kmpl")        

speed = int(input("enter the speed of vechile:"))

milage(speed)
