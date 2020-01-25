class Contact_inforamation:
    def __init__(self,name,email,phoneno):
        self.name=name
        self.email=email
        self.phoneno=phoneno

    def set_name(self,name):
        self.name=name

    def set_email(self,email):
        self.email=email

    def set_phoneno(self,phoneno):
        self.phoneno=phoneno

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phoneno(self):
        return self.phoneno
    def __str__(self):
        return self.name,self.email,self.phoneno

c1=Contact_inforamation('Prachi','p@gmail.com',4444444)

print('Name :', c1.get_name(), '\nEmail Address :', c1.get_email(), '\nPhone Number :', c1.get_phoneno())
print(c1.__str__())