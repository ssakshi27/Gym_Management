import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='gym')
mycursor = mydb.cursor()
print("""__________________________________________
         
                   GYM MANAGEMENT SOFTWARE
         __________________________________________""")

# CREATING DATABASE
mycursor.execute("CREATE DATABASE IF NOT EXISTS gym")
mycursor.execute("USE gym")
mycursor.execute("CREATE TABLE IF NOT EXISTS fees(low INT, mid INT, high INT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS login(username VARCHAR(30), password VARCHAR(25) NOT NULL)")
mycursor.execute("CREATE TABLE IF NOT EXISTS gym_member(id INT, name VARCHAR(30), gender CHAR, category VARCHAR(25), amt INT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS sno(id INT, did INT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS trainer(id INT, name VARCHAR(30), age VARCHAR(30), gender CHAR, salary INT)")
mydb.commit()

# Inserting important data
# login
mycursor.execute("SELECT * FROM login")
flag = 0
for i in mycursor:
    flag = 1
if flag == 0:
    mycursor.execute("INSERT INTO login VALUES ('admin', 'ng')")
    mydb.commit()

# Inserting sno data
flag = 0
mycursor.execute("SELECT * FROM sno")
for i in mycursor:
    flag = 1
if flag == 0:
    mycursor.execute("INSERT INTO sno VALUES(0, 0)")
    mydb.commit()

# Inserting fees data
flag = 0
mycursor.execute("SELECT * FROM fees")
for i in mycursor:
    flag = 1
if flag == 0:
    mycursor.execute("INSERT INTO fees VALUES(500, 800, 1000)")
    mydb.commit()

# Main section
while True:
    print("""
    1-login
    2-exit
    """)
    ch = int(input("enter your choice:"))
    if ch == 1:
        passs = input("enter password:")
        mycursor.execute("SELECT * FROM login")
        for i in mycursor:
            t_user, t_pas = i
        if t_pas == passs:
            print("""
            1. add trainer
            2. add member
            3. remove trainer
            4. remove member
            5. change password
            6. back
            """)
            ch = int(input("enter your choice"))
            if ch == 1:
                name = input("enter name-")
                age = input("enter age-")
                gender = input("enter gender M/F-")
                salary = int(input("enter salary-"))
                mycursor.execute("SELECT * FROM sno")
                for i in mycursor:
                    t_id, t_did = i
                t_id = t_id + 1
                mycursor.execute("INSERT INTO trainer VALUES('" + str(t_id) + "','" + name + "','" + age + "','" + gender + "','" + str(salary) + "')")
                mycursor.execute("UPDATE sno SET id='" + str(t_id) + "'")
                mydb.commit()
                print(f"trainer added with unique id {t_id}")
# add member
            elif ch == 2:
                name = input("enter name-")
                gender = input("enter gender M/F-")
                print("""
                1. low ---> amount -> 1000 [per month 1000]
                2. mid ---> amount -> 3600 [per month 800]
                3. high ---> amount -> 6000 [per month 500]
                """)
                ch = int(input("enter your choice-"))
                if ch == 1:
                    category = 'low'
                    amt = 1000
                elif ch == 2:
                    category = 'mid'
                    amt = 800
                elif ch == 3:
                    category = 'high'
                    amt = 500
                mycursor.execute("SELECT * FROM sno")
                for i in mycursor:
                    t_id, t_did = i
                t_did = t_did + 1
                mycursor.execute("INSERT INTO gym_member VALUES(" + str(t_did) + ",'" + name + "','" + gender + "','" + category + "'," + str(amt) + ")")
                mycursor.execute("UPDATE sno SET did=" + str(t_did) + "")
                mydb.commit()
                print(f"member added successfully with unique id {t_did}")

#remove trainer
            elif ch==3:
                idd=int(input("enter id to remove-"))
                mycursor.execute("select* from trainer")
                flag=0
                for i in mycursor:
                  t_id=i[0]
                  if t_id==idd:
                    flag=1
                  if flag==1:
                   mycursor.execute("delete from trainer where id='"+str(idd)+"'")
                   mydb.commit()
                   print("successfully removed..")
                else:
                   print("id not found..")
#remove member
            elif ch==4:
                 idd=int(input("enter id to remove"))
                 mycursor.execute("select*from member")
                 flag=0
                 for i in mycursor:
                     t_id=i[0]
                     if t_id==idd:
                         flag=1
                     if flag==1:
                         mycursor.execute("delete from member where id='"+str(idd)+"'")
                         mydb.commit()
                         print("removed successfully..")
                     else:
                         print("id not found!!")

#change password
            elif ch==5:
                passs=input("enter old password-")
                mycursor.execute("select*from login")
                for i in mycursor:
                    t_user,t_pas=i
                if t_pas==passs:
                    new_pas=input("enter new password-")
                    mycursor.execute("update login set password='"+new_pas+"'")
                    mydb.commit()
                    print("password successfully changed..")
                else:
                    print("wrong password!!")

            elif ch==7:
                break    
                     


















                
