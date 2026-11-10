# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:11:58 2026

@author: PC123
"""

print("maedeh")










a = "maedeh a "
print(a)
x=5
z=5
print(x*z)
x=4
z=5
print(x/z)
print(type(x))
b = 3.14
print(type(b))
"""
n=input("لطفا نام خود را وارد کنید")
print(n)



f=input("لطفا فامیلی خود را بنویسد")

print(f)



n=int(input("لطفا عدد رو وارد کن"))
n2=int(input("لطفا عدد رو وارد کن"))

print(n+n2)
print(n*n2)
print(n/n2)






name ="maedeh"
print(name)
print(len(name))
print(name[0])
print(name[4])
print(name[3])
print(name[1:3])
n="123456789"
print(n[1:6:2])
print(n[1:7])
print(n[-1: ])

name="fati"
print(name[1:3])


print(name.upper())
n2 ="FATI"
print(n2.lower())
name=input("لطفانام خود را وارد کنید")
print(name.upper())
print(name.capitalize())



n1 =1.8
print(type(n1))
num1 = float((input("لطفا عدد خود راوارد کنید")))
num2= int(input("لطفا عدد خود راوارد کنید"))

print(num1+num2)





new_list = [1, 5, 5]

print(new_list[2])



print(len(new_list))

new_list.append(7)
print(new_list)
new_list.append(9)
print(new_list)
new_list.clear()
print(new_list)
new_list.append(777)
print(new_list)

print(new_list[0])
a = 5
print(type(a))



pasta = 100
p = 7
n = 6
t = 8
hk=  (pasta*p)+ (n*t)
print(hk)
dog =(hk/4)
print(dog)
p =3.14
print(type(p))
m ="3.14"
print(type(m))
name ="maedeh"
print(name)
print(len(name))
print("maedeh"*3)
print("maededh"/3)

name =["maedeh","semaneh","mohsen"]
name.remove("mohsen")
print(name)
my_list =["maedeh","yaseman","neda","mohsen"]
print("neda" in my_list)
my_list =["maedeh","neda","mohsen","raha"]
my_list[3] = "ali"
print(my_list)
my_list2 =[12,38,98,67,43]
my_list2.sort()
print(my_list2)

name3 = "maedeh"
last_name ="fati"
age = 18
print(f"{name3}{last_name}{age}")
my_list =[1,2,4,7]
print(my_list)
print(len(my_list))
my_list = {1,"mohsen", "ali",2}
print(type(my_list))
print(my_list)
my_list.add("narges")
print(my_list)
#اضافه کردن با اد هست داخل لیست ولی واسه یکی دیگه با اپند
#ریمو ینی حذف کردن ولی پاپ برمیداره
my_list1 ={1,2,3,4}
my_list2 ={1,6,5,9}
print(my_list1.union(my_list2))
print(my_list1.intersection(my_list2))
#یونیون اجتماع دوتارو میده 
#این فلان اشتراکشو نشون میده
#دیفرنس تفاظل

print(my_list1-my_list2)
print(my_list1.difference(my_list2))
#این دوتا هیچ فرقی باهم ندارن ولی منها اسون تره

my_set1 ={1,2,3,4}
my_set2 ={5,6,7,8}               
print(my_list1)
print(type(my_list1))
my_set1.add(8)
print(my_set1)
print(my_set1.difference(my_set2))
print(my_set2.difference(my_set1))
print(my_set1.intersection(my_set2))
#چک کردن با این انجام میشه
print(my_set1-my_set2)
#لن ینی طول
#با دستور اد نمیشه چند تا اضافه کرد
#چند تا عنصر بخای از اد استفاد نمکنیم
#چند تا عنصر بخایم اضافه کنیم از اپدیت استفاده میکنیم
my_set1.update({"mohsen","mohmad"})
print(my_set1)
my_set1.remove("mohmad")
print(my_set1)
#ریمو ینی حذف کردن
#اگر سارا میزدیم ک داخل ست نبود ارور میداد میگف پیداش نکردیم
#کلیر پاک میکنیم
#فلوت ینی اعداد اعشار
#تاپل مث لیست هس اصلا هم نمیشه عوضش کرد و با پرانتز نشونش میدن
#تاپل جدید اسما با و جابجا میشن

my_tuple =(1,2,3,"ali")
print(type(my_tuple))

a = (10,)
print(type(10))
#و رو بزاریم تشخیص میده تاپل هس تک عضویی بنویسیم و میزاریم
print(len(my_tuple))
print(my_tuple[3])
print(my_tuple[0:2])
#ست ها این دگس ندارن
my_tuple1 = ("mashad","kreman","shiraz")
print(type(my_tuple1))
print("mashad" in my_tuple1)
# این  واسه چک کردن چیزی هست یا نه.

kmwoo = list(my_tuple)
print( mwoo)

mwoo.append(5)

print(mwoo)
m =tuple(mwoo)
print(m)
"""
person =("maedae",19,"kerman")
name, age, city = person
print(name)
print(age)
print(city)
scores = (18,16,20,14,17)
total = sum(scores)
average = total / len(scores)
print("total:", total)
print("average:", average)
max1 = max(scores)
min1 = min(scores)
#ماکسیمو زیادتری مینیمور کمتری
#کری برای لیست کرلی براکت واسه تاپل
#دیکشنلی
#عدد یا استرینگ
nomre ={"riazi" : 18," adebiat":20,"progeram ":20}
print(nomre["riazi"])
print(type(nomre))
print(len(nomre))
#تایپ ینی میگه کلاسش از نوع فلانه
#ریاضی کیلده ک باید یک مقدار بهش میدیم


nomre2 ={

 "maedeh":{
          "adebiat": 18,
          "riazi": 19},

 
          "neda":{
    "adebiat":18,
    "reazi":18}
    
    }
        
         
print(nomre2["maedeh"]["riazi"])
print(nomre2["neda"]["adebiat"])
print(nomre2.keys())
print(nomre2.values())
print(nomre2.items())
#کلید اسم خودش میاره ولیو کلا ایتم کلش






















