
def check_table_availability(available_tables):
    if available_tables > 0:
        return "Tables Available"
    return "No Tables Available"


def make_reservation(available_tables):
    if available_tables > 0:
        return "Reservation Successful"
    return "Reservation Failed"


def tables_remaining(available_tables):
    if available_tables < 0:
        return -1
    return available_tables


if __name__ == "__main__":
    print(check_table_availability(5))
    print(make_reservation(5))
    print(make_reservation(0))
    print(tables_remaining(3))
