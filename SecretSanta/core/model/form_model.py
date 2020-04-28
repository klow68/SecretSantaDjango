""" Form class to be used for all forms of the website
add some validation functionnalities very usefull """


# initialize all variables necessary for the forms
class Form:

    username = ""
    password = ""
    password2 = ""
    email = ""
    first_name = ""
    last_name = ""
    errors = []

    # make a full validation of the form (email, password...)
    def is_form_valid(form):
        result = True
        form.errors = []

        if (form.password and form.password2):
            Form.check_password(form.password, form.password2)
        else:
            form.errors += ["passwords are differents"]
            result = False

        return result

    # todo check form
    def check_password(password, password2):
        if (password == password2):
            return True
