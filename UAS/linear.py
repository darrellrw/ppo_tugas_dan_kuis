from tabulate import tabulate

#Fungsi Z
def z(x1, x2):
    return 20000 * x1 + 30000 * x2

def fb1(x1, x2):
    return 500 * x1 <= 10000

def fb2(x1, x2):
    return 400 * x2 <= 7500

def fb3(x1, x2):
    return 100 * x1 + 60 * x2 <= 3000

def fb4(x1, x2):
    return 20 * x1 + 25 * x2<= 1000

class Simplex: #Kelas Metode Simplex
    #Inisiasi tabel
    def __init__(self, z, slack, rhs):
        self.tab = []
        self.z = z
        self.slack = slack
        self.rhs = rhs

        self.rk = 0
        self.ck = 0

        self.headers = ["z"]
        for i in range(len(self.z)):
            self.headers.append(f"x{i + 1}")
        for j in range(len(self.slack)):
            self.headers.append(f"s{j + 1}")
        self.headers.append("rhs")
        self.headers.append("ratio")

        self.ratio = 0
        self.pivot = 0

        self.x1 = 0
        self.x2 = 0

    #Menampilkan tabel
    def showTable(self):
        print(tabulate(self.tab, self.headers, tablefmt="grid"))

    #Menentukan nilai awal pada tabel (Kanonik)
    def initTableu(self):
        if(len(self.tab) == 0):
            tab0 = []
            tab0.append(1)
            for j in range(len(self.z)):
                tab0.append(-1 * self.z[j])
            for k in range(len(self.slack) + 2):
                tab0.append(0)
            self.tab.append(tab0)
            for i in range(len(self.slack)):
                tabx = []
                tabx.append(0)
                for f in range(len(self.z)):
                    tabx.append(self.slack[i][f])
                for h in range(len(self.slack)):
                    tabx.append(0)
                tabx.append(self.rhs[i])
                tabx.append(0)
                self.tab.append(tabx)
                self.tab[i + 1][len(self.z) + 1 + i] = 1

    #Mencari Kunci Kolom berdasarkan nilai yang paling negatif
    def columnKey(self):
        xTab = []
        mint = []
        columnK = 0
        for ma in self.tab:
            mint.clear()
            for mj in ma[:3]:
                mint.append(mj)
            xTab.append(min(mint))
        for i in range(len(self.tab)):
            if(min(xTab) in self.tab[i][:3]):
                columnK = self.tab[i].index(min(xTab)) #Operasi untuk mencari nilai paling negatif
        self.ck = columnK

    #Mencari Kunci Baris berdasarkan ratio terkecil
    def rowKey(self):
        cTab = []
        for i in range(len(self.slack)):
            if(self.tab[i + 1][self.ck] == 0):
                ratio = 0
            else:
                ratio = self.tab[i + 1][-2] / self.tab[i + 1][self.ck] #Operasi untuk mencari ratio
            self.tab[i + 1][-1] = ratio
            cTab.append(ratio)
        self.ratio = min(x for x in cTab if x != 0)
        self.rk = cTab.index(self.ratio) + 1 #Operasi untuk mencari kunci baris

    #Menghitung Operasi Baris Dasar
    def obd(self):
        pivot = self.tab[self.rk][self.ck] #Menentukan Pivot
        self.pivot = pivot
        for i in range(len(self.tab[self.rk]) - 1): #Perulangan untuk Kunci Baris
            self.tab[self.rk][i] = self.tab[self.rk][i] / pivot #Nilai pada Baris Kunci dibagi dengan pivot untuk mendapat nilai 1
        for j in range(len(self.tab) - 1): #Perulangan untuk baris lainnya
            oper = self.tab[self.rk - j - 1][self.ck] #Operasi pembentuk nol
            print(f"\tb{self.tab.index(self.tab[self.rk - j - 1]) + 1} - ({oper} * b{self.rk + 1})")
            for k in range(len(self.tab[self.rk]) - 1): #Perulangan untuk setiap nilai pada baris
                self.tab[self.rk - j - 1][k] = self.tab[self.rk - j - 1][k] - (oper * self.tab[self.rk][k]) #Operasi Baris Dasar
        for i in range(len(self.slack)): #Perulangan untuk membuat nol ratio
            self.tab[i + 1][-1] = 0

    #Mengecek apakah nilai tidak negatif untuk baris pertama
    def check(self):
        for row in self.tab[0]:
            if(row < 0):
                return True
        return False

    #Fungsi untuk menjalankan Metode Simplex
    def run(self):
        print("Program Linear Kelompok 2")
        print("Metode Simplex")

        i = 1
        while(True): #Jika nilai tidak negatif untuk baris Z maka perulangan akan berhenti
            print(f"\nTableau {i}")
            self.initTableu()
            self.showTable()
            self.columnKey()
            self.rowKey()
            print(f"\nKolom Kunci: Kolom-{self.ck + 1}")
            print(f"Baris Kunci: Baris-{self.rk + 1}, Ratio Terkecil: {self.ratio}")
            self.showTable()
            print("\nOperasi Baris Dasar:")
            self.obd()
            print(f"Pivot: {self.pivot}")
            self.showTable()

            if(self.check() == False):
                break

            i += 1

        for i in range(len(self.tab)):
            if(self.tab[i][1] == 1):
                self.x1 = self.tab[i][7] #Mengambil nilai x1
            elif(self.tab[i][2] == 1):
                self.x2 = self.tab[i][7] #Mengambil nilai x2

        print(f"\nJadi, nilai x1 = {self.x1} dan x2 = {self.x2}.")
        print(f"Maka nilai maksimum z adalah {self.tab[0][-2]}")
        print("Pembuktian:")
        print(f"\tFungsi Batas 1 = {fb1(self.x1, self.x2)}")
        print(f"\tFungsi Batas 2 = {fb2(self.x1, self.x2)}")
        print(f"\tFungsi Batas 3 = {fb3(self.x1, self.x2)}")
        print(f"\tFungsi Batas 4 = {fb4(self.x1, self.x2)}")
        print(f"\tz({self.x1}, {self.x2}) = {z(self.x1, self.x2)}")

pp = Simplex([20000, 30000], [[500, 0], [0, 400], [100, 60], [20, 25]], [10000, 7500, 3000, 1000])
pp.run()