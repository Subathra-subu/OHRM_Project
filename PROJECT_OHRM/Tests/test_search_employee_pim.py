import pytest
from Actions.LoginActions import LoginActions
from Actions.pimActions import pimActions
from Utilities.ReadConfig import get_config
from Utilities.ExcelUtils import get_data
from Utilities.Logger import log_generator
import os

@pytest.mark.usefixtures("test_setup_and_down")
class Test_Search_Employee_pim:

    logger = log_generator()

    def test_search_employee_pim(self):
        try:
            self.logger.info("******** PIM Search Test Started ********")

            current_dir = os.path.dirname(os.path.abspath(__file__)) 
            file_path = os.path.join(current_dir, "..", "test_data", "add_employee_data.xlsx")  
            data = get_data(file_path, "Sheet1")
            first_row = data[0]
            
            fname  = str(first_row[0]) if len(first_row) > 0 else ""
            mname  = str(first_row[1]) if len(first_row) > 1 else ""
            lname  = str(first_row[2]) if len(first_row) > 2 else ""
            uname  = str(first_row[3]) if len(first_row) > 3 else ""
            pword  = str(first_row[4]) if len(first_row) > 4 else ""
            cpword = str(first_row[5]) if len(first_row) > 5 else ""

            pim = pimActions(self.driver, self.wait)


            actual_url=pim.search_employee_pim(fname, mname, lname, uname, pword, cpword)



            assert "/viewPersonalDetails" in actual_url,"Form submission failed."
            " Browser did not redirect to Personal Details profile page."
            
            self.logger.info("******** PIM Search Test Passed ********")

        except Exception as e:
            self.logger.error("******** PIM Search Test Failed ********")
            self.logger.exception(e)
            raise