def marksheet():
   db = open("databasemarksheet3.txt","r")
   tamil = int(input("tamil"))
   english= int(input())
   maths =int(input())   
   science =int(input())
   social =int(input())    
   total = tamil+english+maths+science+social 
   print(total)
   if(tamil <50 or english <50  or maths<50 or science < 50 or social < 50):
      print("fail")
      db =open("databasemarksheet3.txt","a")
      write = (str(tamil),str(english),str(maths),str(science),str(social),str(total))
      db.write(str(write))
      db.write("fail")
   else:          

      db =open("databasemarksheet3.txt","a")
      write = (str(tamil),str(english),str(maths),str(science),str(social),str(total))
      db.write(str(write))
      db.write("pass")
      print("pass")
      print("sucess!")  
          

marksheet()
  
def access():
    pass