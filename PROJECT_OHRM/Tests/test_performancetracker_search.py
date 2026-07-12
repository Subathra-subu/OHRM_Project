import os
import pytest

from Actions.LoginActions import LoginActions
from Actions.PerformanceTrackerActions import PerformanceTrackersActions
from Utilities.ReadConfig import get_config
from Utilities.CSVUtils import get_data

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "..", "test_data", "TrackerSearch.csv")

@pytest.mark.usefixtures("test_setup_and_down")
class Test_TrackerSearch:
    @pytest.mark.smoke(depends="valid_search")
    @pytest.mark.parametrize("employee", [get_data(csv_path)[0]])
    def test_valid_search_tracker(self, employee):

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

        employee_name = employee[0]

        result = tracker.search_tracker(
            employee_name
        )

        print(f"Search Result : {result}")

        assert employee_name == result
    def test_invalid_search_tracker(self):

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

     employee = get_data(csv_path)[1][0]

     result = tracker.invalid_search_tracker(employee)

     print(f"Search Result : {result}")

     assert result == "No Records Found"