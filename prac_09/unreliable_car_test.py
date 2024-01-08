from unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Mostly Good", 100, 1)
    bad_car = UnreliableCar("Dodgy", 100, 0)

    for i in range(1, 10):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:10} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:10} drove {bad_car.drive(i):2}km")

    print(good_car)
    print(bad_car)


main()