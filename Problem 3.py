def triplets(user_input):#fucntion to find the triplet
    string_split=user_input.split(" ") #splitting the input string
    string_list=[]
    #we will iterate through the string and check if he sum of triplets will be zero. Since we have triplets so we will be using 3 lops.
    #the loop varies in all three loops as we dont want to repeat combination
    for i in range(0,len(string_split)-2):
        for j in range(i+1,len(string_split)-1):
            for k in range(j+1,len(string_split)):
                if int(string_split[i]) +int(string_split[j])+int(string_split[k])==0:
                    print string_split[i] , string_split[j] , string_split[k]

user_input= raw_input("Enter list of numbers seperated by space ") #Assuming the input will be given by user
triplets(user_input)#calling the main function

