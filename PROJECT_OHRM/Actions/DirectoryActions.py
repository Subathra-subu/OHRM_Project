from selenium.webdriver.support import expected_conditions as EC
from Actions.BaseActions import BaseActions
from Pages.DirectoryPage import DirectoryPage
from Pages.BasePage import BasePage

class DirectoryActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def open_directory(self):
        try:
            self.logger.info("Opening Directory Page")
            self.click(BasePage.Directory)
            self.wait.until(lambda d: d.find_element(*DirectoryPage.employee_name))

        except Exception as e:
            self.logger.error("Failed to open Directory page")
            self.logger.exception(e)
            raise

    def search_employee(self, employee_name):

        try:
            self.logger.info("Directory Search By Employee Name Started")
            self.open_directory()
            name_field = self.wait.until(EC.visibility_of_element_located(DirectoryPage.employee_name))
            name_field.clear()
            name_field.send_keys(employee_name)

            try:
                suggestions = self.wait.until(lambda d: d.find_elements(*DirectoryPage.auto_suggestion))
                for s in suggestions:
                    if employee_name.lower() in s.text.lower():
                        s.click()
                        break

            except Exception as e:
                self.logger.info(e)
                raise

            search_btn = self.wait.until(EC.element_to_be_clickable(DirectoryPage.search_btn))
            search_btn.click()
            self.wait.until(lambda d: len(d.find_elements(*DirectoryPage.employee_cards)) > 0)
            self.logger.info("Directory Search By Employee Name Completed")

        except Exception as e:
            self.logger.error("Directory Search Failed")
            self.logger.exception(e)
            raise

    def search_invalid_employee(self, employee_name):

        self.logger.info("Directory Invalid Search Started")
        self.open_directory()
        self.enter_text(DirectoryPage.employee_name, employee_name)
        self.click(DirectoryPage.search_btn)

    def get_error_message(self):
        return self.get_text(DirectoryPage.error_message)
    
    def verify_results_displayed(self):

        try:
            results = self.driver.find_elements(*DirectoryPage.employee_cards)
            return len(results) > 0

        except Exception:
            return False

    def get_employee_name(self):

        elements = self.driver.find_elements(*DirectoryPage.employee_name_results)
        return [e.text for e in elements]

    def search_by_job_title(self, job_title_name):

        try:
            self.logger.info("Directory Search By Job Title Started")

            self.open_directory()

            self.click(DirectoryPage.job_title)

            options = self.wait.until(
                lambda d: d.find_elements(*DirectoryPage.job_title_options)
            )

            for option in options:
                if job_title_name.strip().lower() == option.text.strip().lower():
                    option.click()
                    break

            self.click(DirectoryPage.search_btn)

            self.wait.until(lambda d: True)

            results = self.driver.find_elements(*DirectoryPage.employee_cards)

            if len(results) == 0:
                self.logger.info("No Results Found for Job Title")
            else:
                self.logger.info(f"Job Title Results Found: {len(results)}")

            self.logger.info("Directory Search By Job Title Completed")

            return results   # keep for test assertion

        except Exception as e:
            self.logger.error("Job Title Search Failed")
            self.logger.exception(e)
            raise

    def search_by_location(self, location_name):

        try:
            self.logger.info("Directory Search By Location Started")

            self.open_directory()

            self.click(DirectoryPage.location)

            options = self.wait.until(
                lambda d: d.find_elements(*DirectoryPage.location_options)
            )

            for opt in options:
                if location_name.lower() in opt.text.lower():
                    opt.click()
                    break

            self.click(DirectoryPage.search_btn)

            self.wait.until(lambda d: True)

            results = self.driver.find_elements(*DirectoryPage.employee_cards)

            if len(results) == 0:
                self.logger.info("No Results Found for Location")
            else:
                self.logger.info(f"Location Results Found: {len(results)}")

            self.logger.info("Directory Search By Location Completed")

            return results   # keep for assertion
        
        except Exception as e:
            self.logger.error("Location Search Failed")
            self.logger.exception(e)
            raise