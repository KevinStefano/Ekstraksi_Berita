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


key = "ababababca"
print(len(key))
print(tabelBorder(key))

print(KMP("abacab","abacaabaccabacab"))


