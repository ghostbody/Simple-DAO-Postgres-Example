
# The User Data Access Object handles all interactions with the User table.
class UserDao:
    
    #constructor    
    def __init__(self, db):
        self.db = db
               
    #create table 'td_user'....
    def createTableUser(self):
        self.db.execute("CREATE TABLE tb_user (id int PRIMARY KEY, name text)")

    
    #insert a few user into 'tb_user' table...    
    def insertValues(self):
        make_tb_user = self.db.prepare("INSERT INTO tb_user VALUES ($1, $2)")
        
        with self.db.xact():
            make_tb_user(1, "user1")
            make_tb_user(2, "user2")
            make_tb_user(3, "user3")
   
    
    #select all user from 'tb_user' table...    
    def select(self):
        select_tb_user = self.db.prepare("select * from tb_user")
                            
        with self.db.xact():
            for row in select_tb_user():
                print(row)
      
   
    #update a user info, or name...just look at your sql statement and the field also....             
    def update(self):
        update_tb_user = self.db.prepare("UPDATE tb_user SET name = $2 WHERE id = $1")
        
        with self.db.xact():
            update_tb_user(1,"whatever do you want put here, you can!")
            self.select()
   
    #drop 'tb_user' table from the database...                 
    def dropTable(self):
        self.db.execute("drop table tb_user")
        
        
