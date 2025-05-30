"""**BelföldiJarat:** Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek."""
from Flight import Flight

class DomesticFlight(Flight):

   def __init__(self, flight_number, destination, price):
        super().__init__(flight_number, destination, price)

   def info(self):
       return f"Belföldi járat -  {self.flight_number} - {self.destination}, Ára: {self.ticket_price} Huf - "
