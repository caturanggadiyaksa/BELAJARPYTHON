def TulisKata(string) :
    for character in string :
        print("daftar huruf" + character)
        print("'" + character + "'")
def HurufTengah(string) :
    print ("karakter di tengah adalah:", string[len(string) // 2])

TulisKata("catur")
HurufTengah("anggacaturadiyaksa")
