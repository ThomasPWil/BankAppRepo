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

 




# psuedo code for getting password function
# ask user for password if they do not have one

# use SELECT to check user password and match it up with other account info

#afterwards once user has logged in display options

# func to create user account 
global totalFunds 
global convertedFundsAdder
global convStartFunds 



def checkBalance():
   global convertedFundsAdder
   
   global convStartFunds 
 
   #convertedFundsAdder = int(startFunds)

  #convertedFundsAdder = int()
   
   totalFunds =  convStartFunds + convertedFundsAdder
   print(f'you have {totalFunds}$ in your account!')
   startUp()
   Input()




def createAccount():
  connection = mysql.connector.connect(

    user = 'root',
    database = 'bankingschema',
    password = 'Gigabyte@12*'
)


  # intialize global vars
  global userNameFirst
  global userNameLast
  #passWord
  global userID

  global startFunds
  global totalFunds 
  
  userNameFirst = input("enter your first name ")
  userNameLast = input("enter your last name ")
  passWord = input("enter user password ")

  while  not is_passWord_valid(passWord):
     print(passWord + " not valid password")
     passWord = input("enter user password ")

  userID = input("enter your ID ")

  while not is_ID_valid(userID):
       print(userID + " is not valid ID")
       userID = input("enter your ID ")
  
  startFunds = input("please enter your intial deposit ")

  global convStartFunds 
  convStartFunds  = int(startFunds)


  # get user accunt data and store it in list
  collectAccountData = (print("INSERT INTO  bankingschema.bankingtable (FirstName, LastName, PassWord, ID, Funds) VALUES  (" ,userNameFirst ,"," , userNameLast, "," ,  passWord,  ",", userID,  "," , startFunds )) 
  #collectAccountData = ("INSERT INTO  bankingschema.bankingtable  (FirstName, LastName, PassWord, ID, Funds) VALUES (1, 2, 3, 4, 0) ")

  cursor = connection.cursor()
  
  cursor.execute(collectAccountData)

  connection.commit()

  cursor.close()

  connection.close()

#def logIn():
    #userLogIn = input(" if you have an account log in here")
    #userSignIn = input(" if you are new log in here ")

# code for adding funds
def addFunds():
   global totalFunds 
   global convertedFundsAdder
   totalFunds = 0
   
   fundsAdder = input("how many dollars would you like to add? ")
   convertedFundsAdder = int(fundsAdder)

   totalFunds = convertedFundsAdder + convStartFunds
   #startFunds = totalFunds
   print(f'you now have {totalFunds}$ in your bank account now')
   startUp()
   Input()
   
   #code to add 

# code for remove funds options
def removeFunds():
   
   
   fundsRemover = input("how much money would you like to withdraw from your account ")
   convertedFundsRemover = int(fundsRemover)

   totalFunds = 0

   totalFunds = totalFunds - convertedFundsRemover

   while (totalFunds < 0):
        print("not enough balance to with draw given amount")
        fundsRemover = input("how much money would you like to withdraw from your account ")

   print(f' you now have {totalFunds}$ in your account')
   startUp()
   Input()

   
    

# this function calls up main UI user interacts with
def startUp():
  print("select a number for option you wish to access")

  print("1 check account balance")
  print("2 desposit funds ")
  print("3 withdraw funds")
  #print("4 create new account")
  #print("5 sign in")
  
# function to get what user picks and repsond accordingly
def getChoice():
 #print("entering getChoice function")

 if userInput == "1":
    checkBalance()

 elif userInput == "2":
      addFunds()
      

 elif userInput == "3":
     removeFunds()

 #elif userInput == "4":
     #createAccount()

 #elif userInput == "5":
     #print("function goes here goes to sign in")

 else:
      print("not a valid option")
      
     


#get user input
def Input():
 global userInput
 userInput = input("select an option ")
 getChoice()



 
createAccount()
startUp()
Input()




