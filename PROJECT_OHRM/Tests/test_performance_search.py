import pytest
from Actions.PerformanceActions import PerformanceActions
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
from Utilities.Logger import log_generator


@pytest.mark.usefixtures("test_setup_and_down")
class Test_PerformanceSearch:

    logger = log_generator()

    def test_valid_search(self):

        try:

            self.logger.info("Scenario started")

            login = LoginActions(self.driver, self.wait)

            login.login(
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )
            performance = PerformanceActions(self.driver, self.wait)
           
            ans=performance.valid_search()
            assert ans == "Account Assistant"
        
            self.logger.info("KPI Search Success!")

        except Exception as e:

            self.logger.error(f"Test Failed: {e}")
            raise


            
   
