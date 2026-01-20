"""
Čtvrtý projekt do Engeto Online Python Akademie - Task manager
author: Květoslav Leidorf
email: k.leidorf@gmail.com
discord: kvetos_95684
"""

# Globální seznam pro ukládání úkolů (v budoucnu by mohl být v třídě/objektu)
ukoly = []


def hlavni_menu() -> str:
    """Zobrazí hlavní menu a vrátí volbu uživatele."""
    while True:
        # Sloučení vícenásobných printů do jednoho bloku pro lepší čitelnost
        print(
            "\n" + "-" * 27,
            "Správce úkolů - Hlavní menu",
            "1. Přidat nový úkol",
            "2. Zobrazit všechny úkoly",
            "3. Odstranit úkol",
            "4. Konec programu",
            "-" * 27,
            sep="\n"
        )
        
        volba = input("Vyberte možnost (1-4): ").strip()
        
        if volba in ("1", "2", "3", "4"):
            return volba
        
        print("Neplatná volba, zkuste to prosím znovu.")


def pridat_ukol() -> None:
    """Umožní uživateli zadat název a popis úkolu a uloží jej."""
    while True:
        nazev = input("\nZadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()
        
        # Validace vstupu: kontrola, zda uživatel nezadal jen prázdné znaky
        if not nazev or not popis:
            print("Chyba: Název i popis úkolu nesmí být prázdný! Zadejte znovu.")
            continue
        
        # Uložení úkolu do slovníku
        ukol = {"nazev": nazev, "popis": popis}
        ukoly.append(ukol)
        
        print(f"Úkol '{nazev}' byl úspěšně přidán.")
        break


def zobrazit_ukoly() -> None:
    """Zobrazí všechny uložené úkoly s pořadovým číslem."""
    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")
    # Start=1 zajišťuje uživatelsky přívětivé číslování od jedničky
    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol() -> None:
    """Umožní uživateli odstranit konkrétní úkol podle jeho čísla."""
    if not ukoly:
        print("\nNení co odstranit, seznam je prázdný.")
        return

    zobrazit_ukoly()
    
    try:
        index_str = input("\nZadejte číslo úkolu k odstranění: ").strip()
        # Převod vstupu na index (Python indexuje od 0, uživatel vidí od 1)
        index = int(index_str) - 1
        
        # Kontrola, zda je index v platném rozsahu existujícího seznamu
        if 0 <= index < len(ukoly):
            odstraneny = ukoly.pop(index)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        else:
            print("Chyba: Úkol s tímto číslem neexistuje.")
            
    except ValueError:
        print("Chyba: Zadejte prosím platné celé číslo.")


def spusti_program() -> None:
    """Hlavní řídicí smyčka programu."""
    while True:
        volba = hlavni_menu()
        
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nUkončuji program. Na shledanou!")
            break


if __name__ == "__main__":
    spusti_program()
