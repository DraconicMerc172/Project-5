#Justin Trebour
#COP2002.0M1
#04/11/2023
#Project 5 - Functions
#This program should allow for a practice review of IP address and their subnet masks

import random

#Creates new IP address

def generateRandomIP():
    
    address = ".".join(str(random.randint(1,223))
                            for _ in range(4)) 
    return address      

#Begins Menu for User

def main():
        
      
        print("Welcome to the IPv4 Address Practice Program!")
        print("Main Menu:")
        print("1. Identify whether an IP address is Class A, B, or C.")
        print("2. Identify what the subnet mask is for a given IP address.")
        print("3. Exit")
        choice = input("Choice:  ")
        address = generateRandomIP()

        if choice == "1":
            optionOne()

        elif choice == "2":
            optionTwo()

        elif choice == "3":
            print("Thanks for using the program. I hope you feel more comfortable with IP addressing.")
            quit()

        elif (choice != "1","2","3"):
            main()

            

#Allows for the classification of IP address without User seeing

def whatClass(address):
        
        Class = int(address.split(".", 1)[0])
        
        if (Class >= 1 and Class <= 127):
            return("A")

        elif (Class >= 128 and Class <= 191):
            return("B")

        elif (Class >= 192 and Class <= 223):
            return("C")

#Prompts user to define IP address based on Class

def optionOne():
        
        address = generateRandomIP()
      
        print("Option 1 - Identify the Class")
        print("What Class (A,B,C) is", address, "(q=quit)?")
        choiceOne = input()

        if choiceOne == "q":
              main()

        elif (whatClass(address) == choiceOne):
              print("Correct!")
              optionOne()

        elif (whatClass(address) != choiceOne):
              print("Incorrect. The correct answer is", whatClass(address))
              quit()


#Determines what Subnet Mask the IP address falls into without user seeing

def whatSM(address):
      
        Class = int(address.split(".", 1)[0])
        
        if (Class >= 1 and Class <= 127):
            return("255.0.0.0")

        elif (Class >= 128 and Class <= 191):
            return("255.255.0.0")

        elif (Class >= 192 and Class <= 223):
            return("255.255.255.0")


#Prompts User for input on Subnet Mask

def optionTwo():
     
    address = generateRandomIP()

    print("Option 2 - Provide the default subnet mask.")
    print("What is the default subnet mask for", address, "(q=quit)?")
    choiceTwo = input()

    if choiceTwo == "q":
        main()
    
    elif (whatSM(address) == choiceTwo):
         print("Correct!")
         optionTwo()

    elif (whatSM(address) != choiceTwo):
         print("Incorrect. The answer is", whatSM(address))
         quit()



if (__name__ == "__main__"):
     main()
