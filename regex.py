import re;
from KMP import KMP;
from BooyerMoore import BooyerMoore;

hari = '(senin|selasa|rabu|kamis|jumat|sabtu|minggu|sen|sel|rab|kam|jum|sab|ming|monday|teusday|wednesday|thursday|friday|saturday|sunday)'
bulan = '(januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember|jan|feb|mar|apr|jun|jul|agu|ags|sept|sep|okt|nov|des|january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)'
angka = '(satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|puluh|ratus|ribu|ratus|juta|ribu|belas|sebelas|sepuluh|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|fourty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|milion)'
ket = '(sebelumnya|setelahnya|berlalu|usai|yang lalu|yang akan datang|lalu)'
ket_orang = '(orang|korban|korban jiwa|ODP|PDP)'

ket_number = '(st|rd|nd|th)'

def splitTexttoSentence(text):
    #hasil = re.split(r'((?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\!|\?)\s)',text)
  
    hasil = text.split('. ')
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
    patterns.append('((('+ angka + '\s)*)|(se)*)hari(\s' + ket +'*)') #2 hari yang lalu
    patterns.append(hari+'\s\(*(([3][0-1]|[0-2]*[0-9])(\/|\-)([0]*[1-9]|[1][0-2])(\/|\-)*(\d{4})*)\)*') #Sabtu (11-1-2000) | Sabtu, 11/1/2000
    patterns.append(hari+'\,\s(([3][0-1]|[0-2]*[0-9])(\/|\-)([0]*[1-9]|[1][0-2])(\/|\-)(\d{4})*)') #Sabtu, 11-1-2000 | Sabtu, 11/1/2000
    patterns.append('(([3][0-1]|[0-2]*[0-9])(\/|\-)([0]*[1-9]|[1][0-2])(\/|\-)(\d{4}))') #11-1-2000

    patterns.append(hari+'\s\(*(([3][0-1]|[0-2]*[0-9])('+ket_number+'*)\s'+bulan+'\s(\d{4})*)\)*') #Sabtu (11 April 2000)
    patterns.append(hari+'\,\s(([3][0-1]|[0-2]*[0-9])('+ket_number+'*)\s'+bulan+'\s(\d{4})*)') #Sabtu, 11 April 2000
    patterns.append('(([3][0-1]|[0-2]*[0-9])('+ket_number+'*)\s'+bulan+'\s(\d{4})*)') #11 April 2000

    patterns.append('(\d{1,})(\/|\-)(\d{1,})(\/|\-)(\d{1,})') #13/1/14 (DD MM YY)| 12-18-2014 (MM DD YY)

    for pattern in patterns:
        hasil = re.search(pattern,stringInput)
        if (hasil):
            break
    if (hasil):
        return hasil[0]
    else:
        return '';

def searchTime(stringInput):
    patterns = []
    patterns.append('((pukul\s)*\w{1,}(:|.)\w{1,}\swi\w{1,})') #pukul* 5.06 WIB*
    patterns.append('(\w{1,}:\w{1,})(:\w{1,})*') #05:03
    for pattern in patterns:
        hasil = re.search(pattern,stringInput)
        if (hasil):
            break
    if (hasil):
        return hasil[0]
    else:
        return '';


def searchJumlah(stringInput):
    patterns = []
    patterns.append('\d{1,}((\.|\,)\d{1,})*\s'+ket_orang)
    patterns.append('\d{1,}((\.|\,)\d{1,})*')
    for pattern in patterns:
        hasil = re.search(pattern,stringInput)
        if (hasil):
            break
    if (hasil):
        return hasil[0]
    else:
        return 0;

def searchString(stringInput):
    hasil = re.search[0]

#MAIN
#Masukan file eksternal
def mainProgram(folder, keyword, jenis):
    file =  open(folder, 'r')
    stringnormal = file.read().replace('\n',' ')
    splitnormal = splitTexttoSentence(stringnormal)
    string = stringnormal.lower()
    split = splitTexttoSentence(string)
    hasil = []
    if jenis=="Boyer-Moore":
        for index in searchKeywordBooyerMoore(keyword.lower(),split):
            if (searchDate(split[index])):
                hasil.append(searchDate(split[index]))
            else:
                hasil.append(searchDate(split[0]))

            if (searchTime(split[index])):
                hasil.append(searchTime(split[index]))
            else:
                hasil.append(searchTime(split[0]))
            hasil.append("Jumlah : "+ str(searchJumlah(split[index])))
            hasil.append(splitnormal[index])
    elif jenis=="KMP":
        
        for index in searchKeywordKMP(keyword.lower(),split):
            if (searchDate(split[index])):
                hasil.append(searchDate(split[index]))
            else:
                hasil.append(searchDate(split[0]))

            if (searchTime(split[index])):
                hasil.append(searchTime(split[index]))
            else:
                hasil.append(searchTime(split[0]))
            hasil.append("Jumlah : "+ str(searchJumlah(split[index])))
            hasil.append(splitnormal[index])
    else:
        
        for index in searchKeywordRegex(keyword.lower(),split):
            if (searchDate(split[index])):
                hasil.append(searchDate(split[index]))
            else:
                hasil.append(searchDate(split[0]))

            if (searchTime(split[index])):
                hasil.append(searchTime(split[index]))
            else:
                hasil.append(searchTime(split[0]))
            hasil.append("Jumlah : "+ str(searchJumlah(split[index])))
            hasil.append(splitnormal[index])

    return hasil
