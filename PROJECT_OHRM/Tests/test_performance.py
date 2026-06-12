import pytest
from Actions.PerformanceActions import PerformanceActions
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
from Utilities.Logger import log_generator


@pytest.mark.usefixtures("test_setup_and_down")
class Test_Performance:

    logger = log_generator()

    def test_kip_add(self):

        try:

            self.logger.info("Scenario started")

            login = LoginActions(self.driver, self.wait)

            login.login(
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            kpi = get_config("performance", "kip")

            performance = PerformanceActions(self.driver, self.wait)

            performance.add_kpi(kpi)

            self.logger.info("KPI Added Successfully")

        except Exception as e:

            self.logger.error(f"Test Failed: {e}")
            raise