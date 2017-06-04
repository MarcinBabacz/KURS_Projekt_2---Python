# -*- coding: utf-8 -*-
# ===================================IMPORT BIBLIOTEK========================================>
import pymysql
import datetime
import math

# ===================================CONFIG==================================================>


# ------------>Config database
db_pass=''                              #Hasło dostępu do bazy
db_name=''                      #Nazwa Bazy
db_usser=''                         #Uzytkownik
db_host=''                     #Host


# ------------>Config  VIEW
# W tym obszasze ustawiane są znaki używane przy rysowaniu okien programu

# ZNAKI
menu_char_border_left='|'               #Znak obrmowania z lewej strony
menu_char_border_right='|'              #Znak obrmowania z prawej strony
menu_char_border_top='_'                #Znak obrmowania z górny
menu_char_border_down='_'               #Znak obrmowania z dolnego
menu_char_lin1='='                      #Znak lini poziomej 1
menu_char_lin2='^'                      #Znak lini poziomej 2
menu_char_lin3='*'                      #Znak lini poziomej 3
menu_char_border_col='|'                #Znak oddzielający kolumny tabeli
menu_char_border_row='-'                #Znak oddzielający wiersze tabeli

# ------------> LISTY MENU
# W tym obszarze konfigurowane są pozycje menu programu
menu_main_list={"L":'Logowanie',"W":'Wyjście'}                                          # Lista pozycji menu głównego
menu_prac_list={"O":'Odczyt',"P":'Powrót',"W":'Wyjście'}                                # Lista pozycji menu pracownika
menu_store_list={"E":'Ean',"I":'Index',"G":'Grupa',"Z":'Zawaansowane',"P":'Powrót'}     # Lista pozycji menu odczytu magazynu
menu_name="MENU GŁÓWNE"                                                                 # Etykieta menu głownego

# ------------> ETYKIETY KOLUMN TABELU
# W tym obszarze konfigurowane są nazwy etykiet tabeli odczytu magazyny wraz z ustawieniem oraz formatowaniem pola

table_label_lp=["l.p",5]                              # konfiguracja etykiety pola l.p
table_label_store=["SKLEP",6,"%-6s"]                  # konfiguracja etykiety pola "SKLEP" w tabeli odczytu stanów
table_label_index=["INDEX",7,"%-7s"]                  # konfiguracja etykiety pola "INDEX" w tabeli odczytu stanów
table_label_group=["GRUPA",15,"%-15s"]                # konfiguracja etykiety pola "GRUPA" w tabeli odczytu stanów
table_label_name=["NAZWA",0,"%-30s"]                  # konfiguracja etykiety pola "NAZWA" w tabeli odczytu stanów szerokość ustawiana jest AUTOMATYCZNIE
table_label_quan=["ILOŚĆ",7,"%6s "]                   # konfiguracja etykiety pola "ILOŚĆ" w tabeli odczytu stanów
table_label_price=["CENA",10,"%9s "]                  # konfiguracja etykiety pola "CENA" w tabeli odczytu stanów
table_label_prior=["PRIORYTET",8,"%-8s"]              # konfiguracja etykiety pola "PRIORYTET" w tabeli odczytu stanów
table_label_promo=["PROMOCJA",8,"%-8s"]               # konfiguracja etykiety pola "PROMOCJE" w tabeli odczytu stanów

# ------------> ROZMIAR OKNA
# W tym obszarze konfigurowane są wymiary okna programu
menu_width=100 # minimum 100!!!!
menu_height=15  # minimum 5 !!!!!

# NAPIS OPCJI WYBORU
menu_choice_name=' Podaj opcje wyboru MENU:'

# ===================================END CONFIG==================================================<

# ===================================KLASA Db ==================================================>
# Kalsa Db realizuje połączenie z bazą dancyh, test połączenia oraz zwraca listy wyników zapytań
class Db():
    def __init__(self):     

        sql='SELECT VERSION()'                                                          # Zapytanie inicjujące test połączneie z bazą
        self.sql_test(sql)                                                              # Iicjacja testu bazy
        
    def sql_test(self,sql):                                                             # metoda testująca połącznie z bazą na podstawie przyjętego zapytania
        try:       
            self.conn = pymysql.connect(db_host, db_usser,db_pass,db_name)              # inicjacja połączenia z bazą na podstawie dancy z konfiguracji
            self.c=self.conn.cursor()
            self.c.execute(sql) 
            self.conn.commit()
        except:
            print('Błąd połączenia z bazą dancyh')                                      # komunikat przy błędzie odczytu bazy dancyh
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
# ===================================KLASA Db ==================================================>

                      
# ===================================KLASA ScrPrint=================================================>
# Klasa służy do wyświetlania informacji na ekranie

class ScrPrint(Db):
    def print_header(self):                                                                         # metoda rysuje nagłowek okna programu
        self.date=datetime.date.today()                                                             # inicjacja zmiennej aktualnej daty
                                                                                                                
        print('\n'*30)                                                                              # separacja okna 30 liniami  
        if(self.menu_name!="Menu Główne" and self.menu_name!="LOGOWANIE"):
            self.menu_hello="Zalogowany: "+sesja.usser_name_acces+" "+sesja.usser_name+" "+sesja.usser_surname+" "  
        else:
            self.menu_hello=""
       
        print(' '+menu_char_border_top*(menu_width-1))                                              # Rysuje górną krawędź tabeli
        print(menu_char_border_left+' DATA: '+str(self.date)+' '*(menu_width-18-len(self.menu_hello))+self.menu_hello+menu_char_border_right)  # Rysuje tytułowy wiersz tabeli wraz z informacją o dacie i zalogowanym pracowniku
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)           # Rysuje linie 
        print(menu_char_border_left+self.menu_name.center(menu_width-1)+menu_char_border_right)     # Wiersz z informacją o
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)           # Rysuje linie
        

    def menu_print(self,menu_name,menu_lista):                                                      #metoda rysuje okno menu z pobranej mapy pozycji
        self.menu_lista=menu_lista
        self.menu_name=menu_name
        self.print_header()

        if(self.menu_lista!=''):                                                                    # Sprawdza czy mapa menu nie jest pusta
            for i in (self.menu_lista.keys()):     
                ile=(menu_width-len(self.menu_lista[i].strip())-5-len(i))                           # Ustala ilość znaków do równego wypełnienia pol
                print(menu_char_border_left+' '+str(i)+' - '+self.menu_lista[i].strip()+' '*ile+menu_char_border_right)    # Rysuje wiersze menu z pozycjamu menu z   listy
        for i in range(menu_height-len(self.menu_lista)):                                          # Wypełnienie wierszy do osiągniecia ustalonej wysokości okna
            print(menu_char_border_left+" "*(menu_width-1)+menu_char_border_right)
        
        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)          # Rysuje linie graniczną
        
        if (sesja.info>''):                                                                        # Rysuje wiersze z informacą w razie wystapienia błędu
            print(menu_char_border_left+sesja.info.center(menu_width-1)+menu_char_border_right) 
            print(menu_char_border_left+menu_char_lin2*(menu_width-1)+menu_char_border_right)
                                                                                                   
    def store_print_head(self):                                                                    # -> METODA RYSUJĄCA ETYKIETY TABELI ODCZYTU STANÓW MAGAZYNOWYCH
        print(menu_char_border_left+                                                               # ZnaK krawędzi z lewej strony
                  table_label_lp[0].center(table_label_lp[1])+menu_char_border_col+                # Etykieta pola L.P wraz z formatowaniem
                  table_label_store[0].center(table_label_store[1])+menu_char_border_col+          # Etykieta pola "SKLEP" wraz z formatowaniem
                  table_label_index[0].center(table_label_index[1])+menu_char_border_col+          # Etykieta pola "INDEX" wraz z formatowaniem
                  table_label_name[0].center(menu_width-self.len_name)+menu_char_border_col+       # Etykieta pola "NAZWA" wraz z AUTOMATYCZNYM formatowaniem SZEROKOŚCI
                  table_label_quan[0].center(table_label_quan[1])+menu_char_border_col+            # Etykieta pola "ILOŚĆ" wraz z formatowaniem
                  table_label_price[0].center(table_label_price[1])+                               # Etykieta pola "CENA" wraz z formatowaniem
                  menu_char_border_right)                                                          # ZnaK krawędzi z prawej strony
        print(menu_char_border_left+menu_char_border_row*(menu_width-1)+menu_char_border_right)    # Rysuje linie graniczną wierszy
        
    def store_print(self,menu_name,store_list):                                                    #-> METODA RYSUJĄCA TABELE ODCZYTU STANÓW                        
        self.store_list=store_list                                                                 # Przypianie zmiennej 
        self.menu_name=menu_name                                                                   # Przypianie zmiennej 
        self.len_name=table_label_lp[1]+table_label_store[1]+table_label_index[1]+table_label_quan[1]+table_label_price[1]+6 # Ustalenie szerokości uzytych etykiek
  
        self.print_header()                                                                        # Wyswietlenie nagłówKa okna
        self.store_print_head()                                                                    # Wyswietlenie etykiet tabeli
        
        if(self.store_list!=''):                                                                   # sprawdzenicz czy lista towarów nie jest pusta
            licznik=0                                                                               # inicjacja zmiennej licznika wypisancyh lini
            for i,value in enumerate(self.store_list):                                             # pętla literująca po liscie towarów
                name_list=[]                                                                       # inicjacja tableli do dzielenia długich nazw towarów do szerokości
                # Pętla dzieląca nazwe towaru na części odpowiadające szerokośic ustalonej szerokości pola nazwa
                for y in range(math.ceil(len(value[4])/(menu_width-self.len_name))):               
                    name_list.append(value[4][y*(menu_width-self.len_name):(y+1)*(menu_width-self.len_name)])

                print(menu_char_border_left+                                                        # Wyświetlenie znaku lewej krawędzie tabeli towarów
                      str(i).center(table_label_lp[1])+menu_char_border_col+                        # Wyświetlenie liczby porządkowej towaru wraz z separatorem kolumn
                      table_label_store[2]%value[0].strip()+menu_char_border_col+                   # Wyświetlenie kodu sklepu wraz z separatorem kolumn
                      table_label_index[2]%value[3]+menu_char_border_col+                           # Wyświetlenie INDEKSU wraz z separatorem kolumn
                      name_list[0]+" "*(menu_width-self.len_name-len(name_list[0]))+menu_char_border_col+ # Wyświetlenia pierwszej części nazwy towaru
                      table_label_quan[2]%value[5]+menu_char_border_col+                            # Wyświetlenie ILOŚCI
                      table_label_price[2]%value[6]+                                                # Wyświetlenie CENY 
                      menu_char_border_right)                                                       # Wyświetlenie znaku PRAWEJ krawędzie tabeli towarów 
                licznik+=1                                                                          # Zwiększeni liczkina wyświetlonych linia
                for z,value in enumerate(name_list):                                                # Pętla wyświetlająca pozostale częśc nazwy towaru
                    if z>0:                                                                         # Sprawdzenie czy nazwa była dluższa niż pole nazwy
                        print(menu_char_border_left+                                                # Wyświetlenie pozostałych części nazwy, pozostałe pola są puste
                              " ".center(table_label_lp[1])+"|"+
                              table_label_store[2]%" "+"|"+
                              table_label_index[2]%" "+"|"+
                              value+" "*(menu_width-self.len_name-len(value))+"|"+
                              table_label_quan[2]%" "+"|"+
                              table_label_price[2]%" "+
                              menu_char_border_right)    
                        licznik+=1                                                                  # Zwiększeni liczkina wyświetlonych linia

                strony="Strona "+str(math.ceil(i/menu_height))+" z "+str(int(len(self.store_list)/menu_height+0.5)) # Ustalenie aktualnej strony oraz total stron
                str_info=strony+" , ENTER- DALEJ "                                                  # Dodanie info strony
                if (licznik>=menu_height):                                                          # test czy ilość wierszy jest większa niż ustalona wysokość okan
                    
                    print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)         # Rysuje linie graniczną wierszy
                    print(menu_char_border_left+str_info.center(menu_width-1)+menu_char_border_right)         # Rysuje wiersz z informacją o numerze strony
                    print(menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right)  # Rysuje dolną linie graniczną okna
                    input()                                                                                   # input w celu zatrzymania wyświetlenia listy towarów
                    
                    licznik=0                                                                                 # wyzerowania licznika wirszy
                    self.store_print_head()                                                                   # Wyświetlenie nagłówna okna
                    self.print_header()                                                                       # Wyświetlenie etykiet tabeli

        for i in range(menu_height-len(self.menu_lista)):                                                     # Petla uzupełniająca wiersze do ustalonej wysokości okna
              
            print(menu_char_border_left+
                                      " ".center(table_label_lp[1])+"|"+
                                      table_label_store[2]%" "+"|"+
                                      table_label_index[2]%" "+"|"+
                                      " "*(menu_width-self.len_name)+"|"+
                                      table_label_quan[2]%" "+"|"+
                                      table_label_price[2]%" "+
                                      menu_char_border_right)               

        print(menu_char_border_left+menu_char_lin1*(menu_width-1)+menu_char_border_right)                # Rysuje linie graniczną wierszy
        
        if (sesja.info>''):                                                                              # Rysuje wiersze z informacą w razie wystapienia
            print(menu_char_border_left+sesja.info.center(menu_width-1)+menu_char_border_right) 
            print(menu_char_border_left+menu_char_lin2*(menu_width-1)+menu_char_border_right)
        
        str_info=strony+" , ENTER- POWRÓT "
        print(menu_char_border_left+str_info.center(menu_width-1)+menu_char_border_right)
        print(menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right)

        input()    
        

# ===================================KLASA Login=================================================#  
# Klasa służy do logowania uzytkowaników

class Login(ScrPrint):

    def login_input(self):
        menu_name="LOGOWANIE"                                                               
        sesja.menu_print(menu_name,'')                                                                  #Print Login menu table 
        self.usser_id_in=input('| Podaj swoje ID: ' )                                                   #Input usser login id
        sql=("select pr_pass from pracownicy where id_pracownika="+str(self.usser_id_in))               #Sql qwery
        self.sql_list=mysql.sql_read(sql) 
    
        if (self.sql_list!=False):                                                                      #Test exits usser id in Db
            self.usser_pass_in=input('| Podaj hasło: ')                                                 #Input usser login pass
            return True                                                                                 #Returt True : usser id and usser pass corect input
        else:
            self.info=('Brak  id w bazie')                                                              #Set info : usser id not exist i db
            return False                                                                                #Returt False : usser id not exist i db
     
    def login_pass_test(self):                                                                          # Metoda poronująca wprowadzone hasło z hasłem z bazy
    
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
        
        sesja.menu_print("MENU "+self.usser_name_acces,menu_prac_list)

    def usser_read (self):                                                                                 # Metoda odczytu danych pracownika z bazy
        self.usser_id=self.usser_id_in                                                                     # Przypisanie wprowadzonego ID do zmiennej
        sql="select * from pracownicy natural left join role where id_pracownika="+self.usser_id           # zapytanie odczytu dancyh pracownika
        usser_read_list=mysql.sql_read(sql)                                                                # Wywołanie zapytania w bazie

        self.usser_name=usser_read_list[0][3]
        self.usser_surname=usser_read_list[0][4]
        self.usser_id_location=usser_read_list[0][2]
        self.usser_id_acces=usser_read_list[0][0]
        self.usser_name_acces=usser_read_list[0][6]
        self.usser_menu_list=menu_prac_list
        return self.usser_id_acces
    
    def usser_store_choice(self):                                                                          # Metoda wyboru sklep dla roli regionalny
        sql=("select id_sklepy,sklep_miasto,sklep_adres from sklepy natural left join regiony where id_pracownika='"+self.usser_id+"'")
        self.sql_list=mysql.sql_read(sql) 
        self.store_reg_list={}
       
        if (self.sql_list!=False):
            for i,value in enumerate(self.sql_list):
                self.store_reg_list[value[0]]="%-15s"%value[1]+" "+value[2]
            self.store_reg_list["ALL"]="%-15s"%"Wszyskie"
        else:
            self.info=('Brak sklepów w regionie')                                                              

        while(True):
            sesja.menu_print("WYBÓR SKLEPU",self.store_reg_list)
            self.info=''  
            input_info="Podaj ID sklepu "
            print(menu_char_border_left+input_info+" "*(menu_width-len(input_info)-1)+menu_char_border_right)
            print(menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right)            
            loc_tmp=input()

            if loc_tmp in self.store_reg_list:
                return loc_tmp
            else:
                self.info=('Błędny skelp') 
        
        

# ===================================KLASA Store ================================================#  
# Klasa służy do odczytu informacji o towarach

class Store(Usser):

    def store_menu (self):    
        
        menu_name=self.usser_name_acces
        sesja.menu_print(menu_name,self.store_menu_list)

    def store_read(self,store_read_choice,loc_tmp):
        sql=''
        self.info=''            
        
        if(store_read_choice=="I"):                                                             # Wyszukanie towaru w bazie dla Indeks
            input_info="Podaj index towaru:"
            sesja.menu_print("WYSZUKAJ TOWAR WEDLUG INDEX",'')
            print(menu_char_border_left+input_info+" "*(menu_width-len(input_info)-1)+menu_char_border_right)
            print(menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right)
            self.input_tmp=input()
            
            sql=("SELECT id_sklep,branza,grupa, kod_index, towar_nazwa, zasoby_ilosc, zasoby_cena FROM zasoby NATURAL JOIN towary where id_sklep='"+loc_tmp+"' AND kod_index='"+str(self.input_tmp)+"'")
            serch_name="WYSZUKANY INDEX: "+self.input_tmp
       
        if(store_read_choice=="E"):                                                              # Wyszukanie towaru w bazie dla EAN
            input_info="Podaj EAN towaru:"
            sesja.menu_print("WYSZUKAJ TOWAR WEDŁUG EAN",'')
            print(menu_char_border_left+input_info+" "*(menu_width-len(input_info)-1)+menu_char_border_right)
            print(menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right)
            self.input_tmp=input()            
            
            sql=("SELECT id_sklep,branza,grupa, kod_index, towar_nazwa, zasoby_ilosc, zasoby_cena FROM bazaean NATURAL JOIN zasoby NATURAL JOIN towary where id_sklep='"+loc_tmp+"'  AND kod_ean='"+str(self.input_tmp)+"'")
            serch_name="WYSZUKANY EAN: "+self.input_tmp
       
        if(store_read_choice=="G"):                                                                # Wyszukanie towaru w bazie dla Grupy towarowej
            input_info="Podaj GRUPE towarową: "
            sesja.menu_print("WYSZUKAJ TOWARY Z GRUPY TOWAROWEJ",'')
            print(menu_char_border_left+input_info+" "*(menu_width-len(input_info)-1)+menu_char_border_right)
            print(menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right)
            self.input_tmp=input()            
            
            sql=("SELECT id_sklep,branza,grupa, kod_index, towar_nazwa, zasoby_ilosc, zasoby_cena FROM bazaean NATURAL JOIN zasoby NATURAL JOIN towary where id_sklep='"+loc_tmp+"'  AND grupa='"+str(self.input_tmp)+"'")
            serch_name="WYSZUKANY grupa: "+self.input_tmp      
       
       
        if(len(sql)!=0):                                                                             # spradzenie czy zapytanie zostało wygenrowanie poprawnie
            self.sql_list=mysql.sql_read(sql) 
            if (self.sql_list!=False):
                sesja.store_print(serch_name,self.sql_list)
            else:
                self.info=('BRAK TOWARU W BAZIE SPEŁNIAJĄCEGO KRYTERIA')                             #Set info : usser id not exist i db
                return False  
        else:  
            self.info=('BRAK WYBRANEGO MODUŁU WYSZUKIWANIA')                                         #Set info : usser id not exist i db
            return False             
        

# ===================================KLASA Main================================================#  
# Główna klasa programu

class Main(Store):
    def __init__(self):

        self.main_body()                    

    def main_body(self):
        while(True):                                                                                # GŁÓWNA PĘTLA PROGRAMU

            sesja.menu_print("Menu Główne",menu_main_list)                                          # wyświetlenie menu GŁÓWNE
            self.choice=str(input(menu_char_border_left+menu_choice_name+' '*(menu_width-len(menu_choice_name)-1)+menu_char_border_right+"\n"+menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right+"\n")) # POBIERA WYBÓR    
          
            if (self.choice.upper()=='L'):
                # MENU LOGOWANIE
                sesja.info=''
                
                if (sesja.login_pass_test()==True):                                                                             
                    # MENU UŻYTKOWNIKKA
                    sesja.usser_read()                                                               # ODCZYT DANYCH UŻYTKOWNIAKA Z DB
                    sesja.info='' 

                    while (True):                                                                    # PĘTLA MENU UŻYTKOWNIKA
                        self.choice2=''
                        sesja.usser_menu()                                                           # Wyswietlenie menu użytkowanika
    
                        self.choice2=str(input(menu_char_border_left+menu_choice_name+' '*(menu_width-len(menu_choice_name)-1)+menu_char_border_right+"\n"+menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right+"\n")) # POBIERA WYBÓR   
    
                        if (self.choice2.upper()=='O'):
                            # MENU SZYKANIA TOWARU
                            self.info=''
                            
                            if(sesja.usser_id_acces==2 or sesja.usser_id_acces==6):
                                self.loc_tmp=sesja.usser_store_choice()
                            else:
                                self.loc_tmp=sesja.usser_id_location                            
                            
                            if(self.loc_tmp.strip()=="ALL"):
                                menu_name="WYSZUKAJ TOWAR W REGIONIE"
                            else:
                                menu_name="WYSZUKAJ TOWAR W MAGAZYNIE "+self.loc_tmp                            

                            while(True):                                                            # PĘTLA MENU ODCZYTU TOWARÓW
                                self.choice=''
                                self.info='' 
                                sesja.menu_print(menu_name,menu_store_list)                         # wyświetlenie menu oDCZYT
                                
                                self.choice=str(input(menu_char_border_left+menu_choice_name+' '*(menu_width-len(menu_choice_name)-1)+menu_char_border_right+"\n"+menu_char_border_left+menu_char_border_down*(menu_width-1)+menu_char_border_right+"\n")) # POBIERA WYBÓR   
                
                                if (self.choice.upper() in menu_store_list.keys()):                 # Sprawdzenie czy pobrany znaj jest w kluczem mapy menu
                                    if(self.choice.upper()=='P'):
                                        sesja.info='' 
                                        break                                         
                                    else:
                                        sesja.store_read(self.choice.upper(),self.loc_tmp)

                                else:
                                    sesja.info='Błędna opcja wyboru'
                                
                        elif(self.choice2.upper()=='P'):
                            sesja.info='' 
                            break
                        elif(self.choice2.upper()=='W'):
                            self.choice='W'
                            break                        
                
                        else:
                            sesja.info='Błędna opcja wyboru'
                if(self.choice.upper()=='W'):
                    break  

            elif(self.choice.upper()=='W'):
                break   
                
            else:
                sesja.info='Błędna opcja wyboru'
 



mysql=Db()          # inicjacja bazy dancyh -import ustawień bazy danych / test połączenia
                
sesja=Store()       # wyświetlenie menu GŁÓWNE        
Main()              #uruchomienie głównej klasy pogamu


print('Koniec')
