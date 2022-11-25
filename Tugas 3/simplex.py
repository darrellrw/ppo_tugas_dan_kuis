from tabulate import tabulate
import sympy as sp

#Fungsi Z
def z(x1, x2):
    return 8 * x1 + 6 * x2

#Fungsi Batas 1
def fb1(x1, x2):
    return 4 * x1 + 2 * x2 <= 60

#Fungsi Batas 2
def fb2(x1, x2):
    return 2 * x1 + 4 * x2 >= 48

class Simplex: #Kelas Metode Simplex
    #Inisiasi tabel
    def __init__(self):
        self.M = sp.symbols("M")
        self.tab = [
            ["Z", 1, -8, -6, 0, 0, self.M, 0, 0],
            ["S1", 0, 4, 2, 1, 0, 0, 60, 0],
            ["Y1", 0, 2, 4, 0, -1, 1, 48, 0]
        ]
        self.headers = ["Basic", "Z", "x1", "x2", "S1", "S2", "Y1", "RHS", "Ratio"]

        self.rk = 0
        self.ck = 0

        self.x1 = 0
        self.x2 = 0

    #Menampilkan tabel untuk tableau
    def showTable(self):
        print(tabulate(self.tab, self.headers, tablefmt="grid"))

    #Membuat Baris Z Konsisten dengan Baris yang lain
    def initTableau(self):
        for i in range(len(self.tab[0][1:])):
            self.tab[0][i + 1] = self.tab[0][i + 1] - self.M * self.tab[2][i + 1]
        self.ck = 3

    #Mencari Kunci Kolom berdasarkan nilai yang paling negatif (yang paling kecil bukan nol)
    def columnKey(self):
        xTab = []
        minTab = []
        columnK = 0
        for ma in self.tab:
            minTab.clear()
            for f in range(5):
                minTab.append(ma[f + 1])
            xTab.append(min(x for x in minTab if x != 0))
        for i in range(len(self.tab)):
            if(min(xTab) in self.tab[i]):
                columnK = self.tab[i].index(min(xTab)) #Operasi untuk mencari nilai paling negatif (yang paling kecil bukan nol)
        self.ck = columnK

    #Mencari Kunci Baris berdasarkan ratio terkecil
    def rowKey(self):
        cTab = []
        for i in range(2):
            ratio = self.tab[i + 1][-2] / self.tab[i + 1][self.ck] #Operasi untuk mencari ratio
            self.tab[i + 1][-1] = ratio
            cTab.append(ratio)
        self.ratio = min(cTab)
        self.rk = cTab.index(min(i for i in cTab if i > 0)) + 1 #Operasi untuk mencari kunci baris

    #Menghitung Operasi Baris Dasar
    def obd(self):
        pivot = self.tab[self.rk][self.ck] #Menentukan Pivot
        self.pivot = pivot
        for i in range(len(self.tab[self.rk]) - 2): #Perulangan untuk Kunci Baris
            self.tab[self.rk][i + 1] = self.tab[self.rk][i + 1] / pivot #Nilai pada Baris Kunci dibagi dengan pivot untuk mendapatkan nilai 1
        if(2 <= self.ck <= 3):
            self.tab[self.rk][0] = f"x{self.rk}"
        elif(4 <= self.ck <= 5):
            self.tab[self.rk][0] = f"S{self.rk + 1}"
        for j in range(2): #Perulangan untuk baris lainnya
            oper = self.tab[self.rk - j - 1][self.ck] #Operasi penentu pembentuk nol
            print(f"b{self.tab.index(self.tab[self.rk - j - 1])} - ({oper} * b{self.rk})")
            for k in range(len(self.tab[self.rk]) - 2): #Perulangan untuk setiap nilai pada baris
                self.tab[self.rk - j - 1][k + 1] = self.tab[self.rk - j - 1][k + 1] - (oper * self.tab[self.rk][k + 1]) #Operasi Baris Dasar
        for i in range(2): #Perulangan untuk membuat nol ratio
            self.tab[i + 1][-1] = 0

    #Mengecek apakah nilai tidak negatif untuk kolom Z
    def check(self):
        for num in range(5):
            if(self.tab[0][num] < 0):
                return False
        return True

    #Menjalankan operasi metode simplex
    def run(self):
        print("Metode Simplex")
        print("\nTableau 1")
        self.showTable()
        self.initTableau()
        print("\nMembuat Baris Z Konsisten dengan Baris yang lain")
        self.showTable()
        self.rowKey()
        print("\nMencari Ratio")
        self.showTable()
        self.obd()
        print("\nMelakukan Operasi Baris Dasar")
        self.showTable()

        iter = 2
        while True: #Jika nilai tidak negatif untuk kolom Z maka perulangan akan berhenti
            print(f"\nTableau {iter}")
            self.columnKey()
            self.rowKey()
            self.showTable()
            print("\nMelakukan Operasi Baris Dasar")
            self.obd()
            self.showTable()
            if(self.check()):
                break
            iter += 1

        for i in range(len(self.tab)):
            if(self.tab[i][0] == "x1"):
                self.x1 = self.tab[i][7] #Mengambil nilai x1
            elif(self.tab[i][0] == "x2"):
                self.x2 = self.tab[i][7] #Mengambil nilai x2

        print(f"Jadi, nilai x1 = {self.x1} dan x2 = {self.x2}.")
        print(f"Maka nilai maksimum z adalah {self.tab[0][-2]}")
        print("Pembuktian:")
        print(f"\tfb1({self.x1}, {self.x2}) = {fb1(self.x1, self.x2)}")
        print(f"\tfb2({self.x1}, {self.x2}) = {fb2(self.x1, self.x2)}")
        print(f"\tz({self.x1}, {self.x2}) = {z(self.x1, self.x2)}")

pp = Simplex()
pp.run()