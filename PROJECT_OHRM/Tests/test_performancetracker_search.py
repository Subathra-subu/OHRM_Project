import os
import pytest

from Actions.LoginActions import LoginActions
from Actions.PerformanceTrackerActions import PerformanceTrackersActions
from Utilities.ReadConfig import get_config
from Utilities.CSVUtils import get_data


current_dir = os.path.dirname(
    os.path.abspath(__file__)
)

csv_path = os.path.join(
    current_dir,
    "..",
    "test_data",
    "TrackerSearch.csv"
)


@pytest.mark.usefixtures("test_setup_and_down")
class Test_TrackerSearch:

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

    def test_valid_search_tracker(self):

        self.login()

        data = get_data(csv_path)

        employee = data[0][0]

        tracker = PerformanceTrackersActions(
            self.driver,
            self.wait
        )

        result = tracker.search_tracker(
            employee
        )

        print(
            f"Search Result : {result}"
        )

        assert employee == result

    def test_invalid_search_tracker(self):

        self.login()

        data = get_data(csv_path)

        employee = data[1][0]

        tracker = PerformanceTrackersActions(
            self.driver,
            self.wait
        )

        result = tracker.invalid_search_tracker(
            employee
        )

        print(
            f"Search Result : {result}"
        )

        assert result == "No Records Found"