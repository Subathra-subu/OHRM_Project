import pytest

from Actions.PerformanceActions import PerformanceActions
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
from Utilities.Logger import log_generator


@pytest.mark.usefixtures("test_setup_and_down")
class Test_PerformanceAdd:

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

    def test_kip_add(self):

        self.logger.info(
            "KPI Add Started"
        )

        self.login()

        kpi = get_config(
            "performance",
            "kpi"
        )

        performance = PerformanceActions(
            self.driver,
            self.wait
        )

        msg = performance.add_kpi(kpi)

        assert msg == "Successfully Saved"

        self.logger.info(
            "KPI Added Successfully"
        )

    def test_invalid_add(self):

        self.logger.info(
            "Invalid KPI Add Started"
        )

        self.login()

        kpiinvalid = get_config(
            "performance",
            "kpiinvalid"
        )

        performance = PerformanceActions(
            self.driver,
            self.wait
        )

        result = performance.invalid_add(
            kpiinvalid
        )

        assert result == "Required"

    def test_invalidwithouttitle(self):

        self.logger.info(
            "KPI Without Job Title Started"
        )

        self.login()

        kpi = get_config(
            "performance",
            "kpi"
        )

        performance = PerformanceActions(
            self.driver,
            self.wait
        )

        result = performance.invalid_addwithtitle(
            kpi
        )

        assert result == "Required"

    def test_invalidmax_rate(self):

        self.logger.info(
            "Invalid Max Rate Started"
        )

        self.login()

        kpi = get_config(
            "performance",
            "kpi"
        )

        max_rate = get_config(
            "performance",
            "maxrate"
        )

        performance = PerformanceActions(
            self.driver,
            self.wait
        )

        result = performance.invalid_max_rate(
            kpi,
            max_rate
        )

        assert result == "Should be a number between 0-100"