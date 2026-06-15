import pytest

from Actions.LoginActions import LoginActions
from Actions.PerformanceTrackerActions import PerformanceTrackersActions
from Utilities.ExcelUtils import get_data
from Utilities.Logger import log_generator
from Utilities.ReadConfig import get_config


@pytest.mark.usefixtures("test_setup_and_down")
class Test_TrackerAdd:

    logger = log_generator()
    @pytest.mark.depends(name="valid_search")
    def test_add_tracker(self):

        try:

            self.logger.info("Tracker Add Started")

            login = LoginActions(self.driver, self.wait)

            login.login(get_config("username and password", "username"), get_config("username and password", "password"))

            data = get_data("test_data/TrackerData.xlsx", "Tracker")

            tracker = data[0][0]
            employee = data[0][1]
            reviewer = data[0][2]

            tracker_action = PerformanceTrackersActions(self.driver, self.wait)

            msg = tracker_action.add_tracker(tracker, employee, reviewer)

            assert msg == "Successfully Saved"

            self.logger.info("Tracker Added Successfully")

        except Exception as e:

            self.logger.error(f"Test Failed : {e}")

            raise

    def test_invalid_add_tracker(self):

        try:

            self.logger.info("Invalid Tracker Add Started")

            login = LoginActions(self.driver, self.wait)

            login.login(get_config("username and password", "username"), get_config("username and password", "password"))

            data = get_data("test_data/TrackerData.xlsx", "Tracker")

            employee = data[0][1]
            reviewer = data[0][2]

            tracker_action = PerformanceTrackersActions(self.driver, self.wait)

            msg = tracker_action.invalid_add_tracker(employee, reviewer)

            assert msg == "Required"

            self.logger.info("Required Validation Verified")

        except Exception as e:

            self.logger.error(f"Test Failed : {e}")

            raise
        