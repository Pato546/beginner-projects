import re
import os


class AccountValidator():
    
    def password_regex(self, pass_word):

        password = re.compile(r'(\w?\w\W*\d*){8,}')
    
        mo = password.search(pass_word)

        msg = ''

        try:
            if mo.group():
                for char in mo.group():
                    if char.isdigit():
                        return True 
                else:
                    msg = 'Your password must contain at least a digit'
                    return False, msg 
            
        except AttributeError:
            msg = 'Your password is not strong'
            return False, msg 
       


    def email_regex(self, _email):

        email = re.compile( r'[a-zA-Z0-9_%.-.]+@[a-zA-Z]{2,10}\.[a-z]{2,8}')
        mo = email.search(_email)
        try:
            if mo.group(): return True
        except AttributeError:
            return False


    def phone_number_regex(self, phone_number):
        
        re_pattern = r'(\+233|0)?\d{9}'
        phone_regex = re.compile(re_pattern)
        
        mo = phone_regex.search(phone_number)

        try:
            if mo.group():
                return True
        
        except AttributeError:
            return False


if __name__ == '__main__':

    #password = input("Enter PASSWORD: ")
    email = input("Enter email: ")

    user = AccountValidator()
    #print(user.password_regex(password))
    #print(user.phone_number_regex(phone_number))
    print(user.email_regex(email))

