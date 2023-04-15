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
        "url": "https://testnet.sparrowswap.xyz",
        "token": {
            "FRAX": "0x9b4e2c47e57d1331e6398cf605cbe895b4f93a87",
            "USDC": "0x67ae69fd63b4fc8809adc224a9b82be976039509",
            "ETH": "0x000000000000000000000000000000000000800a",
            "ETH2": "0x5300000000000000000000000000000000000004",
            "MKR": "0xbec22541ca80c4aec9baf6dee8880ee3c1bb612b",
        }
    },
}


class Sparrows(KeplrAuto):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.environment = CONFIG['environment']
        self.config = CONFIG[self.environment]

    def swap(self, account: dict = None):
        amount     = self.params.get('amount', "0.01")
        from_token = self.params.get('from_token')
        to_token   = self.params.get('to_token')
        percent    = self.params.get('percent')

        keplr.switch_to_window(0)
        url = f"{self.config['url']}"
        self.driver.get(url)
        time.sleep(2)

        # close wellcome popup
        keplr.switch_to_window(0)
        keplr.click("//div[contains(text(), 'Enter the App')]", 3)

        # setup metamask with seed phrase and password
        keplr.walletSetup(account['seed_phrase'], account['password'])

        # click on the Connect Wallet button
        keplr.click("//div[text()='Connect Wallet']", 3)

        # click on the keplr wallet button
        portal = self.driver.find_element(By.CSS_SELECTOR, "sparrowblocks-portal")
        keplr_wallet = portal.find_elements(By.CSS_SELECTOR, "button")
        keplr_wallet[1].click()

        keplr.approve()

        # fill in swap form from token
        # Default is SEI
        main = self.driver.find_element(By.CSS_SELECTOR, "main")
        # of = main.find_elements(By.CSS_SELECTOR, "p[text()='SEI']")
        opt_from = keplr.try_find("//p[contains(text(), 'SEI')]")
        opt_to = keplr.try_find("//p[contains(text(), 'Select a token')]")

        if from_token != to_token and from_token != "SEI":
            # default is first token is ETH if to token is not ETH
            self._choose_token(from_token, opt_from)
        if from_token != to_token and from_token != "SEI" and to_token not in ["SEI"]:
            # default is second token is ETH if from token is not ETH
            self._choose_token(to_token, opt_to)

        if percent:
            # choose percent coin
            keplr.click(f"//div[text()='{percent}']")
        else:
            # fill in amount
            inputs = self.driver.find_elements(By.XPATH, '//input')
            inputs[0].click()
            inputs[0].send_keys(amount)

        time.sleep(2)

        # click button Swap
        keplr.click("//button[text()='Swap']", 5)

        # click button Confirm Swap
        keplr.approve()

        volumn = amount or percent
        account['description'] = f"syncswap {from_token} to {to_token} {volumn} completed"
        logger.info("success")

    def _choose_token(self, token_symbol: str, locate_button):
        if token_symbol:
            locate_button.click()
            time.sleep(1)
            keplr.click(f"//p[text()='{token_symbol}']", 3)


if __name__ == '__main__':
    list_account = AccountLoader().parser_file()
    swap_params = {
        "account": list_account[1]
    }
    params = {
        "percent": "1/2",
        "amount": "0.05",
        "from_token": "RUM",
        "to_token": "SEI",
    }
    try:
        Sparrows(params=params).swap(**swap_params)
        # Sparrows(params=params).process_all(method='swap')
    except Exception as e:
        logger.error(e)
