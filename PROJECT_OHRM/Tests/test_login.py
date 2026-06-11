import pytest

from Actions.LoginActions import LoginActions
from Actions.DashboardActions import DashboardActions

from Utilities.ReadConfig import get_config
from Utilities.Logger import log_generator

from Utilities import ExcelUtils
@pytest.mark.usefixtures("test_setup_and_down")
class Test_Login:

    logger = log_generator()
    
    def test_login(self):

        try:

            self.logger.info("Test Started")

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

            dashboard = DashboardActions(
                self.driver,
                self.wait
            )

            dashboard.verify_dashboard()

            self.logger.info("Test Passed")

        except Exception as e:

            self.logger.error("Test Failed")

            self.logger.exception(e)

            raise


    @pytest.mark.parametrize(
    "username,password",
    ExcelUtils.get_data(
        r"test_data\inValid_Login_datas.xlsx",
        "Sheet1"
        )
    )
    def test_invalid_login(self, username, password):

        try:

            self.logger.info("Invalid Login Test Started")

            login = LoginActions(
            self.driver,
            self.wait
        )

            login.invalid_login(
            username,
            password
        )

            self.logger.info("Invalid Login Test Passed")

        except Exception as e:

            self.logger.error("Invalid Login Test Failed")

            self.logger.exception(e)

            raise