import mysql.connector
connection = mysql.connecter.connect(

    user = 'root',
    database = 'example',
    password = 'yours'
)
cursor = connection.cursor()
testQuery = ("SELECT * FROM bankingschema.bankingtable")

print("hello welcome to Wilson banking")

