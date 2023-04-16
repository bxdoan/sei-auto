import time
from selenium.webdriver.common.by import By

from wallet import keplr
from app.account import AccountLoader
from app.base import KeplrAuto
from app.config import get_logger


logger = get_logger(__name__)


CONFIG = {
    "environment": "test",
    "mainnet": {
        "url": "https://app.sparrowswap.xyz",
        "token": {
            "FRAX": "0x9b4e2c47e57d1331e6398cf605cbe895b4f93a87",
            "USDC": "0x67ae69fd63b4fc8809adc224a9b82be976039509",
            "ETH": "0x000000000000000000000000000000000000800a",
            "ETH2": "0x5300000000000000000000000000000000000004",
            "MKR": "0xbec22541ca80c4aec9baf6dee8880ee3c1bb612b",
        }
    },
    "test": {
        "url": "https://sei.eclipsepad.com/project/jumanji",
    },
}


class Eclipsepad(KeplrAuto):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.environment = CONFIG['environment']
        self.config = CONFIG[self.environment]

    def faucet(self, account: dict = None):

        keplr.switch_to_window(0)
        url = f"{self.config['url']}"
        self.driver.get(url)
        time.sleep(5)

        # close wellcome popup
        keplr.switch_to_window(0)
        keplr.click("//div[contains(text(), 'Jumanji Finance')]", 2)

        # setup metamask with seed phrase and password
        keplr.walletSetup(account['seed_phrase'], account['password'])

        keplr.click("//div[contains(text(), 'Jumanji Finance')]")

        # click on the Connect Wallet button
        keplr.click("//button[text()='Connect Wallet']", 3)

        # click on the keplr wallet button
        keplr.click("//div[text()='Keplr']", 3)

        keplr.approve()

        # click on the Connect Wallet button
        keplr.switch_to_window(0)
        keplr.click("//div[contains(text(), 'Jumanji Finance')]")
        keplr.click("//button[text()='Connect Wallet']", 3)

        # click on the keplr wallet button
        keplr.click("//div[text()='Keplr']", 3)

        # click on the Faucet
        count_faucet = 0
        while True:
            try:
                # try to back to main page
                keplr.switch_to_window(0)
                keplr.click("//div[contains(text(), 'Jumanji Finance')]", 0.1)
            except:
                pass

            try:
                keplr.click("//button[text()='Faucet']", 3)
                keplr.approve()
            except:
                pass
            logger.info(f"Process Faucet {count_faucet}")
            time.sleep(5)
            count_faucet += 1

        logger.info(f"Done Faucet {count_faucet}")

    def try_faucet(self):
        # click on the Faucet
        count_faucet = 0
        while True:
            if count_faucet > 200:
                break
            try:
                # try to back to main page
                keplr.switch_to_window(0)
                keplr.click("//div[contains(text(), 'Jumanji Finance')]", 0.1)
            except:
                pass

            try:
                keplr.click("//button[text()='Faucet']", 3)
                keplr.approve()
            except:
                pass
            logger.info(f"Process Faucet {count_faucet}")
            time.sleep(5)
            count_faucet += 1


if __name__ == '__main__':
    list_account = AccountLoader().parser_file()
    swap_params = {
        "account": list_account[0]
    }
    try:
        Eclipsepad().faucet(**swap_params)
    except Exception as e:
        logger.error(e)
