from selenium.webdriver.common.by import By

class buzzPage:
    post_image = (By.XPATH,"//div[@class='orangehrm-buzz-create-post-actions']/child::button[1]")
    share_btn = (By.XPATH,"//div[@class='oxd-form-actions orangehrm-buzz-post-modal-actions']/child::button[1]")
    buzz_file_input = (By.XPATH, "//div[@class='orangehrm-photo-input']//input[@type='file']")
    posted_image = (By.XPATH, "//div[@class='orangehrm-buzz-post-body-picture']/following::img[1]")