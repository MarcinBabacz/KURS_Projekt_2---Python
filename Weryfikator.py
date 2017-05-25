# -*- coding: utf-8 -*-

import pymysql
import datetime






# ===================================KONFIGURACJA==================================================#

# ========>BAZA DANYCH
db_pass='Lerolg_8183'
db_name='projekt1'
db_usser='root'
db_host='localhost'


# ==========>WYGLĄD MENU

# ZNAKI
menu_char_border_left='|'                                           #Znak obrmowania z lewej strony
menu_char_border_right='|'                                          #Znak obrmowania z prawej strony
menu_char_border_top='_'                                            #Znak obrmowania z góryr
menu_char_lin1='='
menu_char_lin2='^'
menu_char_lin3='*'


menu1_list=['Logowanie','Ustawienia','Wyjście']
menu_prac_list=['MENU Pracownik','Odczyt','Ustawienia','Powrót','Wyjście']
menu_name="MAIN MENU"

# szerokość
menu_width=101

# ===================================KONIECKONFIGURACJI==================================================#

class Db():
    def __init__(self):     

        sql='SELECT VERSION()'
        self.sql_test(sql)
        
    def sql_test(self,sql):
        try:
           
            self.conn = pymysql.connect(db_host, db_usser,db_pass,db_name)
            
            self.c=self.conn.cursor()
            self.c.execute(sql) 
            self.conn.commit()
        except:
            print('Błąd połączenia z bazą dancyh')
            return False
    def sql_read(self,sql):

        if(self.sql_test(sql)!=False):
            result=self.c.fetchall()        
            if (len(result)>0):
                return result[0]
            else:
                return False
        else:
            return False
                      
class ScrPrint(Db):
   
    def menu_print(self,menu_name,menu_lista,usser_name,usser_vorname,usser_id_acces):
        self.menu_lista=menu_lista
        self.menu_name=menu_name
        self.date=datetime.date.today()
        choise=''     
        
        menu_hello=(usser_name+' '+usser_vorname+" ")
        
        print('\n'*30)

        print(' '+menu_char_border_top*(menu_width-1))                                                           # Rysuje górną krawędź tabeli
        print(menu_char_border_left+' DATA: '+str(self.date)+' '*(menu_width-18-len(menu_hello))+menu_hello+menu_char_border_right)  # Rysuje tytułowy wiersz tabeli
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)          
        print(menu_char_border_left+self.menu_name.center(menu_width-1)+menu_char_border_right)    
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)                            # Rysuje linie
        
        for i,value in enumerate(self.menu_lista):     
            if(value != None):
                ile=(menu_width-len(value.strip())-6)                                                              # Ustala ilość znaków do równego wypełnienia pol
                print(menu_char_border_left+' '+value[0]+' - '+value.strip()+' '*ile+menu_char_border_right)        # Rysuje wiersze menu z pozycjamu menu z listy
        
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)
        
        if (sesja.info>''):                                                                              # Rysuje wiersze z informacą w razie wystapienia
            print(menu_char_border_left+sesja.info.center(menu_width-1)+menu_char_border_right) 
            print(menu_char_border_left+menu_char_lin2*(menu_width-1)+menu_char_border_right)

class Login(ScrPrint):

    def login_input(self):

        sesja.menu_print("Logowanie","",'','','')                                                                #Print Login menu table          
        self.usser_id_in=input('| Podaj swoje ID: ' )                                                   #Input usser login id
      
        sql=("select pr_pass from pracownicy where id_pracownika="+str(self.usser_id_in))               #Sql qwery
        self.sql_list=mysql.sql_read(sql) 
    
        if (self.sql_list!=False):                                                                      #Test exits usser id in Db
            self.usser_pass_in=input('| Podaj hasło: ')                                                 #Input usser login pass
            return True                                                                                 #Returt True : usser id and usser pass corect input
        else:
            self.info=('Brak  id w bazie')                                                              #Set info : usser id not exist i db
            return False                                                                                #Returt False : usser id not exist i db
     
    def login_pass_test(self):  
    
        if(self.login_input()!=False):
            if(str(self.sql_list[0].strip())==str(self.usser_pass_in.strip())):
                return True
            else:
                self.info=('Błedne HASŁO')
                return False
                

        
class Usser(Login):

    def __init__(self):
        self.info=''
    def usser_menu (self):    
        self.usser_read()
    
    
    def usser_read (self):   
        self.usser_id=self.usser_id_in
        sql="select * from pracownicy natural left join role where id_pracownika="+self.usser_id
        usser_read_list=mysql.sql_read(sql) 
        
        self.usser_name=usser_read_list[3]
        self.usser_vorname=usser_read_list[4]
        self.usser_id_location=usser_read_list[2]
        self.usser_id_acces=usser_read_list[0]
        self.usser_name_acces=usser_read_list[6]
        
        usser_menu_list=usser_read_list[7:14]

        
        sesja.menu_print('MENU '+self.usser_name_acces,usser_menu_list,self.usser_name,self.usser_vorname,self.usser_id_acces)
        input()
    
        
   




print('Początek programu zaczynamy')










class Main():
    def __init__(self):

        self.choise=''

        self.main_body()
        
    
    def main_body(self):
        sesja.menu_print(menu_name,menu1_list,'','','') # wyświetlenie menu GŁÓWNE
        print(menu_char_border_left+' Podaj numer menu:')
        self.choise=str(input()) # POBIERA WYBÓR    
      
        if ((self.choise=='l') or (self.choise=='L')):
            # MENU LOGOWANIE
            sesja.info=''
            
            if (sesja.login_pass_test()==True):                                                                             
                sesja.usser_menu()

            
            if(self.choise!='W' or self.choise!='w'):
                self.main_body()
                       
        elif(self.choise=='3'):
            print('Wyjście')    
            
        else:
            sesja.info='Błędna opcja wyboru'
            self.main_body()


mysql=Db() # inicjacja bazy dancyh -import ustawień bazy danych / test połączenia
sesja=Usser() # wyświetlenie menu GŁÓWNE
    
Main()                #uruchomienie głównej klasy pogamu


print('Koniec')
