#coding=utf-8

import unittest
import HTMLTestRunner


def all_case():
    dis_path="F:\\Testpro\\testcase"  #testcase address
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(dis_path,pattern='test*.py',top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTest(test_case)
    print(testcase)
    return testcase

if __name__=="__main__":
    report_path=input()
    #runner=unittest.TextTestRunner()
    fp=open(report_path,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="testreport",description="simple")
    runner.run(all_case())
    fp.close()