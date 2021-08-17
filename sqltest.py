import pymysql.cursors  
 
# Connectez- vous à la base de données.
connection = pymysql.connect(host='localhost',
                             user='monsieur',
                             password='goodwood',                             
                             db='stock',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
 
sql = "Select pseudo, competence, sante_mental = %s "
 
try :
    cursor = connection.cursor()
 
    # Exécutez sql et passez- lui un paramètre.
    cursor.execute(sql, ( 10 ) )
     
     
     
    print ("cursor.description: ", cursor.description)
     
    print()
     
    for row in cursor:
        print (" ----------- ")
        print ("pseudo: ", row["pseudo"])
        print ("competence: ", row["competence"])
        print ("sante_mental: ", row["sante_mental"])
 
finally:
    # Achevez la connexion
    connection.close()