import shutil
from datetime import datetime

from wallet import keplr
from app import utils
from app.account import AccountLoader
from app.config import ACC_SEI_PATH, HOME_TMP, ACC_SEI, CODE_HOME, get_logger
from app.enums import COLUMN_MAPPING, AccountStatus

logger = get_logger(__name__)


class BaseAuto(object):

    def __init__(self, **kwargs):
        self.list_account = []
        self.file_report = f"{HOME_TMP}/report_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        self.driver = None
        self.auto = None
        self.params = kwargs.get('params', {})

    def save_report(self, data: dict):
        list_index = list(COLUMN_MAPPING.values())

        format_data = []
        for k in list_index:
            value = data.get(k) if data.get(k) else ''
            format_data.append(value)

        utils.add_to_csv(self.file_report, format_data)

    def prepare_file_report(self):
        file_log_latest = utils.file_latest_in_path()
        if file_log_latest:
            index, row = utils.find_latest_row_index_log(file_log_latest)
            logger.info(f"Index: {index} - total account: {len(self.list_account)}")
            if index < len(self.list_account):
                # run not finish, use old file
                self.file_report = file_log_latest
                return index

        # prepare file report
        shutil.copyfile(f"{CODE_HOME}/account.sample.csv", self.file_report)
        return 0

    def process_all(self, method='deposit', **kwargs):
        method = getattr(self, method)
        if not method:
            raise Exception(f"Method {method} not found")

        # prepare list account
        index = self.prepare_file_report()
        list_account = self.list_account
        if index > 0:
            # continue from index in existing file report
            list_account = self.list_account[index:]

        for idx, account in enumerate(list_account):
            real_idx = idx + index
            logger.info(f"Request for account: {real_idx} - {account['address']}")

            if account.get('status') != AccountStatus.Inactive:
                # if account is active, run method
                try:
                    kwargs.update({
                        'account': account,
                    })
                    self.params.update({
                        'account_index': real_idx,
                    })
                    method(**kwargs)
                except Exception as e:
                    logger.error(e)

                self.driver.quit()
                self.driver = self.auto.launchSeleniumWebdriver()

            self.save_report(account)

        logger.info(f'Request Success for account len: {len(list_account)}')
        logger.info(f"file report: {self.file_report}")

    def swap(self, account: dict = None):
        pass

    def addLiquidity(self, account: dict = None):
        pass

    def removeLiquidity(self, account: dict = None):
        pass

    def stake(self, account: dict = None):
        pass

    def unstake(self, account: dict = None):
        pass

    def harvest(self, account: dict = None):
        pass

    def claim(self, account: dict = None):
        pass

    def farm(self, account: dict = None):
        pass


class KeplrAuto(BaseAuto):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.auto = keplr
        self.driver = self.auto.launchSeleniumWebdriver()
        self.list_account = AccountLoader(fp=ACC_SEI_PATH).parser_file()

        self.file_report = f"{HOME_TMP}/report_{ACC_SEI}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"

