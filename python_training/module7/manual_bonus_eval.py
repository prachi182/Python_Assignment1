import pickle
class User_information:
    def __init__(self,name,email,phoneno):
        self.name=name
        self.email=email
        self.phoneno=phoneno
    def __repr__(self):
        return "%s,%s,%s" % (self.name,self.email,self.phoneno)

u1=User_information('Prachi','p@gmail.com',44444)
u2=User_information('Neha','n@gmail.com',44333)
dic={1: u1, 2:u2}
infile=open('employe_data.dat','wb')
pickle.dump(dic,infile)
infile.close()

def look_up():
    infile = open('employe_data.dat', 'rb')
    ID=int(input("Enter the ID :"))
    print(dic[ID])
    pb = pickle.load(infile)
    infile.close()
    print(pb)

def change_contact():
    ID=int(input("Enter the ID"))
    for i in dic.keys():
        if ID==i:
            name=input('Enter new Name :')
            email=input("Enter new Email Address :")
            phoneno=input("Enter new Phone Number :")
            dic[i]=name,email,phoneno
            print(dic[i])
            print(dic)

def delete_contact():
    ID=int(input("Enter ID"))
    try:
        for i in dic.keys():
            if  ID==i:
                del dic[i]
                print(dic)
    except Exception as e:
                print("The size of dictionary are changed",e)

def add_details():
    num=int(input("How many number of details you want to enter in the dictioary :"))
    infile=open('employe_data.dat','wb')


number=int(input("Enter 1 for lookup\nEnter 2 for Change Details\n Enter 3 for Delete the details :"))
if number==1:
    look_up()
elif number==2:
    change_contact()
elif number==3:
    delete_contact()
else:
    print("Sorry dear! You have entered wrong choice :")