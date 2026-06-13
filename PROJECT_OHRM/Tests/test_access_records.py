import pytest
import os
from Actions.MaintenanceActions import MaintenanceActions
from Utilities.ExcelUtils import get_data

@pytest.mark.usefixtures("test_setup_and_down")
class Test_access_records:

    @pytest.fixture(autouse=True)
    def class_initialization(self, test_setup_and_down):
        self.main = MaintenanceActions(self.driver, self.wait)

    def test_valid_access_records(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__)) 
            file_path = os.path.join(current_dir, "..", "test_data", "add_employee_data.xlsx")  
            data = get_data(file_path, "Sheet1")
            
            search_name = str(data[0][0])
            
            is_profile_visible = self.main.valid_access_records(search_name)
            assert is_profile_visible, "Profile payload error: First Name output data field is not visible on screen!"
            
        except Exception as e:
            self.driver.save_screenshot("maintenance_failure.png")
            raise

    def test_blank_search_validation_message(self):
        try:
            is_error_visible = self.main.verify_blank_search_error_state()
            assert is_error_visible, "Localization Mismatch: The input validation error element failed to display!"
            
        except Exception as e:
            self.driver.save_screenshot("blank_search_localization_failure.png")
            raise