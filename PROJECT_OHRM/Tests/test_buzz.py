import pytest
import os
from Actions.buzzActions import buzzActions
from Utilities.Logger import log_generator

@pytest.mark.usefixtures("test_setup_and_down")
class Test_buzz:

    logger = log_generator()

    def test_successfully_share_buzz_photo(self):
        try:
            self.logger.info("******** Buzz Image Share Test Started ********")

            self.buzz = buzzActions(self.driver, self.wait)

            current_dir = os.path.dirname(os.path.abspath(__file__))
            image_relative_path = os.path.join(current_dir, "..", "test_data", "sample_data.jpg")

            self.logger.info(f"Resolving image upload file target path to: {image_relative_path}")
            is_image_visible = self.buzz.share_buzz_image(image_relative_path)
            
            assert is_image_visible, "The uploaded image is not visible on the Buzz feed timeline."
            
            self.logger.info("******** Buzz Image Share Test Passed ********")

        except Exception as e:
            self.logger.error("******** Buzz Image Share Test Failed ********")
            self.logger.exception(e)
            raise