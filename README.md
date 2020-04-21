# Ekstraksi_Berita

## Oleh
Kevin Austin Stefano
13518104

## Deskripsi
Aplkasi berbasis web yang mampu melakukan ekstraksi berita melalui algoritma pencocokkan String KMP, Boyer Moore, dan Regex. Langkah proses mengerjakannya Pertama, exact match dengan keyword yang diberikan pengguna untuk memfilter kalimat yang akan diproses informasinya. Semua teknik (KMP, BM, dan regex) bisa digunakan untuk fitur ini. Kedua, ekstraksi jumlah dan waktu dari kalimat hasil exact match dengan menggunakan regex. 

## Prerequisite
Python 3
Flask ( pip install flask)

## How to Use
WINDOWS (recommended)
     1.  Go to test Folder "src"
     2.  Open command prompt in "src" folder
     3.  set FLASK_APP=Web.py    (case sensitive ....)
     4.  flask run
     5.  copy link http (example : http://127.0.0.1:5000/)
     6.  paste in browser
     7.  klik "refresh" icon + SHIFT if web or background do not load in link

LINUX
     1.  Go to test Folder "src"
     2.  Open terminal in "src" folder
     3.  export FLASK_APP=Web.py
     4.  flask run
     5.  copy link http (example : http://127.0.0.1:5000/)
     6.  paste in browser
