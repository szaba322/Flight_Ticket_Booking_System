from DomesticFlight import DomesticFlight
from InternationalFlight import InternationalFlight
from Airline import Airline
from Ticketing import Ticketing

class Data:
    @staticmethod
    def load_data():
        airline = Airline("Ctrl+Fly Légitársaság")

        f1 = DomesticFlight("D101", "Budapest", 14000)
        f2 = DomesticFlight("D102", "Debrecen", 12000)
        f3 = InternationalFlight("I201", "London", 42000)

        airline.add_flight(f1)
        airline.add_flight(f2)
        airline.add_flight(f3)

        ticket_handler = Ticketing()
        ticket_handler.add_available_date(f1, "2025-06-01")
        ticket_handler.add_available_date(f1, "2025-06-06")
        ticket_handler.add_available_date(f1, "2025-06-10")
        ticket_handler.add_available_date(f1, "2025-06-16")
        ticket_handler.add_available_date(f2, "2025-06-04")
        ticket_handler.add_available_date(f2, "2025-06-08")
        ticket_handler.add_available_date(f2, "2025-06-12")
        ticket_handler.add_available_date(f2, "2025-06-21")
        ticket_handler.add_available_date(f3, "2025-05-27")
        ticket_handler.add_available_date(f3, "2025-06-14")
        ticket_handler.add_available_date(f3, "2025-06-16")
        ticket_handler.add_available_date(f3, "2025-06-23")

        ticket_handler.book_ticket(f1, "2025-06-01")
        ticket_handler.book_ticket(f1, "2025-06-10")
        ticket_handler.book_ticket(f2, "2025-06-08")
        ticket_handler.book_ticket(f2, "2025-06-21")
        ticket_handler.book_ticket(f3, "2025-06-14")
        ticket_handler.book_ticket(f3, "2025-06-16")

        return airline, ticket_handler