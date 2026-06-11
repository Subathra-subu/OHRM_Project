import pytest

from Actions.LoginActions import LoginActions
from Actions.pimActions import pimActions

from Utilities.ReadConfig import get_config
from Utilities.ExcelUtils import get_data
from Utilities.Logger import log_generator


@pytest.mark.usefixtures("test_setup_and_down")
class Test_PIM:

    logger = log_generator()

    def test_add_employee(self):

        try:

            self.logger.info("******** PIM Test Started ********")

            # ======================
            # LOGIN (reusable action)
            # ======================
            username = get_config("username and password", "username")
            password = get_config("username and password", "password")

            login = LoginActions(self.driver, self.wait)
            login.login(username, password)

            # ======================
            # READ EXCEL
            # ======================
            # ======================
            # READ EXCEL
            # ======================
            file_path = r"E:\orangeHrm_project\OHRM_Project\PROJECT_OHRM\test_data\add_employee_data.xlsx"
            data = get_data(file_path, "Sheet1")

            # 🚨 DEBUG PRINT: Check exactly what openpyxl extracted
            print("\n" + "="*50)
            print(f"EXTRACTED DATA ROW 1: {data[0]}")
            print(f"ROW 1 LENGTH: {len(data[0])}")
            print("="*50 + "\n")

            pim = pimActions(self.driver, self.wait)

            # ======================
            # SAFE DATA EXTRACTION
            # ======================
            # Extract values safely, defaulting to empty string if missing
            first_row = data[0]
            
            fname  = str(first_row[0]) if len(first_row) > 0 else ""
            mname  = str(first_row[1]) if len(first_row) > 1 else ""
            lname  = str(first_row[2]) if len(first_row) > 2 else ""
            uname  = str(first_row[3]) if len(first_row) > 3 else ""
            pword  = str(first_row[4]) if len(first_row) > 4 else ""
            cpword = str(first_row[5]) if len(first_row) > 5 else ""

            # 🚨 DEBUG PRINT: Check what is actually being sent to the action
            print(f"SENDING TO SELENIUM -> fname: '{fname}', mname: '{mname}', lname: '{lname}', uname: '{uname}', pword: '{pword}', cpword: '{cpword}'")

            pim.add_employee(fname, mname, lname, uname, pword, cpword)

            self.logger.info("******** PIM Test Passed ********")

        except Exception as e:

            self.logger.error("******** PIM Test Failed ********")
            self.logger.exception(e)
            raise