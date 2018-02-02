
def common_students(python_student_list,web_application_list): #function to calculate the common students
    common_student=[] #list of common students

    total_student=[] #list of total students

    #loop to find the common students
    for names_python in python_student_list:
        for names_web in web_application_list:
            if names_python== names_web:
                common_student.append(names_web)
    return common_student
def not_common_students(python_student_list,web_application_list):#function to calculate the uncommon students
    notcommon_student=[] #list of uncommon students
    #loop to find the students python students who are not attending web application class
    for i in python_student_list:
        if i not in web_application_list:
            notcommon_student.append(i)

    #loop to find the students web application students who are not attending python class
    for j in web_application_list:
        if j not in python_student_list:
            notcommon_student.append(j)
    return notcommon_student

def main(python_student_list,web_application_list): #main function
    print "Common students in both the courses ", common_students(python_student_list,web_application_list) #calling the common fucntion
    print "Not common students ", not_common_students(python_student_list,web_application_list)#calling the uncommon fucntion
    print "Total students ", common_students(python_student_list,web_application_list)+not_common_students(python_student_list,web_application_list) #to caculate the total students


python_student_list=['Rohit Singh', 'Shuai Zhao', 'Jack Daniels','Chivas Regal','Glen'] #list of student in python class
web_application_list=['Rohit Singh','Budlight','Tank','Chivas Regal'] #list of students in web application class
print "Student in Python Class ", python_student_list
print "Student in Web Application Class ",web_application_list

main(python_student_list,web_application_list)#calling the main function





