class Contact:
    """Describe the contact"""
    def __init__(self, surname, name, age, mob_phone, email):
        """Initialize the contact attributes"""
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_phone(self):
        """Return the contact phone number"""
        return self.mob_phone

    def get_email(self):
        """Return the contact email address"""
        return self.email

    @staticmethod
    def send_message(text):
        """Send some message"""
        return text


class UpdateContact(Contact):
    """Update the contact"""
    def __init__(self, surname, name, age, mob_phone, email, job):
        """Initialize the contact attributes, add job"""
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_phone_message(self, text):
        """Return the contact phone message"""
        print(f'{self.get_phone()} : {self.send_message(text)}')

    def get_email_message(self, text):
        """Return the email message"""
        print(f'{self.get_email()} : {self.send_message(text)}')


if __name__ == '__main__':
    cont1 = Contact("Dmitrovich", "Dmytro", 20, "0503456234", "dmytro@gmail.com")
    print(cont1.get_phone())
    print(cont1.get_email())
    print(cont1.send_message("Hello"))

    cont2 = UpdateContact(
        "Yegorovich", "Oleh", 33, "0703446434", "oleh@gmail.com", "programmer")
    cont2.get_phone_message("Hello, how are you?")
    cont2.get_email_message("Hello, how are you?")

    print(cont1.__dict__)
    print(cont2.__dict__)

    print(Contact.__dict__)
    print(UpdateContact.__dict__)

    print(Contact.__base__)
    print(UpdateContact.__base__)

    print(Contact.__bases__)
    print(UpdateContact.__bases__)
