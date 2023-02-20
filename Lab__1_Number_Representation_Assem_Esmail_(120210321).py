#Name: Assem Esmail #Id: 120210321
#Date: 20/2/2023
check_input = True #Check if user input is valid
while check_input: #Loop until user input is valid
    a, b, c = eval(input("Please enter the a, b, c coefficients of your quadratic equation: ")) #Get user input for equation coefficients (a , b, c) 
    try: 
        float(a), float(b), float(c) 
        check_input = False 
    except ValueError: 
        print("Please make sure the coefficients are real numbers and try again") 
        check_input = True 

discriminant = b**2 - 4*a*c #Calculate discriminant
if discriminant < 0: #Check if discriminant is negative
    print("There are no real solutions") #If discriminant is negative, there are no real solutions
elif discriminant == 0: #Check if discriminant is zero
    print("There is one solution: {}".format(-b/(2*a))) #If discriminant is zero, there is one solution (x = -b/2a)
else: #If discriminant is positive, there are two solutions
    print("There are two solutions: {} and {}".format((-b + discriminant**0.5)/(2*a), (-b - discriminant**0.5)/(2*a))) #Calculate and print solutions
