import time
import pandas as pd
from app.enums import GasPrice
from selenium.webdriver.common.by import By
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains

from app import utils
from app.config import get_logger, WIDTH, HEADLESS, \
    EXTENSION_DIR_LEAP, EXTENSION_DIR, DRIVER_PATH

from app.config import PASSWORD, CODE_HOME, EXTENSION_ID_LEAP

logger = get_logger(__name__)

# download the newest version of keplr extension from:
# ref. https://chrome.google.com/webstore/detail/keplr/dmkamcknogkgcdfhhbddcghachkejeap
# or from  https://github.com/chainapsis/keplr-wallet
EXTENSION_ID = EXTENSION_ID_LEAP
EXT_URL = f"chrome-extension://{EXTENSION_ID}/index.html"
CHAIN_ID = 'atlantic-2'
CHAIN_NAME = f'Sei {CHAIN_ID}'
FILE_NAME = f"{CODE_HOME}/account.sei.csv"


def launchSeleniumWebdriver() -> webdriver:
    options = uc.ChromeOptions()
    options.add_argument(f"--load-extension={EXTENSION_DIR_LEAP},{EXTENSION_DIR}")
    prefs = {
        "extensions.ui.developer_mode": True,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)

    # add headless option
    if utils.force2bool(HEADLESS):
        logger.info('headless mode')
        options.add_argument('--headless')

    global driver
    driver = uc.Chrome(options=options)

    if WIDTH:
        driver.set_window_size(WIDTH, 1020)
    else:
        driver.set_window_size(1300, 1020)

    logger.info(f"Extension has been loaded successfully ")
    time.sleep(5)
    return driver


def try_find(xpath="", by=By.XPATH):
    try:
        return driver.find_element(by, xpath)
    except Exception as _e:
        return None


def try_finds(xpath="", by=By.XPATH):
    try:
        return driver.find_elements(by, xpath)
    except Exception as _e:
        return []


def try_click(xpath, time_to_sleep = None, by=By.XPATH) -> None:
    try:
        click(xpath, time_to_sleep, by)
    except:
        pass


def click(xpath, time_to_sleep = None, by=By.XPATH) -> None:
    if time_to_sleep is None:
        time_to_sleep = 1
    # Click once.
    # If click more times, try another method.
    button = driver.find_element(by, xpath)
    try:
        logger.info(f'click on "{button.text}"')
    except:
        pass
    clicking = ActionChains(driver).click(button)
    clicking.perform()
    time.sleep(time_to_sleep)


def insert_text(xpath, text) -> None:
    input_text = driver.find_element(By.XPATH, xpath)
    input_text.send_keys(text)
    time.sleep(0.5)


def walletSetup(recoveryPhrase : 'str', password : str) -> None:
    driver.execute_script("window.open('');")
    time.sleep(5)  # wait for the new window to open
    switch_to_window(-1)
    driver.get(f"{EXT_URL}")
    time.sleep(2)
    switch_to_window(-1)
    time.sleep(2)
    click("//div[contains(text(), 'Keplr')]", 5)

    # fill in recovery seed phrase
    seed_phrase_input = try_find('//textarea')
    seed_phrase_input.send_keys(recoveryPhrase)

    click("//div[contains(text(), 'Import Wallet')]", 2)
    click("//*[@id='root']/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]", 2)
    click("//div[contains(text(), 'Proceed')]", 2)

    inputs = try_finds('//input')
    inputs[0].send_keys(password)
    inputs[1].send_keys(password)
    click("//div[contains(text(), 'Proceed')]", 3)
    switch_to_window(0)
    time.sleep(2)


def switch_to_window(window_number):
    # Switch to another window, start from 0.
    try:
        wh = driver.window_handles
        logger.info(f'we have {len(wh)} windows')
        driver.switch_to.window(wh[window_number])
    except:
        pass
    logger.info(f'switched to window numer: {str(window_number)}')


def approve(gas=GasPrice.Average):
    time.sleep(3)
    switch_to_window(-1)
    if gas in GasPrice.all():
        try:
            click(f"//div[text()='{gas}']")
        except Exception as _e:
            pass

    try:
        click("//button[text()='Approve']", 5)
    except Exception as _e:
        pass


def reject():
    try:
        time.sleep(4)
        switch_to_window(-1)
        click("//button[text()='Reject']", 5)
    except:
        pass

