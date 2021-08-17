import pymysql.cursors  
 
# Connectez- vous à la base de données.
connection = pymysql.connect(host='192.168.1.9',
                             user='admin',
                             password='goodwood',                             
                             db='stock',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
 
try:
  
 
    with connection.cursor() as cursor:
       
        # SQL 
        sql = "SELECT Dept_No, Dept_Name FROM Department "
         
        # Exécutez la requête (Execute Query).
        cursor.execute(sql)
         
        print ("cursor.description: ", cursor.description)
 
        print()
 
        for row in cursor:
            print(row)
             
finally:
    # Closez la connexion (Close connection).      
    connection.close()