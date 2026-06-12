import pytest
from Actions.Recruit_VacanciesActions import Recruit_VacanciesActions
from Utilities.Logger import log_generator

class Testvacancy:
    
    logger = log_generator()
    
    @pytest.mark.usefixtures("test_setup_and_down")
    
    def test_addVacancy(self):
        
        self.logger.info("Test Started")
        
        vacancyAction = Recruit_VacanciesActions(self.driver,self.wait)
        
        vacancyAction.login_entervacancy()
        
        vacancyAction.addVacancy()
        
        self.logger.info("Test Ended")