#Nama : Kevin Austin Stefano
#NIM  : 13518104

import re;
 
############### Dictionary ####################
hari = '(senin|selasa|rabu|kamis|jumat|sabtu|minggu|sen|sel|rab|kam|jum|sab|ming|monday|teusday|wednesday|thursday|friday|saturday|sunday)'
bulan = '(januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember|jan|feb|mar|apr|jun|jul|agu|ags|sept|sep|okt|nov|des|january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)'
angka = '(satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|puluh|ratus|ribu|ratus|juta|ribu|belas|sebelas|sepuluh|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|fourty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|milion)'
ket = '(sebelumnya|setelahnya|berlalu|usai|yang lalu|yang akan datang|lalu)'
ket_orang = '(orang|korban|korban jiwa|odp|pdp|orang odp|orang pdp|kasus|people|person|pasien)'

ket_number = '(st|rd|nd|th)'


################## KMP #######################
def tabelPrefix(keyword):
    tabel = []
    i=1
    while i<len(keyword):
        tabel.append(keyword[0:i])
        i = i+1
    return tabel

def tabelSufix (keyword):
    tabel = []
    i=1
    while i<len(keyword):
        tabel.append(keyword[len(keyword)-i:len(keyword)])
        i = i+1
    return tabel

def tabelBorder(keyword):
    tabel = []
    idx=1
    while idx<=len(keyword):
        tabel_prefix = tabelPrefix(keyword[0:idx])
        tabel_sufix = tabelSufix(keyword[0:idx])
        i=len(tabel_prefix)-1
        while i>=0: 
            if (tabel_prefix[i]==tabel_sufix[i]):
                break
            i = i-1
        tabel.append(i+1)
        idx= idx+1
    tabel.pop()
    tabel.insert(0,0)
    return tabel
    

def KMP(keyword, text):
    tabel_border = tabelBorder(keyword)
    idx_text = 0
    idx_keyword = 0
    found = 0
    while idx_text<len(text):
        if (keyword[idx_keyword] == text[idx_text]) :
            idx_keyword+=1 
            idx_text += 1
        elif idx_keyword!=len(keyword) and idx_keyword!=0:
            idx_keyword = tabel_border[idx_keyword]
        else:
            idx_text +=1
            idx_keyword = 0
        if idx_keyword==len(keyword):
            found = 1
            break
    return found

def searchKeywordKMP(stringInput, text):
    i=0;
    idx = []
    for sentence in text:
        hasil = KMP(stringInput,sentence)
        if (hasil==1) :
            idx.append(i)
        i=i+1
    return idx

############## Booyer Moore ####################
def tabelLo(keyword): #kalau
    tabel = {}
    i= 0;
    while i<len(keyword):
        tabel[keyword[i:i+1]] = i
        i = i+1
    return tabel

def BoyerMoore(keyword, text):
    found =0
    tabel_lo = tabelLo(keyword)
    # print(tabel_lo)
    idx_text = len(keyword)-1
    idx_keyword = len(keyword)-1
    while idx_text < len(text) and idx_keyword>=0:
        if text[idx_text:idx_text+1] not in tabel_lo:
            idx_text +=len(keyword)
            idx_keyword = len(keyword)-1
        else:
            if (keyword[idx_keyword:idx_keyword+1]==text[idx_text:idx_text+1]):
                if (idx_keyword>0):
                    idx_keyword -=1
                    idx_text -=1
                else:
                    found =1
                    break
            else:
                idx_text = idx_text+len(keyword) - min((tabel_lo[text[idx_text:idx_text+1]]+1),idx_keyword)
                idx_keyword = len(keyword)-1
        
    return found

def searchKeywordBoyerMoore(stringInput, text):
    i=0;
    idx = []
    for sentence in text:
        hasil = BoyerMoore(stringInput,str(sentence))
        if (hasil==1) :
            idx.append(i)
        i=i+1
    return idx

################### Regex #######################
def splitTexttoSentence(text):
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

def searchDate(stringInput):
    patterns = []

    patterns.append(hari+'\s\(*(([3][0-1]|[0-2]*[0-9])(\/|\-)([0]*[1-9]|[1][0-2])(\/|\-)*(\d{4})*)\)*') #Sabtu (11-1-2000) | Sabtu, 11/1/2000
    patterns.append(hari+'\,\s(([3][0-1]|[0-2]*[0-9])(\/|\-)([0]*[1-9]|[1][0-2])(\/|\-)(\d{4})*)') #Sabtu, 11-1-2000 | Sabtu, 11/1/2000
    patterns.append('(([3][0-1]|[0-2]*[0-9])(\/|\-)([0]*[1-9]|[1][0-2])(\/|\-)(\d{4}))') #11-1-2000

    patterns.append(hari+'\s\(*(([3][0-1]|[0-2]*[0-9])('+ket_number+'*)\s'+bulan+'\s(\d{4})*)\)*') #Sabtu (11 April 2000)
    patterns.append(hari+'\,\s(([3][0-1]|[0-2]*[0-9])('+ket_number+'*)\s'+bulan+'\s(\d{4})*)') #Sabtu, 11 April 2000
    patterns.append('(([3][0-1]|[0-2]*[0-9])('+ket_number+'*)\s'+bulan+'\s(\d{4})*)') #11 April 2000

    patterns.append('(\d{1,})(\/|\-)(\d{1,})(\/|\-)(\d{1,})') #13/1/14 (DD MM YY)| 12-18-2014 (MM DD YY)
    patterns.append('((('+ angka + '\s)*)|(se)*)hari(\s' + ket +'*)') #2 hari yang lalu
    
    for pattern in patterns:
        hasil = re.search(pattern,stringInput)
        if (hasil):
            break
    if (hasil):
        return hasil.group(0)
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
        return hasil.group(0)
    else:
        return '';


def searchJumlah(keyword, stringInput):
    searchkeyword = re.search(keyword,stringInput)
    if searchkeyword!=None:
        idxkeyi, idxkeyj = searchkeyword.span()
    else:
        return '-'

    min_nilai = -999
    min = 9999
    patterns = []
    patterns.append('([\d][\d]*[\.|\,]*[\d]*[\.|\,]*[\d]*[\s]'+ket_orang+')')
    for pattern in patterns:
        hasils = re.findall(pattern,stringInput)
        for hasil in (hasils):
            if hasil!=None and str(hasil)!=str(keyword):
                i, j = re.search(str(hasil[0]),stringInput).span()
                if abs(i-idxkeyi)<min:
                    min_nilai = hasil[0]
                    min = abs(i-idxkeyi)
    if (min_nilai!=-999 ):
        return min_nilai
    else:
        return '-';


################### MAIN #######################
def kalkulasi(hasil, split, index, splitnormal, keyword, folder):
    hasil.append("\n")
    hasil.append(("--------- Diambil dari : "+ str(folder) + " --------- "))
    if (searchDate(split[index])):
        hasil.append(searchDate(split[index]))
    else:
        hasil.append(searchDate(split[0]))

    if (searchTime(split[index])):
        hasil.append(searchTime(split[index]))
    else:
        hasil.append(searchTime(split[0]))
    hasil.append("Jumlah : "+ str(searchJumlah(keyword.lower(),split[index])))
    hasil.append(splitnormal[index])
    return hasil



def mainProgram(folder, keyword, jenis):
    folder_ = '../test/'+folder
    file =  open(folder_, 'r')
    stringnormal = file.read().replace('\n',' ')
    splitnormal = splitTexttoSentence(stringnormal)
    string = stringnormal.lower()
    split = splitTexttoSentence(string)
    hasil = []
    
    if jenis=="Boyer-Moore":
        for index in searchKeywordBoyerMoore(keyword.lower(),split):
            hasil = kalkulasi(hasil, split, index, splitnormal, keyword, folder)
    elif jenis=="KMP":
        for index in searchKeywordKMP(keyword.lower(),split):
            hasil = kalkulasi(hasil, split, index, splitnormal, keyword, folder)
    else:
        for index in searchKeywordRegex(keyword.lower(),split):
            hasil = kalkulasi(hasil, split, index, splitnormal, keyword, folder)
    return hasil
