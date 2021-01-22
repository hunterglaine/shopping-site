"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, 
                first_name, 
                last_name, 
                email, 
                password):
        """Creates a Customer object with intance attributes, first name, last 
        name, email, and password"""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def __repr__(self):
        """Method to show customer info more clearly in console"""

        return f"<Customer: {self.first_name} {self.last_name}, {self.email}>"
    # TODO: need to implement this


def read_customers_from_file(filepath):
    """Read customer data and create a dictionary of customers"""

    customers = {}

    for line in open(filepath):
        (first_name, last_name, email, password)= line.strip().split("|")
        # user_info = line.strip().split("|")

        customers[email] = Customer(first_name, 
                                    last_name, 
                                    email, 
                                    password)

    return customers


def get_by_email(email):
    """ """
    # Use customers dictionary to 


