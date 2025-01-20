##Gorev1
from iremproje import student

x = 8
type(x) #integer

y = 3.2
type(y) #float

z = 8j + 18
type(z) #complex

a = "Hello World"
type(a) #string

b = True
type(b) #boolean, bool

c = 23 < 22
type(c) #boolean, bool

l = [1,2,3,4]
type(l) #list

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d) #dict

t= ("Machine Learning", "Data Science")
type(t) #tuple

s= {"Python","Machine Learning","Data Science"}
type(s) #set

#Gorev2

text = "The goal is to turn data into information, and information into insight"

def text_upper(text):
    for string in text:
       print(text.upper().split())
text_upper(text)

#gorev3
lst = ["D", "A", "T", "A", "S", "C", "İ", "E", "N", "C", "E"]
len(lst) #eleman sayısı 11
lst.pop(8) #8. index silinir
print(lst)
list(lst[:4]) # yeni liste oluşur
lst.append("F")
print(lst) # eleman ekler
lst.insert(8,"N")
print(lst) #N elemanını tekrar ekler

#gorev4

dict = {"Cristian": ["America", 18],
        "Daisy":["England",12],
        "Antonio" : ["Spain", 22],
        "Dante":["İtaly",25]}
print(dict.keys()) #key değerlerine ulaşma
print(dict.values()) #value değerlerine ulaşma
dict["Daisy"] = ["England",13]
print(dict) #update ile de yapılabilir
dict.pop("Antonio")
print(dict) #Antonio'yu silme
dict["Ahmet"] = ["Turkey",24]
print(dict) #değer ekleme

#gorev5

l = [2,13,18,93,22]
even_list = []
odd_list = []
def function(l):
    for number in l:
        if number % 2 == 0:
            odd_list.append(number)
        else:
            even_list.append(number)
    return even_list, odd_list
even_list , odd_list = function(l)
print(even_list,odd_list)


#gorev6
ogrenciler = ["Ali", "Veli","Ayşe","Talat","Zeynep","Ece"]
print("Mühendislik ")
[o for i, o in enumerate (ogrenciler[1:3])]
print(f"Tıp")
[print(o) for i, o in enumerate(ogrenciler[3:],1)]



#gorev7
ders_kodu = ["CMP1005", "PYS1001", "HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]
for k,c,s in zip(kredi,ders_kodu,kontenjan):
    print(k,c,s)



#gorev8

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def setler_kesişim(k1,k2):

    if kume1.issubset(kume2):
       print(kume1.issubset(kume2))

    else:
        kume1.difference(kume2)
        print(kume1.intersection(kume2))
setler_kesişim(kume1,kume2)

##
def kume_islemi(kume1, kume2):
    if kume1.issubset(kume2):  # 1. küme, 2. kümenin alt kümesi ise
        ortak_elemanlar = kume1 & kume2  # Ortak elemanları al
        print("Ortak Elemanlar:", ortak_elemanlar)
    else:  # 1. küme, 2. kümeyi kapsamıyorsa
        fark = kume2 - kume1  # 2. kümenin 1. kümeden farkı
        print("2. Kümenin 1. Kümeden Farkı:", fark)
kume_islemi(kume1,kume2)




