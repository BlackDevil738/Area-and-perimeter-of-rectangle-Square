class Area_and_Perimeter:
    #Function To Define Wheather it is a Square Or Rectangle
    def Square_rectangle(length,breadth):
        if length == breadth:
            return "It's A Square"
        else :
            return  "It's A Rectangle"


    #Function to Find Area
    def Area(length,breadth):
        Area = length*breadth
        return Area


    #Function to find perimeter of Square
    def Perimeter_square(length):
        if length == breadth:
            Perimeter = 4*length
            return Perimeter
        else:
            return "It's a Rectangle Not a Square"
        
    #Function to find perimeter of Rectangle
    def Perimeter_rectangle(length,breadth):
        if length == breadth:
            return "It's a Square Not a Rectangle"
        else:
            Perimeter = 2*length+breadth
            return Perimeter



while True:
    length = int(input("Length = "))
    breadth = int(input("Breadth = "))
    X = Area_and_Perimeter
    print(X.Square_rectangle(length,breadth))
    print("To Find Area press 1\nTo Find Perimeter press 2")
    a = int(input())
    if a == 1:
        print("Area Of The Given Length and Breadth = ",X.Area(length,breadth))
    elif a == 2:
        print("To Find The Perimeter of Squre Press 1\nTo Find The Perimeter of Rectangle Press 2 ")
        b = int(input())
        if b == 1:
            print("Peremeter of Square = ",X.Perimeter_square(length))
        elif b == 2:            
            print("Peremeter Of Rectangle = ",X.Perimeter_rectangle(length,breadth))
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
    print("TO Exit From The Code Press E")
    Quit = input().upper()
    if Quit == "E":
        break
    else:
        pass

    

        
    
