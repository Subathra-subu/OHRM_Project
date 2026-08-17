import pytest
from Actions.ClaimActions import ClaimActions
from Utilities.Logger import log_generator

@pytest.mark.usefixtures("test_setup_and_down")

class TestAssignClaim:
    
    logger = log_generator()
    
    def test_assignClaim_valid(self):
        
        self.logger.info("Test Started")
        
        claimAction = ClaimActions(self.driver,self.wait)
        
        claimAction.login_entervacancy()
        
        assert claimAction.assign_claim()==True
        
        self.logger.info("Test Ended")
        
    def test_submitClaim_valid(self):
            
            self.logger.info("Test Started")
            
            claimAction = ClaimActions(self.driver,self.wait)
            
            claimAction.login_entervacancy()
            
            assert claimAction.submitClaim()==True
            
            self.logger.info("Test Ended")