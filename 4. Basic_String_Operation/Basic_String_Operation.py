# Mencari Banyaknya Karakter
# Printout 11
helloworld = "Hello World"
print("Banyaknya Jumlah Karakter : ")
print(len(helloworld))

# Mencari Index ke Variabel helloworld
# Printout 10
print(helloworld.index("d"))

# Mencari Banyaknya Karakter Secara Spesifik
# Printout 2
print(helloworld.count("o"))

# Mencari Karakter dari Index ke Index
# Printout lo Wo
print(helloworld[3:8])
# [start:stop:step]
print(helloworld[3:7:2])

# Reverse/Membalik String
# Printout dlroW olleH
print(helloworld[::-1])

# Print Berdasarkan Lowercase & Uppercase
# Printout hello world
# Printout HELLO WORLD
print(helloworld.lower())
print(helloworld.upper())

# Boolean dengan Dimulai dari
# Printout True/False
print(helloworld.startswith("Hello")) # Benar
print(helloworld.startswith("Aku Ganteng")) # Salah

# Splitting
# Printout ['Hello', 'World']
print(helloworld.split(" "))