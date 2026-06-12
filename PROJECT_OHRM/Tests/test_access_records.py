import pytest
import os
from Actions.MaintenanceActions import MaintenanceActions
from Utilities.ExcelUtils import get_data

@pytest.mark.usefixtures("test_setup_and_down")
class Test_access_records:
    def test_valid_access_records(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__)) 
            file_path = os.path.join(current_dir, "..", "test_data", "add_employee_data.xlsx")  
            data = get_data(file_path, "Sheet1")
            
            search_name = str(data[0][0])
            expected_first_name = str(data[0][0])
            
            main = MaintenanceActions(self.driver, self.wait)
            actual_first_name = main.valid_access_records(search_name)
            
            assert actual_first_name == expected_first_name, f"Assertion Mismatch! Expected: '{expected_first_name}', Found: '{actual_first_name}'"
            
        except Exception as e:
            self.driver.save_screenshot("maintenance_failure.png")
            raise