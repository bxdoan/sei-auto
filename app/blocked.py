import time
from selenium.webdriver.common.by import By

from wallet import leap
from app.account import AccountLoader
from app.base import LeapAuto
from app.config import get_logger, ACC_SEI_PATH

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
        "url": "https://edge.blocked.cc/products/1",
    },
}


class Blocked(LeapAuto):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.environment = CONFIG['environment']
        self.config = CONFIG[self.environment]

    def faucet(self, account: dict = None):

        leap.switch_to_window(0)
        time.sleep(3)
        url = f"{self.config['url']}"
        self.driver.get(url)
        time.sleep(5)
        # close wellcome popup
        leap.switch_to_window(0)

        self._try_signup(account)
        self.driver.refresh()
        self._try_login(account)

        # setup metamask with seed phrase and password
        self.auto.walletSetup(account['seed_phrase'], account['password'])

        time.sleep(5)
        self.auto.try_click("//h1[contains(text(), 'Sei')]", 2)
        self.login_twitter(account)
        time.sleep(5)
        self.auto.try_click("//h1[contains(text(), 'Sei')]", 2)
        self.login_discord(account)
        self.driver.get(url)
        time.sleep(5)
        logger.info(f"Done incentive for blocked account {account['dis_email']}")

    def _try_signup(self, account):
        try:
            self.auto.click("//button[contains(text(), 'Sign up')]", 2)
            email_input = self.auto.try_find(":r0:", By.ID)
            email_input.send_keys(account['dis_email'])
            username_input = self.auto.try_find(":r1:", By.ID)
            username_input.send_keys(account['dis_email'].split('@')[0])
            password_input = self.auto.try_find(":r2:", By.ID)
            password_input.send_keys(account['password'])
            time.sleep(1)
            signup_btns = self.auto.try_finds("//button[contains(text(), 'Sign up')]")
            signup_btns[-1].click()
        except Exception as _e:
            logger.error(_e)

    def _try_login(self, account):
        try:
            time.sleep(2)
            self.auto.click("//button[contains(text(), 'Sign in')]")
            email_input = self.auto.try_find(":r0:", By.ID)
            email_input.send_keys(account['dis_email'])
            password_input = self.auto.try_find(":r1:", By.ID)
            password_input.send_keys(account['password'])
            time.sleep(1)
            self.auto.click("//button[contains(text(), 'Log in')]", 2)
        except Exception as _e:
            logger.error(_e)


if __name__ == '__main__':
    # list_account = AccountLoader().parser_file()
    list_account = AccountLoader(fp=ACC_SEI_PATH).parser_file()
    swap_params = {
        "account": list_account[5]
    }
    try:
        Blocked().faucet(**swap_params)
    except Exception as e:
        logger.error(e)
