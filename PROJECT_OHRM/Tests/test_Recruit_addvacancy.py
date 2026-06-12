import pytest
from Actions.Recruit_VacanciesActions import Recruit_VacanciesActions
from Utilities.Logger import log_generator

@pytest.mark.usefixtures("test_setup_and_down")

class Testaddvacancy:
    
    logger = log_generator()
    
    def test_addVacancy_valid(self):
        
        self.logger.info("Test Started")
        
        vacancyAction = Recruit_VacanciesActions(self.driver,self.wait)
        
        vacancyAction.login_entervacancy()
        
        assert vacancyAction.addVacancy() is True
        
        self.logger.info("Test Ended")
        
        
    def test_addVacancy_blank(self):
        
        self.logger.info("Test Started")
        
        vacancyAction = Recruit_VacanciesActions(self.driver,self.wait)
        
        vacancyAction.login_entervacancy()
    
        assert vacancyAction.addinvalidvacancy() is True
        
        self.logger.info("Test Ended")
    
    
    def test_addVacancy_exsist(self):
        
        self.logger.info("Test Started")
        
        vacancyAction = Recruit_VacanciesActions(self.driver,self.wait)
        
        vacancyAction.login_entervacancy()
    
        assert vacancyAction.addexistvacancy() is True
        
        self.logger.info("Test Ended")