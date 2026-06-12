import pytest

from Actions.LoginActions import LoginActions
from Actions.DirectoryActions import DirectoryActions

from Utilities.ReadConfig import get_config
from Utilities.Logger import log_generator


@pytest.mark.usefixtures("test_setup_and_down")
class Test_Directory:
    logger = log_generator()
    def test_search_employee(self):
        try:
            self.logger.info("Directory Test Started")
            username = get_config("username and password","username")
            password = get_config("username and password","password")
            login = LoginActions(self.driver, self.wait)
            login.login(username,password)

            directory = DirectoryActions(self.driver,self.wait)
            directory.search_employee("Ranga")
            actual_names = directory.get_employee_name()
            assert directory.verify_results_displayed()
            assert any("Ranga"
            for name in actual_names
            )
            self.logger.info("Directory Test Passed")

        except Exception as e:

            self.logger.error("Directory Test Failed")
            self.logger.exception(e)
            raise