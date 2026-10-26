
import unittest
from restaurant import (
    check_table_availability,
    make_reservation,
    tables_remaining
)


class TestRestaurant(unittest.TestCase):

    def test_tables_available(self):
        self.assertEqual(check_table_availability(5), "Tables Available")

    def test_no_tables_available(self):
        self.assertEqual(check_table_availability(0), "No Tables Available")

    def test_reservation_successful(self):
        self.assertEqual(make_reservation(5), "Reservation Successful")

    def test_reservation_failed(self):
        self.assertEqual(make_reservation(0), "Reservation Failed")

    def test_valid_table_count(self):
        self.assertEqual(tables_remaining(3), 3)

    def test_invalid_table_count(self):
        self.assertEqual(tables_remaining(-1), -1)


if __name__ == "__main__":
    unittest.main()
