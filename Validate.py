
# this list contains all valid chars for first and last names for users
validChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
               , 'A','B','C','D','E','F' ,'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def is_Firstname_Valid(userNameFirst):
   for i in userNameFirst:
      if i  in validChars:
         return len(userNameFirst)
      
def is_Lastname_Valid(userNameLast):
   for i in userNameLast:
      if i  in validChars:
         return len(userNameLast)
         





# this func checks whether or not user password is over 8 chars
def is_passWord_valid(passWord):
  return len(passWord) >= 8

# this func checks whether or not user Id is over 5 chars
def is_ID_valid(userID):
  return len(userID) >= 5

def addToTotal(a,b):
   return a + b