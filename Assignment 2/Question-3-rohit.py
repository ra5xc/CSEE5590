import random

class Conference: # Class 1 Conference Class
    def __init__(self,conference_name): # _init_ constructor
        self.conference_name=conference_name


class Name: #class 2  Name Class
    def __init__(self,first_name, last_name): # _init_ constructor
        self.first_name=first_name
        self.last_name=last_name
    def print_name(self):
        print("The Author Name is %s %s"%(self.first_name,self.last_name))



class Authors(Name):#class 3 # Author class inheritance from Name class
    #to count the total authors
    def __init__(self,first_name, last_name,author_track): # _init_ constructor
        super(Authors, self).__init__(first_name,last_name) #super call
        self.author_track=author_track



class Registration(Conference,Authors): #class 4  Registartion Class #inheritance from Confrence and Author class
    total_person=0
    def __init__(self,conference_name,first_name, last_name, author_track,registration_number): # _init_ constructor
        Conference.__init__(self,conference_name)
        Authors.__init__(self,first_name, last_name, author_track)
        self.__registration_number = registration_number #private data attribute
        Registration.total_person+=1


class OrganizingCommittee(Conference,Name): #class 5 #inheritance from Conference class and Name Class
    def __init__(self,conference_name,first_name, last_name,role): # _init_ constructor
        Conference.__init__(self,conference_name)
        Name.__init__(self,first_name, last_name)
        self.role=role


class TechnicalProgrammeCommitte(Conference,Name): #class 6 ##inheritance from Conference and Name Class
    def __init__(self,conference_name,first_name, last_name, track_name): # _init_ constructor
        Conference.__init__(self,conference_name)
        Name.__init__(self,first_name, last_name)
        self.track_name=track_name


class Programme (Conference): #class 7 Inheritence from Conference class
    def __init__(self,conference_name, programme_name, schedule): # _init_ constructor
        Conference.__init__(self,conference_name)
        self.programme_name=programme_name
        self.schedule=schedule


c=Conference
n=Name
a=Authors
r=Registration
o=OrganizingCommittee
t=TechnicalProgrammeCommitte
p=Programme

value_1_conference= c("ICC")
value_1_name=n("Rohit","Abhishek")
value_1_author=a("Rohit","Abhishek","Smart Cities")
value_2_name=n("tom","trump")
value_2_author=a("tom","trump","Security")
value_3_name=n("Abc","def")
value_3_author=a("Abc","def","big data")

value_1_registration=r("ICC","Rohit","Abhishek","Smart Cities",''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(12)))
value_2_registration=r("ICC","tom","trump","Security",''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(12)))
value_3_registration=r("ICC","Abc","def","big data",''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(12)))
value_1_organizing_committe1=o("ICC","Deep", "Medhi","Executive-Chair")
value_1_organizing_committe2=o("ICC","Yi", "Qian","TPC Chair")
value_1_organizing_committe3=o("ICC","Rohit", "Abhishek","Web Content Chair")
value_1_tpc1=t("ICC","Jack","Daniels","Wireless Communications")
value_1_tpc2=t("ICC","Chivas","Regal","Security")
value_1_programme1=p("ICC","Keynote","9:00 AM - 10:30 AM")
value_1_programme2=p("ICC","Smart Cities Track,","12:00 PM - 2:30 PM")

print("Conference Name is :", value_1_conference.conference_name)
print("Author Name is :", value_1_author.first_name,value_1_author.last_name)
print("Author registered for \"%s\" track" %(value_1_author.author_track))
print("Author's registration code is:",value_1_registration._Registration__registration_number)

print("Author Name is :", value_2_author.first_name,value_2_author.last_name)
print("Author registered for \"%s\" track" %(value_2_author.author_track))
print("Author's registration code is:",value_2_registration._Registration__registration_number)

print("Author Name is :", value_3_author.first_name,value_3_author.last_name)
print("Author registered for \"%s\" track" %(value_3_author.author_track))
print("Author's registration code is:",value_3_registration._Registration__registration_number)
print("Total Author registered are ",r.total_person)

print("Organizing Committee Members are:")
print(value_1_organizing_committe1.first_name,value_1_organizing_committe1.last_name
      ,":",value_1_organizing_committe1.role,"\n",value_1_organizing_committe2.first_name,value_1_organizing_committe2.last_name
      ,":",value_1_organizing_committe2.role,"\n",value_1_organizing_committe3.first_name,value_1_organizing_committe3.last_name
      , ":",value_1_organizing_committe3.role,"\n")
print("Technical Programme Committee Members are:")

print(value_1_tpc1.first_name,value_1_tpc1.last_name,":",value_1_tpc1.track_name,"\n",
value_1_tpc2.first_name,value_1_tpc2.last_name,":",value_1_tpc2.track_name)

print("Programme ")
print(value_1_programme1.programme_name,":",value_1_programme1.schedule,"\n",
      value_1_programme2.programme_name, ":", value_1_programme2.schedule)



