import pytest

from Actions.LoginActions import LoginActions
from Actions.PerformanceTrackerActions import PerformanceTrackersActions
from Utilities.ReadConfig import get_config
from Utilities.CSVUtils import get_data


@pytest.mark.usefixtures("test_setup_and_down")
class Test_TrackerSearch:

    @pytest.mark.parametrize(
        "employee",
        get_data("test_data/TrackerSearch.csv")
    )
    def test_valid_search_tracker(
            self,
            employee):

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

        tracker = PerformanceTrackersActions(
            self.driver,
            self.wait
        )

        result = tracker.search_tracker(
            employee
        )

        print(f"Search Result : {result}")

        assert employee == result