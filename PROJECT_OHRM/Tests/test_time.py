
import random
import string
import pytest

from Actions.LoginActions import LoginActions
from Actions.TimeActions import TimeActions
from Utilities.ReadConfig import get_config

@pytest.mark.sriram
@pytest.mark.usefixtures("test_setup_and_down")
class TestTime:

    @pytest.mark.test_add_coutomer
    @pytest.mark.order(1)
    @pytest.mark.parametrize(
        "customer_name,description",
        [
            (
                "sriram_",
                "Description_"
            )
        ]
    )
    
    def test_add_customer(
            self,
            customer_name,
            description):

        customer_name = customer_name + "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=5
            )
        )

        description = description + "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=8
            )
        )

        username = get_config(
            "username and password",
            "username"
        )

        password = get_config(
            "username and password",
            "password"
        )

        login = LoginActions(
            self.driver,
            self.wait
        )

        login.login(
            username,
            password
        )

        time = TimeActions(
            self.driver,
            self.wait
        )

        customer = time.add_customer(
            customer_name,
            description
        )

        print(
            f"Customer Created Successfully : {customer}"
        )

    
    @pytest.mark.order(2)
    @pytest.mark.parametrize(
        "customer_prefix,description_prefix",
        [
            (
                "sriram_",
                "Description_"
            )
        ]
    )
    def test_add_existing_customer(
            self,
            customer_prefix,
            description_prefix):

        customer_name = customer_prefix + "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=5
            )
        )

        description = description_prefix + "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=8
            )
        )

        username = get_config(
            "username and password",
            "username"
        )

        password = get_config(
            "username and password",
            "password"
        )

        login = LoginActions(
            self.driver,
            self.wait
        )

        login.login(
            username,
            password
        )

        time = TimeActions(
            self.driver,
            self.wait
        )

        customer = time.add_customer(
            customer_name,
            description
        )

        print(
            f"Customer Created Successfully : {customer}"
        )

        message = time.add_existing_customer(
            customer_name
        )

        print(
            f"Duplicate Customer Validation : {message}"
        )

    @pytest.mark.order(3)
    @pytest.mark.parametrize(
        "date",
        [
            "2026-06-14"
        ]
    )
    def test_attendance_records(
            self,
            date):

        username = get_config(
            "username and password",
            "username"
        )

        password = get_config(
            "username and password",
            "password"
        )

        login = LoginActions(
            self.driver,
            self.wait
        )

        login.login(
            username,
            password
        )

        time = TimeActions(
            self.driver,
            self.wait
        )

        result = time.verify_attendance_records(
            date
        )

        assert "Records Found" in result

        print(
            f"Attendance Records : {result}"
        )

