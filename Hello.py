print ("Init sucessful")
run = True
while run == True:
    choice = input("What functionality do you want? Abs Value Finder, Feedback, or Exit?")

    if choice == "Feedback" or choice == "feedback":
        print ("Testing with Python and Git...")
        fdbck = input("How are we doing? ")
        print ("Thank you for the '"+fdbck+"'")
        print ("I welcome any feedback, I'll get there eventually!")

    elif choice == "Maths" or choice == "maths":
        print("Absolute Value Finder + Other Math init sucessful")
        print(abs(int(input("What number do you want the absolute value of?"))))

    else:
        run = False
#end