# List -> Array(like c prog. Lang.)

List1 = ['Boz Gandalf', 2, True]
for i in List1:
    print(i)

# [:] şekline yaparsam dizinin bir kopyasını oluşturur mevcut dizi korunur
new_list2 = List1[:]
new_list2[0] = 'Sam'
for a in List1:
    print(a)
# Direkt yeni bir değişkene atama yaparsam mevcut dizi artık yeni değişken olur.
new_list1 = List1
new_list1[0] = 'Ak Gandalf'
for b in new_list1:
    print(b)

#adding
List1.append(63)
# List1_add= List1.append(63) yapsaydım  List1_add bana non döndürecekti
List1_add= List1
print(List1_add)
#insert -> istediğimiz index değerine ekleme yapabiliyoruz
List1.insert(1,34)
print(List1)

#removing
List1.pop()
# pop sondaki değeri siler pop(i) de i indexindeki değeri siler
# remove(x) x'i Listeden siler
# clear her şeyi siler
print(List1)
List1.remove(True)
print(List1)

print("Burda Kaldım")