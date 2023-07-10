from project.vehicle import Vehicle
import unittest
from unittest import TestCase, main

class TestVehicle(TestCase):
    def test_construct(self):
        vehicle_1 = Vehicle(60.5, 150.5)
        self.assertEqual(60.5, vehicle_1.fuel)
        self.assertEqual(60.5, vehicle_1.capacity)
        self.assertEqual(150.5, vehicle_1.horse_power)
        self.assertEqual(1.25, vehicle_1.DEFAULT_FUEL_CONSUMPTION)

    def test_raise_exception_when_we_do_not_have_enough_fuel(self):
        vehicle_1 = Vehicle(60.5, 150.5)
        fuel_consumption = 1.25
        km = 100
        fuel_needed = 1.25 * 100
        with self.assertRaises(Exception) as ex:
            vehicle_1.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_if_reduce_fuel_when_drive(self):
        vehicle_1 = Vehicle(60.5, 150.5)
        fuel_consumption = 1.25
        km = 20
        fuel_needed = 1.25 * 20
        vehicle_1.drive(20)
        self.assertEqual(35.5, vehicle_1.fuel)

    def test_if_rise_exception_when_try_to_fill_more_fuel_than_capacity(self):
        vehicle_1 = Vehicle(60.5, 150.5)
        with self.assertRaises(Exception) as ex:
            vehicle_1.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel(self):
        vehicle_1 = Vehicle(60.5, 150.5)
        vehicle_1.drive(20)
        vehicle_1.refuel(15)
        self.assertEqual(50.5, vehicle_1.fuel)
    def test_str(self):
        vehicle_1 = Vehicle(60.5, 150.5)

        self.assertEqual(f"The vehicle has 150.5 horse power with 60.5 fuel left and 1.25 fuel consumption",vehicle_1.__str__() )


if __name__ == '__main__':
    main()

