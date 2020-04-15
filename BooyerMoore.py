def tabelLo(keyword): #kalau
    tabel = {}
    i= 0;
    while i<len(keyword):
        tabel[keyword[i:i+1]] = i
        i = i+1
    return tabel

def BooyerMoore(keyword, text):
    found =0
    tabel_lo = tabelLo(keyword)
    idx_text = len(keyword)-1
    idx_keyword = len(keyword)-1
    while idx_text <= len(text):
        if text[idx_text:idx_text+1] not in tabel_lo:
            tabel_lo[text[idx_text:idx_text+1]] = -1
        if (keyword[idx_keyword:idx_keyword+1]==text[idx_text:idx_text+1]):
            if (idx_keyword!=0):
                idx_keyword -=1
                idx_text -=1
            else:
                found =1
                break
        elif idx_text< tabel_lo[text[idx_text:idx_text+1]]:
            idx_text = idx_text+len(keyword) - (tabel_lo[text[idx_text:idx_text+1]]+1)
            idx_keyword = len(keyword)-1
        else:
            idx_text = idx_text + len(keyword) - idx_keyword
            idx_keyword = len(keyword)-1
    return found

#print(BooyerMoore('abacab','abacaabadcabacabaabb'))
