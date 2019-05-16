# _*_ coding:utf-8 _*_
"""单元测试及生成覆盖率报告"""

import coverage
from UnitTest01 import *

cov = coverage.coverage(source=['UnitTest01','Monkey','MonkeySender'])
cov.start()

doUnitTest()

cov.stop()
cov.report()
cov.html_report(directory='covhtml')

