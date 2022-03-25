# This will randomly generate a secret key everytime the app is initialised
def secretKey() -> str:
    from string import ascii_letters, digits, punctuation
    from re import search
    from random import choice
    import secrets
    from uuid import uuid4
    for num in range(1, 20):
        if num < 15:
            pass
        else:
            alphanumerics = ascii_letters + digits + punctuation
            scr = "".join(choice(alphanumerics) for _ in range(num))
            if search(r'(.)\1\1', scr) and search(r'(..)(.*?)\1', scr):
                secretKey()
            else:
                return scr + str(secrets.token_hex(26)) + str(uuid4().hex)


def passwordStrength(password) -> str:
    from re import compile, search
    from flask import flash
    """
        Password Strength must have:
            # Atleast one number
            # Atleast one uppercase & lowercase letter
            # Atleast one special symbol
            # Should be 8 <= password <= 20 long
    """
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pssword = ""

    # compile the regex experssions
    password_checker = compile(regex)

    # search for the regex in the password
    password_match = search(password_checker, password)

    if len(password) < 8:
        flash("Make sure your password is at least 8 characters long", category='error')
    elif not password_match:
        flash("Make Sure Password Has: one number, one uppercase and lowercase letter and one special symbol", category='error')
    else:
        pssword = password
    
    return pssword


def validEmail(email):
    from re import fullmatch
    from flask import flash
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    valid_email = ""
    if (fullmatch(regex, email)):
        valid_email = email
    else:
        flash("Invalid Email Address. Try Again...", category='error')
    return valid_email