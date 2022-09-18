#!/usr/bin/env python
# coding: utf-8

import sqlite3
import re
import pymorphy2


''' Creating a database (DB). The DB contains 3 tables: frequency table of words forms, lemmas and parts of speech.
The lenght of the chosen part of a text, which is to be analysed is 20,000 tokens (word forms).
The text is going to be devided into 20 samples, each is 1000 tokens long. It is done with the purpose of making further linguistical analysis
of a text possible.
'''

conn = sqlite3.connect('frequency_dict.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS words_forms_freq
                  (word_form TEXT PRIMARY KEY NOT NULL,
                  gen_freq INTEGER, # frequency of a word form in a whole text
                  sample_1 INTEGER, # frequency of a word form in the first sample of the text (one sample = 1000 tokens)
                  sample_2 INTEGER,
                  sample_3 INTEGER,
                  sample_4 INTEGER,
                  sample_5 INTEGER,
                  sample_6 INTEGER,
                  sample_7 INTEGER,
                  sample_8 INTEGER,
                  sample_9 INTEGER,
                  sample_10 INTEGER,
                  sample_11 INTEGER,
                  sample_12 INTEGER,
                  sample_13 INTEGER,
                  sample_14 INTEGER,
                  sample_15 INTEGER,
                  sample_16 INTEGER,
                  sample_17 INTEGER,
                  sample_18 INTEGER,
                  sample_19 INTEGER,
                  sample_20 INTEGER)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS part_of_speech_freq
                  (part_of_speech TEXT PRIMARY KEY NOT NULL,
                  gen_freq INTEGER,
                  x_aver INTEGER, # average frequency of a part of speech in all samples
                  relative_freq INTEGER,
                  sample_1 INTEGER,
                  sample_2 INTEGER,
                  sample_3 INTEGER,
                  sample_4 INTEGER,
                  sample_5 INTEGER,
                  sample_6 INTEGER,
                  sample_7 INTEGER,
                  sample_8 INTEGER,
                  sample_9 INTEGER,
                  sample_10 INTEGER,
                  sample_11 INTEGER,
                  sample_12 INTEGER,
                  sample_13 INTEGER,
                  sample_14 INTEGER,
                  sample_15 INTEGER,
                  sample_16 INTEGER,
                  sample_17 INTEGER,
                  sample_18 INTEGER,
                  sample_19 INTEGER,
                  sample_20 INTEGER)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS lemmas_freq
                  (lemma TEXT PRIMARY KEY NOT NULL,
                  gen_freq INTEGER,
                  sample_1 INTEGER,
                  sample_2 INTEGER,
                  sample_3 INTEGER,
                  sample_4 INTEGER,
                  sample_5 INTEGER,
                  sample_6 INTEGER,
                  sample_7 INTEGER,
                  sample_8 INTEGER,
                  sample_9 INTEGER,
                  sample_10 INTEGER,
                  sample_11 INTEGER,
                  sample_12 INTEGER,
                  sample_13 INTEGER,
                  sample_14 INTEGER,
                  sample_15 INTEGER,
                  sample_16 INTEGER,
                  sample_17 INTEGER,
                  sample_18 INTEGER,
                  sample_19 INTEGER,
                  sample_20 INTEGER)
''')


with open("text.txt",  encoding = "utf-8") as data_1:
    text_1 = data_1.read().lower()

    
# Making tokenization (removing all symbols, that are not words; separating the text on tokens)
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

splitted_1 = str(without_punc_marks).split(' ')


# Delating empty tokens
try:
    for i in splitted_1:
        if i == '':
            splitted_1.remove(i)
except:
    print('No empty tokens are detected')

    
# Selecting first 20,000 tokens from a text
count = 0
edited_list = []
for word in splitted_1:
    if count == 20000:
        break
    count += 1
    edited_list.append(word)


# Deviding a text into samples
sample_1_dict = {}
sample_1_list = []
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

sample_4_list = []
count = 0
for word in edited_list:
    count +=1
    if 3000 < count < 4001:
       sample_4_list.append(word)
       divide_on_samples(4)

sample_5_list = []
count = 0
for word in edited_list:
    count +=1
    if 4000 < count < 5001:
       sample_5_list.append(word)
       divide_on_samples(5)

sample_6_list = []
count = 0
for word in edited_list:
    count +=1
    if 5000 < count < 6001:
       sample_6_list.append(word)
       divide_on_samples(6)

sample_7_list = []
count = 0
for word in edited_list:
    count +=1
    if 6000 < count < 7001:
       sample_7_list.append(word)
       divide_on_samples(7)

sample_8_list = []
count = 0
for word in edited_list:
    count +=1
    if 7000 < count < 8001:
       sample_8_list.append(word)
       divide_on_samples(8)

sample_9_list = []
count = 0
for word in edited_list:
    count +=1
    if 8000 < count < 9001:
       sample_9_list.append(word)
       divide_on_samples(9)

sample_10_list = []
count = 0
for word in edited_list:
    count +=1
    if 9000 < count < 10001:
       sample_10_list.append(word)
       divide_on_samples(10)

sample_11_list = []
count = 0
for word in edited_list:
    count +=1
    if 10000 < count < 11001:
       sample_11_list.append(word)
       divide_on_samples(11)

sample_12_list = []
count = 0
for word in edited_list:
    count +=1
    if 11000 < count < 12001:
       sample_12_list.append(word)
       divide_on_samples(12)

sample_13_list = []
count = 0
for word in edited_list:
    count +=1
    if 12000 < count < 13001:
       sample_13_list.append(word)
       divide_on_samples(13)

sample_14_list = []
count = 0
for word in edited_list:
    count +=1
    if 13000 < count < 14001:
       sample_14_list.append(word)
       divide_on_samples(14)

sample_15_list = []
count = 0
for word in edited_list:
    count +=1
    if 14000 < count < 15001:
       sample_15_list.append(word)
       divide_on_samples(15)

sample_16_list = []
count = 0
for word in edited_list:
    count +=1
    if 15000 < count < 16001:
       sample_16_list.append(word)
       divide_on_samples(16)

sample_17_list = []
count = 0
for word in edited_list:
    count +=1
    if 16000 < count < 17001:
       sample_17_list.append(word)
       divide_on_samples(17)

sample_18_list = []
count = 0
for word in edited_list:
    count +=1
    if 17000 < count < 18001:
       sample_18_list.append(word)
       divide_on_samples(18)

sample_19_list = []
count = 0
for word in edited_list:
    count +=1
    if 18000 < count < 19001:
       sample_19_list.append(word)
       divide_on_samples(19)

sample_20_list = []
count = 0
for word in edited_list:
    count +=1
    if 19000 < count:
       sample_20_list.append(word)
       divide_on_samples(20)

values1 = list(sample_1_dict.values())

# Adding 0 value to the frequecy of word forms, which were present only in the first sample
x = 2
for i in values1:
    while len(i) <21:
        i.append(0)
        x += 1


    gen_freq = sum(i[1:21]) # adding to the list the general frequency
    i.insert(1, gen_freq)

values1_ordered = sorted(values1, key=lambda x:x[1], reverse=True)

for i in values1_ordered:
   cursor.execute("""INSERT INTO words_forms_freq
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()





# Creating parts of speech frequency dictionary

morph = pymorphy2.MorphAnalyzer(lang='uk')
part_of_speech = {}

for i in sample_1_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        part_of_speech[freq][1] += 1
    else:
        part_of_speech[freq] = [freq]
        part_of_speech[freq].append(1)

for i in sample_2_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
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
    count_parts_of_speech(3)

for i in sample_4_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(4)

for i in sample_5_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(5)

for i in sample_6_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(6)

for i in sample_7_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(7)

for i in sample_8_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(8)

for i in sample_9_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(9)

for i in sample_10_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(10)

for i in sample_11_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    if freq in part_of_speech:
        count_parts_of_speech(11)

for i in sample_12_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(12)

for i in sample_13_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(13)

for i in sample_14_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(14)

for i in sample_15_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(15)

for i in sample_16_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(16)

for i in sample_17_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(17)

for i in sample_18_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(18)

for i in sample_14_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(19)

for i in sample_20_list:
    parsed1 = morph.parse(i)[0]
    freq = parsed1.tag.POS
    count_parts_of_speech(20)

values2 = list(part_of_speech.values())


for i in values2:
    while len(i) <21:
        i.append(0)

    gen_freq = sum(i[1:21]) # adding the general frequency to the list
    i.insert(1, gen_freq)

for i in values2:
    if i[0] == None:
        values2.remove(i)

values2_ordered = sorted(values2, key=lambda x:x[1], reverse=True)

for i in values2_ordered:
    i.insert(2, i[1]/20)
    i.insert(3, round(i[1]/20000, 3))

for i in values2_ordered:
   cursor.execute("""INSERT INTO part_of_speech_freq
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()






lemmas = {}
for i in sample_1_list:
    normal_form = morph.parse(i)[0].normal_form
    if normal_form in lemmas:
        lemmas[normal_form][1] += 1
    else:
        lemmas[normal_form] = [normal_form]
        lemmas[normal_form].append(1)

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

for i in sample_4_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(4)

for i in sample_5_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(5)

for i in sample_6_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(6)

for i in sample_7_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(7)

for i in sample_8_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(8)

for i in sample_9_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(9)

for i in sample_10_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(10)

for i in sample_11_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(11)

for i in sample_12_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(12)

for i in sample_13_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(13)

for i in sample_14_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(14)

for i in sample_15_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(15)

for i in sample_16_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(16)

for i in sample_17_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(17)

for i in sample_18_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(18)

for i in sample_19_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(19)

for i in sample_20_list:
    normal_form = morph.parse(i)[0].normal_form
    count_lemmas(20)

values3 = list(lemmas.values())
for i in values3:
    while len(i) <21:
        i.append(0)

    gen_freq = sum(i[1:21])
    i.insert(1, gen_freq)

values3_ordered = sorted(values3, key=lambda x:x[1], reverse=True)

for i in values3_ordered:
   cursor.execute("""INSERT INTO lemmas_freq
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

conn.close()
