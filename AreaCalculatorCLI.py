# Main function

def main():
    PrintWelcomeMessage()
    print("What shape do you want to calculate the area for?\n")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    print("5. Exit the Program\n")
    shape = input("Enter the number corresponding to your choice: ")
    if shape == "1":
        CalculateCircle()
    elif shape == "2":
        CalculateRectangle()
    elif shape == "3":
        CalculateTriangle()
    elif shape == "4":
        CalculateSquare()
    elif shape == "5":
        print("Closing the program.")
        return
    else:
        print("Invalid input. Please try again.\n")
        main()

def CalculateCircle():
    print("You selected Circle.")
    radius = input("Enter the radius of the circle: ")
    if radius.isnumeric() == False:
        print("Invalid input. Please enter a numeric value for radius.")
        CalculateCircle()
    else:
        circlearea = 3.14159 * float(radius) * float(radius)
        print("\nThe area of the circle is: " + str(circlearea)+"\n")
        main()

def CalculateRectangle():
    print("You selected Rectangle.")
    longlength = input("Enter the length of the rectangle: ")
    shortlength = input("Enter the width of the rectangle: ")
    if longlength.isnumeric() == False or shortlength.isnumeric() == False:
        print("Invalid input. Please enter numeric values for length and width.")
        CalculateRectangle()
    else:
        rectanglearea = float(longlength) * float(shortlength)
        print("The area of the rectangle is: " + str(rectanglearea))
        main()

def CalculateTriangle():
    print("You selected Triangle.")
    baselength = input("Enter the base length of the triangle: ")
    heightlength = input("Enter the height of the triangle: ")
    if baselength.isnumeric() == False or heightlength.isnumeric() == False:
        print("Invalid input. Please enter numeric values for base and height.")
        CalculateTriangle()
    else:
        trianglearea = 0.5 * float(baselength) * float(heightlength)
        print("The area of the triangle is: " + str(trianglearea))
        main()

def CalculateSquare():
    print("You selected Square.")
    length = input("Enter the length of one side of the square: ")
    if length.isnumeric() == False:
        print("Invalid input. Please enter a numeric value for length.")
        CalculateSquare()
    else:
        squarearea = float(length) * float(length)
        print("The area of the square is: " + str(squarearea))
        main()


# Function which prints the welcome message
def PrintWelcomeMessage():
        print(r"""                             _____      _            _       _             
     /\                     / ____|    | |          | |     | |            
    /  \   _ __ ___  __ _  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   / /\ \ | '__/ _ \/ _` | | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  / ____ \| | |  __/ (_| | | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 /_/    \_\_|  \___|\__,_|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_| """)
        print(r"""                        Written by Dave Pitt""")
        print("")


# If name=main run main
if __name__ == "__main__":
    main()