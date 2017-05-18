# -*- coding: utf-8 -*-

import pymysql

has='Lerolg_8183'



class Db():
    def __init__(self):     
        self.conn = pymysql.connect('localhost', "root",has,'projekt1')
        sql='SELECT VERSION()'
        self.sql_test(sql)
        
    def sql_test(self,sql):
        try:
            self.c=self.conn.cursor()
            self.c.execute(sql) 
            self.conn.commit()
        except:
            print('Błąd połączenia z bazą dancyh')
    
    def odczyt(self,sql):
        
        self.sql_test(sql)
        result=self.c.fetchall()        
        if (len(result)>0):
            return result[0]
        else:
            return False
        
        




class Logowanie():
    def __init__(self):
        self.menu()

    def menu(self):
        choise=''
        while (choise!='1' and choise!='2'):
            print(' __________________________')
            print('|        MAIN MENU         |')
            print('|==========================|')
            print('| 1 - Logowanie:           |')
            print('| 2 - Wyjsćie              |')
            print('|==========================|')
            print('| Podaj numer opcji:       |')
            
            
            choise=str(input())
        
        if (choise=='1') :
            self.log_input()
        elif(choise=='2'):
            print('Wyjście')
    
    def log_input(self):
        print(' __________________________')
        print('|         LOGOWANIE        |')
        print('|==========================|')        
             
        
        self.usser_id_in=input('Podaj swoje ID: ' )
     
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
        
      
        if(str(self.sql_list[5])==str(self.usser_pass_in)):
            print('Logowanie OK')
        else:
            print('Błędne hasło')
        
        print(str(self.sql_list[5]))
        print(str(self.usser_pass_in))
        



print('Początek programu zaczynamy')


mysql=Db()

login=Logowanie()

print('Koniec')
