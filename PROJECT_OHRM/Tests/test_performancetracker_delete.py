import pytest

from Actions.LoginActions import LoginActions
from Actions.PerformanceTrackerActions import PerformanceTrackersActions
from Utilities.ExcelUtils import get_data
from Utilities.Logger import log_generator
from Utilities.ReadConfig import get_config


@pytest.mark.usefixtures("test_setup_and_down")
class Test_TrackerDelete:

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

    def test_delete_tracker(self):

        self.logger.info(
            "Delete Tracker Started"
        )

        self.login()

        data = get_data(
            "test_data/TrackerData.xlsx",
            "Tracker"
        )

        tracker_name = data[0][0]

        tracker_action = PerformanceTrackersActions(
            self.driver,
            self.wait
        )

        result = tracker_action.delete_tracker(
            tracker_name
        )

        assert result == "Successfully Deleted"