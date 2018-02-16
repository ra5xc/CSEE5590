
from validate_email import validate_email #module to check the validity of email address


def display_contact_name(contact_list): #function to display the contact name
    for i in contact_list:
        print(i["name"], ", ", end="  ")
    print("\n")

def display_contact_number(contact_list):#function to display the contact number
    for j in contact_list: # this won't display the contacts if there is no number assigned to the code
        if (j["number"]!=None) and (j["number"]!=""):
            print(j["name"], " ",j["number"])


def edit_contact_by_name(contact_list): #function to edit contact by name
    contact_name=input("Enter the contact name to edit ")
    number_of_contacts_with_same_name=total_contacts_with_same_name(contact_name, contact_list)# we need to see if there are multiple contacts with the same name, if yes we need to enter other details to edit
    if number_of_contacts_with_same_name==0: #check if the enter name is present in the list or not
        print("Contact Not Found")
    elif number_of_contacts_with_same_name == 1: #unique contact found
        edit_details(contact_list, contact_name) #call edit_details function to edit the contact
        continue_again=input("Do you want to edit more contacts (Y)? ").lower() #ask if the user wants to continue
        if continue_again=="y":
            edit_contact_by_name(contact_list) #if yes iterate throught the same function
        else:
            return
    else:
        print("%d contacts with the name: %s"%(number_of_contacts_with_same_name,contact_name )) #if we multiple contacts with the same name
        second_input=input("Please input either mobile number or email address of the contact") #Enter secondary information, either mobile number or email address
        edit_details_by_mobile_email(contact_list, second_input) #call function to edit details using mobile or email


def edit_details_by_mobile_email(contact_list,second_input): #function to edit details using number or email
    contact_list=contact_list
    for i in contact_list:
        if i.get("number")==second_input or i.get("email")==second_input:
            edit_details = input("What contact details do you want to edit (Name/Number/email) ? ").lower()
            if edit_details == "name":
                new_name = input("Enter new name: ")
                i["name"] = new_name

            elif edit_details == "number":
                new_number = input("Enter new number: ")
                i["number"] = new_number

            elif edit_details == "email":  # we need to check if the email address is valid
                new_email = input("Enter new email: ")
                email_exits = verify_email(new_email)
                while email_exits == False:
                    new_email = input("Enter correct email addres: ")
                    verify_email(new_email)
                    email_exits = verify_email(new_email)
                i["email"] = new_email
            else:
                print("Not a Valid choice: ")
                edit_contact_by_name()



def edit_details(contact_list,contact_name): #this function would edit the contact name, mobile or email
    for i in contact_list:
        if i.get("name") == contact_name: #if contact name found
            edit_details = input("What contact details do you want to edit (Name/Number/email) ? ").lower() #ask user what to edit
            if edit_details == "name": #edit name
                new_name = input("Enter new name: ")
                i["name"] = new_name

            elif edit_details == "number": #edit number
                new_number = input("Enter new number: ")
                i["number"] = new_number

            elif edit_details == "email":  #edit email
                new_email = input("Enter new email: ")
                email_exits = verify_email(new_email)
                while email_exits == False:
                    new_email = input("Enter correct email addres: ")
                    verify_email(new_email)# we need to check if the email address is valid
                    email_exits = verify_email(new_email)
                i["email"] = new_email
            else:
                print("Not a Valid choice: ")
                edit_contact_by_name()


def total_contacts_with_same_name(contact_name,contact_list): #function to find contact with the same name
    counter=0
    for i in contact_list: # loop to see how name contacts are present with the same name
        n = i.get("name")
        for j in n.split():
           # print(j, end=" ")
            if j == contact_name:
                counter = counter + 1
    return counter


def verify_email(new_email): #function to verify the email
    return validate_email(new_email)


def main(contact_list): #main function
    list_use= input("Do you want to use existing dictionary or create a new dictionary (press 1 to use existing list and 2 to create new list ? ") #ask if user wants to use existing list or create a new one
    if list_use == "1": #use existing list
        user_choice(contact_list)

    if list_use=="2": #create new dictionary
        contact_list = []
        number_of_contacts = int(input("how many contact do you want to add? "))
        for i in range(number_of_contacts):
            name = input("Enter the full name: ")
            number = int(input("Enter the number: "))
            email = input("Enter the email address: ")
            while validate_email(email) == False: #check for validity of email
                print("email not valid")
                email = input("Enter the email address again: ")
            contact_list.append({'name': name, 'number': number, 'email': email})
        user_choice(contact_list)



def user_choice(contact_list): #function to ask user choices
    user_option = input("Press 1 to display contact name\n"
                        "Press 2 to display contact number\n"
                        "Press 3 to edit contact\n"
                        "Press 4 to exit\n")
    if user_option == '1': #to display contact name
        print("Contact Names")
        display_contact_name(contact_list)
    if user_option == '2': #to display contact numbers
        print("Contact Numbers")
        display_contact_number(contact_list)
    if user_option == '3': #to edit contact
        edit_contact_by_name(contact_list)
    if user_option == '4': #to exit
        exit()
    print("Updated contact list")
    print(contact_list)
    print("\n")
    contact_list = contact_list
    continue_option=input("Do you want to continue (Y to continue/ Any key to exit )? ") #ask if user wants to continue
    if (continue_option) == "y" or (continue_option) == "Y" :
        print(contact_list)
        user_choice(contact_list)
    return contact_list



stored_contact_list=[{"name":"name1","number":None ,"email":"name@rmail.com"},{"name":"name1","number":54321,"email":"name1@rmail.com"},{"name":"name3","number":5421,"email":"na1@rmail.com"}]
print(stored_contact_list)
main(stored_contact_list)

