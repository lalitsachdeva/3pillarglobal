import sqlite3
conn = sqlite3.connect("example.db")

c = conn.cursor()
#create table for employee
# c.execute('''CREATE TABLE employee1
#                 (ID integer PRIMARY KEY , name text, salary real )''')
if c.employee1 = NULL :
  print"empty "
empCount = 0
#c.execute("DELETE  FROM employee1")
class Employee:
#Common base class for all employees
  

  def  assign(self):
      global empCount 
      empCount += 1
      name1 =raw_input("Name:")
      salary1 = raw_input("Salary:")
      
      #id = "3pg0"
      #id = id+str(empCount)
      sql1 = "INSERT INTO employee1(ID,name,salary) VALUES ( NULL ,'" +name1 + "', '" +salary1 + "')"
      c.execute(sql1)
      conn.commit()
      
   
  # def displayCount(self):
  #    print "Total Employee %d" % Employee.empCount
  # def displayEmployee(self):
  #     print "Name : ", self.name,  ", Salary: ", self.salary
  def showtable(self):
      sql2 = "SELECT * FROM  employee1"
      res =  c.execute(sql2)
      print ""
      print "ID\t "+ "Name\t" +"salary"
      print"-------------------------"
      for row in res:
         print str(row[0]) + " \t" +row[1] +" \t"+ str(row[2]) 
      print "------------------------"
      conn.commit()

  def delete(self):
      print "enter the id wants to delete"
      id = raw_input()
      sql3 = "DELETE FROM employee1 WHERE ID = ('"+id+"')" 
      c.execute(sql3)
      conn.commit()

  def update(self):
     print "enter the id wants to update"
     id = raw_input()
     name1 =raw_input("Name:")
     salary1 = raw_input("Salary:")
     sql4 = "UPDATE employee1   SET name = ('"+name1+"') , salary = ('"+salary1+"') WHERE ID = ('"+id+"') "
     c.execute(sql4)
     conn.commit()
#This would create first object of Employee

emp1 = Employee()
while(1):
   print "please choose from the following:"
   print "1 - show table "
   print "2 - insert values"
   print "3 - delete values"
   print "4 - update values"
   print "5 - Exit"
   print "please provide the input: ", 
   a = (int)(raw_input())
   if (a == 1):
      emp1.showtable();
   elif(a == 2):
      emp1.assign()
   elif(a == 3):
      emp1.delete()
   elif(a == 4):
      emp1.update()
   elif(a == 5):
      exit(0)
   else:
      print" please provide us with the valid input"
      continue

   


#This would create second object of Employee class
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# emp1.displayCount()
#print "Total Employee %d" % Employee.empCount