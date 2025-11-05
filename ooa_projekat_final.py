import numpy as np
import random
import matplotlib.pyplot as plt

koordinate = np.loadtxt("_in263 (4).txt")
broj_gradova = len(koordinate)

def izracunaj_duzinu(putanja):
    tacke = koordinate[putanja]
    dx = tacke[1:,0] - tacke[:-1,0]
    dy = tacke[1:,1] - tacke[:-1,1]
    rastojanja = np.sqrt(dx**2+dy**2)
    return rastojanja.sum()

def napravi_izmenu(putanja):
    n = len(putanja)
    i, j = random.sample(range(n), 2)
    if i > j:
        i, j = j, i
    putanja[i:j+1] = reversed(putanja[i:j+1])
    return putanja

def simulirano_kaljenje_kumulativno(br_iter, T0, seed=None):
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    putanja = list(range(broj_gradova))
    random.shuffle(putanja)

    trenutna_duzina = izracunaj_duzinu(putanja)
    najbolja_duzina = trenutna_duzina
    najbolja_putanja = putanja[:]
    sve_duzine = []
    kumulativni_minimum = []

    for iteracija in range(br_iter):
        nova_putanja = napravi_izmenu(putanja[:])
        nova_duzina = izracunaj_duzinu(nova_putanja)
        razlika = nova_duzina - trenutna_duzina
        temperatura = T0 * (0.99995 ** iteracija)

        if razlika < 0 or random.random() < np.exp(-razlika / temperatura):
            putanja = nova_putanja
            trenutna_duzina = nova_duzina
            if trenutna_duzina < najbolja_duzina:
                najbolja_duzina = trenutna_duzina
                najbolja_putanja = putanja[:]

        sve_duzine.append(trenutna_duzina)
        kumulativni_minimum.append(najbolja_duzina)

    return kumulativni_minimum, sve_duzine, najbolja_putanja

def prosecan_kum_min(lista_minimuma, br_iter):
    matrica = np.zeros((len(lista_minimuma), br_iter))
    for i, niz in enumerate(lista_minimuma):
        duzina = len(niz)
        matrica[i, :duzina] = niz
        if duzina < br_iter:
            matrica[i, duzina:] = niz[-1]
    return np.mean(matrica, axis=0)

temperaturne_vrednosti = [100, 500, 1500]
boje = ['red', 'orange', 'blue']
br_iter = 500000
broj_pokretanja = 10

rezultati = {}  # (T0, seed) → (c_k, sve_duzine, putanja)
najbolja_duzina_globalno = float('inf')
najbolja_putanja_globalno = None

# Pokretanje SA algoritma i čuvanje rezultata
for T0 in temperaturne_vrednosti:
    for seed in range(broj_pokretanja):
        c_k, sve_duzine, putanja = simulirano_kaljenje_kumulativno(br_iter, T0, seed)
        rezultati[(T0, seed)] = (c_k, sve_duzine, putanja)
        print(f"[Kumulativni] T0={T0}, pokretanje={seed}, krajnja duzina={c_k[-1]:.2f}")
        if c_k[-1] < najbolja_duzina_globalno:
            najbolja_duzina_globalno = c_k[-1]
            najbolja_putanja_globalno = putanja

plt.figure(figsize=(10, 5))
for T0, boja in zip(temperaturne_vrednosti, boje):
    for seed in range(broj_pokretanja):
        c_k, _, _ = rezultati[(T0, seed)]
        plt.plot(np.arange(len(c_k)), c_k, color=boja, alpha=0.3, linewidth=1)
    plt.plot([], [], color=boja, label=f"T0={T0}", linewidth=2)

plt.axhline(y=1540, color='green', linestyle='--', label='Referenca: 1540')
plt.xlabel("Iteracija")
plt.ylabel("Kumulativni minimum")
plt.title("Pojedinacni kumulativni minimumi")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
for T0, boja in zip(temperaturne_vrednosti, boje):
    svi_minimumi = [rezultati[(T0, seed)][0] for seed in range(broj_pokretanja)]
    prosek = prosecan_kum_min(svi_minimumi, br_iter)
    print(f"[Prosecan] T0={T0}, prosek krajnje vrednosti={prosek[-1]:.2f}")
    plt.plot(np.arange(br_iter), prosek, label=f"T0={T0}", color=boja, linewidth=2.5)

plt.axhline(y=1540, color='green', linestyle='--', label='Referenca: 1540')
plt.xlabel("Iteracija (log skala)")
plt.ylabel("Prosecan kumulativni minimum")
plt.title("Prosecni kumulativni minimumi")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
for T0, boja in zip(temperaturne_vrednosti, boje):
    sve_duzine = [rezultati[(T0, seed)][1] for seed in range(broj_pokretanja)]
    krajnje = [duzine[-1] for duzine in sve_duzine]
    prosek = np.mean(sve_duzine, axis=0)
    prosecna_krajnja = np.mean(krajnje)
    print(f"\nT0={T0} → Prosečna krajnja dužina: {prosecna_krajnja:.2f}\n")
    plt.plot(np.arange(br_iter), prosek, label=f"T0={T0}", color=boja, linewidth=1.0, alpha=0.6)

plt.axhline(y=1540, color='green', linestyle='--', label='Referenca: 1540')
plt.xlabel("Iteracija (log skala)")
plt.ylabel("Dužina putanje")
plt.title("Prosecna dužina putanje po iteraciji (log skala)")
plt.legend()
plt.grid(True)
plt.xscale("log")
plt.tight_layout()
plt.show()

# Ispis najbolje putanje
print(f"\nNajkraca duzina putanje: {najbolja_duzina_globalno:.2f}")
print(f"Redosled obilaska gradova:\n{najbolja_putanja_globalno}")
