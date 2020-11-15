import unittest
from selenium import webdriver
from pageObject.searchPage import SearchPage
from time import sleep
from ddt import ddt, data, unpack

@ddt
class TestCases(unittest.TestCase):
    # 前置条件
    # -> None 表示是否存有返回值
    def setUp(self) -> None:
        driver = webdriver.Chrome()
        self.sp = SearchPage(driver)

    # 后置条件
    def tearDown(self) -> None:
        self.sp.quit_browser()

    # 测试用例
    @data(['https://www.baidu.com', '林黛玉'], ['https://www.baidu.com', '贾宝玉'])
    @unpack
    def test_1(self, url, input_text):
        self.sp.check(url, input_text)
        sleep(3)
        print('test')
        # self.assertEqual(self.sp.get_tittle(), '百度一下，你就知道', msg='对不起，你不知道')

if __name__ == '__main__':
    unittest.main()