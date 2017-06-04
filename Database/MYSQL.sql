# Tworzenie bazy projekt1
create database projekt1;

# Przełaczenie aktywnej bazy
use projekt1;

#======================== Tworzenie tabel ========================>

#---------TABELA PRACOWNICKÓW
CREATE TABLE pracownicy (
	id_pracownika INT NOT NULL AUTO_INCREMENT,
	id_sklep VARCHAR(10) NOT NULL,
	pr_imie VARCHAR(45) NOT NULL,
	pr_nazwisko VARCHAR(80) NOT NULL,
	id_roli INT NOT NULL,
	pr_pass VARCHAR(45)NULL,
  PRIMARY KEY (id_pracownika),
  UNIQUE INDEX id_pracownika_UNIQUE (id_pracownika ASC));
  
#---------TABELA SKLEPÓW
  CREATE TABLE sklepy (
	id_sklepy VARCHAR(10) NOT NULL,
	id_region VARCHAR(45) NULL,
	sklep_miasto VARCHAR(50) NOT NULL,
	sklep_adres VARCHAR(100) NOT NULL,
	sklep_telefon INT NULL,
	id_godziny INT NULL,

  PRIMARY KEY (id_sklepy),
  UNIQUE INDEX `id_sklepy_UNIQUE` (id_sklepy ASC));
  
#---------TABELA BAZY KODÓW EAN
  CREATE TABLE bazaean (
	kod_ean bigint NOT NULL,
	kod_index int NOT NULL,
  PRIMARY KEY (kod_ean),
  UNIQUE INDEX kod_ean_UNIQUE (kod_ean ASC));
 
#---------TABELA NAZW TOWARÓW
  CREATE TABLE towary (
	kod_index INT NOT NULL,
	BRANZA VARCHAR(50) NULL,
	GRUPA VARCHAR(100) NOT NULL,
	towar_nazwa VARCHAR(200) NOT NULL,
	towar_priorytet INT NOT NULL,
  PRIMARY KEY (kod_index));
  
#---------TABELA PROMOCJI 
  CREATE TABLE promocje (
	id_promo INT NOT NULL AUTO_INCREMENT,
	kod_index INT NOT NULL,
	promo_nazwa VARCHAR(100) NOT NULL,
	promo_rabat VARCHAR(100) NOT NULL,
	promo_data_od DATE NOT NULL,
	promo_dana_do DATE NOT NULL,
  PRIMARY KEY (id_promo));
  
#---------TABELA ZASOBÓW TOWARÓW W POSZCZEGÓLNYCH SKLEPACH
  CREATE TABLE `zasoby` (
	id_zasoby INT NOT NULL AUTO_INCREMENT,
	id_sklep VARCHAR(100) NOT NULL,
	kod_index INT NOT NULL,
	zasoby_ilosc INT(5) NOT NULL,
	zasoby_cena real NOT NULL,
	id_prmo INT,
  PRIMARY KEY (id_zasoby)
 );

#---------TABELA GODZIN OTWARCIA SKLEPÓW
  CREATE TABLE godziny (
    id_godziny INT AUTO_INCREMENT not null,
    mon VARCHAR(20),
    tue VARCHAR(20),
    wed VARCHAR(20),
    thu VARCHAR(20),
    fri VARCHAR(20),
    sat VARCHAR(20),
	sun VARCHAR(20),
    PRIMARY KEY (id_godziny));
    
#---------TABELA REGIONÓW
  CREATE TABLE regiony (
    id_region INT AUTO_INCREMENT not null,
	id_pracownika int(11),
    region_imie VARCHAR(50),
	region_nazw VARCHAR(50),
    PRIMARY KEY (id_region));
    
#---------TABELA Z ROLAMI UŻYTKOWNIKÓW
  CREATE TABLE role (
    id_roli INT AUTO_INCREMENT not null,
	role_nazwa VARCHAR(50) not null,
    role_upr_1 VARCHAR(50),
    role_upr_2 VARCHAR(50),
    role_upr_3 VARCHAR(50),
    role_upr_4 VARCHAR(50),
    role_upr_5 VARCHAR(50),
    role_upr_6 VARCHAR(50),
    role_upr_7 VARCHAR(50),
    role_upr_8 VARCHAR(50),
    PRIMARY KEY (id_roli))
    DEFAULT CHARACTER SET = utf8
	COLLATE = utf8_polish_ci;

#======================== KONIEC TworzeniA tabel ========================<
  
#======================== WCZYTYWANIE DANCYH DO TABEZ Z PLIKÓW CSV ======>

# Baze EAN kodów ean oraz indeksów towarów
  
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/bazaean.csv' INTO TABLE BAZAEAN;

# Wczytanie bazy sklepów
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/sklepy.csv' INTO TABLE sklepy;

# Wczytanie godzin otwarcia
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/godziny.csv' INTO TABLE godziny ;

# Wczytanie regionów

LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/regiony.csv' INTO TABLE regiony ;

# Wczytanie tabli pracownicy
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/PRACOWNICY.csv' INTO TABLE PRACOWNICY;

# Wczytanie tabli role
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/role.csv' INTO TABLE role;
select * from PRACOWNICY;

# Wczytanie towarów z podzialem na granże

LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/towary_csv/agd.csv' INTO TABLE towary;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/towary_csv/it.csv' INTO TABLE towary;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/towary_csv/rtv.csv' INTO TABLE towary;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/towary_csv/telekom.csv' INTO TABLE towary;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/towary_csv/foto.csv' INTO TABLE towary;

# Wczytanie zaspbóe dla poszczególnych sklepów

LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s315.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s316.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s317.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s318.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s319.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s320.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s321.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s322.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s323.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s324.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s325.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s326.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s327.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s328.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s329.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s330.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s331.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s332.csv' INTO TABLE zasoby ;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/zasoby/zas_s333.csv' INTO TABLE zasoby ;

# Wczytanie promocji

LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/Kurs/Projekty/Projekt 1/csv/promocje.csv' INTO TABLE promocje ;

#======================== KONIEC WCZYTYWANIE DANCYH DO TABEZ Z PLIKÓW CSV ======<

# Tworzenie widoku podstawowych dancyh dla sklpu S315

create view zasoby_S315 as select id_sklep,kod_index,towar_nazwa,zasoby_ilosc,zasoby_cena from zasoby natural join towary where id_sklep='s315';

# Tworzenie widoku zestawiającego regionalnych ze sklepami
create view reg_sklep as select id_region,region_imie,region_nazw,id_sklepy,sklep_miasto from regiony natural join sklepy;

