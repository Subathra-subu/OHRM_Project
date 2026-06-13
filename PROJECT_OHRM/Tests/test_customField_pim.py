import pytest
import os
from Actions.pimActions import pimActions
from Utilities.CSVUtils import get_data

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, "..", "test_data", "custom_field_data.csv")

@pytest.mark.usefixtures("test_setup_and_down")
class Test_customField_pim:

    @pytest.mark.parametrize(
        "field_name", 
        get_data(csv_file_path)
    )
    def test_successfully_add_custom_field(
            self, 
            field_name):
        try:
            pim = pimActions(
                self.driver, 
                self.wait
            )

            target_field_name = str(field_name[0])
            expected_url_snippet = "/pim/listCustomFields"

            actual_url = pim.add_new_dropdown_custom_field(target_field_name)

            assert expected_url_snippet in actual_url

        except Exception as e:
            raise