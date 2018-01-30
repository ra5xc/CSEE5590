import re

def main(): #Main function

    password=input_user() #calling the functipn to get input from the user and storing it in variable password
    length_password= len(password) #finding the length of the password the user has input

    #print length_password
    len_condition=(len(password)<6) or (len(password)>16) #to check whether length condition is true or not
    #print(len_condition)
    num_condition=(num_in_string(password)!=True)#to check whether numeric condition is true or not
    #print(num_condition)
    special_condition=(("$"not in password) and ("@" not in password) and ("!"not in password) and ("*" not in password))#to check whether special character condition is true or not
    #print(special_condition)
    lowercase_cond=((lower_case(password)!="True") or( upper_case(password)!="True")) #to check whether lower case condition is true or not
    #print(lowercase_cond)


    #loop to check which all condition is not satisfied and accordingly asking the user to input password
    while (len_condition==True and num_condition== True and special_condition==True and lowercase_cond==True):
        print("The password length should be in range 6-16 characters\n"
              "The password should have atleast one number\n"
              "The password should have atleast  one special character in [$@!*]\n"
              "The password should have atleast  one lowercase and atleast  one uppercase character\n")
        password=ask_cont()

    while (num_condition== True and lowercase_cond==True):
        print(
              "The password should have atleast one number\n"
              "The password should have atleast  one lowercase and atleast  one uppercase character\n")
        password=ask_cont()

    while (len_condition==True and num_condition== True and special_condition==True ):
        print("The password length should be in range 6-16 characters\n"
              "The password should have atleast one number\n"
              "The password should have atleast  one special character in [$@!*]\n")
        password= ask_cont()



    while (len_condition==True and num_condition== True) :
        print("The password length should be in range 6-16 characters\n"
              "The password should have atleast one number\n")
        password=ask_cont()

    while (num_condition== True and special_condition==True and lowercase_cond==True):
        print(
              "The password should have atleast one number\n"
              "The password should have atleast  one special character in [$@!*]\n"
              "The password should have atleast  one lowercase and atleast  one uppercase character\n")
        password=ask_cont()

    while  (special_condition==True and lowercase_cond==True):
        print(
              "The password should have atleast  one special character in [$@!*]\n"
              "The password should have atleast  one lowercase and atleast  one uppercase character\n")
        password=ask_cont()

    while (num_condition== True and special_condition==True ):
        print(
              "The password should have atleast one number\n"
              "The password should have atleast  one special character in [$@!*]\n"
              )
        password=ask_cont()

    while (len_condition==True and lowercase_cond==True):
        print("The password length should be in range 6-16 characters\n"
              "The password should have atleast  one lowercase and atleast  one uppercase character\n")
        password=ask_cont()



    #checking the password range is between 6-16 and then printing out whether the password is greater or less.
    # In either case it will ask the user if he wants to continue and input the password again
    while ((len(password)<6) or (len(password)>16)) :
        if (len(password)<6):
            print "Then passoword lenght should be greater than 6"
        elif (len(password)>16):
            print "Then passoword lenght should be less than 16"
        password=ask_cont()
    #calling the fucntion to check if the input password has integer.
    # If not it will ask the user if he wants to continue and  input the password again
    while (num_in_string(password)!=True) :
        print "Then password should have atleast one numeric digit"
        password=ask_cont()
    #calling the fucntion to check if the input password has atleast one special characters.
    # If not it will ask the user if he wants to continue and  input the password again
    while (("$"not in password) and ("@" not in password) and ("!"not in password) and ("*" not in password)) :
        print "Then password should have atleast one special characters ($,@,!,*)"
        password=ask_cont()
    #calling the fucntion to check if the input password has atleast one upper case and one lower case.
    # If not if will ask the user if he wants to continue and  input the password again
    while lower_case(password)!="True" or upper_case(password)!="True":
        if lower_case(password)!="True":
            print "The password should have atleast on lower case"
        elif upper_case(password)!="True":
            print "The password should have atleast on upper case"
        password=ask_cont()
    print "The password has been accepted"

def num_in_string(password): #function to check for integer in the input password
    return any(i.isdigit() for i in password)

def input_user():#function to get input from the user
    password=raw_input("Enter a the password you want to use ")
    return password

def lower_case(password): #function to check for lower case in the input password
    for word in password:
        if word.islower():
            return "True"

def upper_case(password):#function to check for upper case in the input password
    for word in password:
        if word.isupper():
            return "True"
def ask_cont(): #function to ask the user if he wants to continue after entering the wrong password
    asktocontinue=raw_input("Do you want to continue (Press Y for Yes and any key to exit)")
    if (asktocontinue=="Y" ) or (asktocontinue=="y" ):
        return input_user()
    else:
        exit()

main() #calling the main function
