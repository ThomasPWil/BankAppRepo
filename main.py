import mysql.connector

print("hello welcome to Wilson banking")

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
def createAccount():
  
  # intialize global vars
  global userNameFirst
  global userNameLast
  global passWord
  global ID
  global startingFunds

  userNameFirst = input ("enter your first name ")
  userNameLast = input("enter your last name ")
  passWord = input("enter user password")
  ID = input("enter your ID ")
  startingFunds = input("please enter your intial deposit ")




def startUp():
  print("select a number for option you wish to acess")

  print("1 check account balance")
  print("2 desposit funds ")
  print("3 withdraw funds")
  print("4 create new account")
  print("5 sign in")
  

def getChoice():
 if userInput == 4:
      createAccount()
 else:
      print("not a valid option")
     



def Input():
 global userInput
 userInput = input("select an option ")
 getChoice()



 

startUp()
Input()




