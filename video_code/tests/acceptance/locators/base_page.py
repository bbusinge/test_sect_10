from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'h1'  # same as tuple in python wc wd hv bn --> (By.TAG_NAME, 'h1')
    NAV_LINKS = By.CLASS_NAME, 'nav-link'
