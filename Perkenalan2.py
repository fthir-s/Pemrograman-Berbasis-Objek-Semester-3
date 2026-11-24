class Teman:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}")

    def hallo(self, nama):
        print(f"Hallo {nama}, nama saya {self.nama}")


teman1 = Teman()
teman1.nama = "Fathir"

teman2 = Teman()
teman2.nama = "Jems"


print("=== PERKENALAN ===")
teman1.perkenalan()
teman2.perkenalan()


print("\n=== PERCAKAPAN FATHIR DAN JEMS ===")
teman1.hallo("Jems")
teman2.hallo("Fathir")


print("\n=== TRUK DI BOJONEGARA ===")
print(f"{teman1.nama}: Jems, kamu tahu nggak soal truk yang lewat di Bojonegara?")
print(f"{teman2.nama}: Tahu, Fathir. Memangnya ada apa?")
print(f"{teman1.nama}: Saya lihat masih banyak truk yang lewat tidak sesuai jam operasionalnya.")
print(f"{teman2.nama}: Iya, saya juga sering lihat. Padahal sudah ada aturan jam lewatnya.")
print(f"{teman1.nama}: Apalagi kalau truk lewat pagi hari, jalan jadi macet.")
print(f"{teman2.nama}: Betul, aktivitas masyarakat juga jadi terganggu.")
print(f"{teman1.nama}: Menurut kamu, kenapa truk-truk itu masih lewat di luar jam yang ditentukan?")
print(f"{teman2.nama}: Mungkin pengawasannya masih kurang ketat.")
print(f"{teman1.nama}: Seharusnya ada petugas yang mengawasi supaya aturan dipatuhi.")
print(f"{teman2.nama}: Iya, perusahaan truk juga harus ikut bertanggung jawab.")
print(f"{teman1.nama}: Semoga masalah ini cepat diselesaikan.")
print(f"{teman2.nama}: Amin, supaya jalan di Bojonegara lebih tertib dan nggak macet lagi.")