import unittest
from keyTestDemo import TestKeyWords
from time import sleep
from ddt import ddt, data, unpack

@ddt
class TestForKey(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        self.tk = TestKeyWords('https://www.baidu.com', 'Chrome')
    
    # 后置条件
    def tearDown(self) -> None:
        self.tk.quit_browser()
    
    # 测试用例 
    # 1. unittest所有的测试用例均为【test_*】
    # 2. setUp和tearDown分别在每条测试用例执行之前和之后执行一次
    # 3. *表示基于元组的形式处理，**表示字典，基于键值对的形式
    @data(['id','林黛玉'], ['id','薛宝钗'])
    @unpack
    def test_1(self, locator, input_value):
        # 关键字驱动
        self.tk.input_text(locator, 'kw', input_value)
        self.tk.click_element(locator, 'su')
        sleep(3)
    
    # def test_2(self):
    #     print('test_2')

if __name__ == '__main__':
    unittest.main()

