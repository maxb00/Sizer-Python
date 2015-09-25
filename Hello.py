print ("Init sucessful")
run = True
goAgain = 1
while run == True & goAgain == 1:
    print ("Testing with Python and Git...")
    fdbck = input("How are we doing? ")
    print ("Thank you for the '"+fdbck+"'")
    print ("I welcome any feedback, I'll get there eventually!")
    again = input("Anything more to say? Want to try again? (yes/no)")
    if input == "yes":
        goAgain = 1
    else:
        run = False
        goAgain = 0

