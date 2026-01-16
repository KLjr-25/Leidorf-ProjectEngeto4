"""
projekt_4.py: čtvrtý projekt do Engeto Online Python Akademie
author: Květoslav Leidorf
email: k.leidorf@gmail.com
discord: Ketosh
"""

# Seznam pro ukládání úkolů
ukoly = []

def hlavni_menu() -> str:
    """Zobrazí hlavní menu a vrátí volbu uživatele."""
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Vyberte možnost (1-4): ").strip()
        
        if volba in ("1", "2", "3", "4"):
            return volba
        else:
            print("Neplatná volba, zkuste to prosím znovu.")

def pridat_ukol() -> None:
    """Umožní uživateli zadat název a popis úkolu a uloží jej."""
    while True:
        nazev = input("\nZadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()
        
        # Kontrola prázdného vstupu 
        if not nazev or not popis:
            print("Chyba: Název i popis úkolu nesmí být prázdný! Zadejte znovu.")
            continue
        
        ukol = {"nazev": nazev, "popis": popis}
        ukoly.append(ukol)
        print(f"Úkol '{nazev}' byl přidán.")
        break

def zobrazit_ukoly() -> None:
    """Zobrazí všechny uložené úkoly."""
    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")
    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukol() -> None:
    """Umožní uživateli odstranit konkrétní úkol podle čísla."""
    if not ukoly:
        print("\nNení co odstranit, seznam je prázdný.")
        return

    zobrazit_ukoly()
    try:
        index_str = input("\nZadejte číslo úkolu, který chcete odstranit: ").strip()
        index = int(index_str) - 1
        
        if 0 <= index < len(ukoly):
            odstraneny = ukoly.pop(index)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        else:
            print("Chyba: Úkol s tímto číslem neexistuje.")
    except ValueError:
        print("Chyba: Zadejte prosím platné číslo.")

def spusti_program() -> None:
    """Hlavní smyčka programu."""
    while True:
        volba = hlavni_menu()
        
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nKonec programu.")
            break

if __name__ == "__main__":
    spusti_program()
