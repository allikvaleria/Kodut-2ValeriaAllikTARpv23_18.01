from base64 import b16decode
from datetime import *
from random import *
#8.2 Poes
arve_nr= date.today()#datetime.now()
print(arve_nr)
tsekk="arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
for toode in ["Piim","Leib","Komm"]:
    hind=randint(50,150)/100
    v=input("Toode:"+toode+" Hind:"+str(hind)+"nkas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("Mitu? "))
        tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
        summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
while True:
    raha=float(input("maksa "+str(summa)+"\n"))
    if raha==summa:
        print("tänan ostu eest!")
        break
    elif raha>summa:
        print("Tänan ostu eest! Tagasi "+str(raha-summa))
        break
    else:
        summa=raha
        print("Maksa veel"+str(summa-raha))

#8.1 Poes
arve_nr= date.today()#datetime.now()
print(arve_nr)
tsekk="arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

toode="Piim"
hind=randint(50,150)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+"nkas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
toode="Leib"
hind=randint(90,300)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+"nkas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
toode="Kommid"
hind=randint(600,1500)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+"nkas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
raha=float(input("maksa "+str(summa)))
if raha==summa:
    print("Tänan ostu eest!")
elif raha>summa:
    print("Tänan ostu eest! Tagasi "+str(raha-summa))
#1(JUKU)
#a
#nimi=input("Mis sinu eesnimi on?").capitalize()
#print("Tere",nimi)
#if nimi=="Juku":
#    print("lähme kinno")
#    vanus=int(input("Kui vana sa oled?"))
#    if vanus<0 or vanus>100:
#        vastus="viga andmetega"
#    elif 0<=vanus<6:
#        vastus="tasuta"
#    elif 6<=vanus<=14:
#        vastus="lastepilet"
#    elif 15<=vanus<65:
#        vastus="täispilet"
#    elif 65<=vanus<=100:
#        vastus="sooduspilet"
#    print(vastus)  #ilus vastust

#else:
#    print("ei lähe kinno")

#print()

#b
#from random import *
#vanus=randint(0,100)
#print(vanus, "Tere tulemast ja see on")
#if vanus<0 or vanus>100:
#    vastus="viga andmetega"
#elif 0<=vanus<6:
#    vastus="tasuta"
#elif 6<=vanus<=14:
#    vastus="lastepilet"
#elif 15<=vanus<65:
#    vastus="täispilet"
#else:
#    vastus="sooduspilet"
#print(vastus)
#print()



2
print("Sisestage oma nimed")
nimi1=input("1: ")
nimi2=input("2: ")

print(nimi1," ja ",nimi2," olete pinginabrid")


#ülesanne 3
a=float(input("milline on esimese seinapikkus?"))
b=float(input("milline on teise seinapikkus?"))
pindala=a*b
print("ruumi pindala on", pindala)
vastus=input("Kas tahate remondi teha? jah/ei: ")
if vastus=="jah":
     hind=float(input("Sisestage 1 meetri hind: "))
     remondiHind=pindala*hind
     print("Remondi hind on ",remondiHind)



 #ülesanne 4
hind=int(input("milline on hind?"))

if hind > 700:
     soodus=hind*0.3
     hindSoodustega=hind-soodus

     print("Hind soodustega on: ",hindSoodustega)


 #ülesanne 5
temp=int(input("Sisestage temperatuur: "))

if temp > 18:
    print("Temperatuur üle 18 kraadi")
else:
    print("Temperatuur vähem kui 18 kraadi")


 #ulesanne 6
pikkus=int(input("Sisestage oma pikkus sm: "))

if pikkus <=160:
    print("Te olete lühike")

elif pikkus >160 and pikkus <= 175:
    print("Te olete keskmine")

elif pikkus > 175:
    print("Te olete suur")

#ülesanne 7

pikkus=int(input("Sisestage oma pikkus sm: "))
sugu=input("Sisestage oma sugu, mees või naine: ")

if sugu=="naine":
        
    if pikkus <=160:
        print("Te olete väike")

    elif pikkus >160 and pikkus <= 175:
        print("Te olete keskmine", sugu)

    elif pikkus > 175:
        print("Te olete suur ",sugu)
elif sugu=="mees":
    if pikkus <=170:
        print("Te olete väike")

    elif pikkus >170 and pikkus <= 185:
        print("Te olete keskmine ",sugu)

    elif pikkus > 185:
        print("Te olete suur ",sugu)



#ülesanne 9
a=float(input("storona : "))
b=float(input("storona : "))
if a==b:
    print("kvadrat")
else :
    print("ne kvadrat")


#ülesanne 10
arv=float(input("vvesti lubuju tsivru : "))
arv1=float(input("vvesti lubuju tsivru : "))
operation=input("Mis tehet ta soovib jah , ei ? : ")
if operation=="jah" :
    vastus=input("Toimingu valimine (+ ; - ; * ; / ) : ")
    tulemus=arv+arv1
    print("slozenie : ")
    tulemus=arv-arv1
    print("vichitanie : ")
    tulemus=arv*arv1
    print("umnozenie : ")
    tulemus=arv/arv1
    print("delenie : ")
else: 
    print("viga")




#ülesanne 11
from datetime import *
from random import *
ta=date.today().year
sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: "))).year
if (ta-sp)%5==0:
    print("Juubel")
else:
    print("Tavaline sünnipäev")


#ülesanne 12
hind=float(input("Kakaja tsena? : "))
if hind<=10 :
    allahindlus=hind*0.1
    print("hind")
elif hind>=10 :
    allahindlus=hind*0.2
    print("hind")




#ülesanne 13
gender=input("Mis om sinu gender? (woman/male) : ")
if gender=="male" :
    vanus=int(input("Kui vana sa oled?"))
    if 16<vanus<=18 :
        print("Sa sobid hästi")
    else:
        print("Sa ei sobi hästi")




#ülesanne 14
maht=int(input("Buss maht: "))
i=int(input("Inimeste arv: "))
ba=round(i/maht) #2,3 -> 2
if i%maht!=0:
    ba+=1
vb=i%maht
print("Kokku on vaja {0} bussi ja viimasel sõidavad {1 inimest}".format(ba,vb))