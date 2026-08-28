from selenium.webdriver.common.by import By

class buzzPage:

    post_image = (
        By.XPATH,
        "//div[@class='orangehrm-buzz-create-post-actions']/child::button[1]"
    )

    share_btn = (
        By.XPATH,
        "//div[@class='oxd-form-actions orangehrm-buzz-post-modal-actions']/child::button[1]"
    )

    buzz_file_input = (
        By.XPATH,
        "//input[@type='file' and contains(@class,'oxd-file-input')]"
    )

    image_preview = (
        By.XPATH,
        "//div[contains(@class,'orangehrm-buzz-post-modal')]//img"
    )

    posted_image = (
        By.XPATH,
        "//div[@class='orangehrm-buzz-post-body-picture']/following::img[1]"
    )

    textarea = (
        By.XPATH,
        "//div[@class='oxd-buzz-post oxd-buzz-post--active']/textarea"
    )

    postbutton = (
        By.XPATH,
        "//div[@class='orangehrm-buzz-create-post-header-text']/descendant::button[1]"
    )
    threedot = (
        By.XPATH,
        "//div[@class='oxd-grid-1 orangehrm-buzz-newsfeed-posts']/div[1]/descendant::button[1]"
    )
    editpostBUT = (
        By.XPATH,"//ul[@class='oxd-dropdown-menu']/descendant::p[2]"
    )
    deletepostBUT = (
        By.XPATH,"//ul[@class='oxd-dropdown-menu']/descendant::p[1]"
    )
    textarea_edit = (
        By.XPATH,
        "//div[@class='orangehrm-buzz-post-modal-header-text']/descendant::textarea"
    )
    edit_post_btn = (
        By.XPATH,   
        "//div[@class='oxd-form-actions orangehrm-buzz-post-modal-actions']/descendant::button[1]"
    )
    delete_post_btn = (
        By.XPATH,
        "//div[@class='orangehrm-modal-footer']/child::button[2]"
    )
    @staticmethod
    def posted_text_locator(message):
        return (
            By.XPATH,
            f"//p[contains(@class,'orangehrm-buzz-post-body-text') and normalize-space()='{message}']"
        )