from Data import Data

class Main():

    def preload_data(self):
        return Data.load_data()

    def menu_interact(self):
        airline, ticket_handler = self.preload_data()
        while True:
            print("\n Repülőjegy foglalás Menü")
            print("1. Járatok listázása")
            print("2. Lefoglalt jegyek listázása")
            print("3. Jegy vétel")
            print("4. Jegy lemondása")
            print("0. Kilépés")

            menu_input = input("Válasszon a lehetőségek közül: ")

            if menu_input == "1":  # Járatok listázása
                for f in airline.list_flights(ticket_handler):
                    print(f)

            elif menu_input == "2": # Jegyek listázása
                for b in ticket_handler.list_bookings():
                    print(b)

            elif menu_input == "3": # Jegy vétele
                flight_number = input("Írja be a járat számát: ")
                date = input("Írja be a dátumot (YYYY-MM-DD) formátumban: ")
                flight = airline.get_flight(flight_number)
                if flight:
                    print(ticket_handler.book_ticket(flight, date))
                else:
                    print("Hiba: Járat nem található!")


            elif menu_input == "4": # Jegy lemondása
                flight_number = input("Írja be a járat számát: ")
                date = input("Írja be a dátumot (YYYY-MM-DD) formátumban: ")
                print(ticket_handler.cancel_ticket(flight_number, date))

            elif menu_input == "0": # Kilépés
                print("Kilépés")
                break
            else:
                print("Érvénytelen szám")

usermenu = Main()
usermenu.menu_interact()