
#!/usr/bin/env python
# coding: utf-8

import sqlite3
from math import sqrt
from tabulate import tabulate
import matplotlib.pyplot as plt

conn = sqlite3.connect('frequency_dict.db')
cursor = conn.cursor()

#cursor.execute('drop table іменник_середня_частота_2')
#conn.commit()

def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS іменник_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS іменник_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS дієслово_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS дієслово_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прикметник_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                   квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прикметник_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS сполучник_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS сполучник_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS займенниковий_іменник_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS займенниковий_іменник_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прийменник_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прийменник_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS частка_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS частка_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прислівник_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прислівник_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS вигук_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS вигук_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS компаратив_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS компаратив_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS дієприслівник_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS дієприслівник_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS предикатив_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS предикатив_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS числівник_середня_частота
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS числівник_статистичні_дані
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS іменник_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS іменник_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS дієслово_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS дієслово_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прикметник_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                   квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прикметник_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS сполучник_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS сполучник_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS займенниковий_іменник_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS займенниковий_іменник_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прийменник_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прийменник_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS частка_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS частка_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прислівник_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS прислівник_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS вигук_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS вигук_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS компаратив_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS компаратив_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS дієприслівник_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS дієприслівник_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS предикатив_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS предикатив_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS числівник_середня_частота_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_сер INTEGER,
                    різниця_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_сер INTEGER,
                    квадрат_різниці_xi_та_x_серni INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS числівник_статистичні_дані_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    серед_квадратич_відхил REAL,
                    міра_колив_серед_част REAL,
                    x_сер_плюс_мінус_сигма TEXT,
                    x_сер_плюс_мінус_2_сигма TEXT,
                    x_сер_плюс_мінус_3_сигма TEXT,
                    інтервал_міри_колив_сигма TEXT,
                    інтервал_міри_колив_2_сигма TEXT,
                    інтервал_міри_колив_3_сигма TEXT)
    ''')
    conn.commit()
create_tables()


#СТВОРЮЄМО ВАРІАЦІЙНИЙ РЯД ДЛЯ ІМЕННИКА
cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'NOUN'""")
rows = cursor.fetchall()
aver_freq_noun = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_noun:
            aver_freq_noun[i][1] += 1
            xini = aver_freq_noun[i][0]*aver_freq_noun[i][1]
            aver_freq_noun[i][2] = xini
        else:
            aver_freq_noun[i] = [i]
            aver_freq_noun[i].append(1)
            xini = aver_freq_noun[i][0]*aver_freq_noun[i][1]
            aver_freq_noun[i].append(xini)
#for key, value in aver_freq_noun.items():
#    print(f"{key}: {value}")

aver_freq_noun = list(aver_freq_noun.values())
aver_freq_noun_ordered = []
for i in aver_freq_noun:
    aver_freq_noun_ordered.append(i)
#print(aver_freq_noun_ordered)
for i in aver_freq_noun_ordered:
    count = 0
    while count in range(0, len(aver_freq_noun_ordered)-1):
        if aver_freq_noun_ordered[count][0] > aver_freq_noun_ordered[count+1][0]:
          aver_freq_noun_ordered[count], aver_freq_noun_ordered[count+1] = aver_freq_noun_ordered[count+1], aver_freq_noun_ordered[count]
        count += 1
#print(aver_freq_noun_ordered)
count=0
while count in range (0, len(aver_freq_noun_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_noun_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = sum(xini)/sum(ni_2)
    aver_freq_noun_ordered[count].append(x_aver)
    aver_freq_noun_ordered[count].append(round(aver_freq_noun_ordered[count][0]-x_aver, 2))
    aver_freq_noun_ordered[count].append(round((aver_freq_noun_ordered[count][0]-x_aver)**2, 2))
    aver_freq_noun_ordered[count].append(round((aver_freq_noun_ordered[count][0]-x_aver)**2*aver_freq_noun_ordered[count][1], 2))
    count += 1
#print(aver_freq_numr_ordered)

#for i in aver_freq_x_ordered:
#    cursor.execute("""INSERT INTO іменник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()
#print(aver_freq_noun_ordered)

# ДОДАЄМО ДО ТАБЛИЦІ ЗНАЧЕННЯ Х СЕРЕДНЬОГО, ТА ЗНАЧЕННЯ, НЕОБХІДНІ ДЛЯ ПОДАЛЬШИХ РОЗРАХУНКІВ
cursor.execute("select * from іменник_середня_частота")
rows = cursor.fetchall()
xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO іменник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('СТАТИСТИЧНІ ДАНІ ДЛЯ ІМЕННИКА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))


x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum
ni_in_interval_sigma = []
for i in aver_freq_noun_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum
ni_in_interval_2_sigma = []
for i in aver_freq_noun_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum
ni_in_interval_3_sigma = []
for i in aver_freq_noun_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))
#rows = cursor.fetchall()
#for row in rows:
#    print(row)








cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'NOUN'""")
rows = cursor.fetchall()
aver_freq_noun = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_noun:
            aver_freq_noun[i][1] += 1
            xini = aver_freq_noun[i][0]*aver_freq_noun[i][1]
            aver_freq_noun[i][2] = xini
        else:
            aver_freq_noun[i] = [i]
            aver_freq_noun[i].append(1)
            xini = aver_freq_noun[i][0]*aver_freq_noun[i][1]
            aver_freq_noun[i].append(xini)
#for key, value in aver_freq_noun.items():
#    print(f"{key}: {value}")

aver_freq_noun = list(aver_freq_noun.values())
aver_freq_noun_ordered = []
for i in aver_freq_noun:
    aver_freq_noun_ordered.append(i)
#print(aver_freq_noun_ordered)
for i in aver_freq_noun_ordered:
    count = 0
    while count in range(0, len(aver_freq_noun_ordered)-1):
        if aver_freq_noun_ordered[count][0] > aver_freq_noun_ordered[count+1][0]:
          aver_freq_noun_ordered[count], aver_freq_noun_ordered[count+1] = aver_freq_noun_ordered[count+1], aver_freq_noun_ordered[count]
        count += 1
#print(aver_freq_noun_ordered)
count=0
while count in range (0, len(aver_freq_noun_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_noun_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = sum(xini)/sum(ni_2)
    aver_freq_noun_ordered[count].append(x_aver)
    aver_freq_noun_ordered[count].append(round(aver_freq_noun_ordered[count][0]-x_aver, 2))
    aver_freq_noun_ordered[count].append(round((aver_freq_noun_ordered[count][0]-x_aver)**2, 2))
    aver_freq_noun_ordered[count].append(round((aver_freq_noun_ordered[count][0]-x_aver)**2*aver_freq_noun_ordered[count][1], 2))
    count += 1
#print(aver_freq_noun_ordered)

#for i in aver_freq_noun_ordered:
#    cursor.execute("""INSERT INTO іменник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from іменник_середня_частота_2")
rows = cursor.fetchall()
xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO іменник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('СТАТИСТИЧНІ ДАНІ ДЛЯ ІМЕННИКА, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))


x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum2
ni_in_interval_sigma = []
for i in aver_freq_noun_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum2
ni_in_interval_2_sigma = []
for i in aver_freq_noun_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum2
ni_in_interval_3_sigma = []
for i in aver_freq_noun_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))
#СТВОРЮЄМО ПОЛІГОН ЧАСТОТ ІМЕННИКА
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот іменника')
plt.legend()
plt.show()










cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'VERB'""")
rows = cursor.fetchall()
aver_freq_verb = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_verb:
            aver_freq_verb[i][1] += 1
            xini = aver_freq_verb[i][0]*aver_freq_verb[i][1]
            aver_freq_verb[i][2] = xini
        else:
            aver_freq_verb[i] = [i]
            aver_freq_verb[i].append(1)
            xini = aver_freq_verb[i][0]*aver_freq_verb[i][1]
            aver_freq_verb[i].append(xini)
#for key, value in aver_freq_verb.items():
#    print(f"{key}: {value}")

aver_freq_verb = list(aver_freq_verb.values())
aver_freq_verb_ordered = []
for i in aver_freq_verb:
    aver_freq_verb_ordered.append(i)
for i in aver_freq_verb_ordered:
    count = 0
    while count in range(0, len(aver_freq_verb_ordered)-1):
        if aver_freq_verb_ordered[count][0] > aver_freq_verb_ordered[count+1][0]:
          aver_freq_verb_ordered[count], aver_freq_verb_ordered[count+1] = aver_freq_verb_ordered[count+1], aver_freq_verb_ordered[count]
        count += 1
#print(aver_freq_verb_ordered)

count=0
while count in range (0, len(aver_freq_verb_ordered)):
    xini= []
    ni = []
    for i in aver_freq_verb_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = sum(xini)/sum(ni)
    aver_freq_verb_ordered[count].append(x_aver)
    aver_freq_verb_ordered[count].append(round(aver_freq_verb_ordered[count][0]-x_aver, 2))
    aver_freq_verb_ordered[count].append(round((aver_freq_verb_ordered[count][0]-x_aver)**2, 2))
    aver_freq_verb_ordered[count].append(round((aver_freq_verb_ordered[count][0]-x_aver)**2*aver_freq_verb_ordered[count][1], 2))
    count += 1
#print(aver_freq_numr_ordered)

#for i in aver_freq_verb_ordered:
#    cursor.execute("""INSERT INTO дієслово_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()
#print(aver_freq_noun_ordered)

cursor.execute("select * from дієслово_середня_частота")
rows = cursor.fetchall()
xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO дієслово_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄСЛОВА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))
#cursor.execute('drop table іменник_статистичні_дані')

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_v
ni_in_interval_sigma = []
for i in aver_freq_verb_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_v = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_v*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_v
ni_in_interval_2_sigma = []
for i in aver_freq_verb_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_v = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_v*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_v
ni_in_interval_3_sigma = []
for i in aver_freq_verb_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_v = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_v*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))













cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'VERB'""")
rows = cursor.fetchall()
aver_freq_verb = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_verb:
            aver_freq_verb[i][1] += 1
            xini = aver_freq_verb[i][0]*aver_freq_verb[i][1]
            aver_freq_verb[i][2] = xini
        else:
            aver_freq_verb[i] = [i]
            aver_freq_verb[i].append(1)
            xini = aver_freq_verb[i][0]*aver_freq_verb[i][1]
            aver_freq_verb[i].append(xini)
#for key, value in aver_freq_verb.items():
#    print(f"{key}: {value}")

aver_freq_verb = list(aver_freq_verb.values())
aver_freq_verb_ordered = []
for i in aver_freq_verb:
    aver_freq_verb_ordered.append(i)
for i in aver_freq_verb_ordered:
    count = 0
    while count in range(0, len(aver_freq_verb_ordered)-1):
        if aver_freq_verb_ordered[count][0] > aver_freq_verb_ordered[count+1][0]:
          aver_freq_verb_ordered[count], aver_freq_verb_ordered[count+1] = aver_freq_verb_ordered[count+1], aver_freq_verb_ordered[count]
        count += 1
#print(aver_freq_verb_ordered)

count=0
while count in range (0, len(aver_freq_verb_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_verb_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = round(sum(xini)/sum(ni_2))
    aver_freq_verb_ordered[count].append(x_aver)
    aver_freq_verb_ordered[count].append(round(aver_freq_verb_ordered[count][0]-x_aver, 2))
    aver_freq_verb_ordered[count].append(round((aver_freq_verb_ordered[count][0]-x_aver)**2, 2))
    aver_freq_verb_ordered[count].append(round((aver_freq_verb_ordered[count][0]-x_aver)**2*aver_freq_verb_ordered[count][1], 2))
    count += 1
#print(aver_freq_verb_ordered)

#for i in aver_freq_verb_ordered:
#    cursor.execute("""INSERT INTO дієслово_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from дієслово_середня_частота_2")
rows = cursor.fetchall()
xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO дієслово_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄСЛОВА, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))
#cursor.execute('drop table іменник_статистичні_дані')

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_v2
ni_in_interval_sigma = []
for i in aver_freq_verb_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_v2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_v2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_v2
ni_in_interval_2_sigma = []
for i in aver_freq_verb_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_v2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_v2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_v2
ni_in_interval_3_sigma = []
for i in aver_freq_verb_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_v2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_v2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))
#print(xi)
#print(ni)
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот дієслова')
plt.legend()
plt.show()










cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'ADJF'""")
rows = cursor.fetchall()
aver_freq_adjf = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_adjf:
            aver_freq_adjf[i][1] += 1
            xini = aver_freq_adjf[i][0]*aver_freq_adjf[i][1]
            aver_freq_adjf[i][2] = xini
        else:
            aver_freq_adjf[i] = [i]
            aver_freq_adjf[i].append(1)
            xini = aver_freq_adjf[i][0]*aver_freq_adjf[i][1]
            aver_freq_adjf[i].append(xini)
#for key, value in aver_freq_adjf.items():
#    print(f"{key}: {value}")

aver_freq_adjf = list(aver_freq_adjf.values())
aver_freq_adjf_ordered = []
for i in aver_freq_adjf:
    aver_freq_adjf_ordered.append(i)
for i in aver_freq_adjf_ordered:
    count = 0
    while count in range(0, len(aver_freq_adjf_ordered)-1):
        if aver_freq_adjf_ordered[count][0] > aver_freq_adjf_ordered[count+1][0]:
          aver_freq_adjf_ordered[count], aver_freq_adjf_ordered[count+1] = aver_freq_adjf_ordered[count+1], aver_freq_adjf_ordered[count]
        count += 1
#print(aver_freq_adjf_ordered)

count=0
while count in range (0, len(aver_freq_adjf_ordered)):
    xini= []
    ni = []
    for i in aver_freq_adjf_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = round(sum(xini)/sum(ni))
    aver_freq_adjf_ordered[count].append(x_aver)
    aver_freq_adjf_ordered[count].append(round(aver_freq_adjf_ordered[count][0]-x_aver, 2))
    aver_freq_adjf_ordered[count].append(round((aver_freq_adjf_ordered[count][0]-x_aver)**2, 2))
    aver_freq_adjf_ordered[count].append(round((aver_freq_adjf_ordered[count][0]-x_aver)**2*aver_freq_adjf_ordered[count][1], 2))
    count += 1

#for i in aver_freq_adjf_ordered:
#    cursor.execute("""INSERT INTO прикметник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()
#print(aver_freq_adjf_ordered)

cursor.execute("select * from прикметник_середня_частота")
rows = cursor.fetchall()
xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO прикметник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИКМЕТНИКА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_ad
ni_in_interval_sigma = []
for i in aver_freq_adjf_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_ad = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_ad*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_ad
ni_in_interval_2_sigma = []
for i in aver_freq_adjf_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_ad = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_ad*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_ad
ni_in_interval_3_sigma = []
for i in aver_freq_adjf_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_ad = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_ad*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота прикметника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота прикметника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота прикметника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))











cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'ADJF'""")
rows = cursor.fetchall()
aver_freq_adjf = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_adjf:
            aver_freq_adjf[i][1] += 1
            xini = aver_freq_adjf[i][0]*aver_freq_adjf[i][1]
            aver_freq_adjf[i][2] = xini
        else:
            aver_freq_adjf[i] = [i]
            aver_freq_adjf[i].append(1)
            xini = aver_freq_adjf[i][0]*aver_freq_adjf[i][1]
            aver_freq_adjf[i].append(xini)
#for key, value in aver_freq_adjf.items():
#    print(f"{key}: {value}")

aver_freq_adjf = list(aver_freq_adjf.values())
aver_freq_adjf_ordered = []
for i in aver_freq_adjf:
    aver_freq_adjf_ordered.append(i)
for i in aver_freq_adjf_ordered:
    count = 0
    while count in range(0, len(aver_freq_adjf_ordered)-1):
        if aver_freq_adjf_ordered[count][0] > aver_freq_adjf_ordered[count+1][0]:
          aver_freq_adjf_ordered[count], aver_freq_adjf_ordered[count+1] = aver_freq_adjf_ordered[count+1], aver_freq_adjf_ordered[count]
        count += 1


count=0
while count in range (0, len(aver_freq_adjf_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_adjf_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = round(sum(xini)/sum(ni_2))
    aver_freq_adjf_ordered[count].append(x_aver)
    aver_freq_adjf_ordered[count].append(round(aver_freq_adjf_ordered[count][0]-x_aver, 2))
    aver_freq_adjf_ordered[count].append(round((aver_freq_adjf_ordered[count][0]-x_aver)**2, 2))
    aver_freq_adjf_ordered[count].append(round((aver_freq_adjf_ordered[count][0]-x_aver)**2*aver_freq_adjf_ordered[count][1], 2))
    count += 1
#print(aver_freq_adjf_ordered)
#for i in aver_freq_adjf_ordered:
#    cursor.execute("""INSERT INTO прикметник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()

cursor.execute("select * from прикметник_середня_частота_2")
rows = cursor.fetchall()
xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO прикметник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИКМЕТНИКА, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_ad2
ni_in_interval_sigma = []
for i in aver_freq_adjf_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_ad2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_ad2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_ad2
ni_in_interval_2_sigma = []
for i in aver_freq_adjf_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_ad2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_ad2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_ad2
ni_in_interval_3_sigma = []
for i in aver_freq_adjf_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_ad2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_ad2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота прикметника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота прикметника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота прикметника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))


plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот прикметника')
plt.legend()
plt.show()








cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'CONJ'""")
rows = cursor.fetchall()
aver_freq_conj = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_conj:
            aver_freq_conj[i][1] += 1
            xini = aver_freq_conj[i][0]*aver_freq_conj[i][1]
            aver_freq_conj[i][2] = xini
        else:
            aver_freq_conj[i] = [i]
            aver_freq_conj[i].append(1)
            xini = aver_freq_conj[i][0]*aver_freq_conj[i][1]
            aver_freq_conj[i].append(xini)
#for key, value in aver_freq_conj.items():
#    print(f"{key}: {value}")

aver_freq_conj = list(aver_freq_conj.values())
aver_freq_conj_ordered = []
for i in aver_freq_conj:
    aver_freq_conj_ordered.append(i)
for i in aver_freq_conj_ordered:
    count = 0
    while count in range(0, len(aver_freq_conj_ordered)-1):
        if aver_freq_conj_ordered[count][0] > aver_freq_conj_ordered[count+1][0]:
          aver_freq_conj_ordered[count], aver_freq_conj_ordered[count+1] = aver_freq_conj_ordered[count+1], aver_freq_conj_ordered[count]
        count += 1
#print(aver_freq_conj_ordered)

count=0
while count in range (0, len(aver_freq_conj_ordered)):
    xini= []
    ni = []
    for i in aver_freq_conj_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = round(sum(xini)/sum(ni))
    aver_freq_conj_ordered[count].append(x_aver)
    aver_freq_conj_ordered[count].append(round(aver_freq_conj_ordered[count][0]-x_aver, 2))
    aver_freq_conj_ordered[count].append(round((aver_freq_conj_ordered[count][0]-x_aver)**2, 2))
    aver_freq_conj_ordered[count].append(round((aver_freq_conj_ordered[count][0]-x_aver)**2*aver_freq_conj_ordered[count][1], 2))
    count += 1

#for i in aver_freq_conj_ordered:
#    cursor.execute("""INSERT INTO сполучник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()
#print(aver_freq_conj_ordered)

cursor.execute("select * from сполучник_середня_частота")
rows = cursor.fetchall()

xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO сполучник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ СПОЛУЧНИКА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_con
ni_in_interval_sigma = []
for i in aver_freq_conj_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_con = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_con*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_con
ni_in_interval_2_sigma = []
for i in aver_freq_conj_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_con = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_con*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_con
ni_in_interval_3_sigma = []
for i in aver_freq_conj_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_con = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_con*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота сполучника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота сполучника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота сполучника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))











cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'CONJ'""")
rows = cursor.fetchall()
aver_freq_conj = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_conj:
            aver_freq_conj[i][1] += 1
            xini = aver_freq_conj[i][0]*aver_freq_conj[i][1]
            aver_freq_conj[i][2] = xini
        else:
            aver_freq_conj[i] = [i]
            aver_freq_conj[i].append(1)
            xini = aver_freq_conj[i][0]*aver_freq_conj[i][1]
            aver_freq_conj[i].append(xini)
#for key, value in aver_freq_conj.items():
#    print(f"{key}: {value}")

aver_freq_conj = list(aver_freq_conj.values())
aver_freq_conj_ordered = []
for i in aver_freq_conj:
    aver_freq_conj_ordered.append(i)
for i in aver_freq_conj_ordered:
    count = 0
    while count in range(0, len(aver_freq_conj_ordered)-1):
        if aver_freq_conj_ordered[count][0] > aver_freq_conj_ordered[count+1][0]:
          aver_freq_conj_ordered[count], aver_freq_conj_ordered[count+1] = aver_freq_conj_ordered[count+1], aver_freq_conj_ordered[count]
        count += 1
#print(aver_freq_conj_ordered)

count=0
while count in range (0, len(aver_freq_conj_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_conj_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = round(sum(xini)/sum(ni_2))
    aver_freq_conj_ordered[count].append(x_aver)
    aver_freq_conj_ordered[count].append(round(aver_freq_conj_ordered[count][0]-x_aver, 2))
    aver_freq_conj_ordered[count].append(round((aver_freq_conj_ordered[count][0]-x_aver)**2, 2))
    aver_freq_conj_ordered[count].append(round((aver_freq_conj_ordered[count][0]-x_aver)**2*aver_freq_conj_ordered[count][1], 2))
    count += 1
#print(aver_freq_conj_ordered)
#for i in aver_freq_conj_ordered:
#    cursor.execute("""INSERT INTO сполучник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from сполучник_середня_частота_2")
rows = cursor.fetchall()

xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO сполучник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ СПОЛУЧНИКА, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_con2
ni_in_interval_sigma = []
for i in aver_freq_conj_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_con2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_con2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_con2
ni_in_interval_2_sigma = []
for i in aver_freq_conj_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_con2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_con2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_con2
ni_in_interval_3_sigma = []
for i in aver_freq_conj_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_con2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_con2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота сполучника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота сполучника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота сполучника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))


plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот сполучника')
plt.legend()
plt.show()












cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'NPRO'""")
rows = cursor.fetchall()
aver_freq_npro = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_npro:
            aver_freq_npro[i][1] += 1
            xini = aver_freq_npro[i][0]*aver_freq_npro[i][1]
            aver_freq_npro[i][2] = xini
        else:
            aver_freq_npro[i] = [i]
            aver_freq_npro[i].append(1)
            xini = aver_freq_npro[i][0]*aver_freq_npro[i][1]
            aver_freq_npro[i].append(xini)
#for key, value in aver_freq_npro.items():
#    print(f"{key}: {value}")

aver_freq_npro = list(aver_freq_npro.values())
aver_freq_npro_ordered = []
for i in aver_freq_npro:
    aver_freq_npro_ordered.append(i)
for i in aver_freq_npro_ordered:
    count = 0
    while count in range(0, len(aver_freq_npro_ordered)-1):
        if aver_freq_npro_ordered[count][0] > aver_freq_npro_ordered[count+1][0]:
          aver_freq_npro_ordered[count], aver_freq_npro_ordered[count+1] = aver_freq_npro_ordered[count+1], aver_freq_npro_ordered[count]
        count += 1
#print(aver_freq_npro_ordered)

count=0
while count in range (0, len(aver_freq_npro_ordered)):
    xini= []
    ni = []
    for i in aver_freq_npro_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = round(sum(xini)/sum(ni))
    aver_freq_npro_ordered[count].append(x_aver)
    aver_freq_npro_ordered[count].append(round(aver_freq_npro_ordered[count][0]-x_aver, 2))
    aver_freq_npro_ordered[count].append(round((aver_freq_npro_ordered[count][0]-x_aver)**2, 2))
    aver_freq_npro_ordered[count].append(round((aver_freq_npro_ordered[count][0]-x_aver)**2*aver_freq_npro_ordered[count][1], 2))
    count += 1

#for i in aver_freq_npro_ordered:
#    cursor.execute("""INSERT INTO займенниковий_іменник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()
#print(aver_freq_npro_ordered)

cursor.execute("select * from займенниковий_іменник_середня_частота")
rows = cursor.fetchall()

xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO займенниковий_іменник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЗАЙМЕННИКОВОГО ІМЕННИКА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_npro
ni_in_interval_sigma = []
for i in aver_freq_npro_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_npro = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_npro*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_npro
ni_in_interval_2_sigma = []
for i in aver_freq_npro_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_npro = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_npro*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_npro
ni_in_interval_3_sigma = []
for i in aver_freq_npro_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_npro = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_npro*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота займенникового іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота займенникового іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота займенникового іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))









cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'NPRO'""")
rows = cursor.fetchall()
aver_freq_npro = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_npro:
            aver_freq_npro[i][1] += 1
            xini = aver_freq_npro[i][0]*aver_freq_npro[i][1]
            aver_freq_npro[i][2] = xini
        else:
            aver_freq_npro[i] = [i]
            aver_freq_npro[i].append(1)
            xini = aver_freq_npro[i][0]*aver_freq_npro[i][1]
            aver_freq_npro[i].append(xini)
#for key, value in aver_freq_npro.items():
#    print(f"{key}: {value}")

aver_freq_npro = list(aver_freq_npro.values())
aver_freq_npro_ordered = []
for i in aver_freq_npro:
    aver_freq_npro_ordered.append(i)
for i in aver_freq_npro_ordered:
    count = 0
    while count in range(0, len(aver_freq_npro_ordered)-1):
        if aver_freq_npro_ordered[count][0] > aver_freq_npro_ordered[count+1][0]:
          aver_freq_npro_ordered[count], aver_freq_npro_ordered[count+1] = aver_freq_npro_ordered[count+1], aver_freq_npro_ordered[count]
        count += 1
#print(aver_freq_npro_ordered)

count=0
while count in range (0, len(aver_freq_npro_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_npro_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = round(sum(xini)/sum(ni_2))
    aver_freq_npro_ordered[count].append(x_aver)
    aver_freq_npro_ordered[count].append(round(aver_freq_npro_ordered[count][0]-x_aver, 2))
    aver_freq_npro_ordered[count].append(round((aver_freq_npro_ordered[count][0]-x_aver)**2, 2))
    aver_freq_npro_ordered[count].append(round((aver_freq_npro_ordered[count][0]-x_aver)**2*aver_freq_npro_ordered[count][1], 2))
    count += 1
#print(aver_freq_npro_ordered)
#for i in aver_freq_npro_ordered:
#    cursor.execute("""INSERT INTO займенниковий_іменник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from займенниковий_іменник_середня_частота_2")
rows = cursor.fetchall()

xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO займенниковий_іменник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЗАЙМЕННИКОВОГО ІМЕННИКА, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_npro2
ni_in_interval_sigma = []
for i in aver_freq_npro_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_npro2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_npro2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_npro2
ni_in_interval_2_sigma = []
for i in aver_freq_npro_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_npro2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_npro2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_npro2
ni_in_interval_3_sigma = []
for i in aver_freq_npro_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_npro2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_npro2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота займенникового іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота займенникового іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота займенникового іменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))


plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот займенникового іменника')
plt.legend()
plt.show()












cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'PREP'""")
rows = cursor.fetchall()
aver_freq_prep = {}
for row in rows:
     freq = row[2:22]
     for i in freq:
        if i in aver_freq_prep:
            aver_freq_prep[i][1] += 1
            xini = aver_freq_prep[i][0]*aver_freq_prep[i][1]
            aver_freq_prep[i][2] = xini
        else:
            aver_freq_prep[i] = [i]
            aver_freq_prep[i].append(1)
            xini = aver_freq_prep[i][0]*aver_freq_prep[i][1]
            aver_freq_prep[i].append(xini)
#for key, value in aver_freq_prep.items():
#    print(f"{key}: {value}")

aver_freq_prep = list(aver_freq_prep.values())
aver_freq_prep_ordered = []
for i in aver_freq_prep:
    aver_freq_prep_ordered.append(i)
for i in aver_freq_prep_ordered:
    count = 0
    while count in range(0, len(aver_freq_prep_ordered)-1):
        if aver_freq_prep_ordered[count][0] > aver_freq_prep_ordered[count+1][0]:
          aver_freq_prep_ordered[count], aver_freq_prep_ordered[count+1] = aver_freq_prep_ordered[count+1], aver_freq_prep_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_prep_ordered)):
    xini= []
    ni = []
    for i in aver_freq_prep_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = sum(xini)/sum(ni)
    aver_freq_prep_ordered[count].append(x_aver)
    aver_freq_prep_ordered[count].append(round(aver_freq_prep_ordered[count][0]-x_aver, 2))
    aver_freq_prep_ordered[count].append(round((aver_freq_prep_ordered[count][0]-x_aver)**2, 2))
    aver_freq_prep_ordered[count].append(round((aver_freq_prep_ordered[count][0]-x_aver)**2*aver_freq_prep_ordered[count][1], 2))
    count += 1
#print(aver_freq_prep_ordered)
#for i in aver_freq_prep_ordered:
#    cursor.execute("""INSERT INTO прийменник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from прийменник_середня_частота")
rows = cursor.fetchall()

xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO прийменник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИЙМЕННИКА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_prep
ni_in_interval_sigma = []
for i in aver_freq_prep_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_prep = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_prep*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_prep
ni_in_interval_2_sigma = []
for i in aver_freq_prep_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_prep = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_prep*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_prep
ni_in_interval_3_sigma = []
for i in aver_freq_prep_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_prep = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_prep*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота прийменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота прийменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота прийменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))









cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'PREP'""")
rows = cursor.fetchall()
aver_freq_prep = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_prep:
            aver_freq_prep[i][1] += 1
            xini = aver_freq_prep[i][0]*aver_freq_prep[i][1]
            aver_freq_prep[i][2] = xini
        else:
            aver_freq_prep[i] = [i]
            aver_freq_prep[i].append(1)
            xini = aver_freq_prep[i][0]*aver_freq_prep[i][1]
            aver_freq_prep[i].append(xini)
#for key, value in aver_freq_prep.items():
#    print(f"{key}: {value}")

aver_freq_prep = list(aver_freq_prep.values())
aver_freq_prep_ordered = []
for i in aver_freq_prep:
    aver_freq_prep_ordered.append(i)
for i in aver_freq_prep_ordered:
    count = 0
    while count in range(0, len(aver_freq_prep_ordered)-1):
        if aver_freq_prep_ordered[count][0] > aver_freq_prep_ordered[count+1][0]:
          aver_freq_prep_ordered[count], aver_freq_prep_ordered[count+1] = aver_freq_prep_ordered[count+1], aver_freq_prep_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_prep_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_prep_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = sum(xini)/sum(ni_2)
    aver_freq_prep_ordered[count].append(x_aver)
    aver_freq_prep_ordered[count].append(round(aver_freq_prep_ordered[count][0]-x_aver, 2))
    aver_freq_prep_ordered[count].append(round((aver_freq_prep_ordered[count][0]-x_aver)**2, 2))
    aver_freq_prep_ordered[count].append(round((aver_freq_prep_ordered[count][0]-x_aver)**2*aver_freq_prep_ordered[count][1], 2))
    count += 1
#print(aver_freq_prep_ordered)
#for i in aver_freq_prep_ordered:
#    cursor.execute("""INSERT INTO прийменник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from прийменник_середня_частота_2")
rows = cursor.fetchall()

xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO прийменник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИЙМЕННИКА, ВИБІРКА 2' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_prep2
ni_in_interval_sigma = []
for i in aver_freq_prep_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_prep2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_prep2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_prep2
ni_in_interval_2_sigma = []
for i in aver_freq_prep_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_prep2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_prep2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_prep2
ni_in_interval_3_sigma = []
for i in aver_freq_prep_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_prep2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_prep2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота прийменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота прийменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота прийменника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))


plt.plot(xi, ni, label = '1  вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2  вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот прийменника')
plt.legend()
plt.show()








cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'PRCL'""")
rows = cursor.fetchall()
aver_freq_prcl = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_prcl:
            aver_freq_prcl[i][1] += 1
            xini = aver_freq_prcl[i][0]*aver_freq_prcl[i][1]
            aver_freq_prcl[i][2] = xini
        else:
            aver_freq_prcl[i] = [i]
            aver_freq_prcl[i].append(1)
            xini = aver_freq_prcl[i][0]*aver_freq_prcl[i][1]
            aver_freq_prcl[i].append(xini)
#for key, value in aver_freq_prcl.items():
#    print(f"{key}: {value}")

aver_freq_prcl = list(aver_freq_prcl.values())
aver_freq_prcl_ordered = []
for i in aver_freq_prcl:
    aver_freq_prcl_ordered.append(i)
for i in aver_freq_prcl_ordered:
    count = 0
    while count in range(0, len(aver_freq_prcl_ordered)-1):
        if aver_freq_prcl_ordered[count][0] > aver_freq_prcl_ordered[count+1][0]:
          aver_freq_prcl_ordered[count], aver_freq_prcl_ordered[count+1] = aver_freq_prcl_ordered[count+1], aver_freq_prcl_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_prcl_ordered)):
    xini= []
    ni = []
    for i in aver_freq_prcl_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = sum(xini)/sum(ni)
    aver_freq_prcl_ordered[count].append(x_aver)
    aver_freq_prcl_ordered[count].append(round(aver_freq_prcl_ordered[count][0]-x_aver, 2))
    aver_freq_prcl_ordered[count].append(round((aver_freq_prcl_ordered[count][0]-x_aver)**2, 2))
    aver_freq_prcl_ordered[count].append(round((aver_freq_prcl_ordered[count][0]-x_aver)**2*aver_freq_prcl_ordered[count][1], 2))
    count += 1
#print(aver_freq_prcl_ordered)
#for i in aver_freq_prcl_ordered:
#    cursor.execute("""INSERT INTO частка_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from частка_середня_частота")
rows = cursor.fetchall()

xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO частка_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧАСТКИ, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_prcl
ni_in_interval_sigma = []
for i in aver_freq_prcl_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_prcl = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_prcl*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_prcl
ni_in_interval_2_sigma = []
for i in aver_freq_prcl_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_prcl = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_prcl*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_prcl
ni_in_interval_3_sigma = []
for i in aver_freq_prcl_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота частки коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота частки коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота частки коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))












cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'PRCL'""")
rows = cursor.fetchall()
aver_freq_prcl = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_prcl:
            aver_freq_prcl[i][1] += 1
            xini = aver_freq_prcl[i][0]*aver_freq_prcl[i][1]
            aver_freq_prcl[i][2] = xini
        else:
            aver_freq_prcl[i] = [i]
            aver_freq_prcl[i].append(1)
            xini = aver_freq_prcl[i][0]*aver_freq_prcl[i][1]
            aver_freq_prcl[i].append(xini)
#for key, value in aver_freq_prcl.items():
#    print(f"{key}: {value}")

aver_freq_prcl = list(aver_freq_prcl.values())
aver_freq_prcl_ordered = []
for i in aver_freq_prcl:
    aver_freq_prcl_ordered.append(i)
for i in aver_freq_prcl_ordered:
    count = 0
    while count in range(0, len(aver_freq_prcl_ordered)-1):
        if aver_freq_prcl_ordered[count][0] > aver_freq_prcl_ordered[count+1][0]:
          aver_freq_prcl_ordered[count], aver_freq_prcl_ordered[count+1] = aver_freq_prcl_ordered[count+1], aver_freq_prcl_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_prcl_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_prcl_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = sum(xini)/sum(ni_2)
    aver_freq_prcl_ordered[count].append(x_aver)
    aver_freq_prcl_ordered[count].append(round(aver_freq_prcl_ordered[count][0]-x_aver, 2))
    aver_freq_prcl_ordered[count].append(round((aver_freq_prcl_ordered[count][0]-x_aver)**2, 2))
    aver_freq_prcl_ordered[count].append(round((aver_freq_prcl_ordered[count][0]-x_aver)**2*aver_freq_prcl_ordered[count][1], 2))
    count += 1
#print(aver_freq_prcl_ordered)
#for i in aver_freq_prcl_ordered:
#    cursor.execute("""INSERT INTO частка_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from частка_середня_частота_2")
rows = cursor.fetchall()

xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO частка_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧАСТКИ, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_prcl2
ni_in_interval_sigma = []
for i in aver_freq_prcl_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_prcl2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_prcl2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_prcl2
ni_in_interval_2_sigma = []
for i in aver_freq_prcl_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_prcl2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_prcl2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_prcl2
ni_in_interval_3_sigma = []
for i in aver_freq_prcl_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота частки коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота частки коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота частки коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))


plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот частки')
plt.legend()
plt.show()










cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'ADVB'""")
rows = cursor.fetchall()
aver_freq_advb = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_advb:
            aver_freq_advb[i][1] += 1
            xini = aver_freq_advb[i][0]*aver_freq_advb[i][1]
            aver_freq_advb[i][2] = xini
        else:
            aver_freq_advb[i] = [i]
            aver_freq_advb[i].append(1)
            xini = aver_freq_advb[i][0]*aver_freq_advb[i][1]
            aver_freq_advb[i].append(xini)
#for key, value in aver_freq_advb.items():
#    print(f"{key}: {value}")

aver_freq_advb = list(aver_freq_advb.values())
aver_freq_advb_ordered = []
for i in aver_freq_advb:
    aver_freq_advb_ordered.append(i)
for i in aver_freq_advb_ordered:
    count = 0
    while count in range(0, len(aver_freq_advb_ordered)-1):
        if aver_freq_advb_ordered[count][0] > aver_freq_advb_ordered[count+1][0]:
          aver_freq_advb_ordered[count], aver_freq_advb_ordered[count+1] = aver_freq_advb_ordered[count+1], aver_freq_advb_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_advb_ordered)):
    xini= []
    ni = []
    for i in aver_freq_advb_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = sum(xini)/sum(ni)
    aver_freq_advb_ordered[count].append(x_aver)
    aver_freq_advb_ordered[count].append(round(aver_freq_advb_ordered[count][0]-x_aver, 2))
    aver_freq_advb_ordered[count].append(round((aver_freq_advb_ordered[count][0]-x_aver)**2, 2))
    aver_freq_advb_ordered[count].append(round((aver_freq_advb_ordered[count][0]-x_aver)**2*aver_freq_advb_ordered[count][1], 2))
    count += 1
#print(aver_freq_advb_ordered)
#for i in aver_freq_advb_ordered:
#    cursor.execute("""INSERT INTO прислівник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from прислівник_середня_частота")
rows = cursor.fetchall()

xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO прислівник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИСЛІВНИКА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_advb
ni_in_interval_sigma = []
for i in aver_freq_advb_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_advb = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_advb*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_advb
ni_in_interval_2_sigma = []
for i in aver_freq_advb_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_advb = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_advb*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_advb
ni_in_interval_3_sigma = []
for i in aver_freq_advb_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_advb = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_advb*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота прислівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота прислівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота прислівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))














cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'ADVB'""")
rows = cursor.fetchall()
aver_freq_advb = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_advb:
            aver_freq_advb[i][1] += 1
            xini = aver_freq_advb[i][0]*aver_freq_advb[i][1]
            aver_freq_advb[i][2] = xini
        else:
            aver_freq_advb[i] = [i]
            aver_freq_advb[i].append(1)
            xini = aver_freq_advb[i][0]*aver_freq_advb[i][1]
            aver_freq_advb[i].append(xini)
#for key, value in aver_freq_advb.items():
#    print(f"{key}: {value}")

aver_freq_advb = list(aver_freq_advb.values())
aver_freq_advb_ordered = []
for i in aver_freq_advb:
    aver_freq_advb_ordered.append(i)
for i in aver_freq_advb_ordered:
    count = 0
    while count in range(0, len(aver_freq_advb_ordered)-1):
        if aver_freq_advb_ordered[count][0] > aver_freq_advb_ordered[count+1][0]:
          aver_freq_advb_ordered[count], aver_freq_advb_ordered[count+1] = aver_freq_advb_ordered[count+1], aver_freq_advb_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_advb_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_advb_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = sum(xini)/sum(ni_2)
    aver_freq_advb_ordered[count].append(x_aver)
    aver_freq_advb_ordered[count].append(round(aver_freq_advb_ordered[count][0]-x_aver, 2))
    aver_freq_advb_ordered[count].append(round((aver_freq_advb_ordered[count][0]-x_aver)**2, 2))
    aver_freq_advb_ordered[count].append(round((aver_freq_advb_ordered[count][0]-x_aver)**2*aver_freq_advb_ordered[count][1], 2))
    count += 1
#print(aver_freq_advb_ordered)
#for i in aver_freq_advb_ordered:
#    cursor.execute("""INSERT INTO прислівник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from прислівник_середня_частота_2")
rows = cursor.fetchall()

xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO прислівник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИСЛІВНИКА, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_advb2
ni_in_interval_sigma = []
for i in aver_freq_advb_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_advb2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_advb2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_advb2
ni_in_interval_2_sigma = []
for i in aver_freq_advb_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_advb2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_advb2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_advb2
ni_in_interval_3_sigma = []
for i in aver_freq_advb_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_advb2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_advb2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота прислівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота прислівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота прислівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))


plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот прислівника')
plt.legend()
plt.show()











cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'INTJ'""")
rows = cursor.fetchall()
aver_freq_intj = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_intj:
            aver_freq_intj[i][1] += 1
            xini = aver_freq_intj[i][0]*aver_freq_intj[i][1]
            aver_freq_intj[i][2] = xini
        else:
            aver_freq_intj[i] = [i]
            aver_freq_intj[i].append(1)
            xini = aver_freq_intj[i][0]*aver_freq_intj[i][1]
            aver_freq_intj[i].append(xini)
#for key, value in aver_freq_intj.items():
#    print(f"{key}: {value}")

aver_freq_intj = list(aver_freq_intj.values())
aver_freq_intj_ordered = []
for i in aver_freq_intj:
    aver_freq_intj_ordered.append(i)
for i in aver_freq_intj_ordered:
    count = 0
    while count in range(0, len(aver_freq_intj_ordered)-1):
        if aver_freq_intj_ordered[count][0] > aver_freq_intj_ordered[count+1][0]:
          aver_freq_intj_ordered[count], aver_freq_intj_ordered[count+1] = aver_freq_intj_ordered[count+1], aver_freq_intj_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_intj_ordered)):
    xini= []
    ni = []
    for i in aver_freq_intj_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = sum(xini)/sum(ni)
    aver_freq_intj_ordered[count].append(x_aver)
    aver_freq_intj_ordered[count].append(round(aver_freq_intj_ordered[count][0]-x_aver, 2))
    aver_freq_intj_ordered[count].append(round((aver_freq_intj_ordered[count][0]-x_aver)**2, 2))
    aver_freq_intj_ordered[count].append(round((aver_freq_intj_ordered[count][0]-x_aver)**2*aver_freq_intj_ordered[count][1], 2))
    count += 1
#print(aver_freq_intj_ordered)
#for i in aver_freq_intj_ordered:
#    cursor.execute("""INSERT INTO вигук_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from вигук_середня_частота")
rows = cursor.fetchall()

xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO вигук_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ВИГУКА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_intj
ni_in_interval_sigma = []
for i in aver_freq_intj_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_intj = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_intj*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_intj
ni_in_interval_2_sigma = []
for i in aver_freq_intj_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_intj = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_intj*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_intj
ni_in_interval_3_sigma = []
for i in aver_freq_intj_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_intj = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_intj*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота вигука коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота вигука коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота вигука коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))











cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'INTJ'""")
rows = cursor.fetchall()
aver_freq_intj = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_intj:
            aver_freq_intj[i][1] += 1
            xini = aver_freq_intj[i][0]*aver_freq_intj[i][1]
            aver_freq_intj[i][2] = xini
        else:
            aver_freq_intj[i] = [i]
            aver_freq_intj[i].append(1)
            xini = aver_freq_intj[i][0]*aver_freq_intj[i][1]
            aver_freq_intj[i].append(xini)
#for key, value in aver_freq_intj.items():
#    print(f"{key}: {value}")

aver_freq_intj = list(aver_freq_intj.values())
aver_freq_intj_ordered = []
for i in aver_freq_intj:
    aver_freq_intj_ordered.append(i)
for i in aver_freq_intj_ordered:
    count = 0
    while count in range(0, len(aver_freq_intj_ordered)-1):
        if aver_freq_intj_ordered[count][0] > aver_freq_intj_ordered[count+1][0]:
          aver_freq_intj_ordered[count], aver_freq_intj_ordered[count+1] = aver_freq_intj_ordered[count+1], aver_freq_intj_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_intj_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_intj_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = sum(xini)/sum(ni_2)
    aver_freq_intj_ordered[count].append(x_aver)
    aver_freq_intj_ordered[count].append(round(aver_freq_intj_ordered[count][0]-x_aver, 2))
    aver_freq_intj_ordered[count].append(round((aver_freq_intj_ordered[count][0]-x_aver)**2, 2))
    aver_freq_intj_ordered[count].append(round((aver_freq_intj_ordered[count][0]-x_aver)**2*aver_freq_intj_ordered[count][1], 2))
    count += 1
#print(aver_freq_intj_ordered)
#for i in aver_freq_intj_ordered:
#    cursor.execute("""INSERT INTO вигук_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from вигук_середня_частота_2")
rows = cursor.fetchall()

xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO вигук_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ВИГУКА, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_intj2
ni_in_interval_sigma = []
for i in aver_freq_intj_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_intj2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_intj2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_intj2
ni_in_interval_2_sigma = []
for i in aver_freq_intj_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_intj2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_intj2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_intj2
ni_in_interval_3_sigma = []
for i in aver_freq_intj_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_intj2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_intj2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота вигука коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота вигука коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота вигука коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))


plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот вигука')
plt.legend()
plt.show()













cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'COMP'""")
rows = cursor.fetchall()
aver_freq_comp = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_comp:
            aver_freq_comp[i][1] += 1
            xini = aver_freq_comp[i][0]*aver_freq_comp[i][1]
            aver_freq_comp[i][2] = xini
        else:
            aver_freq_comp[i] = [i]
            aver_freq_comp[i].append(1)
            xini = aver_freq_comp[i][0]*aver_freq_comp[i][1]
            aver_freq_comp[i].append(xini)
#for key, value in aver_freq_comp.items():
#    print(f"{key}: {value}")

aver_freq_comp = list(aver_freq_comp.values())
aver_freq_comp_ordered = []
for i in aver_freq_comp:
    aver_freq_comp_ordered.append(i)
for i in aver_freq_comp_ordered:
    count = 0
    while count in range(0, len(aver_freq_comp_ordered)-1):
        if aver_freq_comp_ordered[count][0] > aver_freq_comp_ordered[count+1][0]:
          aver_freq_comp_ordered[count], aver_freq_comp_ordered[count+1] = aver_freq_comp_ordered[count+1], aver_freq_comp_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_comp_ordered)):
    xini= []
    ni = []
    for i in aver_freq_comp_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = sum(xini)/sum(ni)
    aver_freq_comp_ordered[count].append(x_aver)
    aver_freq_comp_ordered[count].append(round(aver_freq_comp_ordered[count][0]-x_aver, 2))
    aver_freq_comp_ordered[count].append(round((aver_freq_comp_ordered[count][0]-x_aver)**2, 2))
    aver_freq_comp_ordered[count].append(round((aver_freq_comp_ordered[count][0]-x_aver)**2*aver_freq_comp_ordered[count][1], 2))
    count += 1
#print(aver_freq_comp_ordered)
#for i in aver_freq_comp_ordered:
#    cursor.execute("""INSERT INTO компаратив_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from компаратив_середня_частота")
rows = cursor.fetchall()

xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO компаратив_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ КОМПАРАТИВУ, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_comp
ni_in_interval_sigma = []
for i in aver_freq_comp_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_comp = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_comp*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_comp
ni_in_interval_2_sigma = []
for i in aver_freq_comp_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_comp = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_comp*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_comp
ni_in_interval_3_sigma = []
for i in aver_freq_comp_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_comp = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_comp*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота компаративу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота компаративу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота компаративу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))













cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'COMP'""")
rows = cursor.fetchall()
aver_freq_comp = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_comp:
            aver_freq_comp[i][1] += 1
            xini = aver_freq_comp[i][0]*aver_freq_comp[i][1]
            aver_freq_comp[i][2] = xini
        else:
            aver_freq_comp[i] = [i]
            aver_freq_comp[i].append(1)
            xini = aver_freq_comp[i][0]*aver_freq_comp[i][1]
            aver_freq_comp[i].append(xini)
#for key, value in aver_freq_comp.items():
#    print(f"{key}: {value}")

aver_freq_comp = list(aver_freq_comp.values())
aver_freq_comp_ordered = []
for i in aver_freq_comp:
    aver_freq_comp_ordered.append(i)
for i in aver_freq_comp_ordered:
    count = 0
    while count in range(0, len(aver_freq_comp_ordered)-1):
        if aver_freq_comp_ordered[count][0] > aver_freq_comp_ordered[count+1][0]:
          aver_freq_comp_ordered[count], aver_freq_comp_ordered[count+1] = aver_freq_comp_ordered[count+1], aver_freq_comp_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_comp_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_comp_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = sum(xini)/sum(ni_2)
    aver_freq_comp_ordered[count].append(x_aver)
    aver_freq_comp_ordered[count].append(round(aver_freq_comp_ordered[count][0]-x_aver, 2))
    aver_freq_comp_ordered[count].append(round((aver_freq_comp_ordered[count][0]-x_aver)**2, 2))
    aver_freq_comp_ordered[count].append(round((aver_freq_comp_ordered[count][0]-x_aver)**2*aver_freq_comp_ordered[count][1], 2))
    count += 1
#print(aver_freq_comp_ordered)
#for i in aver_freq_comp_ordered:
#    cursor.execute("""INSERT INTO компаратив_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from компаратив_середня_частота_2")
rows = cursor.fetchall()

xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO компаратив_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ КОМПАРАТИВУ, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_comp2
ni_in_interval_sigma = []
for i in aver_freq_comp_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_comp2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_comp2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_comp2
ni_in_interval_2_sigma = []
for i in aver_freq_comp_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_comp2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_comp2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_comp2
ni_in_interval_3_sigma = []
for i in aver_freq_comp_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_comp2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_comp2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота компаративу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота компаративу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота компаративу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот компаративу')
plt.legend()
plt.show()












cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'GRND'""")
rows = cursor.fetchall()
aver_freq_grnd = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_grnd:
            aver_freq_grnd[i][1] += 1
            xini = aver_freq_grnd[i][0]*aver_freq_grnd[i][1]
            aver_freq_grnd[i][2] = xini
        else:
            aver_freq_grnd[i] = [i]
            aver_freq_grnd[i].append(1)
            xini = aver_freq_grnd[i][0]*aver_freq_grnd[i][1]
            aver_freq_grnd[i].append(xini)
#for key, value in aver_freq_grnd.items():
#    print(f"{key}: {value}")

aver_freq_grnd = list(aver_freq_grnd.values())
aver_freq_grnd_ordered = []
for i in aver_freq_grnd:
    aver_freq_grnd_ordered.append(i)
for i in aver_freq_grnd_ordered:
    count = 0
    while count in range(0, len(aver_freq_grnd_ordered)-1):
        if aver_freq_grnd_ordered[count][0] > aver_freq_grnd_ordered[count+1][0]:
          aver_freq_grnd_ordered[count], aver_freq_grnd_ordered[count+1] = aver_freq_grnd_ordered[count+1], aver_freq_grnd_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_grnd_ordered)):
    xini= []
    ni = []
    for i in aver_freq_grnd_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = sum(xini)/sum(ni)
    aver_freq_grnd_ordered[count].append(x_aver)
    aver_freq_grnd_ordered[count].append(round(aver_freq_grnd_ordered[count][0]-x_aver, 2))
    aver_freq_grnd_ordered[count].append(round((aver_freq_grnd_ordered[count][0]-x_aver)**2, 2))
    aver_freq_grnd_ordered[count].append(round((aver_freq_grnd_ordered[count][0]-x_aver)**2*aver_freq_grnd_ordered[count][1], 2))
    count += 1
#print(aver_freq_grnd_ordered)
#for i in aver_freq_grnd_ordered:
#    cursor.execute("""INSERT INTO дієприслівник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from дієприслівник_середня_частота")
rows = cursor.fetchall()

xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO дієприслівник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄПРИСЛІВНИКА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_grnd
ni_in_interval_sigma = []
for i in aver_freq_grnd_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_grnd = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_grnd*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_grnd
ni_in_interval_2_sigma = []
for i in aver_freq_grnd_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_grnd = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_grnd*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_grnd
ni_in_interval_3_sigma = []
for i in aver_freq_grnd_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_grnd = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_grnd*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота дієприслівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота дієприслівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота дієприслівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))








cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'GRND'""")
rows = cursor.fetchall()
aver_freq_grnd = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_grnd:
            aver_freq_grnd[i][1] += 1
            xini = aver_freq_grnd[i][0]*aver_freq_grnd[i][1]
            aver_freq_grnd[i][2] = xini
        else:
            aver_freq_grnd[i] = [i]
            aver_freq_grnd[i].append(1)
            xini = aver_freq_grnd[i][0]*aver_freq_grnd[i][1]
            aver_freq_grnd[i].append(xini)
#for key, value in aver_freq_grnd.items():
#    print(f"{key}: {value}")

aver_freq_grnd = list(aver_freq_grnd.values())
aver_freq_grnd_ordered = []
for i in aver_freq_grnd:
    aver_freq_grnd_ordered.append(i)
for i in aver_freq_grnd_ordered:
    count = 0
    while count in range(0, len(aver_freq_grnd_ordered)-1):
        if aver_freq_grnd_ordered[count][0] > aver_freq_grnd_ordered[count+1][0]:
          aver_freq_grnd_ordered[count], aver_freq_grnd_ordered[count+1] = aver_freq_grnd_ordered[count+1], aver_freq_grnd_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_grnd_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_grnd_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = sum(xini)/sum(ni_2)
    aver_freq_grnd_ordered[count].append(x_aver)
    aver_freq_grnd_ordered[count].append(round(aver_freq_grnd_ordered[count][0]-x_aver, 2))
    aver_freq_grnd_ordered[count].append(round((aver_freq_grnd_ordered[count][0]-x_aver)**2, 2))
    aver_freq_grnd_ordered[count].append(round((aver_freq_grnd_ordered[count][0]-x_aver)**2*aver_freq_grnd_ordered[count][1], 2))
    count += 1
#print(aver_freq_grnd_ordered)
#for i in aver_freq_grnd_ordered:
#    cursor.execute("""INSERT INTO дієприслівник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from дієприслівник_середня_частота_2")
rows = cursor.fetchall()

xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO дієприслівник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄПРИСЛІВНИКА, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_grnd2
ni_in_interval_sigma = []
for i in aver_freq_grnd_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_grnd2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_grnd2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_grnd2
ni_in_interval_2_sigma = []
for i in aver_freq_grnd_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_grnd2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_grnd2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_grnd2
ni_in_interval_3_sigma = []
for i in aver_freq_grnd_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_grnd2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_grnd2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота дієприслівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота дієприслівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота дієприслівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))


plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот дієприслівника')
plt.legend()
plt.show()










cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'PRED'""")
rows = cursor.fetchall()
aver_freq_pred = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_pred:
            aver_freq_pred[i][1] += 1
            xini = aver_freq_pred[i][0]*aver_freq_pred[i][1]
            aver_freq_pred[i][2] = xini
        else:
            aver_freq_pred[i] = [i]
            aver_freq_pred[i].append(1)
            xini = aver_freq_pred[i][0]*aver_freq_pred[i][1]
            aver_freq_pred[i].append(xini)
#for key, value in aver_freq_pred.items():
#    print(f"{key}: {value}")

aver_freq_pred = list(aver_freq_pred.values())
aver_freq_pred_ordered = []
for i in aver_freq_pred:
    aver_freq_pred_ordered.append(i)
for i in aver_freq_pred_ordered:
    count = 0
    while count in range(0, len(aver_freq_pred_ordered)-1):
        if aver_freq_pred_ordered[count][0] > aver_freq_pred_ordered[count+1][0]:
          aver_freq_pred_ordered[count], aver_freq_pred_ordered[count+1] = aver_freq_pred_ordered[count+1], aver_freq_pred_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_pred_ordered)):
    xini= []
    ni = []
    for i in aver_freq_pred_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = sum(xini)/sum(ni)
    aver_freq_pred_ordered[count].append(x_aver)
    aver_freq_pred_ordered[count].append(round(aver_freq_pred_ordered[count][0]-x_aver, 2))
    aver_freq_pred_ordered[count].append(round((aver_freq_pred_ordered[count][0]-x_aver)**2, 2))
    aver_freq_pred_ordered[count].append(round((aver_freq_pred_ordered[count][0]-x_aver)**2*aver_freq_pred_ordered[count][1], 2))
    count += 1
#print(aver_freq_pred_ordered)
#for i in aver_freq_pred_ordered:
#    cursor.execute("""INSERT INTO предикатив_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from предикатив_середня_частота")
rows = cursor.fetchall()

xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO предикатив_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРЕДИКАТИВА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_pred
ni_in_interval_sigma = []
for i in aver_freq_pred_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_pred = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_pred*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_pred
ni_in_interval_2_sigma = []
for i in aver_freq_pred_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_pred = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_pred*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_pred
ni_in_interval_3_sigma = []
for i in aver_freq_pred_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_pred = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_pred*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота предикативу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота предикативу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота предикативу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))










cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'PRED'""")
rows = cursor.fetchall()
aver_freq_pred = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_pred:
            aver_freq_pred[i][1] += 1
            xini = aver_freq_pred[i][0]*aver_freq_pred[i][1]
            aver_freq_pred[i][2] = xini
        else:
            aver_freq_pred[i] = [i]
            aver_freq_pred[i].append(1)
            xini = aver_freq_pred[i][0]*aver_freq_pred[i][1]
            aver_freq_pred[i].append(xini)
#for key, value in aver_freq_pred.items():
#    print(f"{key}: {value}")

aver_freq_pred = list(aver_freq_pred.values())
aver_freq_pred_ordered = []
for i in aver_freq_pred:
    aver_freq_pred_ordered.append(i)
for i in aver_freq_pred_ordered:
    count = 0
    while count in range(0, len(aver_freq_pred_ordered)-1):
        if aver_freq_pred_ordered[count][0] > aver_freq_pred_ordered[count+1][0]:
          aver_freq_pred_ordered[count], aver_freq_pred_ordered[count+1] = aver_freq_pred_ordered[count+1], aver_freq_pred_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_pred_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_pred_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = sum(xini)/sum(ni_2)
    aver_freq_pred_ordered[count].append(x_aver)
    aver_freq_pred_ordered[count].append(round(aver_freq_pred_ordered[count][0]-x_aver, 2))
    aver_freq_pred_ordered[count].append(round((aver_freq_pred_ordered[count][0]-x_aver)**2, 2))
    aver_freq_pred_ordered[count].append(round((aver_freq_pred_ordered[count][0]-x_aver)**2*aver_freq_pred_ordered[count][1], 2))
    count += 1
#print(aver_freq_pred_ordered)
#for i in aver_freq_pred_ordered:
#    cursor.execute("""INSERT INTO предикатив_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from предикатив_середня_частота_2")
rows = cursor.fetchall()

xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO предикатив_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРЕДИКАТИВА, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_pred2
ni_in_interval_sigma = []
for i in aver_freq_pred_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_pred2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_pred2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_pred2
ni_in_interval_2_sigma = []
for i in aver_freq_pred_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_pred2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_pred2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_pred2
ni_in_interval_3_sigma = []
for i in aver_freq_pred_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_pred2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_pred2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота предикативу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота предикативу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота предикативу коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))


plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот предикативу')
plt.legend()
plt.show()











cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'NUMR'""")
rows = cursor.fetchall()
aver_freq_numr = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_numr:
            aver_freq_numr[i][1] += 1
            xini = aver_freq_numr[i][0]*aver_freq_numr[i][1]
            aver_freq_numr[i][2] = xini
        else:
            aver_freq_numr[i] = [i]
            aver_freq_numr[i].append(1)
            xini = aver_freq_numr[i][0]*aver_freq_numr[i][1]
            aver_freq_numr[i].append(xini)
#for key, value in aver_freq_numr.items():
#    print(f"{key}: {value}")

aver_freq_numr = list(aver_freq_numr.values())
aver_freq_numr_ordered = []
for i in aver_freq_numr:
    aver_freq_numr_ordered.append(i)
for i in aver_freq_numr_ordered:
    count = 0
    while count in range(0, len(aver_freq_numr_ordered)-1):
        if aver_freq_numr_ordered[count][0] > aver_freq_numr_ordered[count+1][0]:
          aver_freq_numr_ordered[count], aver_freq_numr_ordered[count+1] = aver_freq_numr_ordered[count+1], aver_freq_numr_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_numr_ordered)):
    xini= []
    ni = []
    for i in aver_freq_numr_ordered:
            xini.append(i[2])
            ni.append(i[1])
    x_aver = sum(xini)/sum(ni)
    aver_freq_numr_ordered[count].append(x_aver)
    aver_freq_numr_ordered[count].append(round(aver_freq_numr_ordered[count][0]-x_aver, 2))
    aver_freq_numr_ordered[count].append(round((aver_freq_numr_ordered[count][0]-x_aver)**2, 2))
    aver_freq_numr_ordered[count].append(round((aver_freq_numr_ordered[count][0]-x_aver)**2*aver_freq_numr_ordered[count][1], 2))
    count += 1
#print(aver_freq_numr_ordered)
#for i in aver_freq_numr_ordered:
#    cursor.execute("""INSERT INTO числівник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from числівник_середня_частота")
rows = cursor.fetchall()

xi = []
for row in rows:
    xi.append(row[1])

ni = []
for row in rows:
    ni.append(row[2])
ni_sum = sum(ni)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO числівник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧИСЛІВНИКА, ВИБІРКА 1' + '\n')
table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_numr
ni_in_interval_sigma = []
for i in aver_freq_numr_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_numr = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_numr*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_numr
ni_in_interval_2_sigma = []
for i in aver_freq_numr_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_numr = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_numr*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_numr
ni_in_interval_3_sigma = []
for i in aver_freq_numr_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_numr = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_numr*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота числівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота числівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота числівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))














cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'NUMR'""")
rows = cursor.fetchall()
aver_freq_numr = {}
for row in rows:
     freq = row[4:24]
     for i in freq:
        if i in aver_freq_numr:
            aver_freq_numr[i][1] += 1
            xini = aver_freq_numr[i][0]*aver_freq_numr[i][1]
            aver_freq_numr[i][2] = xini
        else:
            aver_freq_numr[i] = [i]
            aver_freq_numr[i].append(1)
            xini = aver_freq_numr[i][0]*aver_freq_numr[i][1]
            aver_freq_numr[i].append(xini)
#for key, value in aver_freq_numr.items():
#    print(f"{key}: {value}")

aver_freq_numr = list(aver_freq_numr.values())
aver_freq_numr_ordered = []
for i in aver_freq_numr:
    aver_freq_numr_ordered.append(i)
for i in aver_freq_numr_ordered:
    count = 0
    while count in range(0, len(aver_freq_numr_ordered)-1):
        if aver_freq_numr_ordered[count][0] > aver_freq_numr_ordered[count+1][0]:
          aver_freq_numr_ordered[count], aver_freq_numr_ordered[count+1] = aver_freq_numr_ordered[count+1], aver_freq_numr_ordered[count]
        count += 1
count = 0

while count in range (0, len(aver_freq_numr_ordered)):
    xini= []
    ni_2 = []
    for i in aver_freq_numr_ordered:
            xini.append(i[2])
            ni_2.append(i[1])
    x_aver = sum(xini)/sum(ni_2)
    aver_freq_numr_ordered[count].append(x_aver)
    aver_freq_numr_ordered[count].append(round(aver_freq_numr_ordered[count][0]-x_aver, 2))
    aver_freq_numr_ordered[count].append(round((aver_freq_numr_ordered[count][0]-x_aver)**2, 2))
    aver_freq_numr_ordered[count].append(round((aver_freq_numr_ordered[count][0]-x_aver)**2*aver_freq_numr_ordered[count][1], 2))
    count += 1
#print(aver_freq_numr_ordered)
#for i in aver_freq_numr_ordered:
#    cursor.execute("""INSERT INTO числівник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
#                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from числівник_середня_частота_2")
rows = cursor.fetchall()

xi_2 = []
for row in rows:
    xi_2.append(row[1])

ni_2 = []
for row in rows:
    ni_2.append(row[2])
ni_sum = sum(ni_2)
#print(ni_sum)

xini = []
for row in rows:
    xini.append(row[3])
xini_sum = sum(xini)

x_aver = rows[0][4]

xi_minus_x_aver = []
for row in rows:
    xi_minus_x_aver.append(row[5])

xi_minus_x_aver_squared = []
for row in rows:
    xi_minus_x_aver_squared.append(row[6])

xi_minus_x_aver_squared_ni = []
for row in rows:
    xi_minus_x_aver_squared_ni.append(row[7])

sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)
#print(sigma)

sigma_x_aver = sigma/sqrt(ni_sum)
#print(sigma_x_aver)

interval_sigma = [x_aver-sigma, x_aver+sigma]
interval_2_sigma = [x_aver-2*sigma, x_aver+2*sigma]
interval_3_sigma = [x_aver-3*sigma, x_aver+3*sigma]
#print(interval_sigma)
#print(interval_2_sigma)
#print(interval_3_sigma)

interval_sigma_x_aver = [x_aver-sigma_x_aver, x_aver+sigma_x_aver]
interval_sigma_2_x_aver = [x_aver-2*sigma_x_aver, x_aver+2*sigma_x_aver]
interval_sigma_3_x_aver = [x_aver-3*sigma_x_aver, x_aver+3*sigma_x_aver]

my_list = []
my_list.append(sigma)
my_list.append(sigma_x_aver)
my_list.append(str(interval_sigma))
my_list.append(str(interval_2_sigma))
my_list.append(str(interval_3_sigma))
my_list.append(str(interval_sigma_x_aver))
my_list.append(str(interval_sigma_2_x_aver))
my_list.append(str(interval_sigma_3_x_aver))
#print(my_list)

#cursor.execute(""" INSERT INTO числівник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
#               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
#              інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма)
#               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
#conn.commit()

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧИСЛІВНИКА, ВИБІРКА 2' + '\n')
table = {'xi': xi_2,'ni': ni_2, 'xi*ni': xini, 'x середнє': [x_aver], 'xi - x середнє': xi_minus_x_aver, '(xi - x середнє)^2': xi_minus_x_aver_squared, '(xi - x середнє)^2*ni': xi_minus_x_aver_squared_ni}
print(tabulate(table, headers='keys'))

table = [['серед. квадр. відхил.', 'міра колив. серед. част.', 'інтервал із сігма', 'інтервал із 2*сігма', 'інтервал із 3*сігма', 'інтервал міри колив. із сігма', 'інтервал міри колив. із 2*сігма', 'інтервал міри колив. із 3*сігма'], [sigma, sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, interval_sigma_3_x_aver]]
print('\n')
print(tabulate(table, headers='firstrow'))

x_aver_minus_sigma = round(interval_sigma[0])
x_aver_plus_sigma = round(interval_sigma[1])
#print(x_aver_minus_sigma)
#print(x_aver_plus_sigma)
global ni_in_interval_sigma_sum_numr2
ni_in_interval_sigma = []
for i in aver_freq_numr_ordered:
    if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
        ni_in_interval_sigma.append(i[1])
        ni_in_interval_sigma_sum_numr2 = sum(ni_in_interval_sigma)
percentage = round(ni_in_interval_sigma_sum_numr2*100/ni_sum, 1)

print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((68.3 - percentage)*100/68.3, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_2_sigma = round(interval_2_sigma[0])
x_aver_plus_2_sigma = round(interval_2_sigma[1])
#print(x_aver_minus_2_sigma)
#print(x_aver_plus_2_sigma)
global ni_in_interval_2_sigma_sum_numr2
ni_in_interval_2_sigma = []
for i in aver_freq_numr_ordered:
    if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
        ni_in_interval_2_sigma.append(i[1])
        ni_in_interval_2_sigma_sum_numr2 = sum(ni_in_interval_2_sigma)
percentage = round(ni_in_interval_2_sigma_sum_numr2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((95.5 - percentage)*100/95.5, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_3_sigma = round(interval_3_sigma[0])
x_aver_plus_3_sigma = round(interval_3_sigma[1])
#print(x_aver_minus_3_sigma)
#print(x_aver_plus_3_sigma)
global ni_in_interval_3_sigma_sum_numr2
ni_in_interval_3_sigma = []
for i in aver_freq_numr_ordered:
    if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
        ni_in_interval_3_sigma.append(i[1])
        ni_in_interval_3_sigma_sum_numr2 = sum(ni_in_interval_3_sigma)
percentage = round(ni_in_interval_3_sigma_sum_numr2*100/ni_sum, 1)
print('\n' + 'В інтервалі x сер. ± 3*сігма знаходиться ' + str(percentage) + '% абсолютниих частот')

if round((99.7 - percentage)*100/99.7, 1) < 5:
    print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
else:
    print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота числівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота числівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота числівника коливатиметься в межах '''
      + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))


plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markersize = 4)
plt.plot(xi_2, ni_2, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот числівника')
plt.legend()
plt.show()




cursor.execute("select * from дієслово_статистичні_дані")
rows = cursor.fetchall()
#for row in rows:
#    print(row)


#print("Table dropped")
cursor.close()
