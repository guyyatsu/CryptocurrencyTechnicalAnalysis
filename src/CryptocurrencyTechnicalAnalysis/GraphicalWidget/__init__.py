#!/bin/py


from tkinter import Tk
from tkinter import END
from tkinter import Entry
from tkinter import Label
from tkinter import Button

from Lab93CryptographyAPI import CryptogramAPI


cryptogram = CryptogramAPI()
SHA256   = lambda string: cryptogram.sha_256(string)
BUILDKEY = lambda string: cryptogram.build_key(string)


class GraphicalCredentialManagement
    def __init__(self, database):

        self.root = Tk()


    def UserLogin(self, root):

        root.title("User Login")

        username_label = Label( text="Username:" )
        username       = Entry()

        password_label = Label( text="Password:" )
        password       = Entry()

        _userlogin_button  = Button( text="Login",  action=_user_login  )
        _createuser_button = Button( text="Signup", action=_create_user )


        def _user_login(): pass

            userpass = SHA256(
                f"{ SHA256( username.get() ) }"
                f"{ SHA256( password.get() ) }"
            )

            if ValidateUserCredentials(database, userpass) == userpass:
                key = BUILDKEY( f"{username.get()}{password.get()" )
                username.delete(0, END); password.delete(0, END)

            else: pass


        def _create_user(): pass

