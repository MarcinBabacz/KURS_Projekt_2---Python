# -*- coding: utf-8 -*-

import pymysql





# ===================================KONFIGURACJA==================================================#

# ========>BAZA DANYCH
db_pass='Lerolg_8183'
db_nazwa='projekt1'
db_usser='root'
db_host='localhost'


# ==========>WYGLĄD MENU

# ZNAKI
menu_char_border_left='|'                                           #Znak obrmowania z lewej strony
menu_char_border_right='|'                                          #Znak obrmowania z prawej strony
menu_char_border_top='_'                                            #Znak obrmowania z góryr
menu_char_lin1='='
menu_char_lin2='^'


menu1_list=['Logowanie','Ustawienia','Wyjście']
menu_prac_list=['MENU Pracownik','Odczyt','Ustawienia','Powrót','Wyjście']

# szerokość
menu_width=60

# ===================================KONIECKONFIGURACJI==================================================#

class Db():
    def __init__(self):     

        sql='SELECT VERSION()'
        self.sql_test(sql)
        
    def sql_test(self,sql):
        try:
           
            self.conn = pymysql.connect(db_host, db_usser,db_pass,db_nazwa)
            
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
        
        




class Logowanie(Db):
    #def __init__(self):
        #self.menu()

    def menu(self,menu_name,menu_lista):
        self.menu_lista=menu_lista
        self.menu_name=menu_name
        choise=''     
            
        print(' '+menu_char_border_top*(menu_width-1))                                                  # Rysuje górną krawędź tabeli
        menu_center=round((menu_width-len(self.menu_name))/2)                                         # Ustala ilość znaków do wycentrowania tytułu
        
        print(menu_char_border_left+' '*menu_center+self.menu_name+' '*menu_center+menu_char_border_right)  # Rysuje tytułowy wiersz tabeli
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)               # Rysuje linie
        
        for i,value in enumerate(self.menu_lista):                                                      
            ile=(menu_width-len(value)-6)                                                               # Ustala ilość znaków do równego wypełnienia pol
            print(menu_char_border_left+' '+str(i+1)+' - '+value+' '*ile+menu_char_border_right)        # Rysuje wiersze menu z pozycjamu menu z listy
        
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)
        
        if (sesja.info>''):                                                                              # Rysuje wiersze z informacą w razie wystapienia
            print(menu_char_border_left+' '*round((menu_width-len(sesja.info))/2-5)+' -!!- '+sesja.info+' -!!-'+' '*round((menu_width-6-len(sesja.info))/2-5)+menu_char_border_right)
            print(menu_char_border_left+menu_char_lin2*(menu_width-1)+menu_char_border_right)

       
    

    
    def log_input(self):
        sesja.menu("Logowanie","")
             
        
        self.usser_id_in=input('| Podaj swoje ID: ' )
        
        sql=("select * from pracownicy natural left join role where id_pracownika="+str(self.usser_id_in))
        self.sql_list=mysql.odczyt(sql) 
    
        if (self.sql_list!=False):
            self.usser_pass_in=input('| Podaj hasło: ')   
            
        else:
            self.info=('Brak  id w bazie')
            return False
     
    def log_pass_test(self):  
    
    
         
        if(str(self.sql_list[5].strip())==str(self.usser_pass_in.strip())):
            #self.id_roli=(self.sql_list[4])           
            return True
        else:
            self.info=('Błedne HASŁO')
            

        
class Uzytkownicy(Logowanie):

    def __init__(self):
        self.info=''


    
        
        
    def role_select (self):
        self.rola=sesja.sql_list[6].strip()
      
        sesja.menu(menu_prac_list)
        print('| Podaj numer opcji:       |')        
       
        ''' 
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
         '''
        input()
    





print('Początek programu zaczynamy')




mysql=Db() # import ustawień bazy danych / test połączenia

sesja=Uzytkownicy() # wyświetlenie menu GŁÓWNE
choise=''
menu_name="MAIN MENU"

while (choise!='3'):

    sesja.menu(menu_name,menu1_list) # wyświetlenie menu GŁÓWNE
    print(menu_char_border_left+' Podaj numer menu:')
    choise=str(input()) # POBIERA WYBÓR    
  
    if (choise=='1') :
        # MENU LOGOWANIE
        sesja.info=''
        
        if (sesja.log_input()!=False): # POBIERA ID UŻYTKOWNIKA I HASŁA (FALSE JEŻEL BRAK ID W BAZIE)
            if (sesja.log_pass_test()==True): # PORÓWNUJE WPROWADZONE HASLO Z HASŁEM BAZY)
                sesja.role_select()
    
    elif(choise=='3'):
        print('Wyjście')    
        
    else:
        sesja.info='Błędna opcja wyboru'
       



    
    


print('Koniec')
