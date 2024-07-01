class Person:
    def __init__(self, lastname, firstname, phone, mail):
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.mail = mail
    
    def __repr__(self):
        return "Last name : {} / First name : {} / Phone : {} / Mail : {}".format(self.lastname, self.firstname, self.phone, self.mail)

class Work():
    def __init__(self, lastname, firstname, phone, mail, company, address, company_phone):
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.mail = mail
        self.company = company
        self.address = address
        self.company_phone = company_phone

    def __repr__(self):
        return "Last name : {} / First name : {} / Phone : {} / Mail : {} \n Company : {} / Address : {} / Work Phone : {}".format(self.lastname, self.firstname, self.phone, self.mail, self.company, self.address, self.company_phone)

class Dev():
    def __init__(self, lastname, firstname, phone, mail, company, address, company_phone, languages = [], preferred_stack = ""):
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.mail = mail
        self.company = company
        self.address = address
        self.company_phone = company_phone
        self.languages = languages
        self.preferred_stack = preferred_stack

    def __repr__(self):
        return "Last name : {} / First name : {} / Phone : {} / Mail : {} \nCompany : {} / Address : {} / Work Phone : {} \nLanguages : {} / Stack : {}".format(self.lastname, self.firstname, self.phone, self.mail, self.company, self.address, self.company_phone, self.languages, self.preferred_stack)

class Contacts():
    
    def __init__(self):
        self.objects = []

    def __repr__(self):
        display = ""
        for contact in self.objects:
            display += "Last name : {} / First name : {} / Phone : {} / Mail : {} \n".format(contact.lastname, contact.firstname, contact.phone, contact.mail)
        return display
    
    def add_contact(self, person):
        self.objects.append(person)

    def search_contact(self, lastname, firstname = ""):
        foundContacts = []
        # return self.objects
        for contact in self.objects:            
            if contact.lastname == lastname:
                foundContacts.append(contact)
        return foundContacts
    
    def remove_contact(self, lastname, firstname):
        for i in range(len(self.objects)):
            if self.objects[i].lastname == lastname and self.objects[i].firstname == firstname:
                self.objects.pop(i)                
            return

me = Person("esteve", "jean-marc", "0651948449", "me@me.me")
you = Person("plantin", "zoe", "0654268693", "you@you.you")
them = Person("plantin", "dazig", "0654265593", "you@you.you")
# print(me)

my_contacts = Contacts()
my_contacts.add_contact(me)
my_contacts.add_contact(me)
my_contacts.add_contact(you)
my_contacts.add_contact(them)

doublon = my_contacts.search_contact("esteve")
print(doublon)
print("- \n")

my_contacts.remove_contact("esteve","jean-marc")

print(my_contacts)
print(" , \n")


my_me = Work("esteve", "jean-marc", "0651948449", "me@me.me", "CmP ltd", "65 bd Green, 75000 PARIS", "0756857456")
# print(my_me)

real_me = Dev("esteve", "jean-marc", "0651948449", "me@me.me", "CmP ltd", "65 bd Green, 75000 PARIS", "0756857456",['php','python'],"backend")
# print(real_me)