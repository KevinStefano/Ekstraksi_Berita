import re;


def searchDate(stringInput):
    tup = []
    hasil = re.findall(r'(([3][0-1]|[0-2][0-9])(\/|\-)([0][1-9]|1[0-2]|)(\/|\-)(\d{4}))',stringInput)
    for i in hasil :
        a,b,c,d,e,f = i
        if (hasil):
            tup.append(a)
    
    return tup

def searchString(stringInput):
    hasil = re.search

print(searchDate('tanggal 11/01/2000. 11/02/2011 juga'));

#MAIN
#Masukan file eksternal
file =  open('data.txt', 'r')
string = file.read().replace('\n',' ')
print(searchDate(string))



