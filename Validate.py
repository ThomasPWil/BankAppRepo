
# this func checks whether or not user password is over 8 chars
def is_passWord_valid(passWord):
  return len(passWord) >= 8

# this func checks whether or not user Id is over 5 chars
def is_ID_valid(userID):
  return len(userID) >= 5

def addToTotal(a,b):
   return a + b