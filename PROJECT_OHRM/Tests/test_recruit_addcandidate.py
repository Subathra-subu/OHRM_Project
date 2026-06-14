import pytest
from Actions.Recruit_CandidatesActions import Recruit_CandidatesActions
from Utilities.Logger import log_generator

@pytest.mark.usefixtures("test_setup_and_down")

class Testaddcandidate:
    
    logger = log_generator()
    
    def test_addVacancy_valid(self):
        
        self.logger.info("Test Started")
        
        candidateAction = Recruit_CandidatesActions(self.driver,self.wait)
        
        candidateAction.login_entervacancy()
        
        assert candidateAction.addCandidate_valid() is True
        
        self.logger.info("Test Ended")
        
    def test_addcandidate_blank(self):
        
        self.logger.info("Test Started")
        
        candidateAction = Recruit_CandidatesActions(self.driver,self.wait)
        
        candidateAction.login_entervacancy()
        
        assert candidateAction.addCandidate_blank() is True
        
        self.logger.info("Test Ended")