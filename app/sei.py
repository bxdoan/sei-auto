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
    },
    "test": {
    },
}


class Sei(KeplrAuto):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.environment = CONFIG['environment']
        self.config = CONFIG[self.environment]

    def send(self, account: dict = None):
        main_acc   = self.params['main_acc']
        amount     = self.params['amount']
        list_add   = self.params['list_add']

        keplr.switch_to_window(0)
        url = f"https://testnet.sparrowswap.xyz"
        self.driver.get(url)
        time.sleep(2)

        # close wellcome popup
        keplr.switch_to_window(0)
        keplr.click("//div[contains(text(), 'Enter the App')]", 3)

        # setup metamask with seed phrase and password
        keplr.walletSetup(main_acc['seed_phrase'], main_acc['password'])

        # click on the Connect Wallet button
        keplr.click("//div[text()='Connect Wallet']", 3)

        # click on the keplr wallet button
        portal = self.driver.find_element(By.CSS_SELECTOR, "sparrowblocks-portal")
        keplr_wallet = portal.find_elements(By.CSS_SELECTOR, "button")
        keplr_wallet[1].click()

        keplr.approve()

        keplr.switch_to_window(0)
        self.driver.get(keplr.EXT_URL)
        time.sleep(2)

        # choose sei network
        keplr.click(f'//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[1]', 2)
        keplr.click(f"//div[text()='{keplr.CHAIN_NAME}']", 2)

        # send SEI
        if list_add:
            for add in list_add:
                self._send(add, amount)
        else:
            self._send(account, amount)

        logger.info(f"Send success")

    def _send(self, to_acc: dict, amount: float) -> None:
        keplr.click("//button[contains(text(), 'Send')]", 2)

        inputs = self.driver.find_elements(By.CSS_SELECTOR, "input")
        inputs[0].send_keys(to_acc['address'])
        inputs[1].send_keys(amount)

        keplr.click("//button[contains(text(), 'Send')]", 2)
        keplr.click("//button[contains(text(), 'Approve')]", 5)

        logger.info(f"Send {amount} to {to_acc['address']}")


if __name__ == '__main__':
    list_account = AccountLoader().parser_file()
    swap_params = {
        "account": list_account[4],
    }
    params = {
        "main_acc": list_account[3],
        "amount": 5,
        # "list_add": [],
        "list_add": list_account[4:],
    }
    try:
        Sei(params=params).send(**swap_params)
    except Exception as e:
        logger.error(e)
