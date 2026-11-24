class Argentina:
    pass

class Pemain:
    pass

Goat = Argentina()
Lionel_Messi= Pemain()

print(type (Goat))
print(type (Lionel_Messi))

Lionel_Scaloni = Argentina()
Thiago_Messi = Pemain()

print(type (Lionel_Scaloni))
print(type (Thiago_Messi))

Lionel_Scaloni = Argentina()
Lionel_Scaloni.nomor_punggung = 18
Lionel_Scaloni.tempat_kelahiran = "Pujato"

print(Lionel_Scaloni.nomor_punggung)
print(Lionel_Scaloni.tempat_kelahiran)

Thiago_Messi = Pemain()
Thiago_Messi.nomor_punggung = 10
Thiago_Messi.tempat_kelahiran =  "Barcelona"

print(Thiago_Messi.nomor_punggung)
print(Thiago_Messi.tempat_kelahiran)

