import mysql.connector

from Validate import is_passWord_valid
from Validate import is_ID_valid

print("hello welcome to Wilson Banking")

connection = mysql.connector.connect(

    user = 'root',
    database = 'bankingschema',
    password = 'Gigabyte@12*'
)

#cursor = connection.cursor()
#cursorTest = connection.cursor()

#testQuery = ("SELECT * FROM bankingschema.bankingtable")

#addData = ("INSERT INTO  bankingschema.bankingtable (FirstName, LastName, PassWord, ID, Funds) VALUES (Y, P, pip, 124, 5000) ")

#cursor.execute(testQuery)
#cursorTest.execute(addData)

#for item in cursor:

    #print(item)


#for thing in addData:
    #print(thing)

#cursor.close()
#cursorTest.close()

#connection.commit()

#connection.close()

cursor = connection.cursor()

 

addData = ("INSERT INTO  bankingschema.bankingtable (FirstName, LastName, PassWord, ID, Funds) VALUES (1, 2, 3, 124, 5000) ")

 

cursor.execute(addData)

 

connection.commit()

cursor.close()

connection.close()


#def logIn():
    #userLogIn = input(" if you have an account log in here")
    #userSignIn = input(" if you are new log in here ")

global totalFunds 
global convertedFundsAdder
global convStartFunds 





# function to create account
def createAccount():
  connection = mysql.connector.connect(

    user = 'root',
    database = 'bankingschema',
    password = 'Gigabyte@12*'
)


  # intialize global vars
  global userNameFirst
  global userNameLast
  global passWord
  global userID

  global startFunds
  global totalFunds
  totalFunds = 0 

  global convertedFundsAdder
  convertedFundsAdder = 0
  
  userNameFirst = input("enter your first name ")
  userNameLast = input("enter your last name ")
  passWord = input("enter user password (Has to be > 7 characters) ")

# if user password < 8 chars throw this
  while  not is_passWord_valid(passWord):
     print(passWord + " not valid password")
     passWord = input("enter user password ")

  userID = input("enter your ID (Has to be > 4 charcaters) ")

  # if user ID < 5 chars throw this
  while not is_ID_valid(userID):
       print(userID + " is not valid ID")
       userID = input("enter your ID ")
  
  startFunds = input("please enter your intial deposit ")

  global convStartFunds 
  convStartFunds  = int(startFunds)


  # get user accunt data and store it in mySQL databae
  collectAccountData = (print("INSERT INTO  bankingschema.bankingtable (FirstName, LastName, PassWord, ID, Funds) VALUES  (" ,userNameFirst ,"," , userNameLast, "," ,  passWord,  ",", userID,  "," , startFunds )) 
  #collectAccountData = ("INSERT INTO  bankingschema.bankingtable  (FirstName, LastName, PassWord, ID, Funds) VALUES (1, 2, 3, 4, 0) ")

  cursor = connection.cursor()
  
  cursor.execute(collectAccountData)

  connection.commit()

  cursor.close()

  connection.close()


# code to check users balance
def checkBalance():
   global totalFunds
   #global convertedFundsAdder
   #convertedFundsAdder = 0

   #global convStartFunds 
 
   #convertedFundsAdder = int(startFunds)

  #convertedFundsAdder = int()
   
   totalFunds =  convStartFunds + convertedFundsAdder
   print(f'you have {totalFunds}$ in your account!')
   startUp()
   Input()



# code for adding funds
def addFunds():
   
   global convertedFundsAdder
   #global test
   global totalFunds

   fundsAdder = input("how many dollars would you like to add? ")
   convertedFundsAdder = int(fundsAdder)
   
   totalFunds = convertedFundsAdder + convStartFunds
   
   #totalFunds = totalFunds + convStartFunds
   #startFunds = totalFunds
   print(f'you now have {totalFunds}$ in your bank account now')
   startUp()
   Input()
   
   

# code for remove funds option
def removeFunds():
   global totalFunds
   totalFunds = 0

   fundsRemover = input(f"how much money would you like to withdraw from your account you currently have {totalFunds}$ in your account ")
   convertedFundsRemover = int(fundsRemover)

  

   totalFunds = totalFunds - convertedFundsRemover

   while (totalFunds < 0):
        print("not enough balance to with draw given amount")
        fundsRemover = input("how much money would you like to withdraw from your account ")
   
   print(f' you now have {totalFunds}$ in your account')
   startUp()
   Input()

# code to modify account info
def modifyAccount():
  checkPassword = input("enter you current password ")

  if checkPassword == passWord:
      print("you passed the check you may modify your account info")
      modifyPassword = input("enter your new password ")

      while  not is_passWord_valid(modifyPassword):
       print(passWord + " not valid password")
       passWord = input("enter user password ")
     

      getNewData = ("INSERT INTO  bankingschema.bankingtable (FirstName, LastName, PassWord, ID, Funds) VALUES  (" ,userNameFirst ,"," , userNameLast, "," ,  passWord,  ",", userID,  "," , startFunds )
      (print("INSERT INTO  bankingschema.bankingtable (FirstName, LastName, PassWord, ID, Funds) VALUES  (" ,userNameFirst ,"," , userNameLast, "," ,  passWord,  ",", userID,  "," , startFunds ))
      #UPDATE bankingschema.bankingtable
      
  else:
      print("incorrect password entered please try again ")
      checkPassword = input("enter you current password ")





# this function calls up main UI user interacts with
def startUp():
  print("select a number for option you wish to access")

  print("1 check account balance")
  print("2 desposit funds ")
  print("3 withdraw funds")
  print("4 modify account info")

  
# function to get what user picks and respond accordingly
def getChoice():
 

 if userInput == "1":
    checkBalance()

 elif userInput == "2":
      addFunds()
      
 elif userInput == "3":
     removeFunds()

 elif userInput == "4":
      modifyAccount()



 else:
      print("not a valid option")
      startUp()
      Input()
      
     


#get user input
def Input():
 global userInput
 userInput = input("select an option ")
 getChoice()



 # driver code
createAccount()
startUp()
Input()




