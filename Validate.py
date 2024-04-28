
# this list contains all valid chars for first and last names for users
validChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
               , 'A','B','C','D','E','F' ,'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

validNums = ["1", "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" ]


# this function checks whether or not first name contains letters
def is_Firstname_Valid(userNameFirst):
   for i in userNameFirst:
      if i  in validChars:
         return len(userNameFirst)

# this function checks whether or not last name contains letters
def is_Lastname_Valid(userNameLast):
   for i in userNameLast:
      if i  in validChars:
         return len(userNameLast)
      
         

def isIntialDeposValid(startFunds):
    for i in startFunds:
       if i in validNums:
         return len(startFunds)




# this func checks whether or not user password is over 8 chars
def is_passWord_valid(passWord):
  return len(passWord) >= 8

# this func checks whether or not user Id is over 5 chars
def is_ID_valid(userID):
  return len(userID) >= 5


def addToTotal(a,b):
   return a + b