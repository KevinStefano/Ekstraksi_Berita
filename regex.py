import re;
from KMP import KMP;
from BooyerMoore import BooyerMoore;

hari = '(senin|selasa|rabu|kamis|jumat|sabtu|minggu|sen|sel|rab|kam|jum|sab|ming)'
bulan = '(januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember|jan|feb|mar|apr|jun|jul|agu|ags|sept|sep|okt|nov|des)'

def splitTexttoSentence(text):
    hasil = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',text)
    return hasil

def searchKeywordRegex(stringInput, text):
    i=0;
    idx = []
    for sentence in text:
        hasil = re.search(stringInput,sentence)
        if (hasil) :
            idx.append(i)
        i=i+1
    return idx

def searchKeywordKMP(stringInput, text):
    i=0;
    idx = []
    for sentence in text:
        hasil = KMP(stringInput,sentence)
        if (hasil==1) :
            idx.append(i)
        i=i+1
    return idx

def searchKeywordBooyerMoore(stringInput, text):
    i=0;
    idx = []
    for sentence in text:
        hasil = BooyerMoore(stringInput,sentence)
        if (hasil==1) :
            idx.append(i)
        i=i+1
    return idx

def searchDate(stringInput):
    patterns = []
    patterns.append(hari+'\s\(*(([3][0-1]|[0-2]*[0-9])(\/|\-)([0]*[1-9]|[1][0-2])(\/|\-)*(\d{4})*)\)*') #Sabtu (11-1-2000)
    patterns.append(hari+'\,\s(([3][0-1]|[0-2]*[0-9])(\/|\-)([0]*[1-9]|[1][0-2])(\/|\-)(\d{4})*)') #Sabtu, 11-1-2000
    patterns.append('(([3][0-1]|[0-2]*[0-9])(\/|\-)([0]*[1-9]|[1][0-2])(\/|\-)(\d{4}))') #11-1-2000

    patterns.append(hari+'\s\(*(([3][0-1]|[0-2]*[0-9])\s'+bulan+'\s(\d{4})*)\)*') #Sabtu (11 April 2000)
    patterns.append(hari+'\,\s(([3][0-1]|[0-2]*[0-9])\s'+bulan+'\s(\d{4})*)') #Sabtu, 11 April 2000
    patterns.append('(([3][0-1]|[0-2]*[0-9])\s'+bulan+'\s(\d{4})*)') #11 April 2000
    for pattern in patterns:
        hasil = re.search(pattern,stringInput)
        if (hasil):
            break
    if (hasil):
        return hasil[0]
    else:
        return 0;

def searchTime(stringInput):
    patterns = []
    patterns.append('((pukul\s)*\w{1,}(:|.)\w{1,}\swi\w{1,})')
    patterns.append('\w{1,}:\w{1,}')
    for pattern in patterns:
        hasil = re.search(pattern,stringInput)
        if (hasil):
            break
    if (hasil):
        return hasil[0]
    else:
        return 0;


def searchJumlah(stringInput):
    hasil = re.search('\d{1,}(\.\d{1,})*\sorang',stringInput)
    if (hasil):
        return hasil[0]
    else:
        return 0;

def searchString(stringInput):
    hasil = re.search[0]

#print(searchDate('tanggal 11/11/2000. 11/02/2011 juga'));

#MAIN
#Masukan file eksternal
file =  open('data.txt', 'r')
stringnormal = file.read().replace('\n',' ')
splitnormal = splitTexttoSentence(stringnormal)
string = stringnormal.lower()
#keyword= input().lower()
split = splitTexttoSentence(string)
for index in searchKeywordBooyerMoore('terkonfirmasi positif'.lower(),split):
    if (searchDate(split[index])):
        print(searchDate(split[index]))
    else:
        print(searchDate(split[0]))

    if (searchTime(split[index])):
        print(searchTime(split[index]))
    else:
        print(searchTime(split[0]))
    print(searchJumlah(split[index]))
    print(splitnormal[index])


