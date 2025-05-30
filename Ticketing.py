"""**JegyFoglalás:** A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja."""
from datetime import datetime

class Ticketing:
    def __init__(self):
        self.bookings = []
        self.available_dates = []

    def add_available_date(self, flight, date):
        self.available_dates.append((flight.flight_number, date))

    def book_ticket(self, flight, date):
        try:
            if not isinstance(date, str):
                return "Hiba! A dátum rosszul lett megadva. (Helyesen: '2025-06-01')."

            date_object = datetime.strptime(date, "%Y-%m-%d")
            if date_object < datetime.now():
                return "Hiba!: Múltbéli dátum!"

            if (flight.flight_number, date) not in self.available_dates:
                return "Hiba! Ezen a dátumon nem indul járat!"

            for booked_flight, booked_date in self.bookings:
                if booked_flight.flight_number == flight.flight_number and booked_date == date:
                    return "Hiba! Erre a napra már van foglalás erre a járatra!"

        except ValueError:
            return "Hiba! Érvénytelen időformátum (YYYY-MM-DD)."

        self.bookings.append((flight, date))
        return f"{flight.ticket_price} Huf értékben a jegy vétel sikeres."

    def cancel_ticket(self, flight_number, date):
        for i, (flight, booking_date) in enumerate(self.bookings):
            if flight.flight_number == flight_number and booking_date == date:
                del self.bookings[i]
                return "Jegy lemondva"
        return  "Nem található lefoglalt jegy!"

    def list_bookings(self):
        if not self.bookings:
            return ["Nincs megvásárolt jegy."]
        return [f"{flight.info()}, Dátum: {date}" for flight,date in self.bookings]