import pytest
from Actions.PerformanceActions import PerformanceActions
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
from Utilities.Logger import log_generator


@pytest.mark.usefixtures("test_setup_and_down")
class Test_PerformanceAdd:

    logger = log_generator()

    def test_kip_add(self):

        try:

            self.logger.info("Scenario started")

            login = LoginActions(self.driver, self.wait)

            login.login(
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            kpi = get_config("performance", "kpi")

            performance = PerformanceActions(self.driver, self.wait)

            msg = performance.add_kpi(kpi)

            assert msg == "Successfully Saved"

            self.logger.info("KPI Added Successfully")

        except Exception as e:

            self.logger.error(f"Test Failed: {e}")
            raise
    
    def test_invalid_add(self):
        try:
            self.logger.info("Scenario started")
            login = LoginActions(self.driver, self.wait)

            login.login(
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            kpiinvalid = get_config("performance", "kpiinvalid")
            performance = PerformanceActions(self.driver, self.wait)
            res=performance.invalid_add(kpiinvalid)
            assert res == "Required"
            self.logger.info("KPI Not Added Successfully")
        except Exception as e:

            self.logger.error(f"Test Failed: {e}")
            raise
    def test_invalidwithouttitle(self):
        try:
            self.logger.info("Scenario started")
            login = LoginActions(self.driver, self.wait)

            login.login(
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            kpiinvalid = get_config("performance", "kpi")
            performance = PerformanceActions(self.driver, self.wait)
            res=performance.invalid_addwithtitle(kpiinvalid)
            assert res == "Required"
            self.logger.info("KPI Not Added Successfully")
        except Exception as e:

            self.logger.error(f"Test Failed: {e}")
            raise
    def test_invalidmax_rate(self):
        try:
            self.logger.info("Scenario started")
            login = LoginActions(self.driver, self.wait)

            login.login(
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            kpiinvalid = get_config("performance", "kpi")
            max_rate = get_config("performance","maxrate")

            performance = PerformanceActions(self.driver, self.wait)
            res=performance.invalid_max_rate(kpiinvalid,max_rate)
            assert res == "Should be a number between 0-100"
            self.logger.info("KPI Not Added Successfully")
        except Exception as e:

            self.logger.error(f"Test Failed: {e}")
            raise

          




