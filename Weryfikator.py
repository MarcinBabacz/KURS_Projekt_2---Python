# -*- coding: utf-8 -*-

import pymysql

has='Lerolg_8183'



class Db():
    def __init__(self):     
        print('sdgsdgsdgdgdsf')
        self.conn = pymysql.connect('localhost', "root",has,'projekt1')
        sql='SELECT VERSION()'
        self.sql_test(sql)
        
    def sql_test(self,sql):
        try:
            print('TEST')
            self.conn = pymysql.connect('localhost', "root",has,'projekt1')
            
            print(sql)
            self.c=self.conn.cursor()
            self.c.execute(sql) 
            self.conn.commit()
        except:
            print('Błąd połączenia z bazą dancyh')
    
    def odczyt(self,sql):
        print('odczyt')
        print(sql)
        
        
        self.sql_test(sql)
        result=self.c.fetchall()        
        if (len(result)>0):
            return result[0]
        else:
            return False
        
        




class Logowanie(Db):
    def __init__(self):
        self.menu()

    def menu(self):
        choise=''
        #menu_list=[]
        
        
        
        while (choise!='1' and choise!='2'):
            
            
            
            
            
            print(' __________________________')
            print('|        MAIN MENU         |')
            print('|==========================|')
            print('| 1 - Logowanie:           |')
            print('| 2 - Ustawienia           |')
            print('| 3 - Wyjsćie              |')
            print('|==========================|')
            print('| Podaj numer opcji:       |')
            
            
            choise=str(input())
        
        if (choise=='1') :
            self.log_input()
        elif(choise=='3'):
            print('Wyjście')
    
    def log_input(self):
        print(' __________________________')
        print('|         LOGOWANIE        |')
        print('|==========================|')        
             
        
        self.usser_id_in=input('| Podaj swoje ID: ' )
     
        sql=("select * from pracownicy where id_pracownika="+self.usser_id_in)
        self.sql_list=mysql.odczyt(sql) 
        print(str(self.sql_list[5]))
        self.usser_pass_in=input('Podaj hasło: ')   
    
        if (self.sql_list!=False):
            self.log_test()
        else:
            print('Brak  id w bazie')
            self.__init__()    
 
    def log_test(self):
    
    
    
         
        if(str(self.sql_list[5].strip())==str(self.usser_pass_in.strip())):
            self.id_roli=(self.sql_list[4])
            
            Uzytkownicy(self)
        
        else:
            print('Błędne hasło')
            self.menu()

        
class Uzytkownicy(Logowanie):

    def __init__(self,id_roli):

        self.lista=login.sql_list
        self.id_roli=id_roli
        self.role_select()
    
        
        
    def role_select (self):
        print(' __________________________')
        print(' __________________________')
        print('|        MENU'+'%10S'% (self.lista[5])+'|')
        print('|==========================|')
        print('| 1 - Logowanie:           |')
        print('| 2 - Ustawienia           |')
        print('| 3 - Wyjsćie              |')
        print('|==========================|')
        print('| Podaj numer opcji:       |')        
        
        if (self.id_roli==1):       
            print('admin')
        elif (self.id_roli==2):
            print('Regionalny')
        elif (self.id_roli==3):
            print('Kierownik')       
        elif (self.id_roli==4):
            print('Zastępca') 
        elif (self.id_roli==5):
            print('Sprzedawca') 
        elif (self.id_roli==6):
            print('Gość')  
        

    



print('Początek programu zaczynamy')


mysql=Db()

login=Logowanie()

print('Koniec')
