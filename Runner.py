from abc import abstractmethod

from selenium.webdriver.chromium.webdriver import ChromiumDriver

from mainUtil import *


class Runner:
    def run(self, targetURL: str, times: int):
        while times >= 0:
            try:

                ip=self.new_ip()
                option = webdriver.ChromeOptions()
                option.add_experimental_option('excludeSwitches', ['enable-automation'])
                option.add_experimental_option('useAutomationExtension', False)
                if ip!=None:
                    option.add_argument(f"--proxy-server=http://{ip}")

                broswer = webdriver.Chrome(options=option)
                broswer.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                                        {
                                            'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
                broswer.get(targetURL)
                time.sleep(1)
                self.logic(broswer)
            except Exception as e:
                print(e)
                pass
            times -= 1

    @abstractmethod
    def logic(self, WebBrowser: ChromiumDriver):
        pass

    def new_ip(self) -> str:
        return None
