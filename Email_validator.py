mail=input("Enter Email: ")
def email_validator(mail):
    if("@" not in mail and mail.count("@")!=1):
        return False
    loc,dom=mail.split("@")
    if(not loc or not dom):
        return False
    if("." not in dom or dom.endswith(".")):
        return False
    invalid_char=' ()[]{}",:;\\<>@._+%# '
    if any(i in invalid_char for i in loc):
        return False
    return True
print("Result:",email_validator(mail))