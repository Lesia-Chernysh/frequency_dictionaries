#!/usr/bin/env python
# coding: utf-8

import sqlite3
import re
import pymorphy2


#Створюємо базу даних і таблицю частотності словоформ

conn = sqlite3.connect('frequency_dict.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS част_словоформ
                  (словоформа TEXT PRIMARY KEY NOT NULL,
                  gen_freq INTEGER,
                  підв_1 INTEGER,
                  підв_2 INTEGER,
                  підв_3 INTEGER,
                  підв_4 INTEGER,
                  підв_5 INTEGER,
                  підв_6 INTEGER,
                  підв_7 INTEGER,
                  підв_8 INTEGER,
                  підв_9 INTEGER,
                  підв_10 INTEGER,
                  підв_11 INTEGER,
                  підв_12 INTEGER,
                  підв_13 INTEGER,
                  підв_14 INTEGER,
                  підв_15 INTEGER,
                  підв_16 INTEGER,
                  підв_17 INTEGER,
                  підв_18 INTEGER,
                  підв_19 INTEGER,
                  підв_20 INTEGER)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS част_частин_мови
                  (частина_мови TEXT PRIMARY KEY NOT NULL,
                  gen_freq INTEGER,
                  x_aver INTEGER,
                  relative_freq INTEGER,
                  підв_1 INTEGER,
                  підв_2 INTEGER,
                  підв_3 INTEGER,
                  підв_4 INTEGER,
                  підв_5 INTEGER,
                  підв_6 INTEGER,
                  підв_7 INTEGER,
                  підв_8 INTEGER,
                  підв_9 INTEGER,
                  підв_10 INTEGER,
                  підв_11 INTEGER,
                  підв_12 INTEGER,
                  підв_13 INTEGER,
                  підв_14 INTEGER,
                  підв_15 INTEGER,
                  підв_16 INTEGER,
                  підв_17 INTEGER,
                  підв_18 INTEGER,
                  підв_19 INTEGER,
                  підв_20 INTEGER)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS част_лем
                  (лема TEXT PRIMARY KEY NOT NULL,
                  gen_freq INTEGER,
                  підв_1 INTEGER,
                  підв_2 INTEGER,
                  підв_3 INTEGER,
                  підв_4 INTEGER,
                  підв_5 INTEGER,
                  підв_6 INTEGER,
                  підв_7 INTEGER,
                  підв_8 INTEGER,
                  підв_9 INTEGER,
                  підв_10 INTEGER,
                  підв_11 INTEGER,
                  підв_12 INTEGER,
                  підв_13 INTEGER,
                  підв_14 INTEGER,
                  підв_15 INTEGER,
                  підв_16 INTEGER,
                  підв_17 INTEGER,
                  підв_18 INTEGER,
                  підв_19 INTEGER,
                  підв_20 INTEGER)
''')

with open("вибірка 1.txt",  encoding = "utf-8") as data_1:
    text_1 = data_1.read().lower()
#print(text_1)

#Робимо токенізацію

without_punc_marks = []
edited = re.sub('\.', '', text_1)
edited = re.sub(',', '', edited)
edited = re.sub('!', '', edited)
edited = re.sub('\?', '', edited)
edited = re.sub(':', '', edited)
edited = re.sub(';', '', edited)
edited = re.sub('\.\.', '', edited)
edited = re.sub('\(', '', edited)
edited = re.sub('\)', '', edited)
edited = re.sub('[a-zA-Z]+', '', edited)
edited = re.sub('"', '', edited)
edited = re.sub("'", '', edited)
edited = re.sub('\[', '', edited)
edited = re.sub('\]', '', edited)
edited = re.sub('\d', '', edited)
edited = re.sub('%', '', edited)
edited = re.sub('\\\\', '', edited)
edited = re.sub('\n', ' ', edited)
edited = re.sub("'\]", '', edited)
edited = re.sub("\['", '', edited)
edited = re.sub('\s-\s', ' ', edited)
without_punc_marks.append(edited)
#print(without_punc_marks)

splitted_1 = str(without_punc_marks).split(' ')
#print(splitted_1)

#Видаляємо пусті слова
try:
    for i in splitted_1:
        if i == '':
            splitted_1.remove(i)
except:
    print('Пустих слів немає')

#Відраховуємо потрібну кількість слововживань (20000)
count = 0
edited_list = []
for word in splitted_1:
    if count == 20000:
        break
    count += 1
    edited_list.append(word)
#print(edited_list)

sample_1_dict = {}
sample_1_list = []

#Ділимо вибірку на підвибірки
count = 0
x = 0
for word in edited_list:
    if count == 1000:
        break
    count += 1
    sample_1_list.append(word)
    if word in sample_1_dict:
         sample_1_dict[word][1] += 1
    else:
         sample_1_dict[word] = [word]
         sample_1_dict[word].append(1)
#for key, value in sample_1_dict.items():
#    print(f"{key}: {value}")
#print(sample_1_list)

sample_2_list = []
count = 0
for word in edited_list:
    count +=1

    if 1000 < count < 2001:
       sample_2_list.append(word)
       if word in sample_1_dict:
           try:
               sample_1_dict[word][2] += 1
           except:
               sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 1:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_2_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

def divide_on_samples(number):
    if word in sample_1_dict:
          try:
               sample_1_dict[word][number] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < number:
                x = sample_len
                while x < number:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
    else:
         sample_1_dict[word] = [word]
         x = 0
         while x < number-1:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)

sample_3_list = []
count = 0
for word in edited_list:
    count +=1
    if 2000 < count < 3001:
       sample_3_list.append(word)
       divide_on_samples(3)
#print(sample_3_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_4_list = []
count = 0
for word in edited_list:
    count +=1
    if 3000 < count < 4001:
       sample_4_list.append(word)
       divide_on_samples(4)
#print(sample_4_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_5_list = []
count = 0
for word in edited_list:
    count +=1
    if 4000 < count < 5001:
       sample_5_list.append(word)
       divide_on_samples(5)
#print(sample_5_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_6_list = []
count = 0
for word in edited_list:
    count +=1
    if 5000 < count < 6001:
       sample_6_list.append(word)
       divide_on_samples(6)
#print(sample_6_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_7_list = []
count = 0
for word in edited_list:
    count +=1
    if 6000 < count < 7001:
       sample_7_list.append(word)
       divide_on_samples(7)
#print(sample_7_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_8_list = []
count = 0
for word in edited_list:
    count +=1
    if 7000 < count < 8001:
       sample_8_list.append(word)
       divide_on_samples(8)
#print(sample_8_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_9_list = []
count = 0
for word in edited_list:
    count +=1
    if 8000 < count < 9001:
       sample_9_list.append(word)
       divide_on_samples(9)
#print(sample_9_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_10_list = []
count = 0
for word in edited_list:
    count +=1
    if 9000 < count < 10001:
       sample_10_list.append(word)
       divide_on_samples(10)
#print(sample_10_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_11_list = []
count = 0
for word in edited_list:
    count +=1
    if 10000 < count < 11001:
       sample_11_list.append(word)
       divide_on_samples(11)
#print(sample_11_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_12_list = []
count = 0
for word in edited_list:
    count +=1
    if 11000 < count < 12001:
       sample_12_list.append(word)
       divide_on_samples(12)
#print(sample_12_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_13_list = []
count = 0
for word in edited_list:
    count +=1
    if 12000 < count < 13001:
       sample_13_list.append(word)
       divide_on_samples(13)
#print(sample_13_list)
#for key, value in sample_13_dict.items():
#   print(f"{key}: {value}")

sample_14_list = []
count = 0
for word in edited_list:
    count +=1
    if 13000 < count < 14001:
       sample_14_list.append(word)
       divide_on_samples(14)
#print(sample_14_list)
#for key, value in sample_14_dict.items():
#   print(f"{key}: {value}")

sample_15_list = []
count = 0
for word in edited_list:
    count +=1
    if 14000 < count < 15001:
       sample_15_list.append(word)
       divide_on_samples(15)
#print(sample_15_list)
#for key, value in sample_15_dict.items():
#   print(f"{key}: {value}")

sample_16_list = []
count = 0
for word in edited_list:
    count +=1
    if 15000 < count < 16001:
       sample_16_list.append(word)
       divide_on_samples(16)
#print(sample_16_list)
#for key, value in sample_16_dict.items():
#   print(f"{key}: {value}")

sample_17_list = []
count = 0
for word in edited_list:
    count +=1
    if 16000 < count < 17001:
       sample_17_list.append(word)
       divide_on_samples(17)
#print(sample_17_list)
#for key, value in sample_17_dict.items():
#   print(f"{key}: {value}")

sample_18_list = []
count = 0
for word in edited_list:
    count +=1
    if 17000 < count < 18001:
       sample_18_list.append(word)
       divide_on_samples(18)
#print(sample_18_list)
#for key, value in sample_18_dict.items():
#   print(f"{key}: {value}")

sample_19_list = []
count = 0
for word in edited_list:
    count +=1
    if 18000 < count < 19001:
       sample_19_list.append(word)
       divide_on_samples(19)
#print(sample_19_list)
#for key, value in sample_19_dict.items():
#   print(f"{key}: {value}")

sample_20_list = []
count = 0
for word in edited_list:
    count +=1
    if 19000 < count:
       sample_20_list.append(word)
       divide_on_samples(20)
#print(sample_20_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

values1 = list(sample_1_dict.values())

#print(values1)
#Додаємо значення 0 до словоформ, які зустрілися лише в першій підвибірці
x = 2
for i in values1:
    while len(i) <21:
        i.append(0)
        x += 1


    gen_freq = sum(i[1:21]) #додаємо до списку загальу кількість слововживань
    i.insert(1, gen_freq)

    #print(x_aver)
    #print(gen_freq)
#print(values1)

values1_ordered = sorted(values1, key=lambda x:x[1], reverse=True)
#print(values1_ordered)

for i in values1_ordered:
   cursor.execute("""INSERT INTO част_словоформ
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()







morph = pymorphy2.MorphAnalyzer(lang='uk')
part_of_speech = {}

# складаємо словник частин мови у першій підвибірці
for i in sample_1_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    #print(freq)
    if freq in part_of_speech:
        part_of_speech[freq][1] += 1
    else:
        part_of_speech[freq] = [freq]
        part_of_speech[freq].append(1)
    #print(i + ' ' + str(parsed1.tag.POS))
#print(part_of_speech)

for i in sample_2_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    #print(freq)
    if freq in part_of_speech:
        try:
            part_of_speech[freq][2] += 1
        except:
            part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 1:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

def count_parts_of_speech(number):
    if freq in part_of_speech:
        try:
            part_of_speech[freq][number] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < number:
                x = freq_len
                while x < number:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        while x < number-1:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)

for i in sample_3_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    #print(freq)
    count_parts_of_speech(3)
#print(part_of_speech)

for i in sample_4_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(4)
#print(part_of_speech)

for i in sample_5_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    #print(freq)
    count_parts_of_speech(5)
#print(part_of_speech)

for i in sample_6_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(6)
#print(part_of_speech)

for i in sample_7_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(7)
#print(part_of_speech)

for i in sample_8_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    #print(freq)
    count_parts_of_speech(8)
#print(part_of_speech)

for i in sample_9_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(9)
#print(part_of_speech)

for i in sample_10_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(10)
#print(part_of_speech)

for i in sample_11_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        count_parts_of_speech(11)
#print(part_of_speech)

for i in sample_12_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(12)
#print(part_of_speech)

for i in sample_13_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(13)
#print(part_of_speech)

for i in sample_14_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(14)
#print(part_of_speech)

for i in sample_15_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(15)
#print(part_of_speech)

for i in sample_16_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(16)
#print(part_of_speech)

for i in sample_17_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(17)
#print(part_of_speech)

for i in sample_18_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(18)
#print(part_of_speech)

for i in sample_14_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(19)
#print(part_of_speech)

for i in sample_20_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(20)
#print(part_of_speech)

values2 = list(part_of_speech.values())


for i in values2:
    while len(i) <21:
        i.append(0)

    gen_freq = sum(i[1:21]) #додаємо до списку загальу кількість слововживань
    i.insert(1, gen_freq)

for i in values2:
    if i[0] == None:
        values2.remove(i)
#print(values2)

values2_ordered = sorted(values2, key=lambda x:x[1], reverse=True)
#print(values2_ordered)

for i in values2_ordered:
    i.insert(2, i[1]/20)
    i.insert(3, round(i[1]/20000, 3))
#print(values2_ordered)

for i in values2_ordered:
   cursor.execute("""INSERT INTO част_частин_мови
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()






lemmas = {}
for i in sample_1_list:
    normal_form = morph.parse(i)[0].normal_form
    #print(normal_form)
    if normal_form in lemmas:
        lemmas[normal_form][1] += 1
    else:
        lemmas[normal_form] = [normal_form]
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_2_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][2] += 1
        except:
            lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 1:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

def count_lemmas(number):
    if normal_form in lemmas:
        try:
            lemmas[normal_form][number] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < number:
                x = lemmas_len
                while x < number:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < number-1:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)

for i in sample_3_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(3)
#print(lemmas)

for i in sample_4_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(4)
#print(lemmas)

for i in sample_5_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(5)
#print(lemmas)

for i in sample_6_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(6)
#print(lemmas)

for i in sample_7_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(7)
#print(lemmas)

for i in sample_8_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(8)
#print(lemmas)

for i in sample_9_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(9)
#print(lemmas)

for i in sample_10_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(10)
#print(lemmas)

for i in sample_11_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(11)
#print(lemmas)

for i in sample_12_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(12)
#print(lemmas)

for i in sample_13_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(13)
#print(lemmas)

for i in sample_14_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(14)
#print(lemmas)

for i in sample_15_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(15)
#print(lemmas)

for i in sample_16_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(16)
#print(lemmas)

for i in sample_17_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(17)
#print(lemmas)

for i in sample_18_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(18)
#print(lemmas)

for i in sample_19_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(19)
#print(lemmas)

for i in sample_20_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(20)
#print(lemmas)

values3 = list(lemmas.values())
for i in values3:
    while len(i) <21:
        i.append(0)

    gen_freq = sum(i[1:21]) #додаємо до списку загальу кількість слововживань
    i.insert(1, gen_freq)
#print(values3)

values3_ordered = sorted(values3, key=lambda x:x[1], reverse=True)

for i in values3_ordered:
   cursor.execute("""INSERT INTO част_лем
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

cursor.execute("select * from част_частин_мови")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("select * from част_лем")
rows = cursor.fetchall()
#for row in rows:
#    print(row)


conn.close()


