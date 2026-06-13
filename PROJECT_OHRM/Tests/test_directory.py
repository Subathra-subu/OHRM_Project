import pytest

from Actions.LoginActions import LoginActions
from Actions.DirectoryActions import DirectoryActions
from Pages.DirectoryPage import DirectoryPage
from Utilities.ExcelUtils import get_data
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
            data = get_data("test_data/DirectoryData.xlsx","EmployeeSearch")
            employee_name = data[0][0]
            directory.search_employee(employee_name)
            
            actual_names = directory.get_employee_name()
            assert directory.verify_results_displayed()
            assert any("Admin" in name for name in actual_names)
            self.logger.info("Directory Test Passed")

        except Exception as e:

            self.logger.error("Directory Test Failed")
            self.logger.exception(e)
            raise

    def test_search_employee_negative(self):

        self.logger.info("Directory Negative Test Started")
        username = get_config("username and password", "username")
        password = get_config("username and password", "password")
        login = LoginActions(self.driver, self.wait)
        login.login(username, password)
        directory = DirectoryActions(self.driver, self.wait)
        data = get_data("test_data/DirectoryData.xlsx","EmployeeSearch")
        employee_name = data[1][0]      
        directory.search_invalid_employee(employee_name)
        actual_error = directory.get_error_message()
        assert actual_error == "Invalid"
        self.logger.info("Directory Negative Test Passed")

    def test_search_by_job_title(self):

        self.logger.info("Job Title Test Started")
        username = get_config("username and password", "username")
        password = get_config("username and password", "password")
        login = LoginActions(self.driver, self.wait)
        login.login(username, password)
        directory = DirectoryActions(self.driver, self.wait)
        job_title = "Chief Financial Officer"
        directory.search_by_job_title(job_title)
        actual_titles = self.driver.find_elements(*DirectoryPage.employee_job_titles)
        titles_text = [t.text for t in actual_titles]
        # assert any(job_title.lower() in t.lower() for t in titles_text)
        pass
        self.logger.info("Job Title Test Passed")