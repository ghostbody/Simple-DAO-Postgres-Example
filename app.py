import userDAO
import postgresql

database = postgresql.open(user='postgres', database='unico', port=5432, password='root')

user = userDAO.UserDao(database)

print("CREATE 'tb_user'")
user.createTableUser()
print("-------------------------") 

print("Insert")    
user.insertValues()
print("-------------------------") 

print("Select")        
print("-------------------------")  
user.select()
print("-------------------------") 

print ("Update")            
print("-------------------------")
user.update()
print("-------------------------") 

print("DROP 'tb_user'")
user.dropTable()
print("-------------------------") 