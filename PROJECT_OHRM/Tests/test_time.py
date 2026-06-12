import random
import string
import pytest

from Actions.LoginActions import LoginActions
from Actions.TimeActions import TimeActions
from Utilities.ReadConfig import get_config


@pytest.mark.usefixtures("test_setup_and_down")
class TestTime:



    @pytest.mark.parametrize(
        "customer_name,description",
        [
            (
                "sriram_" ,
                "Description_"
            )
        ]
    )
    def test_add_customer(self, customer_name, description):

        customer_name = customer_name + "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
        description = description + "".join(random.choices(string.ascii_uppercase + string.digits, k=8))

        username = get_config("username and password", "username")
        password = get_config("username and password", "password")

        login = LoginActions(self.driver, self.wait)
        login.login(username, password)

        time = TimeActions(self.driver, self.wait)

        customer = time.add_customer(customer_name, description)

        print(f"Customer Created Successfully : {customer}")

    @pytest.mark.parametrize(
        "customer_name,description",
        [
            (
                "sriram_" ,
                "Description_"
            )
        ]
    )
    def test_add_existing_customer(self, customer_name, description):

        description = description + "".join(random.choices(string.ascii_uppercase + string.digits, k=8))

        username = get_config("username and password", "username")
        password = get_config("username and password", "password")

        login = LoginActions(self.driver, self.wait)
        login.login(username, password)

        time = TimeActions(self.driver, self.wait)

        message = time.add_existing_customer(customer_name)

        print(f"Duplicate Customer Creation Attempted : {message}")