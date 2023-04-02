import matplotlib.pyplot as plt
import numpy as np

# Definisi fungsi keanggotaan

def linear_up(a, b, x):
    if x <= a:
        return 0
    elif x >= b:
        return 1
    else:
        return (x - a) / (b - a)

def linear_down(a, b, x):
    if x <= a:
        return 1
    elif x >= b:
        return 0
    else:
        return (b - x) / (b - a)

def segitiga(a, b, c, x):
    if x <= a or x >= c:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return (c - x) / (c - b)

def trapesium(a, b, c, d, x):
    if x <= a or x >= d:
        return 0
    elif b <= x <= c:
        return 1
    elif a <= x <= b:
        return (x - a) / (b - a)
    elif c <= x <= d:
        return (d - x) / (d - c)

def sigmoid(a, b, c, x):
    return 1 / (1 + np.exp(-a * (x - c)))**b

def gauss(a, c, s, x):
    return np.exp(-a * (x - c)**2 / s**2)

def beta(a, b, c, d, x):
    return (x - a) / (b - a) if a <= x <= b else (d - x) / (d - c)

# Menampilkan menu

while True:
    print("====================================")
    print("PROGRAM MENGHITUNG FUNGSI KEANGGOTAAN")
    print("      WAHYUDI MALIHI_E1E120099      ")
    print("====================================")
    print("1. Linear naik")
    print("2. Linear turun")
    print("3. Segitiga")
    print("4. Trapesium")
    print("5. Sigmoid")
    print("6. Gauss")
    print("7. Beta")
    print("8. Keluar")

    choice = input("Pilih fungsi keanggotaan: ")

    if choice == "1":
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        x = np.linspace(a - 1, b + 1, 100)
        y = [linear_up(a, b, xi) for xi in x]
        plt.plot(x, y)
        plt.title(f"Fungsi Keanggotaan Linear Naik (a={a}, b={b})")
        plt.show()
    elif choice == "2":
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        x = np.linspace(a - 1, b + 1, 100)
        y = [linear_down(a, b, xi) for xi in x]
        plt.plot(x, y)
        plt.title(f"Fungsi Keanggotaan Linear Turun (a={a}, b={b})")
        plt.show()
    elif choice == "3":
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = float(input("Masukkan nilai c: "))
        x = np.linspace(a - 1, c + 1, 100)
        y = [segitiga(a, b, c, xi) for xi in x]
        plt.plot(x, y)
        plt.title(f"Fungsi Keanggotaan Segitiga (a={a}, b={b}, c={c})")
        plt.show()
    elif choice == "4":
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = float(input("Masukkan nilai c: "))
        d = float(input("Masukkan nilai d: "))
        x = np.linspace(a - 1, d + 1, 100)
        y = [trapesium(a, b, c, d, xi) for xi in x]
        plt.plot(x, y)
        plt.title(f"Fungsi Keanggotaan Trapesium (a={a}, b={b}, c={c}, d={d})")
        plt.show()
    elif choice == "5":
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = float(input("Masukkan nilai c: "))
        x = np.linspace(c - 5, c + 5, 100)
        y = [sigmoid(a, b, c, xi) for xi in x]
        plt.plot(x, y)
        plt.title(f"Fungsi Keanggotaan Sigmoid (a={a}, b={b}, c={c})")
        plt.show()
    elif choice == "6":
        a = float(input("Masukkan nilai a: "))
        c = float(input("Masukkan nilai c: "))
        s = float(input("Masukkan nilai s: "))
        x = np.linspace(c - 5 * s, c + 5 * s, 100)
        y = [gauss(a, c, s, xi) for xi in x]
        plt.plot(x, y)
        plt.title(f"Fungsi Keanggotaan Gauss (a={a}, c={c}, s={s})")
        plt.show()
    elif choice == "7":
       a = float(input("Masukkan nilai a: "))
       b = float(input("Masukkan nilai b: "))
       c = float(input("Masukkan nilai c: "))
       d = float(input("Masukkan nilai d: "))
       x = np.linspace(a - 1, d + 1, 100)
       y = [beta(a, b, c, d, xi) for xi in x]
       plt.plot(x, y)
       plt.title(f"Fungsi Keanggotaan Beta (a={a}, b={b}, c={c}, d={d})")
       plt.show()
    elif choice == "8":
      print(" Program selesai, terima kasih :)")
      print("  By : Wahyudi Malihi_E1E120099 ")
      break
    else:
       print("Pilihan tidak valid")

