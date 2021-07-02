import unittest
import json
import pytest
from passenger import Passenger

class Testing(unittest.TestCase):
    passenger = Passenger("fName", "lName", "passportID")
    passenger.add()
    def test_passenger_create(self):
        self.assertIsInstance(self.passenger, Passenger)
        self.assertIsNotNone(self.passenger.f_name)
        with open("passenger_records.json", "r") as file:
            json_file = json.load(file)
            passenger_json = json_file["passenger"]
            for person in passenger_json:
                if person["passportNumber"] == "passportID":
                    id = person["passportNumber"]
            self.assertEquals(id, "passportID")

