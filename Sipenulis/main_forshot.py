import Sipenulis.rabin_karp as rk
import time
import statistics
import speech_recognition as sr
import docx
from getch import pause_exit
from xlwt import Workbook
#from openpyxl import Workbook,load_workbook


startTime = time.time()
n = 2
#w = 2
p = 2
student = 1
question = 2
jmlquest = 2
human_rater = [35, 73, 36, 62, 42, 75, 90, 65, 86, 68, 97, 57, 15, 77, 92, 97, 93, 96, 80, 87, 88, 98, 94, 96, 98, 79,
               79, 81, 70, 74, 37, 81, 37, 77, 90, 73, 42, 96, 87, 94, 88, 63, 72]
no1 = []
excel = []
list_score = []
text = docx.Document('soal1.docx')


for count in range(1, student + 1):
    print("======================================")
    print("MAHASISWA", count)
    print("======================================")
    arr_score = []
    current_score = 0
    score = 0
    #doc = ps.read_txt("mahasiswa" + str(count) + ".docx")

    test = []
    r = sr.Recognizer()
    #jmlquest = int(input("Masukan jumlah soal\n"))
    print("Jawablah pertanyaan berikut ini")


    with sr.Microphone() as source:
        for i in range(jmlquest):
            print(text.paragraphs[i].text)
            input("Press Enter to answer...")
            audio = r.listen(source)
            sample_rate_hertz = 8000
            enable_automatic_punctuation = True
            r.adjust_for_ambient_noise(source)

            try:
                test.append(r.recognize_google(audio, language="ja-JP"))
                print("あなたの答えは:", test)
                print("\n")

            except:
                print('Sorry.. run again...')



    for q in range(0, question):
        kj = 1
        scores = []

        # process the student's answer document
        prep = rk.preprocessing(test[q])                       #delete repetitive from question, convert to romaji(if needed), filter text
        #prep = ps.winnow(test[q])

        print('\nJAWABAN ', q + 1)

        pattern = rk.read_txt("jwbDosen" + str(q + 1) + ".docx")  #read answer key documents
        #for each answer keys (from each questions)
        for x in range(0, len(pattern)):
            #process answer keys
            prep2 = rk.preprocessing(pattern[x])                  #delete repetitive from question, convert to romaji(if needed), filter text
            winnowing = rk.rabin(prep, p, n)
            winnowing2 = rk.rabin(prep2, p, n)
            # similarity measurement
            jac_measure = rk.jaccard(winnowing, winnowing2)
            dice_measure = rk.dice(winnowing, winnowing2)
            cos_measure = rk.cosine(winnowing, winnowing2)
            scores.append(cos_measure)
            # print("jaccard : " + str(jac_measure) + " | dice : " + str(dice_measure) + " | cosine : " + str(cos_measure))
            # nilai terbesar dari ketiga metode pengukuran
            score = max(jac_measure, dice_measure, cos_measure)
            print("Nomor " + str(q + 1) + " : " + str(score))
            print("human rater: " + str(human_rater[q-1]))
            temp_score = score
            if current_score <= temp_score:
                current_score = temp_score
            else:
                continue

            # #print all processes' results
            print('----------------')
            print('KUNCI JAWABAN '+str(kj))
            print('---\npreprocessing dosen\n', prep2)
            print('---\npreprocessing siswa\n', prep)

            kj += 1 #loop for each answer keys

        arr_score.append(max(scores))

    list_score.append(round(sum(arr_score),2))
    akurasi = []
    for n in range(student):
        acc = round((100 - (((abs(list_score[n] - human_rater[n])) / 100) * 100)),2)
        akurasi.append(acc)
    totalscore =  sum(arr_score) / len(arr_score)
    print("======================================")
    print("======================================")
    #print("Human Rater\t\t\t: ", human_rater)
    print("Nilai-nilai Siswa\t: ", totalscore)
    print("Nilai per soal \t\t: ", arr_score)
    print("Akurasi\t\t\t\t: ", akurasi)
    #print("Rata-rata Akurasi\t: ", round(statistics.mean(akurasi),2))
    #print("Standar Deviasi\t\t: ", round(statistics.stdev(akurasi),2))
    print("Program Execution Duration: ", (time.time() - startTime), "seconds")


    pause_exit(status=0, message='Press any key to exit.')


#create excel file of the data
wb = Workbook()                                             # Workbook is created
#wb = xlwt.Workbook()
sheet1 = wb.add_sheet("Test")                  # add_sheet is used to create sheet.
for n in range(1, 43):
    for o in range(len(excel)):
        for m in range(2,6):
            sheet1.write(row=n, column=1, value=n)
            sheet1.write(row=n, column=m, value=excel[o])
            for n in range(len(human_rater)):
                sheet1.write(row=1, column=1, value='Siswa')
                sheet1.write(row=1, column=2, value='Human Rater Score')
                sheet1.write(row=1, column=3, value='Simple-O Score')
                sheet1.write(row=1, column=4, value='Accuracy')
                sheet1.write(row=n+2, column=1, value=n)
                sheet1.write(row=n+2, column=2, value=human_rater[n])
                sheet1.write(row=n+2, column=3, value=list_score[n])
                sheet1.write(row=n+2, column=4, value=akurasi[n])
                wb.save('data.xlsx')


