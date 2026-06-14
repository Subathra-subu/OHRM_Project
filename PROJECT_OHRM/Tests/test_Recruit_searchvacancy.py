import pytest
from Actions.Recruit_VacanciesActions import Recruit_VacanciesActions
from Utilities.Logger import log_generator
import time

@pytest.mark.usefixtures("test_setup_and_down")

class Testsearchvacancy():
    
    logger = log_generator()
    
    def test_searchvacancy_valid(self):
        
        self.logger.info("Test Started")
        
        vacancyAction = Recruit_VacanciesActions(self.driver,self.wait)
        
        vacancyAction.login_entervacancy()
        
        assert vacancyAction.searchVacancy()==True
        
        self.logger.info("Test Ended")
        
    def test_searchvacancy_blank(self):
        
        self.logger.info("Test Started")
        
        vacancyAction = Recruit_VacanciesActions(self.driver,self.wait)
        
        vacancyAction.login_entervacancy()
        
        assert vacancyAction.searchVacancy_blank()==True
        
        self.logger.info("Test Ended")
      