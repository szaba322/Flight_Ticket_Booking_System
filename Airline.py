"""**LégiTársaság:** Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve."""

class Airline:
    def __init__(self, name):
        self.name = name
        self._flights = []

    def add_flight(self,flight):
        self._flights.append(flight)

    def get_flight(self, flight_number):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                return flight
        return

    def list_flights(self,ticketing):
        print(f"\n ----- {self.name} ----- \n")
        result = []
        for flight in self._flights:
            dates = [date for fn, date in ticketing.available_dates if fn == flight.flight_number]
            if dates:
                date_list = ", ".join(dates)
                result.append(f"{flight.info()}  Indulási napok: {date_list}")
            else:
                result.append(f"{flight.info()}  Nincs beütemezett indulási dátum")
        return result