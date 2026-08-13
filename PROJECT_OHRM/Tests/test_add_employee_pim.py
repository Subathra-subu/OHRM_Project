import pytest

from Actions.pimActions import pimActions

from Utilities.ExcelUtils import get_data
from Utilities.Logger import log_generator
import os
import random

@pytest.mark.usefixtures("test_setup_and_down")
@pytest.mark.krishna
class Test_add_employee_pim:

    logger = log_generator()

    def test_add_employee_pim(self):

        try:

            self.logger.info("******** PIM Test Started ********")


            current_dir = os.path.dirname(os.path.abspath(__file__)) 
            file_path = os.path.join(current_dir, "..", "test_data", "add_employee_data.xlsx")  
            data = get_data(file_path, "Sheet1")
            print("\n" + "="*50)
            print(f"EXTRACTED DATA ROW 1: {data[0]}")
            print(f"ROW 1 LENGTH: {len(data[0])}")
            print("="*50 + "\n")

            self.pim = pimActions(self.driver, self.wait)


            first_row = data[0]
            
            fname  = str(first_row[0]) if len(first_row) > 0 else ""
            mname  = str(first_row[1]) if len(first_row) > 1 else ""
            lname  = str(first_row[2]) if len(first_row) > 2 else ""
            uname  = str(first_row[3]) if len(first_row) > 3 else ""
            if uname:
                uname = f"{uname}{random.randint(100, 999)}"
            pword  = str(first_row[4]) if len(first_row) > 4 else ""
            cpword = str(first_row[5]) if len(first_row) > 5 else ""

            print(f"SENDING TO SELENIUM -> fname: '{fname}', mname: '{mname}', lname: '{lname}', uname: '{uname}', pword: '{pword}', cpword: '{cpword}'")
            actual_url = self.pim.add_employee_pim(fname, mname, lname, uname, pword, cpword)        
            assert "/viewPersonalDetails" in actual_url,"Form submission failed."
            " Browser did not redirect to Personal Details profile page."


            self.logger.info("******** PIM Test Passed ********")

        except Exception as e:

            self.logger.error("******** PIM Test Failed ********")
            self.logger.exception(e)
            raise
        #test for missing lastname 

    @pytest.mark.parametrize("missing_field_type", ["first_name", "last_name"])
    def test_missing_employee_fields_validation(self, missing_field_type):
        try:
            self.logger.info(f"******** PIM Missing field validation test started for: {missing_field_type} ********")
            
            current_dir = os.path.dirname(os.path.abspath(__file__)) 
            file_path = os.path.join(current_dir, "..", "test_data", "add_employee_data.xlsx")  
            data = get_data(file_path, "Sheet1")
            
            self.pim = pimActions(self.driver, self.wait)

            if missing_field_type == "last_name":
                input_name = str(data[0][0])  
            else:
                input_name = str(data[0][2])  

            actual_err_msg = self.pim.missing_field_validation(input_name, missing_field_type)

            assert actual_err_msg == "Required", f"Validation message mismatch! Found: '{actual_err_msg}'"
            self.logger.info(f"Missing {missing_field_type} validation test successfully completed.")

        except Exception as e:
            self.logger.error(f"******** PIM Validation Test Failed for field: {missing_field_type} ********")
            self.logger.exception(e)
            raise