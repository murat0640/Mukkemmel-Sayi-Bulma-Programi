print("""" 
Mukkemmel Sayi Bulma Programina Hosgeldiniz
""")

x = int(input("Sorgulamak istediginiz sayiyi giriniz:"))
y=0
for i in range(1,x):
    if (x%i)==0:
      y+=i
if y==x:
    print("Girdiginiz {} sayisi mukkemmel.".format(x))
else:
    print("Girdiginiz {} sayisi mukkemmel degil.".format(x))
