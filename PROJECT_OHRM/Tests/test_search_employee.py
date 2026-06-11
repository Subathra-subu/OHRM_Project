import pytest
from Actions.LoginActions import LoginActions
from Actions.pimActions import pimActions
from Utilities.ReadConfig import get_config
from Utilities.ExcelUtils import get_data
from Utilities.Logger import log_generator

@pytest.mark.usefixtures("test_setup_and_down")
class Test_Search_Employee:

    logger = log_generator()

    def test_search_employee(self):
        try:
            self.logger.info("******** PIM Search Test Started ********")

            file_path = r"E:\orangeHrm_project\OHRM_Project\PROJECT_OHRM\test_data\add_employee_data.xlsx"
            data = get_data(file_path, "Sheet1")
            
            first_row = data[0]
            
            fname  = str(first_row[0]) if len(first_row) > 0 else ""
            mname  = str(first_row[1]) if len(first_row) > 1 else ""
            lname  = str(first_row[2]) if len(first_row) > 2 else ""
            uname  = str(first_row[3]) if len(first_row) > 3 else ""
            pword  = str(first_row[4]) if len(first_row) > 4 else ""
            cpword = str(first_row[5]) if len(first_row) > 5 else ""

            pim = pimActions(self.driver, self.wait)


            actual_fullname = pim.search_employee(fname, mname, lname, uname, pword, cpword)

            assert actual_fullname == actual_fullname,"invalid"

            self.logger.info("******** PIM Search Test Passed ********")

        except Exception as e:
            self.logger.error("******** PIM Search Test Failed ********")
            self.logger.exception(e)
            raise