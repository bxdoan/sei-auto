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
        "url": "https://app.astroport.fi",
        "token": {
            "FRAX": "0x9b4e2c47e57d1331e6398cf605cbe895b4f93a87",
            "USDC": "0x67ae69fd63b4fc8809adc224a9b82be976039509",
            "ETH": "0x000000000000000000000000000000000000800a",
            "ETH2": "0x5300000000000000000000000000000000000004",
            "MKR": "0xbec22541ca80c4aec9baf6dee8880ee3c1bb612b",
        }
    },
}


class Astroport(KeplrAuto):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.environment = CONFIG['environment']
        self.config = CONFIG[self.environment]

    def swap(self, account: dict = None):
        amount     = self.params.get('amount', "0.01")
        from_token = self.params.get('from_token')
        to_token   = self.params.get('to_token')
        percent    = self.params.get('percent')

        self.driver.close()
        self.auto.switch_to_window(0)
        url = f"{self.config['url']}/swap"
        self.driver.get(url)
        time.sleep(3)
        input_disclaimer = self.auto.try_finds("//input[@type='checkbox']")
        for id in input_disclaimer:
            id.click()
        self.auto.try_click("//button[contains(text(), 'Confirm')]", 2)
        self.auto.try_click("//button[contains(text(), 'Accept All Cookies')]", 2)

        # close wellcome popup
        self.auto.switch_to_window(0)
        # setup metamask with seed phrase and password
        keplr.walletSetup(account['seed_phrase'], account['password'])

        self.auto.switch_to_window(0)
        self.auto.try_click("//h2[contains(text(), 'Swap')]")
        self.auto.try_click("//span[contains(text(), 'Terra')]", 2)
        self.auto.try_click("//*[contains(@id, 'headlessui-switch')]", 4)
        self.auto.try_click("//div[contains(text(), 'Sei')]", 3)

        # click on the Connect Wallet button
        cnt_btn = self.auto.try_find("//p[contains(text(), 'Connect Wallet')]")
        self.auto.switch_to_window(0)
        cnt_btn.click()
        # click on the keplr wallet button
        self.auto.try_click("//p[contains(text(), 'Keplr')]", 3)
        self.auto.approve()

        # fill in swap form from token
        # Default is SEI
        self.auto.switch_to_window(0)
        time.sleep(5)
        opt_from = self.auto.try_find("//div[contains(text(), 'SEI')]")
        opt_to = self.auto.try_find("//div[contains(text(), 'ASTRO')]")

        if from_token != to_token and from_token != "SEI":
            # default is first token is SEI if to token is not SEI
            self._choose_token(from_token, opt_from)
        if from_token != to_token and from_token != "SEI":
            # default is second token is SEI if from token is not SEI
            self._choose_token(to_token, opt_to)

        if percent:
            # choose percent coin
            self.auto.click(f"//div[text()='{percent}']")
        else:
            # fill in amount
            inputs = self.driver.find_elements(By.XPATH, '//input')
            inputs[0].click()
            inputs[0].clear()
            inputs[0].send_keys(amount)

        time.sleep(5)

        # click button Swap
        self.auto.switch_to_window(0)
        self.auto.click("//button[contains(text(), 'Swap')]", 3)
        self.auto.click("//button[contains(text(), 'Confirm Swap')]", 3)

        # click button Confirm Swap
        self.auto.approve()

        volume = amount or percent
        account['description'] = f"Astroport {from_token} to {to_token} {volume} completed"
        logger.info("success")

    def _choose_token(self, token_symbol: str, locate_button):
        if token_symbol:
            locate_button.click()
            time.sleep(1)
            if token_symbol == "SEI":
                keplr.try_click('//*[@id="__next"]/div/div[1]/div[2]/main/div/div[1]/div[3]/div[3]/div[1]/div[1]/div/p[1]', 3)
            else:
                keplr.try_click(f"//p[text()='{token_symbol}']", 3)

    def addLiquidity(self, account: dict = None):
        pair   = self.params.get('pair')
        volume = self.params.get('volume')

        self.auto.switch_to_window(0)
        url = f"{self.config['url']}/pools/{pair}/provide"
        self.driver.get(url)
        time.sleep(3)
        input_disclaimer = self.auto.try_finds("//input[@type='checkbox']")
        for id in input_disclaimer:
            id.click()
        self.auto.try_click("//button[contains(text(), 'Confirm')]", 2)
        self.auto.try_click("//button[contains(text(), 'Accept All Cookies')]", 2)

        # setup metamask with seed phrase and password
        self.auto.switch_to_window(0)
        self.auto.walletSetup(account['seed_phrase'], account['password'])

        self.auto.switch_to_window(0)
        self.auto.try_click("//h2[contains(text(), 'Swap')]")
        self.auto.try_click("//span[contains(text(), 'Terra')]", 2)
        self.auto.try_click("//*[contains(@id, 'headlessui-switch')]", 4)
        self.auto.try_click("//div[contains(text(), 'Sei')]", 3)

        # click on the Connect Wallet button
        cnt_btn = self.auto.try_find("//p[contains(text(), 'Connect Wallet')]")
        self.auto.switch_to_window(0)
        cnt_btn.click()
        # click on the keplr wallet button
        self.auto.try_click("//p[contains(text(), 'Keplr')]", 3)
        self.auto.approve()
        time.sleep(5)

        self.auto.switch_to_window(0)
        url = f"{self.config['url']}/pools/{pair}/provide"
        self.driver.get(url)
        time.sleep(5)

        inputs = self.auto.try_finds('//input')
        inputs[0].click()
        inputs[0].clear()
        inputs[0].send_keys(volume)

        self.auto.try_click("//button[contains(text(), 'Add Liquidity')]", 3)
        self.auto.try_click("//button[contains(text(), 'Providing')]", 5)
        self.auto.approve()

        account['description'] = f"add liquidity {pair}"
        logger.info("success")

    def incentive(self, account: dict = None):
        keplr.switch_to_window(0)
        url = f"{self.config['url']}"
        self.driver.get(url)
        time.sleep(2)

        # close wellcome popup
        keplr.switch_to_window(0)

        # setup metamask with seed phrase and password
        keplr.walletSetup(account['seed_phrase'], account['password'])

        # click on the Connect Wallet button
        keplr.click("//div[text()='Connect Wallet']", 3)

        # click on the keplr wallet button
        portal = self.driver.find_element(By.CSS_SELECTOR, "sparrowblocks-portal")
        keplr_wallet = portal.find_elements(By.CSS_SELECTOR, "button")
        keplr_wallet[1].click()

        keplr.approve()

        # Swap 0.7 SEI to RUM
        keplr.switch_to_window(0)
        keplr.click("//p[contains(text(), 'Swap between')]")

        opt_to = keplr.try_find("//p[contains(text(), 'Select a token')]")
        self._choose_token("RUM", opt_to)

        # fill in amount
        inputs = self.driver.find_elements(By.XPATH, '//input')
        inputs[1].click()
        inputs[1].clear()
        inputs[1].send_keys("0,7")

        time.sleep(2)
        # click button Swap
        keplr.switch_to_window(0)
        keplr.click("//p[contains(text(), 'Swap between')]")
        swaps = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Swap')]")
        swaps[1].click()

        # click button Confirm Swap
        keplr.approve()
        keplr.try_click('//*[@id="__next"]/div/div[2]/div/div/button')
        time.sleep(15)

        # Swap 0.2 SEI to USDC
        keplr.switch_to_window(0)
        self.driver.get(url)
        time.sleep(2)
        keplr.try_click("//div[contains(text(), 'Enter the App')]")

        keplr.click("//p[contains(text(), 'Swap between')]")

        opt_to = keplr.try_find("//p[contains(text(), 'Select a token')]")
        self._choose_token("USDC", opt_to)

        # fill in amount
        inputs = self.driver.find_elements(By.XPATH, '//input')
        inputs[1].click()
        inputs[1].clear()
        inputs[1].send_keys("0,2")

        time.sleep(2)
        # click button Swap
        keplr.switch_to_window(0)
        keplr.click("//p[contains(text(), 'Swap between')]")
        swaps = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Swap')]")
        swaps[1].click()

        # click button Confirm Swap
        keplr.approve()
        keplr.try_click('//*[@id="__next"]/div/div[2]/div/div/button')
        time.sleep(15)

        # Add liquidity SEI-RUM with 30 RUM
        keplr.switch_to_window(0)
        self.driver.get(f"{self.config['url']}/liquidity/SEIRUM")
        time.sleep(2)

        # add liquidity
        keplr.try_click("//div[contains(text(), 'Enter the App')]")
        keplr.click("//div[contains(text(), 'Liquidity')]")

        inputs = self.driver.find_elements(By.XPATH, '//input')
        inputs[2].click()
        inputs[2].clear()
        inputs[2].send_keys("30")
        time.sleep(2)

        keplr.click("//button[contains(text(), 'Add')]")
        keplr.approve()
        keplr.try_click('//*[@id="__next"]/div/div[2]/div/div/button/span/svg')

        # Add liquidity SEI-USDC with 30 USDC
        keplr.switch_to_window(0)
        self.driver.get(f"{self.config['url']}/liquidity/SEIUSDC")
        time.sleep(2)

        # add liquidity
        keplr.click("//div[contains(text(), 'Enter the App')]")
        keplr.click("//div[contains(text(), 'Liquidity')]")

        inputs = self.driver.find_elements(By.XPATH, '//input')
        inputs[2].click()
        inputs[2].clear()
        inputs[2].send_keys("30")
        time.sleep(2)

        keplr.click("//button[contains(text(), 'Add')]")
        keplr.approve()
        keplr.try_click('//*[@id="__next"]/div/div[2]/div/div/button/span/svg')

        logger.info("success")

    def removeLiquidity(self, account: dict = None):
        keplr.switch_to_window(0)
        self.driver.get(f"{self.config['url']}/liquidity/SEIRUM")
        time.sleep(2)

        # remove liquidity
        keplr.try_click("//div[contains(text(), 'Enter the App')]")
        keplr.click("//div[contains(text(), 'Liquidity')]")

        inputs = self.driver.find_elements(By.XPATH, '//input')
        inputs[2].click()
        inputs[2].clear()
        inputs[2].send_keys("0,1")
        time.sleep(2)

        keplr.click("//button[contains(text(), 'Remove')]")
        keplr.approve()
        keplr.try_click('//*[@id="__next"]/div/div[2]/div/div/button/span/svg')

        logger.info("success")


if __name__ == '__main__':
    list_account = AccountLoader().parser_file()
    swap_params = {
        "account": list_account[0]
    }
    params = {
        "volume": "10",
        "amount": "0.3",
        "from_token": "SEI",
        "to_token": "ASTRO",
        "pair": "sei1memw56ewvpmh6qkg9jlyp25yxkc9r9la3mrvasaffrrxdts7vkrs5d3gl0",
    }
    try:
        # Astroport(params=params).incentive(**swap_params)
        # Astroport(params=params).swap(**swap_params)
        Astroport(params=params).addLiquidity(**swap_params)
        # Astroport(params=params).process_all(method='incentive')
    except Exception as e:
        logger.error(e)
