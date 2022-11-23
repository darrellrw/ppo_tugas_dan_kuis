from tabulate import tabulate

#Fungsi Z
def z(x1, x2):
    return 8 * x1 + 6 * x2

#Fungsi Batas 1
def fb1(x1, x2):
    return 4 * x1 + 2 * x2 <= 60

#Fungsi Batas 2
def fb2(x1, x2):
    return 2 * x1 + 4 * x2 >= 48

class Simplex:
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
        for j in range(len(self.z)):
            self.headers.append(f"s{j + 1}")
        self.headers.append("rhs")
        self.headers.append("ratio")

        self.ratio = 0
        self.pivot = 0

    #Menampilkan Tabel
    def showTable(self):
        print(tabulate(self.tab, self.headers, tablefmt="grid"))

    #Menentukan nilai awal pada tabel (Kanonik)
    def initTableu(self):
        if(len(self.tab) == 0):
            tab0 = []
            tab0.append(1)
            for j in range(len(self.z)):
                tab0.append(-1 * self.z[j])
            for k in range(len(self.z)):
                tab0.append(0)
            tab0.append(0)
            tab0.append(0)
            self.tab.append(tab0)
            for i in range(len(self.slack)):
                tabx = []
                tabx.append(0)
                for f in range(len(self.z)):
                    tabx.append(self.slack[i][f])
                for h in range(len(self.z)):
                    tabx.append(0)
                tabx.append(self.rhs[i])
                tabx.append(0)
                self.tab.append(tabx)
                self.tab[i + 1][len(self.z)+ 1 + i] = 1

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
            ratio = self.tab[i + 1][-2] / self.tab[i + 1][self.ck] #Operasi untuk mencari ratio
            self.tab[i + 1][-1] = ratio
            cTab.append(ratio)
        self.ratio = min(cTab)
        self.rk = cTab.index(min(cTab)) + 1 #Operasi untuk mencari kunci baris

    #Menghitung Operasi Baris Dasar
    def obd(self):
        pivot = self.tab[self.ck][self.rk] #Menentukan Pivot
        self.pivot = pivot
        for i in range(len(self.tab[self.ck]) - 1): #Perulangan untuk Kunci Baris
            self.tab[self.ck][i] = self.tab[self.ck][i] / pivot #Nilai pada Baris Kunci dibagi dengan pivot

        for j in range(len(self.tab) - 1): #Perulangan untuk baris lainnya
            oper = self.tab[self.ck - j - 1][self.rk] #Operasi pembentuk nol
            print(f"b{self.tab.index(self.tab[self.ck - j - 1])} - ({oper} * b{self.ck})")
            for k in range(len(self.tab[self.ck]) - 1): #Perulangan untuk setiap nilai pada baris
                self.tab[self.ck - j - 1][k] = self.tab[self.ck - j - 1][k] - (oper * self.tab[self.ck][k]) #Operasi Baris Dasar

        for i in range(len(self.slack)): #Perulangan untuk membuat nol ratio
            self.tab[i + 1][-1] = 0

    #Fungsi untuk menjalankan Metode Simplex
    def run(self):
        print("Tableau 1")
        self.initTableu()
        self.showTable()
        self.columnKey()
        self.rowKey()
        print(f"\nKolom Kunci: Kolom-{self.ck + 1}")
        print(f"Baris Kunci: Baris-{self.rk + 1}, Ratio Terkecil: {self.ratio}")
        self.showTable()
        print("\nOperasi Baris Dasar")
        self.obd()
        print(f"Pivot: {self.pivot}")
        self.showTable()

        print("\nTableau 2")
        self.showTable()
        self.columnKey()
        self.rowKey()
        print(f"\nKolom Kunci: Kolom-{self.ck + 1}")
        print(f"Baris Kunci: Baris-{self.rk + 1}, Ratio Terkecil: {self.ratio}")
        self.showTable()
        print("\nOperasi Baris Dasar")
        self.obd()
        print(f"Pivot: {self.pivot}")
        self.showTable()

        print("\nTableau 3")
        self.showTable()

        print(f"Jadi, nilai x1 = {self.tab[1][-2]} dan x2 = {self.tab[2][-2]}.")
        print(f"Maka nilai maksimum z adalah {self.tab[0][-2]}")
        print("Pembuktian:")
        print(f"    fb1({self.tab[1][-2]}, {self.tab[2][-2]}) = {fb1(self.tab[1][-2], self.tab[2][-2])}")
        print(f"    fb2({self.tab[1][-2]}, {self.tab[2][-2]}) = {fb2(self.tab[1][-2], self.tab[2][-2])}")
        print(f"    z({self.tab[1][-2]}, {self.tab[2][-2]}) = {z(self.tab[1][-2], self.tab[2][-2])}")

pp = Simplex([8, 6], [[4, 2], [2, 4]], [60, 48])
pp.run()