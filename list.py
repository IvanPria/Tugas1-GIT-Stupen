# loop
print("pakai for loop")
kumpulanAngka = [4,6,1,7,2,3]

for a in kumpulanAngka:
    print(f"angka: {a}")


# for loop dan range
print("\npakai for loop dan range")
kumpulanAngka = [4,6,1,7,2,3]

panjang = len(kumpulanAngka)
for i in range(panjang):
    print(f"angka: {kumpulanAngka[i]}")


# While
print("\nPakai While")
kumpulanAngka = [4,6,1,7,2,3]

panjang = len(kumpulanAngka)
i = 0
while i < panjang:
    print(f"angka: {kumpulanAngka[i]}")
    i += 1


# List Comprehension
print("\nList Comprehension")
data = ("ucup",1,2,3,"otong")
[print(f"data: {i}") for i in data]

angka = [10,5,4,2,8]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)


# Enumerate
print("\nEnumerate")
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index: {index},data: {data_list}")
    