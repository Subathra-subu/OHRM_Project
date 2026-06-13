import os
import pytest

from Actions.LoginActions import LoginActions
from Actions.ChangePasswordActions import ChangePasswordActions
from Utilities.ReadConfig import get_config
from Utilities.CSVUtils import get_data


csv_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "test_data",
    "change_password.csv"
)


@pytest.mark.usefixtures("test_setup_and_down")
class TestChangePassword:

    @pytest.mark.parametrize(
        "old_password,new_password,confirm_password",
        get_data(csv_path)
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

        print(f"Password Changed Successfully : {message}")