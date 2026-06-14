
import os
import pytest

from Actions.LoginActions import LoginActions
from Actions.ChangePasswordActions import ChangePasswordActions

from Utilities.ReadConfig import get_config
from Utilities.CSVUtils import get_data


positive_csv = os.path.join(
    os.path.dirname(__file__),
    "..",
    "test_data",
    "change_password.csv"
)

negative_csv = os.path.join(
    os.path.dirname(__file__),
    "..",
    "test_data",
    "negative_change_password.csv"
)


@pytest.mark.usefixtures("test_setup_and_down")
class TestChangePassword:


    @pytest.mark.order(1)
    @pytest.mark.parametrize(
        "old_password,new_password,confirm_password,expected_result",
        get_data(negative_csv)
    )
    def test_negative_change_password(
            self,
            old_password,
            new_password,
            confirm_password,
            expected_result):

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

        change = ChangePasswordActions(
            self.driver,
            self.wait
        )

        change.negative_change_password(
            old_password,
            new_password,
            confirm_password
        )

        if expected_result == "Passwords do not match":

            message = (
                change.get_password_mismatch_message()
            )

        elif expected_result == (
                "Current Password is Incorrect"):

            message = (
                change.get_error_toast_message()
            )

        else:

            message = (
                change.get_required_message()
            )

        assert expected_result in message

        print(
            f"Validation Message : {message}"
        )


    @pytest.mark.order(2)
    @pytest.mark.parametrize(
        "old_password,new_password,confirm_password",
        get_data(positive_csv)
    )
    def test_change_password(
            self,
            old_password,
            new_password,
            confirm_password):

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

        change = ChangePasswordActions(
            self.driver,
            self.wait
        )

        message = change.change_password(
            old_password,
            new_password,
            confirm_password
        )

        print(
            f"Password Changed Successfully : {message}"
        )

