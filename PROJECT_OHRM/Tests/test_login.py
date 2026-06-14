
import os
import pytest

from Actions.LoginActions import LoginActions
from Actions.DashboardActions import DashboardActions

from Utilities.ReadConfig import get_config
from Utilities.Logger import log_generator
from Utilities import ExcelUtils


invalid_login_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "test_data",
    "inValid_Login_datas.xlsx"
)

@pytest.mark.sriram
@pytest.mark.usefixtures("test_setup_and_down")
class Test_Login:

    logger = log_generator()

    @pytest.mark.login
    def test_login(self):

        try:

            self.logger.info("Login Test Started")

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

            self.logger.info(
                "Login Test Passed"
            )

        except Exception as e:

            self.logger.error(
                "Login Test Failed"
            )

            self.save_screenshot(
                "login_test_failed"
            )

            self.logger.exception(e)

            raise


    @pytest.mark.parametrize(
        "username,password",
        ExcelUtils.get_data(
            invalid_login_path,
            "Sheet1"
        )
    )

    @pytest.mark.inValLogin
    def test_invalid_login(
            self,
            username,
            password):

        try:

            self.logger.info(
                "Invalid Login Test Started"
            )

            login = LoginActions(
                self.driver,
                self.wait
            )

            login.invalid_login(
                username,
                password
            )

            self.logger.info(
                "Invalid Login Test Passed"
            )

        except Exception as e:

            self.logger.error(
                "Invalid Login Test Failed"
            )

            self.save_screenshot(
                "invalid_login_test_failed"
            )

            self.logger.exception(e)

            raise


    @pytest.mark.parametrize(
        "username,password",
        ExcelUtils.get_data(
            invalid_login_path,
            "Sheet2"
        )
    )

    @pytest.mark.withoutCredential
    def test_without_credential(
            self,
            username,
            password):

        try:

            self.logger.info(
                "Without Credential Test Started"
            )

            login = LoginActions(
                self.driver,
                self.wait
            )

            login.without_credential(
                username,
                password
            )

            self.logger.info(
                "Without Credential Test Passed"
            )

        except Exception as e:

            self.logger.error(
                "Without Credential Test Failed"
            )

            self.save_screenshot(
                "without_credential_test_failed"
            )

            self.logger.exception(e)

            raise

