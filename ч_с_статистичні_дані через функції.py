#!/usr/bin/env python
# coding: utf-8

import sqlite3
from math import sqrt
from tabulate import tabulate
import matplotlib.pyplot as plt

conn = sqlite3.connect('frequency_dict.db')
cursor = conn.cursor()

def drop_tables():
    cursor.execute('drop table Стьюдент_хі_квадрат')
    conn.commit()
    cursor.execute('drop table іменник_середня_частота')
    conn.commit()
    cursor.execute('drop table іменник_середня_частота_2')
    conn.commit()
    cursor.execute('drop table іменник_статистичні_дані')
    conn.commit()
    cursor.execute('drop table іменник_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table дієслово_середня_частота')
    conn.commit()
    cursor.execute('drop table дієслово_статистичні_дані')
    conn.commit()
    cursor.execute('drop table дієслово_середня_частота_2')
    conn.commit()
    cursor.execute('drop table дієслово_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table прикметник_середня_частота')
    conn.commit()
    cursor.execute('drop table прикметник_статистичні_дані')
    conn.commit()
    cursor.execute('drop table прикметник_середня_частота_2')
    conn.commit()
    cursor.execute('drop table прикметник_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table прислівник_середня_частота')
    conn.commit()
    cursor.execute('drop table прислівник_статистичні_дані')
    conn.commit()
    cursor.execute('drop table прислівник_середня_частота_2')
    conn.commit()
    cursor.execute('drop table прислівник_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table компаратив_середня_частота')
    conn.commit()
    cursor.execute('drop table компаратив_статистичні_дані')
    conn.commit()
    cursor.execute('drop table компаратив_середня_частота_2')
    conn.commit()
    cursor.execute('drop table компаратив_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table дієприслівник_середня_частота')
    conn.commit()
    cursor.execute('drop table дієприслівник_статистичні_дані')
    conn.commit()
    cursor.execute('drop table дієприслівник_середня_частота_2')
    conn.commit()
    cursor.execute('drop table дієприслівник_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table прийменник_середня_частота')
    conn.commit()
    cursor.execute('drop table прийменник_статистичні_дані')
    conn.commit()
    cursor.execute('drop table прийменник_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table прийменник_середня_частота_2')
    conn.commit()
    cursor.execute('drop table частка_середня_частота')
    conn.commit()
    cursor.execute('drop table частка_статистичні_дані')
    conn.commit()
    cursor.execute('drop table частка_середня_частота_2')
    conn.commit()
    cursor.execute('drop table частка_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table вигук_середня_частота')
    conn.commit()
    cursor.execute('drop table вигук_статистичні_дані')
    conn.commit()
    cursor.execute('drop table вигук_середня_частота_2')
    conn.commit()
    cursor.execute('drop table вигук_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table числівник_середня_частота')
    conn.commit()
    cursor.execute('drop table числівник_статистичні_дані')
    conn.commit()
    cursor.execute('drop table числівник_середня_частота_2')
    conn.commit()
    cursor.execute('drop table числівник_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table займенниковий_іменник_середня_частота')
    conn.commit()
    cursor.execute('drop table займенниковий_іменник_статистичні_дані')
    conn.commit()
    cursor.execute('drop table займенниковий_іменник_середня_частота_2')
    conn.commit()
    cursor.execute('drop table займенниковий_іменник_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table сполучник_середня_частота')
    conn.commit()
    cursor.execute('drop table сполучник_статистичні_дані')
    conn.commit()
    cursor.execute('drop table сполучник_середня_частота_2')
    conn.commit()
    cursor.execute('drop table сполучник_статистичні_дані_2')
    conn.commit()
    cursor.execute('drop table предикатив_середня_частота')
    conn.commit()
    cursor.execute('drop table предикатив_статистичні_дані')
    conn.commit()
    cursor.execute('drop table предикатив_середня_частота_2')
    conn.commit()
    cursor.execute('drop table предикатив_статистичні_дані_2')
    conn.commit()
drop_tables()

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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
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
                    інтервал_міри_колив_3_сигма TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()
create_tables()

cursor.execute('''CREATE TABLE IF NOT EXISTS Стьюдент_хі_квадрат
                    (id INTEGER PRIMARY KEY NOT NULL,
                    part_of_sp TEXT,
                    student REAL,
                    xi_squared REAL
                    )
''')
conn.commit()

def count_aver_freq():
        global aver_freq_x
        global aver_freq_x_ordered
        global freq
        global part_of_sp
        aver_freq_x = {}
        #print(aver_freq_x)
        rows = cursor.fetchall()
        for row in rows:
             freq = row[4:24]
             part_of_sp = row[0]
             for i in freq:
                if i in aver_freq_x:
                    aver_freq_x[i][1] += 1
                    xini0 = aver_freq_x[i][0]*aver_freq_x[i][1]
                    aver_freq_x[i][2] = xini0
                else:
                    aver_freq_x[i] = [i]
                    aver_freq_x[i].append(1)
                    xini0 = aver_freq_x[i][0]*aver_freq_x[i][1]
                    aver_freq_x[i].append(xini0)
        #for key, value in aver_freq_noun.items():
        #    print(f"{key}: {value}")
        aver_freq_x = list(aver_freq_x.values())
        #print(aver_freq_x)

        aver_freq_x_ordered = sorted(aver_freq_x, key=lambda x:x[0])
        #print(aver_freq_x_ordered)

        count=0
        while count in range (0, len(aver_freq_x_ordered)):
            xini0= []
            ni0 = []
            for i in aver_freq_x_ordered:
                xini0.append(i[2])
                ni0.append(i[1])
            x_aver0 = sum(xini0)/sum(ni0)
            aver_freq_x_ordered[count].append(x_aver0)
            aver_freq_x_ordered[count].append((aver_freq_x_ordered[count][0]-x_aver0))
            aver_freq_x_ordered[count].append(((aver_freq_x_ordered[count][0]-x_aver0)**2))
            aver_freq_x_ordered[count].append(((aver_freq_x_ordered[count][0]-x_aver0)**2*aver_freq_x_ordered[count][1]))
            count += 1
        #print(x_aver0)
        #aver_freq_x_ordered = tuple(aver_freq_x_ordered)
        #print(aver_freq_x_ordered)
        #print(str(x_aver) + '='+ str(sum(xini)) + '/' + str(sum(ni)))

def statistics():
        global xi, ni, xini, ni_sum, x_aver, xi_minus_x_aver, xi_minus_x_aver_squared, xi_minus_x_aver_squared_ni, sigma, \
            sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, \
            interval_sigma_3_x_aver, coef_of_variation, coef_of_variation_max, D, error
        global my_list
        rows = cursor.fetchall()
        xi = []
        for row in rows:
            xi.append(row[1])
        #print(xi)

        ni = []
        for row in rows:
            ni.append(row[2])
        ni_sum = sum(ni)
        #print(ni)
        #print(ni_sum)

        xini = []
        for row in rows:
            xini.append(row[3])
        xini_sum = sum(xini)
        #print(xini_sum)

        x_aver = rows[0][4]
        #print(x_aver)

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
        #print(x_aver)

        sigma_x_aver = sigma/sqrt(ni_sum)
        #print(sigma_x_aver)

        interval_sigma = [round(x_aver-sigma), round(x_aver+sigma)]
        interval_2_sigma = [round(x_aver-2*sigma), round(x_aver+2*sigma)]
        interval_3_sigma = [round(x_aver-3*sigma), round(x_aver+3*sigma)]
        #print(interval_sigma)
        #print(interval_2_sigma)
        #print(interval_3_sigma)

        interval_sigma_x_aver = [round(x_aver-sigma_x_aver), round(x_aver+sigma_x_aver)]
        interval_sigma_2_x_aver = [round(x_aver-2*sigma_x_aver), round(x_aver+2*sigma_x_aver)]
        interval_sigma_3_x_aver = [round(x_aver-3*sigma_x_aver), round(x_aver+3*sigma_x_aver)]

        coef_of_variation = round(sigma/x_aver, 2)
        coef_of_variation_max = sqrt(ni_sum-1)
        D = 1-coef_of_variation/coef_of_variation_max
        error = round((1.96*coef_of_variation)/sqrt(sum(ni)), 2)
        #print(coef_of_variation)
        #print(coef_of_variation_max)
        #print(D)
        #print(error)

        my_list = []
        my_list.append(sigma)
        my_list.append(sigma_x_aver)
        my_list.append(str(interval_sigma))
        my_list.append(str(interval_2_sigma))
        my_list.append(str(interval_3_sigma))
        my_list.append(str(interval_sigma_x_aver))
        my_list.append(str(interval_sigma_2_x_aver))
        my_list.append(str(interval_sigma_3_x_aver))
        my_list.append(coef_of_variation)
        my_list.append(coef_of_variation_max)
        my_list.append(D)
        my_list.append(error)
        #print(my_list)

def print_results():
        table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'х̅': [x_aver], 'xi - х̅': xi_minus_x_aver,
                 '(xi - х̅)^2': xi_minus_x_aver_squared, '(xi - х̅)^2*ni': xi_minus_x_aver_squared_ni}
        print(tabulate(table, headers='keys'))

        table = [['σ', 'σх̅', 'інт. із σ', 'інт. із 2σ',
                  'інт. із 3σ', 'інт. σх̅', 'інт. 2σх̅',
                  'інт. 3σх̅', 'V', 'Vmax', 'D', 'похибка'], [round(sigma), round(sigma_x_aver),
                  interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver,
                  interval_sigma_3_x_aver, coef_of_variation, coef_of_variation_max, D, error]]
        print('\n')
        print(tabulate(table, headers='firstrow'))


        x_aver_minus_sigma = round(interval_sigma[0])
        x_aver_plus_sigma = round(interval_sigma[1])
        #print(x_aver_minus_sigma)
        #print(x_aver_plus_sigma)
        global ni_in_interval_sigma_sum
        ni_in_interval_sigma = []
        for i in aver_freq_x_ordered:
            if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
                ni_in_interval_sigma.append(i[1])
                ni_in_interval_sigma_sum = sum(ni_in_interval_sigma)
        percentage = round(ni_in_interval_sigma_sum*100/ni_sum, 1)

        print('\n' + 'В інтервалі x сер. ± сігма знаходиться ' "(" + str(sum(ni_in_interval_sigma)) + ') -  ' + str(percentage) + '% абсолютниих частот')

        if round((68.3 - percentage)*100/68.3, 1) < 5:
            print('Це вказує на хорошу узгодженіcть теоретично обчисленого й емпіричного результату')
        else:
            print('Це вказує на погану узгодженіcть теоретично обчисленого й емпіричного результату')

        x_aver_minus_2_sigma = round(interval_2_sigma[0])
        x_aver_plus_2_sigma = round(interval_2_sigma[1])
        #print(interval_2_sigma)
        global ni_in_interval_2_sigma_sum
        ni_in_interval_2_sigma = []
        for i in aver_freq_x_ordered:
            if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
                ni_in_interval_2_sigma.append(i[1])
                ni_in_interval_2_sigma_sum = sum(ni_in_interval_2_sigma)
        percentage = round(ni_in_interval_2_sigma_sum*100/ni_sum, 1)
        print('\n' + 'В інтервалі x сер. ± 2*сігма знаходиться ' + "(" + str(sum(ni_in_interval_2_sigma)) + ') -  ' + str(percentage) + '% абсолютниих частот')

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
        for i in aver_freq_x_ordered:
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
        print('\n' + '''З імовірністю 68.3% ми можемо стверджувати, що в даній генеральній сукупності середня частота даної частини мови коливатиметься в межах '''
              + 'від '+ str(x_aver_minus_sigma_x_aver) + ' до ' + str(x_aver_plus_sigma_x_aver))

        x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
        x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
        print('\n' + '''З імовірністю 95.5% ми можемо стверджувати, що в даній генеральній сукупності середня частота даної частини мови коливатиметься в межах '''
              + 'від '+ str(x_aver_minus_2_sigma_x_aver) + ' до ' + str(x_aver_plus_2_sigma_x_aver))

        x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
        x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
        print('\n' + '''З імовірністю 99.7% ми можемо стверджувати, що в даній генеральній сукупності середня частота даної частини мови коливатиметься в межах '''
              + 'від '+ str(x_aver_minus_3_sigma_x_aver) + ' до ' + str(x_aver_plus_3_sigma_x_aver))

def interval_row(K):
    global interval_row_list # список з межами інтервалів і серединами
    global ni_in_intervals   # список з кількостями хі в кожному інтервалі

    R = max(xi) - min(xi)
    #print(R)
    h = R/K
    interval_row_list = []
    ni_in_intervals = []
    xini_intervals = []
    for i in range(0, K):
        interval_row_list.append([min(xi)+i*h, round((min(xi)+i*h)+h, 1), round((min(xi)+i*h)+h/2, 1)])
        ni_for_one_interval = []
        for o in aver_freq_x_ordered:
            if min(xi)+i*h <= o[0] <= (min(xi)+i*h)+h:
                #print(o[1])
                ni_for_one_interval.append(o[1])
            #print(ni_for_interval)
            else:
                continue
        ni_in_intervals.append(ni_for_one_interval)
        xini_intervals.append([round((min(xi)+i*h)+h/2, 1), sum(ni_for_one_interval)])
    ni_interval_sum = []
    xini_intervals_sum = []
    for i in xini_intervals:
        ni_interval_sum.append(i[1])
        xini_intervals_sum.append(i[0]*i[1])
    ni_interval_sum = sum(ni_interval_sum)
    xini_intervals_sum = sum(xini_intervals_sum)
    x_aver_interval = xini_intervals_sum/ni_interval_sum
    #print(x_aver_interval)

def student(x, y, s_1_x, s_2_x):
    global t
    t = abs(x-y)/sqrt(s_1_x+s_2_x)
    print('Критерій Стьюдента: ' + str(t))

def X_squared_count(M1, M2, K):
    global X_squared
    X_squared = []
    for i in range(0, ni_sum):
        X_squared.append(M1[i]**2/(sum(M1)*sum(K[i])))
        X_squared.append(M2[i]**2/(sum(M2)*sum(K[i])))
    N = sum(M1)+sum(M2)
    X_squared = N*((sum(X_squared))-1)
    print('xi квадрат ' + str(X_squared))



#СТВОРЮЄМО ВАРІАЦІЙНИЙ РЯД ДЛЯ ІМЕННИКА
cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'NOUN'""")
count_aver_freq()
#print(aver_freq_x_ordered)
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO іменник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер,
                       квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()
M1 = freq

# ДОДАЄМО ДО ТАБЛИЦІ ЗНАЧЕННЯ Х СЕРЕДНЬОГО, ТА ЗНАЧЕННЯ, НЕОБХІДНІ ДЛЯ ПОДАЛЬШИХ РОЗРАХУНКІВ
cursor.execute("select * from іменник_середня_частота")
statistics()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
#print(my_list)
cursor.execute(""" INSERT INTO іменник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()



print('СТАТИСТИЧНІ ДАНІ ДЛЯ ІМЕННИКА, ВИБІРКА 1' + '\n')
print_results()
#СТВОРЮЄМО ПОЛІГОН ЧАСТОТ ІМЕННИКА
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))
print(xi_interval)
plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)




cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'NOUN'""")
count_aver_freq()

for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO іменник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

# ДОДАЄМО ДО ТАБЛИЦІ ЗНАЧЕННЯ Х СЕРЕДНЬОГО, ТА ЗНАЧЕННЯ, НЕОБХІДНІ ДЛЯ ПОДАЛЬШИХ РОЗРАХУНКІВ
cursor.execute("select * from іменник_середня_частота_2")
statistics()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute(""" INSERT INTO іменник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()



print('СТАТИСТИЧНІ ДАНІ ДЛЯ ІМЕННИКА, ВИБІРКА 2' + '\n')
print_results()

interval_row(11)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот іменника')
plt.legend()
plt.show()


student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp

cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()



cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'VERB'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO дієслово_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from дієслово_середня_частота")
statistics()
cursor.execute(""" INSERT INTO дієслово_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq
print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄСЛОВА, ВИБІРКА 1' + '\n')
print_results()
#СТВОРЮЄМО ПОЛІГОН ЧАСТОТ ДІЄСЛОВА
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(9)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)




cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'VERB'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO дієслово_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from дієслово_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO дієслово_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄСЛОВА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)

plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот дієслова')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()





cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'ADJF'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO прикметник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from прикметник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO прикметник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИКМЕТНИКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)
print(xi_interval)




cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'ADJF'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO прикметник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from прикметник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO прикметник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))
print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИКМЕТНИКА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)

plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот прикметника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()








cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'CONJ'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO сполучник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()
#print(aver_freq_conj_ordered)

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from сполучник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO сполучник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ СПОЛУЧНИКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)
#plt.legend()
#plt.show()




cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'CONJ'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO сполучник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from сполучник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO сполучник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))
print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ СПОЛУЧНИКА, ВИБІРКА 2' + '\n')
print_results()

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)

#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот сполучника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()






cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'NPRO'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO займенниковий_іменник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()
#print(aver_freq_npro_ordered)

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from займенниковий_іменник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO займенниковий_іменник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()
M1 = freq

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЗАЙМЕННИКОВОГО ІМЕННИКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(9)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)





cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'NPRO'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO займенниковий_іменник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from займенниковий_іменник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO займенниковий_іменник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЗАЙМЕННИКОВОГО ІМЕННИКА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)

plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот займенникового іменника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()








cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'PREP'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO прийменник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from прийменник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO прийменник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИЙМЕННИКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)








cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'PREP'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO прийменник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from прийменник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO прийменник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИЙМЕННИКА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2  вибірка', marker = 'o', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)


plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот прийменника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()





cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'PRCL'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO частка_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from частка_середня_частота")
statistics()
cursor.execute(""" INSERT INTO частка_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧАСТКИ, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)






cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'PRCL'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO частка_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from частка_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO частка_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧАСТКИ, ВИБІРКА 2' + '\n')
print_results()

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)

#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот частки')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()







cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'ADVB'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO прислівник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from прислівник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO прислівник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИСЛІВНИКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)




cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'ADVB'""")
count_aver_freq()
#print(aver_freq_x_ordered)
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO прислівник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from прислівник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO прислівник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИСЛІВНИКА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)


plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот прислівника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()






cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'INTJ'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO вигук_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from вигук_середня_частота")
statistics()
cursor.execute(""" INSERT INTO вигук_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ВИГУКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)




cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'INTJ'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO вигук_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from вигук_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO вигук_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ВИГУКА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)


plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот вигука')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()








cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'COMP'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO компаратив_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from компаратив_середня_частота")
statistics()
cursor.execute(""" INSERT INTO компаратив_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ КОМПАРАТИВУ, ВИБІРКА 1' + '\n')
print_results()
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)















cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'GRND'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO дієприслівник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from дієприслівник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO дієприслівник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄПРИСЛІВНИКА, ВИБІРКА 1' + '\n')
print_results()
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)






cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'GRND'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO дієприслівник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from дієприслівник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO дієприслівник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄПРИСЛІВНИКА, ВИБІРКА 2' + '\n')
print_results()
plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот дієприслівника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()







cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'PRED'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO предикатив_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from предикатив_середня_частота")
statistics()
cursor.execute(""" INSERT INTO предикатив_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРЕДИКАТИВА, ВИБІРКА 1' + '\n')
print_results()
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)






cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'PRED'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO предикатив_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from предикатив_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO предикатив_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРЕДИКАТИВА, ВИБІРКА 2' + '\n')
print_results()
plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот предикативу')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()







cursor.execute("""select * from част_частин_мови
                   where частина_мови = 'NUMR'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO числівник_середня_частота (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from числівник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO числівник_статистичні_дані (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
               інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧИСЛІВНИКА, ВИБІРКА 1' + '\n')
print_results()
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)





cursor.execute("""select * from част_частин_мови_2
                   where частина_мови = 'NUMR'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO числівник_середня_частота_2 (xi, ni, xini, x_сер, різниця_xi_та_x_сер, квадрат_різниці_xi_та_x_сер, квадрат_різниці_xi_та_x_серni)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from числівник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO числівник_статистичні_дані_2 (серед_квадратич_відхил, міра_колив_серед_част,
               x_сер_плюс_мінус_сигма, x_сер_плюс_мінус_2_сигма, x_сер_плюс_мінус_3_сигма, інтервал_міри_колив_сигма,
              інтервал_міри_колив_2_сигма, інтервал_міри_колив_3_сигма, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧИСЛІВНИКА, ВИБІРКА 2' + '\n')
print_results()
plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот числівника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Стьюдент_хі_квадрат (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()

conn.close()
