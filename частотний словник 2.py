#!/usr/bin/env python
# coding: utf-8

import sqlite3
import re
import pymorphy2

#Створюємо базу даних і таблицю частотності словоформ

conn = sqlite3.connect('frequency_dict.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS част_словоформ_2
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

cursor.execute('''CREATE TABLE IF NOT EXISTS част_частин_мови_2
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

cursor.execute('''CREATE TABLE IF NOT EXISTS част_лем_2
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

with open("вибірка 2.txt",  encoding = "utf-8") as data_2:
    text_2 = data_2.read().lower()
#print(text_2)

#Робимо токенізацію

without_punc_marks = []
edited = re.sub('\.', '', text_2)
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
edited = re.sub("—", '', edited)
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

#locale.setlocale(locale.LC_ALL, 'Ukrainian')
#splitted_1.sort(key=functools.cmp_to_key(locale.strcoll))
#print("Lokale:", splitted_1 )

#Відраховуємо потрібну кількість слововживань (20000)
count = 0
edited_list = []
for word in splitted_1:
    if count == 20000:
        break
    count += 1
    edited_list.append(word)
#print(edited_list)

#with open('відредагована вибірка 1.txt', 'w+', encoding = "utf-8") as file:
#    file.write(str(edited_list_0))

#with open('відредагована вибірка 1.txt', encoding = "utf-8") as file:
#    edited_list = file.read().
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

sample_3_list = []
count = 0
for word in edited_list:
    count +=1
    if 2000 < count < 3001:
       sample_3_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][3] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 3:
                x = sample_len
                while x < 3:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 2:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_3_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_4_list = []
count = 0
for word in edited_list:
    count +=1
    if 3000 < count < 4001:
       sample_4_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][4] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 4:
                x = sample_len
                while x < 4:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 3:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_4_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_5_list = []
count = 0
for word in edited_list:
    count +=1
    if 4000 < count < 5001:
       sample_5_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][5] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 5:
                x = sample_len
                while x < 5:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 4:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_5_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_6_list = []
count = 0
for word in edited_list:
    count +=1
    if 5000 < count < 6001:
       sample_6_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][6] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 6:
                x = sample_len
                while x < 6:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 5:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_6_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_7_list = []
count = 0
for word in edited_list:
    count +=1
    if 6000 < count < 7001:
       sample_7_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][7] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 7:
                x = sample_len
                while x < 7:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 6:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_7_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_8_list = []
count = 0
for word in edited_list:
    count +=1
    if 7000 < count < 8001:
       sample_8_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][8] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 8:
                x = sample_len
                while x < 8:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 7:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_8_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_9_list = []
count = 0
for word in edited_list:
    count +=1
    if 8000 < count < 9001:
       sample_9_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][9] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 9:
                x = sample_len
                while x < 9:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 8:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_9_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_10_list = []
count = 0
for word in edited_list:
    count +=1
    if 9000 < count < 10001:
       sample_10_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][10] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 10:
                x = sample_len
                while x < 10:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 9:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_10_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_11_list = []
count = 0
for word in edited_list:
    count +=1
    if 10000 < count < 11001:
       sample_11_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][11] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 11:
                x = sample_len
                while x < 11:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 10:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_11_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_12_list = []
count = 0
for word in edited_list:
    count +=1
    if 11000 < count < 12001:
       sample_12_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][12] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 12:
                x = sample_len
                while x < 12:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 11:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_12_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

sample_13_list = []
count = 0
for word in edited_list:
    count +=1
    if 12000 < count < 13001:
       sample_13_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][13] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 13:
                x = sample_len
                while x < 13:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 12:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_13_list)
#for key, value in sample_13_dict.items():
#   print(f"{key}: {value}")

sample_14_list = []
count = 0
for word in edited_list:
    count +=1
    if 13000 < count < 14001:
       sample_14_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][14] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 14:
                x = sample_len
                while x < 14:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 13:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_14_list)
#for key, value in sample_14_dict.items():
#   print(f"{key}: {value}")

sample_15_list = []
count = 0
for word in edited_list:
    count +=1
    if 14000 < count < 15001:
       sample_15_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][15] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 15:
                x = sample_len
                while x < 15:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 14:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_15_list)
#for key, value in sample_15_dict.items():
#   print(f"{key}: {value}")

sample_16_list = []
count = 0
for word in edited_list:
    count +=1
    if 15000 < count < 16001:
       sample_16_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][16] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 16:
                x = sample_len
                while x < 16:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 15:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_16_list)
#for key, value in sample_16_dict.items():
#   print(f"{key}: {value}")

sample_17_list = []
count = 0
for word in edited_list:
    count +=1
    if 16000 < count < 17001:
       sample_17_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][17] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 17:
                x = sample_len
                while x < 17:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 16:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_17_list)
#for key, value in sample_17_dict.items():
#   print(f"{key}: {value}")

sample_18_list = []
count = 0
for word in edited_list:
    count +=1
    if 17000 < count < 18001:
       sample_18_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][18] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 18:
                x = sample_len
                while x < 18:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 17:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_18_list)
#for key, value in sample_18_dict.items():
#   print(f"{key}: {value}")

sample_19_list = []
count = 0
for word in edited_list:
    count +=1
    if 18000 < count < 19001:
       sample_19_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][19] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 19:
                x = sample_len
                while x < 19:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 18:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_19_list)
#for key, value in sample_19_dict.items():
#   print(f"{key}: {value}")

sample_20_list = []
count = 0
for word in edited_list:
    count +=1
    if 19000 < count:
       sample_20_list.append(word)
       if word in sample_1_dict:
          try:
               sample_1_dict[word][20] += 1
          except:
             sample_len = len(sample_1_dict[word])
             if sample_len < 20:
                x = sample_len
                while x < 20:
                    sample_1_dict[word].append(0)
                    x += 1
                sample_1_dict[word].append(1)
             else:
                sample_1_dict[word].append(1)
       else:
         sample_1_dict[word] = [word]
         x = 0
         for i in sample_1_dict[word]:
             while x < 19:
                sample_1_dict[word].append(0)
                x += 1
         sample_1_dict[word].append(1)
#print(sample_20_list)
#for key, value in sample_1_dict.items():
#   print(f"{key}: {value}")

values1 = list(sample_1_dict.values())

#Додаємо значення 0 до словоформ, які зустрілися лише в першій підвибірці
x = 2
for i in values1:
    while len(i) <21:
        i.append(0)
        x += 1


    gen_freq = sum(i[1:21]) #додаємо до списку загальу кількість слововживань
    i.insert(1, gen_freq)
    #print(gen_freq)
#print(values1)

values1_ordered = []
#for i in values1:
#   values1_ordered.append(i)
#for i in values1_ordered:
#    count = 0
#    while count in range(0, len(values1_ordered)-1):
#        if values1_ordered[count][1] < values1_ordered[count+1][1]:
#          values1_ordered[count], values1_ordered[count+1] = values1_ordered[count+1], values1_ordered[count]
#        count += 1
#print(values1_ordered)

#for i in values1_ordered:
#   cursor.execute("""INSERT INTO част_словоформ_2
#                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()


cursor.execute("select * from част_словоформ_2")
rows = cursor.fetchall()
#for row in rows:
#    print(row)
#cursor.execute('drop table част_словоформ_2')
#print("Table dropped")




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

for i in sample_3_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    #print(freq)
    if freq in part_of_speech:
        try:
            part_of_speech[freq][3] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 3:
                x = freq_len
                while x < 3:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 2:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_4_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][4] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 4:
                x = freq_len
                while x < 4:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 3:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_5_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    #print(freq)
    if freq in part_of_speech:
        try:
            part_of_speech[freq][5] += 1
        except:
            freq_len = len(part_of_speech[freq])
            #print(freq_len)
            if freq_len < 5:
                x = freq_len
                while x < 5:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 4:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_6_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][6] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 6:
                x = freq_len
                while x < 6:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 5:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_7_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][7] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 7:
                x = freq_len
                while x < 7:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 6:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_8_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    #print(freq)
    if freq in part_of_speech:
        try:
            part_of_speech[freq][8] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 8:
                x = freq_len
                while x < 8:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 7:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_9_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][9] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 9:
                x = freq_len
                while x < 9:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 8:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_10_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][10] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 10:
                x = freq_len
                while x < 10:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 9:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_11_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][11] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 11:
                x = freq_len
                while x < 11:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 10:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_12_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][12] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 12:
                x = freq_len
                while x < 12:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 11:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_13_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][13] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 13:
                x = freq_len
                while x < 13:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 12:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_14_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][14] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 14:
                x = freq_len
                while x < 14:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 14:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_15_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][15] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 15:
                x = freq_len
                while x < 15:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 15:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_16_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][16] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 16:
                x = freq_len
                while x < 16:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 16:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_17_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][17] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 17:
                x = freq_len
                while x < 17:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 17:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_18_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][18] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 18:
                x = freq_len
                while x < 18:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 18:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_14_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][19] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 19:
                x = freq_len
                while x < 19:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 19:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
#print(part_of_speech)

for i in sample_20_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        try:
            part_of_speech[freq][20] += 1
        except:
            freq_len = len(part_of_speech[freq])
            if freq_len < 20:
                x = freq_len
                while x < 20:
                    part_of_speech[freq].append(0)
                    x += 1
                part_of_speech[freq].append(1)
            else:
                part_of_speech[freq].append(1)
    else:
        part_of_speech[freq] = [freq]
        x = 0
        for o in part_of_speech[freq]:
             while x < 20:
                part_of_speech[freq].append(0)
                x += 1
        part_of_speech[freq].append(1)
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

values2_ordered = []
for i in values2:
   values2_ordered.append(i)

for i in values2_ordered:
    aver_freq = {}
    freq = i[2:22]
    for o in freq:
        if o in aver_freq:
            aver_freq[o][1] += 1
            xini = aver_freq[o][0]*aver_freq[o][1]
            aver_freq[o][2] = xini
        else:
            aver_freq[o] = [o]
            aver_freq[o].append(1)
            xini = aver_freq[o][0]*aver_freq[o][1]
            aver_freq[o].append(xini)

    aver_freq= list(aver_freq.values())
    aver_freq_ordered = []
    for p in aver_freq:
        aver_freq_ordered.append(p)
    for p in aver_freq_ordered:
        count = 0
        while count in range(0, len(aver_freq_ordered)-1):
            if aver_freq_ordered[count][0] > aver_freq_ordered[count+1][0]:
              aver_freq_ordered[count], aver_freq_ordered[count+1] = aver_freq_ordered[count+1], aver_freq_ordered[count]
            count += 1
    #print(aver_freq_ordered)
    ni = []
    xini = []
    for p in aver_freq_ordered:
        ni.append(p[1])

        xini.append(p[2])
    ni_sum = sum(ni)
    xini_sum = sum(xini)
    #print(xini_sum)

    x_aver = xini_sum/ni_sum
    i.insert(2, x_aver)

    i.insert(3, round(i[1]/20000, 3))


for i in values2_ordered:
   count = 0
   while count in range(0, len(values2_ordered)-1):
        if values2_ordered[count][1] < values2_ordered[count+1][1]:
          values2_ordered[count], values2_ordered[count+1] = values2_ordered[count+1], values2_ordered[count]
        count += 1
#print(values2_ordered)

#for i in values2_ordered:
#   cursor.execute("""INSERT INTO част_частин_мови_2
#                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()

cursor.execute("select * from част_частин_мови_2")
rows = cursor.fetchall()
#for row in rows:
#    print(row)

#cursor.execute("drop table част_частин_мови_2")
#conn.commit()





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

for i in sample_3_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][3] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 3:
                x = lemmas_len
                while x < 3:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 2:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_4_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][4] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 4:
                x = lemmas_len
                while x < 4:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 3:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_5_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][5] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 5:
                x = lemmas_len
                while x < 5:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 4:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_6_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][6] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 6:
                x = lemmas_len
                while x < 6:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 5:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_7_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][7] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 7:
                x = lemmas_len
                while x < 7:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 6:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_8_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][8] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 8:
                x = lemmas_len
                while x < 8:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 7:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_9_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][9] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 9:
                x = lemmas_len
                while x < 9:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 8:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_10_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][10] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 10:
                x = lemmas_len
                while x < 10:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 9:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_11_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][11] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 11:
                x = lemmas_len
                while x < 11:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 10:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_12_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][12] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 12:
                x = lemmas_len
                while x < 12:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 11:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_13_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][13] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 13:
                x = lemmas_len
                while x < 13:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 12:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_14_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][14] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 14:
                x = lemmas_len
                while x < 14:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 13:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_15_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][15] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 15:
                x = lemmas_len
                while x < 15:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 14:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_16_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][16] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 16:
                x = lemmas_len
                while x < 16:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 15:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_17_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][17] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 17:
                x = lemmas_len
                while x < 17:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 16:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_18_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][18] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 18:
                x = lemmas_len
                while x < 18:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 17:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_19_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][19] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 19:
                x = lemmas_len
                while x < 19:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 18:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

for i in sample_20_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        try:
            lemmas[normal_form][20] += 1
        except:
            lemmas_len = len(lemmas[normal_form])
            if lemmas_len < 20:
                x = lemmas_len
                while x < 20:
                    lemmas[normal_form].append(0)
                    x += 1
                lemmas[normal_form].append(1)
            else:
                lemmas[normal_form].append(1)
    else:
        lemmas[normal_form] = [normal_form]
        x = 0
        for o in lemmas[normal_form]:
             while x < 19:
                lemmas[normal_form].append(0)
                x += 1
        lemmas[normal_form].append(1)
#print(lemmas)

values3 = list(lemmas.values())
for i in values3:
    while len(i) <21:
        i.append(0)

    gen_freq = sum(i[1:21]) #додаємо до списку загальу кількість слововживань
    i.insert(1, gen_freq)
#print(values3)

values3_ordered = []
#for i in values3:
#   values3_ordered.append(i)
#for i in values3_ordered:
#    count = 0
#    while count in range(0, len(values3_ordered)-1):
#        if values3_ordered[count][1] < values3_ordered[count+1][1]:
#          values3_ordered[count], values3_ordered[count+1] = values3_ordered[count+1], values3_ordered[count]
#        count += 1
#print(values3_ordered)

#for i in values3_ordered:
#   cursor.execute("""INSERT INTO част_лем_2
#                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", i)
#conn.commit()

cursor.execute("select * from част_лем_2")
rows = cursor.fetchall()
#for row in rows:
#    print(row)

conn.close()
