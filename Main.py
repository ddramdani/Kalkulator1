# Latihan

# Kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=")

angka_1 = float(input("Masukan angka 1 = "))
operator = input("Operator (+,-,x,/) : ")
angka_2 = float(input("Masukan angka 2 = ")) 

# percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print(f"masukan operator yang benar")

print("Akhir dari program")
