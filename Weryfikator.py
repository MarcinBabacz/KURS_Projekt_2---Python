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
menu_char_border_down='_'   
menu_char_lin1='='
menu_char_lin2='^'
menu_char_lin3='*'

# POZYCJE MENU
menu_main_list={"L":'Logowanie',"W":'Wyjście'}
menu_prac_list={"O":'Odczyt',"P":'Powrót',"W":'Wyjście'}
menu_store_list={"E":'Ean',"I":'Index',"G":'Grupa',"Z":'Zawaansowane',"P":'Powrót'}
menu_name="GŁÓWNE"


# szerokość
menu_width=150
menu_height=10

# NAPIS OPCJI WYBORU
menu_choice_name=' Podaj opcje wyboru MENU:'

# ===================================KONIEC KONFIGURACJI==================================================#

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
                return result
            else:
                return False
        else:
            return False
                      
# ===================================KLASA ScrPrint=================================================#  
# Klasa służy do wyświetlania informacji na ekrania

class ScrPrint(Db):
   
    def menu_print(self,menu_name,usser_acces_name,menu_lista,usser_name,usser_surname,usser_id_acces):
        self.menu_lista=menu_lista
        self.menu_name="MENU: "+menu_name
        
        self.date=datetime.date.today()
        choise=''     
        
        menu_hello=(usser_acces_name+' '+usser_name+' '+usser_surname+' ')
        
        print('\n'*30)

        print(' '+menu_char_border_top*(menu_width-1))                                                           # Rysuje górną krawędź tabeli
        print(menu_char_border_left+' DATA: '+str(self.date)+' '*(menu_width-18-len(menu_hello))+menu_hello+menu_char_border_right)  # Rysuje tytułowy wiersz tabeli
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)          
        print(menu_char_border_left+self.menu_name.center(menu_width-1)+menu_char_border_right)    
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)                            # Rysuje linie
        
 
      
        if(self.menu_lista!=''):
            for i in (self.menu_lista.keys()):     
                ile=(menu_width-len(self.menu_lista[i].strip())-6)                                                      # Ustala ilość znaków do równego wypełnienia pol
                print(menu_char_border_left+' '+i+' - '+self.menu_lista[i].strip()+' '*ile+menu_char_border_right)    # Rysuje wiersze menu z pozycjamu menu z   listy
         

        for i in range(menu_height-len(self.menu_lista)):
            print(menu_char_border_left+" "*(menu_width-1)+menu_char_border_right)
        
        print(menu_char_border_left+"="*(menu_width-1)+menu_char_border_right)
        
        if (sesja.info>''):                                                                              # Rysuje wiersze z informacą w razie wystapienia
            print(menu_char_border_left+sesja.info.center(menu_width-1)+menu_char_border_right) 
            print(menu_char_border_left+menu_char_lin2*(menu_width-1)+menu_char_border_right)
            
            
    def store_print(self,menu_name,usser_acces_name,store_list,usser_name,usser_surname,usser_id_acces):
        self.store_list=store_list
        self.menu_name="MENU: "+menu_name
        
        self.date=datetime.date.today()
        choise=''     
        
        menu_hello=(usser_acces_name+' '+usser_name+' '+usser_surname+' ')
        
        print('\n'*30)

        print(' '+menu_char_border_top*(menu_width-1))                                                           # Rysuje górną krawędź tabeli
        print(menu_char_border_left+' DATA: '+str(self.date)+' '*(menu_width-18-len(menu_hello))+menu_hello+menu_char_border_right)  # Rysuje tytułowy wiersz tabeli
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)          
        print(menu_char_border_left+self.menu_name.center(menu_width-1)+menu_char_border_right)    
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)                            # Rysuje linie
  
        print(menu_char_border_left+" l.P    |        SKLEP        |          GRUPA         |                 NAZWA          |      ILOŚĆ     |        CENA        |"+menu_char_border_right)
        print(menu_char_border_left+"-"*(menu_width-1)+menu_char_border_right)   
       
       
        if(self.store_list!=''):
            for i,value in enumerate(self.store_list):
               # print(i)
                                                              # Ustala ilość znaków do równego wypełnienia pol
                print(menu_char_border_left+' '+str(i)+' - '+value[1].strip()+"                       "+menu_char_border_right)   
                print(menu_char_border_left+"-"*(menu_width-1)+menu_char_border_right)
                
                
                # Rysuje wiersze menu z pozycjamu menu z   listy    
        
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)
        
        if (sesja.info>''):                                                                              # Rysuje wiersze z informacą w razie wystapienia
            print(menu_char_border_left+sesja.info.center(menu_width-1)+menu_char_border_right) 
            print(menu_char_border_left+menu_char_lin2*(menu_width-1)+menu_char_border_right)
        
        
        
        

# ===================================KLASA Login=================================================#  
# Klasa służy do logowania uzytkowaników

class Login(ScrPrint):

    def login_input(self):

        sesja.menu_print("Logowanie",'','','','','')                                                                #Print Login menu table          
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
            if(str(self.sql_list[0][0].strip())==str(self.usser_pass_in.strip())):
                return True
            else:
                self.info=('Błedne HASŁO')
                return False

# ===================================KLASA Usser=================================================#  
# Klasa służy do odczytu danych użytkowniaków
        
class Usser(Login):

    def __init__(self):
        self.info=''
    
    def usser_menu (self):    
        
        print('menu_main_list')
        sesja.menu_print(self.usser_name_acces,self.usser_name_acces,menu_prac_list,self.usser_name,self.usser_surname,self.usser_id_acces)
        
    
    def usser_read (self):   
        self.usser_id=self.usser_id_in
        sql="select * from pracownicy natural left join role where id_pracownika="+self.usser_id
        usser_read_list=mysql.sql_read(sql) 
        
        self.usser_name=usser_read_list[0][3]
        self.usser_surname=usser_read_list[0][4]
        self.usser_id_location=usser_read_list[0][2]
        self.usser_id_acces=usser_read_list[0][0]
        self.usser_name_acces=usser_read_list[0][6]
        self.usser_menu_list=menu_prac_list

        
        
       
        return self.usser_id_acces

# ===================================KLASA Store================================================#  
# Klasa służy do odczytu informacji o towarach

class Store(Usser):

    def store_menu (self):    
        
        
        sesja.menu_print(self.usser_name_acces,self.usser_name_acces,self.store_menu_list,self.usser_name,self.usser_surname,self.usser_id_acces)
    
        
    def store_read(self,store_read_choice):
        self.info=('')  
        print(store_read_choice)
        
        if(store_read_choice=="I"):
            sesja.menu_print("WYSZUKA TOWAR PO INDEX",self.usser_name_acces,'',self.usser_name,self.usser_surname,self.usser_id_acces)
            
        
          
            self.index=int(input('| Podaj index towaru: ' ))  
           
            
            sql=("SELECT id_sklep,branza,grupa, kod_index, towar_nazwa, zasoby_ilosc, zasoby_cena FROM zasoby NATURAL JOIN towary where id_sklep='"+self.usser_id_location+"' AND kod_index='"+str(self.index)+"'")
            #print(sql)
           
            self.sql_list=mysql.sql_read(sql) 
    
            
            if (self.sql_list!=False):
                sesja.store_print("WYSZUKANY INDEX",self.usser_name_acces,self.sql_list,self.usser_name,self.usser_surname,self.usser_id_acces)
 
                
                #Returt True : usser id and usser pass corect input
            else:
                self.info=('Brak  INDEXU w bazie')                                                              #Set info : usser id not exist i db
                return False  
            


print('Początek programu zaczynamy')





# ===================================KLASA Main================================================#  
# Główna klasa programu




class Main():
    def __init__(self):

       
   
        

        self.main_body()
        
    
    def main_body(self):

        sesja.info=''
        self.choice=''
        while(True):
            print(len(menu_main_list))
            sesja.menu_print(menu_name,'',menu_main_list,'','','') # wyświetlenie menu GŁÓWNE
            self.choice=str(input(menu_char_border_left+menu_choice_name+' '*(menu_width-len(menu_choice_name)-1)+menu_char_border_right+"\n"+menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right+"\n")) # POBIERA WYBÓR    
          
            if ((self.choice=='l') or (self.choice=='L')):
                # MENU LOGOWANIE
                sesja.info=''
                
                if (sesja.login_pass_test()==True):                                                                             
                    # MENU UŻYTKOWNIKKA
                    sesja.usser_read()                                                                      # ODCZYT DANYCH UŻYTKOWNIAKA Z DB
                    sesja.info='' 

                  
                    while (True):
                        self.choice2=''
                        
                        sesja.usser_menu()
    
                        self.choice2=str(input(menu_char_border_left+menu_choice_name+' '*(menu_width-len(menu_choice_name)-1)+menu_char_border_right+"\n"+menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right+"\n")) # POBIERA WYBÓR   
    
                        if ((self.choice2=='O') or (self.choice2=='o')):
                            # MENU SZYKANIA TOWARU
                            sesja.info=''
                            
                            while(True):
                                self.choice=''
                                
                                sesja.menu_print('WYSZUKAJ TOWAR',sesja.usser_name_acces,menu_store_list,sesja.usser_name,sesja.usser_surname,sesja.usser_id_acces) # wyświetlenie menu oDCZYT
                                self.choice=str(input(menu_char_border_left+menu_choice_name+' '*(menu_width-len(menu_choice_name)-1)+menu_char_border_right+"\n"+menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right+"\n")) # POBIERA WYBÓR   
                            
                                                   
                                if (self.choice.upper() in menu_store_list.keys()):
                  
                                    if(self.choice=='P' or self.choice=='p'):
                                        sesja.info='' 
                                        break                                         
                                    else:
                                        sesja.store_read(self.choice.upper())

                                else:
                                    sesja.info='Błędna opcja wyboru'
                                
                        elif(self.choice2=='P' or self.choice2=='p'):
                            sesja.info='' 
                            break
                        elif(self.choice2=='W' or self.choice2=='w'):
                            self.choise='W'
                            break                        
                
                        else:
                            sesja.info='Błędna opcja wyboru'
                if(self.choice=='W' or self.choice=='w'):
                    break  

            elif(self.choice=='W' or self.choice=='w'):
                break   
                
            else:
                sesja.info='Błędna opcja wyboru'
 



mysql=Db() # inicjacja bazy dancyh -import ustawień bazy danych / test połączenia
                
sesja=Store() # wyświetlenie menu GŁÓWNE        
Main()                #uruchomienie głównej klasy pogamu


print('Koniec')
