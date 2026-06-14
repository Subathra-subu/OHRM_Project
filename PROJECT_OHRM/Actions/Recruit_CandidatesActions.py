from Actions.BaseActions import BaseActions
from Pages.RecruitmentPage import Recruit_VacanciesPage
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Utilities.CSVUtils import get_data


class Recruit_CandidatesActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def login_entervacancy(self):

        try:

            LoginActions.login(
                self,
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            self.js_click(Recruit_VacanciesPage.Recruitment)
            self.logger.info("Recruitment link clicked")

        except Exception as e:

            self.logger.error("Login failed")
            self.logger.exception(e)
            raise

    def addCandidate_valid(self):

        actions = ActionChains(self.driver)

        try:

            candidate_data = get_data("test_data/candidate_data.csv")

            self.js_click(Recruit_VacanciesPage.add)
            self.logger.info("Add button clicked")

            self.enter_text(Recruit_VacanciesPage.first_name, candidate_data[0][0])
            self.enter_text(Recruit_VacanciesPage.middle_name, candidate_data[0][1])
            self.enter_text(Recruit_VacanciesPage.last_name, candidate_data[0][2])

            self.click(Recruit_VacanciesPage.vacancy_dropdown)
            self.wait_for_visibility(Recruit_VacanciesPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

            self.enter_text(Recruit_VacanciesPage.email, candidate_data[0][3])
            self.enter_text(Recruit_VacanciesPage.contact_number, candidate_data[0][4])
            self.enter_text(Recruit_VacanciesPage.keywords, candidate_data[0][5])

            self.js_click(Recruit_VacanciesPage.save)
            self.logger.info("Save button clicked")

            self.wait_for_visibility(Recruit_VacanciesPage.candidate_profile_message)
            return self.is_displayed(Recruit_VacanciesPage.candidate_profile_message)

        except Exception as e:

            self.logger.error("Add candidate failed")
            self.logger.exception(e)
            raise
        
    def addCandidate_blank(self):

        try:

            self.click(Recruit_VacanciesPage.add)
            self.logger.info("Add button clicked")

            self.js_click(Recruit_VacanciesPage.save)
            self.logger.info("Save button clicked")

            return self.is_displayed(Recruit_VacanciesPage.required_messages)

        except Exception as e:

            self.logger.error("Blank candidate test failed")
            self.logger.exception(e)
            raise