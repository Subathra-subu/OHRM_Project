import pytest
from Actions.Recruit_VacanciesActions import Recruit_VacanciesActions
from PROJECT_OHRM.Tests.test_Recruit_addvacancy import Testaddvacancy
from Utilities.Logger import log_generator

@pytest.mark.usefixtures("test_setup_and_down")

class Testsearchvacancy(Testaddvacancy):
    
    logger = log_generator()
    
    def test_searchvacancy_valid(self):
        
        self.logger.info("Test Started")
        
        vacancyAction = Recruit_VacanciesActions(self.driver,self.wait)
        
        vacancyAction.login_entervacancy()
        
        assert vacancyAction.searchVacancy() is True
        
        self.logger.info("Test Ended")