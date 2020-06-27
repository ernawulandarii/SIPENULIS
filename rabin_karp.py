from pykakasi import kakasi  # untuk proses mengubah karakter jp ke roman
import re  # regular expression
import docx2txt
import tinysegmenter
from math import *
from numpy import zeros, sum  # library to create a matrix, etc.
from scipy.linalg import svd, eig  # library for the svd process

kakasi = kakasi()


# read documents, .txt or .docx
def read_txt(doc):
    read1 = docx2txt.process(doc)
    read = read1.splitlines()  # split document to lists on new line
    read = [x for x in read if not x.isdigit()]  # remove number from words
    read = [x for x in read if x]  # remove empty list
    return read


'''
mulai  preprocessing
1. menghilangkan kata-kata yang mengulang soal
2. romanisasi, konversi kana ke romaji
3. whitespace removal, menghapus spasi dan enter
4. case folding, menyeragamkan ke lower case
5. filtering, menghapus selain huruf dan angka

'''


# menghapus kata yang mengulang soal
def remove_rep(text):
    rep_words = ["2020年東京オリンピックのマスコットは", "ハラルは", "ハラルというは", "ハラルというのは",
                 "生前退位は", "生前退位というは", "生前退位というのは",
                 "衆院選は", "衆院選というは", "衆院選というのは",
                 "Uターンは", "Uターンのは", "Uターンというは", "Uターンというのは",
                 "Uターン就職は", "Uターン就職というは", "U-ターン就職というのは"]

    word_list = set(rep_words)
    for words in word_list:
        if words in text:
            text = text.replace(words, "")
    return text


# mengubah katakana, hiragana, dan kanji ke romaji (romanisasi)
def to_romaji(text_jpn):
    kakasi.setMode("H", "a")  # Hiragana ke romaji
    kakasi.setMode("K", "a")  # Katakana ke romaji
    kakasi.setMode("J", "a")  # Japanese ke romaji
    kakasi.setMode("r", "Hepburn")  # default: Hepburn Roman table
    # kakasi.setMode("s", True) # add space, default: no separator
    # kakasi.setMode("C", True) # capitalize, default: no capitalize
    convert = (kakasi.getConverter()).do(text_jpn)
    return convert


# filtering
def filter_text(romaji):
    filtering = re.sub("\n", "", romaji).casefold()
    filtering = re.sub("[^A-Za-z0-9]+", "", filtering)
    return filtering


# selesai preprocessing


'''
mulai rabinkarp
1. pembentukan ngram (penggalan lata) sebanyak n
2. hashing, konversi tiap karakter pada ngram ke bentuk hash dengan rumus rolling hash
'''


# n gram
def nGram(text, n):
    ngram = [text[i:i + n] for i in range(len(text) - n + 1)]
    return ngram


# hashing
def to_hash(text, p):
    result = 0
    length = len(text)
    ascii_code = [ord(i) for i in text]  # mengubah ke ascii
    for i in range(length):
        result = result + (ascii_code[i] * pow(p, length - 1))  # rumus rolling hash
        length = length - 1
    return result


def hashing(ngram, p):
    roll_hash = [to_hash(ngram[i], p) for i in range(len(ngram))]
    return roll_hash


# selesai rabin-karp


'''
mulai similarity measurement, mencari tingkat kesamaan fingerprint
1. jaccard similarity
2. dice coefficient
3. cosine similarity
'''


# jaccard similarity
def jaccard(fingerprint1, fingerprint2):
    num = len(set(fingerprint1).intersection(set(fingerprint2)))
    denum = len(set(fingerprint1).union(set(fingerprint2)))
    if denum == 0:
        jaccard = 0.0
    else:
        jaccard = float(num / denum) * 100
    return jaccard


# dice coefficient
def dice(fingerprint1, fingerprint2):
    num = 2 * (len(set(fingerprint1).intersection(set(fingerprint2))))
    denum = len(set(fingerprint1)) + len(set(fingerprint2))
    if denum == 0:
        dice = 0.0
    else:
        dice = float(num / denum) * 100
    return dice


# cosine similarity
def cosine(fingerprint1, fingerprint2):
    num = len(set(fingerprint1).intersection(set(fingerprint2)))
    denum = (len(set(fingerprint1)) ** .5) * (len(set(fingerprint2)) ** .5)
    if denum == 0:
        cosine = 0.0
    else:
        cosine = float(num / denum) * 100
        if cosine > 100:
            cosine = 100.0
    return cosine


# selesai similarity measurement

# run preprocessing
def preprocessing(text):
    text = remove_rep(text)
    romaji = to_romaji(text)
    filtering = filter_text(romaji)
    return filtering


# run rabinkarp
def rabin(text, p, n):
    ngram = nGram(text, n)
    roll_hash = hashing(ngram, p)
    return roll_hash

#run similarity measurement
def measure(key, student):
    jaccard_sim = jaccard(key, student)
    dice_sim = dice(key, student)
    cosine_sim = cosine(key, student)
    print("\n======================================================")
    print("SIMILARITY MEASUREMENT")
    print("======================================================")
    print(" JACCARD SIMILARITY : ", jaccard_sim)
    print("\n DICE COEFFICIENT   : ", dice_sim)
    print("\n COSINE SIMILARITY  : ", cosine_sim)
    return jaccard_sim, dice_sim, cosine_sim



