from selenium.webdriver.chromium.webdriver import ChromiumDriver

from Runner import *


class realRunner(Runner):
    weight = [0.1, 0.3, 0.4, 0.2]
    word = ["人机验证"]

    def logic(self, WebBrowser: ChromiumDriver):
        SingleChoiceInTwo(WebBrowser, 1, [0.5, 0.5])
        SingleChoice(WebBrowser, 2, self.weight)
        SingleChoice(WebBrowser, 3, self.weight)
        SingleChoice(WebBrowser, 4, self.weight)
        SingleChoice(WebBrowser, 5, self.weight)
        SingleChoice(WebBrowser, 6, self.weight)
        SingleChoiceInTwo(WebBrowser, 7, [0.5, 0.5])
        MultiChoice(WebBrowser, 8, self.weight)
        MultiChoice(WebBrowser, 9, self.weight)
        FillBlank(WebBrowser, 10, self.word)
        SubmitResult(WebBrowser)
        pass


if __name__ == '__main__':
    runner = realRunner()
    runner.run("https://www.wjx.cn/vm/PHEWDay.aspx",10)
