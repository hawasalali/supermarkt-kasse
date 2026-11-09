import tkinter as tk
from tkinter import ttk, messagebox

# --------------------
# Funktionen
# --------------------

def produkt_hinzufuegen():
    name = produkt_entry.get().strip()
    preis = preis_entry.get().strip()

    if not name:
        messagebox.showwarning("Fehler", "Produktname fehlt!")
        return

    try:
        preis = float(preis.replace(",", "."))
    except:
        messagebox.showwarning("Fehler", "Preis ungültig!")
        return

    liste.insert(tk.END, f"{name} - {preis:.2f} €")

    produkte.append(preis)

    produkt_entry.delete(0, tk.END)
    preis_entry.delete(0, tk.END)

    summe_aktualisieren()

def produkt_loeschen():
    auswahl = liste.curselection()

    if not auswahl:
        return

    index = auswahl[0]

    liste.delete(index)
    produkte.pop(index)

    summe_aktualisieren()

def alles_loeschen():
    liste.delete(0, tk.END)
    produkte.clear()
    summe_aktualisieren()

def summe_aktualisieren():
    gesamt = sum(produkte)
    summen_label.config(
        text=f"Gesamtsumme: {gesamt:.2f} €"
    )

def bezahlen():
    gesamt = sum(produkte)

    if gesamt == 0:
        messagebox.showinfo(
            "Hinweis",
            "Keine Produkte vorhanden."
        )
        return

    zahlung = zahlungsart.get()

    messagebox.showinfo(
        "Bezahlung",
        f"Zu zahlen: {gesamt:.2f} €\n\nZahlungsart: {zahlung}"
    )

# --------------------
# Fenster
# --------------------

root = tk.Tk()
root.title("🛒 Supermarkt Kasse")
root.geometry("700x600")

produkte = []

# --------------------
# Titel
# --------------------

titel = tk.Label(
    root,
    text="🛒 Supermarkt Einkaufsliste",
    font=("Arial", 22, "bold")
)
titel.pack(pady=10)

# --------------------
# Produktname
# --------------------

tk.Label(
    root,
    text="Produkt:"
).pack()

produkt_entry = tk.Entry(
    root,
    font=("Arial", 12)
)
produkt_entry.pack(fill="x", padx=20)

# --------------------
# Preis
# --------------------

tk.Label(
    root,
    text="Preis in €:"
).pack()

preis_entry = tk.Entry(
    root,
    font=("Arial", 12)
)
preis_entry.pack(fill="x", padx=20)

# --------------------
# Hinzufügen
# --------------------

tk.Button(
    root,
    text="➕ Produkt hinzufügen",
    command=produkt_hinzufuegen
).pack(fill="x", padx=20, pady=10)

# --------------------
# Liste
# --------------------

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=20)

scrollbar = tk.Scrollbar(frame)

liste = tk.Listbox(
    frame,
    font=("Arial", 13)
)

scrollbar.pack(side="right", fill="y")
liste.pack(side="left", fill="both", expand=True)

liste.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=liste.yview)

# --------------------
# Gesamtsumme
# --------------------

summen_label = tk.Label(
    root,
    text="Gesamtsumme: 0.00 €",
    font=("Arial", 16, "bold")
)
summen_label.pack(pady=10)

# --------------------
# Zahlungsart
# --------------------

tk.Label(
    root,
    text="Zahlungsart:"
).pack()

zahlungsart = ttk.Combobox(
    root,
    values=[
        "Bar",
        "EC-Karte",
        "Kreditkarte",
        "PayPal"
    ]
)

zahlungsart.current(0)
zahlungsart.pack(pady=5)

# --------------------
# Buttons
# --------------------

tk.Button(
    root,
    text="❌ Produkt löschen",
    command=produkt_loeschen
).pack(fill="x", padx=20, pady=5)

tk.Button(
    root,
    text="🗑 Alles löschen",
    command=alles_loeschen
).pack(fill="x", padx=20, pady=5)

tk.Button(
    root,
    text="💰 Bezahlen",
    bg="lightgreen",
    command=bezahlen
).pack(fill="x", padx=20, pady=15)

root.mainloop()