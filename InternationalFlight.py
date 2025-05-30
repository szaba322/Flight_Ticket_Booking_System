"""**NemzetkoziJarat:** Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal."""
from Flight import Flight

class InternationalFlight(Flight):

    def __init__(self, flight_number, destination, price):
        super().__init__(flight_number, destination, price)

    def info(self):
        return f"Külföldi járat -  {self.flight_number} - {self.destination}, Ára: {self.ticket_price} Huf - "