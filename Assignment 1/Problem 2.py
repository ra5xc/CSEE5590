from __future__ import print_function

#function to abstract the middle word
def middle_word(string_split,len_string):
    if len_string==2: #if the string has lenght 2 then both will be considered as middle words
        print ("The middle word is : %s %s" %(string_split[0],string_split[1]))

    elif len_string % 2 ==0: #check if the len is divisible by 2, if yes then there should be 2 middle words
        print ("The middle words are : %s %s"%(string_split[(len_string/2)-1],string_split[(len_string/2)]))
    else:
        print ("The middle word is : %s" %string_split[(len_string/2)])

#fucntion to get the longest word
def longest_word(string_split,len_string):
    #iterating through the splitted string to find the length of each word and store the len and the words in another 2 dimensinal array long_word_lst
    long_word_lst=[]
    for i in range(len_string):
        long_word_lst.append([len(string_split[i]),string_split[i]])

    #sort the long_word_lst based on the len of the words. the last item should be the longest item
    long_word_lst=sorted(long_word_lst)
    #print(long_word_lst)
    #long_word_lst_tmp=[]

    print ("The longest word is: ",end="")
    #checking if there is any other item in the string of the same lenghth by comparing it to the last item since it is the longest
    for i in range(len_string):
        if long_word_lst[len_string-1][0]==long_word_lst[i][0]:
            #long_word_lst_tmp.append(long_word_lst[i][1])
            print(long_word_lst[i][1]," ",end='')
    print(" ")

#fuction to reverse a word
def reverse_word(string_split,len_string):
    print ("Sentence with reverse words is: ",end='')
    for i in range(len_string):
        print (string_split[i][::-1]," ",end='')

#main function
def main():
    user_input=raw_input("Enter a sentense ")
    string_split=user_input.split(" ") #to split the string
    len_string=len(string_split)#calculating the len of the string
    middle_word(string_split,len_string) #calling the fucntion to get the middle_word
    longest_word(string_split,len_string) #calling the function to get the longest word
    reverse_word(string_split,len_string) #calling the function to reverse the word

main() #calling the main function
