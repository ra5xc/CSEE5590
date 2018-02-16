
def create_dictionary(): #function to create the dictionary
	umkc_dictionary={}
	total_books= int(input("how many items you want to add ")) #ask user how many item they want
	for i in range(total_books):
		book_name=input("Enter the name of %d item "%(i+1))
		book_price=int(input("Enter the price of %s "%book_name))
		umkc_dictionary[book_name]=book_price
	return umkc_dictionary


def find_books(umkc_dictionary): #function to find the books within the range
	lower_range=int(input("Enter the lower range ")) #lower range
	higher_range=int(input("Enter higher range")) #higher range
	if lower_range>higher_range: #if lower range is greater than higher ranger
		user_retry=int(input("Range not valid (lower range is less than higher range) \n" #ask if user wants to retry
		      "Press 1 to retry \n" 
		      "Press any other key to exit \n"))
		if user_retry==1:
			find_books(umkc_dictionary) #if user wants to retry, call the function again
		else:
			exit()

	for books,price in umkc_dictionary.items(): #loop to iterate the dictionary to find the books in the range
		if lower_range<= price <=higher_range:
			print(books)




umkc_dictionary= {"python":50, "web": 30, "c":20,"java":40} #Existing dictionary
user_option= int(input("Would you like to use existing dictionary or create a new one\n" #ask if user wants to use an existing dictionary or create new dictionary
                   "1-Press 1 to use existing dictionary\n"
                   "2-Press 2 create new one \n"
                   "3-Press any other key to exit\n"))
if user_option==1:
	find_books(umkc_dictionary)
elif user_option==2:
	umkc_dictionary=create_dictionary()
	find_books(umkc_dictionary)
else:
	exit()

