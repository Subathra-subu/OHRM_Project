import pytest

from Actions.PerformanceActions import PerformanceActions
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
from Utilities.Logger import log_generator


@pytest.mark.usefixtures("test_setup_and_down")
class Test_PerformanceSearch:

    logger = log_generator()

    def login(self):

        login = LoginActions(
            self.driver,
            self.wait
        )

        login.login(
            get_config(
                "username and password",
                "username"
            ),
            get_config(
                "username and password",
                "password"
            )
        )

    def test_valid_search(self):

        self.logger.info(
            "Valid KPI Search Started"
        )

        self.login()

        performance = PerformanceActions(
            self.driver,
            self.wait
        )

        result = performance.valid_search()

        assert result == "Account Assistant"

        self.logger.info(
            "KPI Search Success"
        )

    def test_invalid_search(self):

        self.logger.info(
            "Invalid KPI Search Started"
        )

        self.login()

        performance = PerformanceActions(
            self.driver,
            self.wait
        )

        result = performance.invalid_search()

        assert result == "No Records Found"

        self.logger.info(
            "Invalid KPI Search Verified"
        )