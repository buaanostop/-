# -*- coding: utf-8 -*-
import unittest
from Monkey import *
import HTMLTestRunner
from Operation import *
class TestMonkeyFunc(unittest.TestCase):
    """Test Monkey.py"""
    def test01_connect(self):
        """Test method connect()"""
        self.assertTrue(connect())

    def test02_open_app(self):
        """Test method open_app(package_name, activity_name)"""
        self.assertTrue(open_app("com.Jelly.JellyFish","com.untiy3d.player.UnityPlayerActivity"))

    def test03a_set_resolution_ratio(self):
        """Test method set_resolution_ratio(width, height)"""
        self.assertTupleEqual((720,1280),set_resolution_ratio(720,1280))

    def test03b_set_resolution_ratio(self):
        """Test method set_resolution_ratio(width, height)"""
        self.assertTupleEqual((1080,1920),set_resolution_ratio(1080,1920))
        
    def test04a_touch(self):
        """Test method touch(pos_x, pos_y, touch_number=1, interval_time=1.0)"""
        opright = Operation('touch', ((100,200),), 1, 1.0, 0, 0, 0)
        optest = touch(100, 200)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)
        
    def test04b_touch(self):
        """Test method touch(pos_x, pos_y, touch_number=1, interval_time=1.0)"""
        opright = Operation('touch', ((200,400),), 5, 1.5, 0, 0, 0)
        optest = touch(200,400,5,1.5)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test05a_long_touch(self):
        """Test method long_touch(pos_x, pos_y, touch_time=1.0, touch_number=1, interval_time=1.0)"""
        opright = Operation('long_touch',((100,200),),1,1.0,1.0,0,0)
        optest = long_touch(100,200)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test05b_long_touch(self):
        """Test method long_touch(pos_x, pos_y, touch_time=1.0, touch_number=1, interval_time=1.0)"""
        opright = Operation('long_touch',((200,400),),5,0.5,2.2,0,0)
        optest = long_touch(200,400,2.2,5,0.5)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test06a_multi_touch(self):
        """Test method multi_touch(pointlist, loop_number=1, interval_time = 1.0, loop_time = 1.0)"""
        pointlist = ((1,1),(222,333),(577,600))
        opright = Operation('multi_touch',pointlist, 1, 1.0, 0, 0, 1.0)
        optest = multi_touch(pointlist)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test06b_multi_touch(self):
        """Test method multi_touch(pointlist, loop_number=1, interval_time = 1.0, loop_time = 1.0)"""
        pointlist = ((1,1),(222,333),(577,600),(200,2),(300,3),(100,1),(200,2))
        opright = Operation('multi_touch',pointlist, 5, 2.0, 0, 0, 0.5)
        optest = multi_touch(pointlist,5,2.0,0.5)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test07a_random_touch(self):
        """Test method random_touch(pointlist, touch_number=1, interval_time=1.0)"""
        opright = Operation('random_touch', None, 1, 1.0, 0, 0, 0)
        optest = random_touch(None)
        self.assertEqual(opright.optype, optest.optype)
        self.assertIsNone(optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test07b_random_touch(self):
        """Test method random_touch(pointlist, touch_number=1, interval_time=1.0)"""
        pointlist = ((1,1),(300,300))
        opright = Operation('random_touch', pointlist, 100, 0.5, 0, 0, 0)
        optest = random_touch(pointlist, 100, 0.5)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test08a_drag(self):
        """Test method drag(pointlist, drag_time=1.0, drag_number=1, interval_time=1.0)"""
        pointlist = ((30,40),(50,60))
        opright = Operation('drag',pointlist, 1, 1.0, 1.0, 0, 0)
        optest = drag(pointlist)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test08b_drag(self):
        """Test method drag(pointlist, drag_time=1.0, drag_number=1, interval_time=1.0)"""
        pointlist = ((299,300),(433,60))
        opright = Operation('drag',pointlist, 5, 0.1, 2.3, 0, 0)
        optest = drag(pointlist, 2.3, 5, 0.1)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test09a_multi_drag(self):
        """Test method multi_drag(pointlist, loop_number=1, interval_time = 1.0, drag_time=1.0, loop_time = 1.0)"""
        point1 = (1,2,3,4)
        point2 = (20,30,40,50)
        point3 = (33,44,77,88)
        pointlist = (point1,point2,point3)
        opright = Operation('multi_drag',pointlist, 1, 1.0, 1.0, 0, 1.0)
        optest = multi_drag(pointlist)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test09b_multi_drag(self):
        """Test method multi_drag(pointlist, loop_number=1, interval_time = 1.0, drag_time=1.0, loop_time = 1.0)"""
        point1 = (1,2,3,4)
        point2 = (20,30,40,50)
        point3 = (33,44,77,88)
        point4 = (300,400,1000,1020)
        pointlist = (point1,point2,point3,point4)
        opright = Operation('multi_drag',pointlist, 10, 0.5, 2.0, 0, 10.0)
        optest = multi_drag(pointlist, 10, 0.5, 2.0, 10.0)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)
        
    def test10a_random_drag(self):
        """Test method random_drag(pointlist, drag_number=1, interval_time=1.0, drag_time=1.0)"""
        opright = Operation('random_drag',None, 1, 1.0, 1.0, 0, 0)
        optest = random_drag(None)
        self.assertEqual(opright.optype, optest.optype)
        self.assertIsNone(optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test10b_random_drag(self):
        """Test method random_drag(pointlist, drag_number=1, interval_time=1.0, drag_time=1.0)"""
        pointlist = ((1,1),(1000,1000))
        opright = Operation('random_drag',pointlist, 100, 0.5, 2.0, 0, 0)
        optest = random_drag(pointlist, 100, 0.5, 2.0)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test11a_touch_drag(self):
        """Test method touch_drag(pointlist, touch_time=1.0, drag_time=1.0, touch_number=1, interval_time=1.0)"""
        pointlist = ((300,300),(300,400))
        opright = Operation('touch_drag',pointlist, 1, 1.0, 1.0, 0, 1.0)
        optest = touch_drag(pointlist)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test11b_touch_drag(self):
        """Test method touch_drag(pointlist, touch_time=1.0, drag_time=1.0, touch_number=1, interval_time=1.0)"""
        pointlist = ((303,305),(307,404))
        opright = Operation('touch_drag',pointlist, 5, 0.5, 2.0, 0, 1.5)
        optest = touch_drag(pointlist, 1.5, 2.0, 5, 0.5)
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test12a_press(self):
        """Test method press(key_name)"""
        home = "KEYCODE_HOME"
        opright = Operation('press', None, 0, 0, 0, "KEYCODE_HOME", 0)
        optest = press(home)
        self.assertEqual(opright.optype, optest.optype)
        self.assertIsNone(optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test12b_press(self):
        """Test method press(key_name)"""
        back = "KEYCODE_BACK"
        opright = Operation('press', None, 0, 0, 0, "KEYCODE_BACK", 0)
        optest = press(back)
        self.assertEqual(opright.optype, optest.optype)
        self.assertIsNone(optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test13a_typestr(self):
        """Test method typestr(typestring)"""
        opright = Operation('typestr', None, 0, 0, 0, "Hello World", 0)
        optest = typestr("Hello World")
        self.assertEqual(opright.optype, optest.optype)
        self.assertIsNone(optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test13b_typestr(self):
        """Test method typestr(typestring)"""
        opright = Operation('typestr', None, 0, 0, 0, "", 0)
        optest = typestr("")
        self.assertEqual(opright.optype, optest.optype)
        self.assertIsNone(optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test14_wait(self):
        """Test method wait(wait_time)"""
        opright = Operation('wait', None, 0, 0, 0, 0, 0.5)
        optest = wait(0.5)
        self.assertEqual(opright.optype, optest.optype)
        self.assertIsNone(optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)        

    def test15_start(self):
        """Test method start()"""
        clear()
        touch(1,1)
        touch(2,2,2,0.5)
        long_touch(1,1)
        long_touch(2,2,0.5,2,0.5)
        multi_touch(((1,1),(2,2)),2,0.5,0.5)
        random_touch(None,2,0.5)
        random_touch(((1,1),(100,100)),2,0.5)
        drag(((1,1),(5,5)),0.5,2,0.5)
        multi_drag(((1,1,2,2),(2,2,3,3)),2,0.5,0.5,0.5)
        random_drag(None,2,0.5,0.5)
        random_drag(((1,1),(10,10)),2,0.5,0.5)
        touch_drag(((1,1),(5,5)),0.5,0.5,2,0.5)
        press("KEYCODE_HOME")
        typestr("hello world")
        self.assertTrue(start())

    def test16_pause(self):
        """Test method pause()"""
        self.assertTrue(pause())

    def test17_resume(self):
        """Test method resume()"""
        self.assertTrue(resume())

    def test18_stop(self):
        """Test method stop()"""
        self.assertTrue(stop())

    def test19_clear(self):
        """Test method clear()"""
        touch(1,1)
        oplisttest = clear()
        self.assertEqual(0, len(oplisttest))

    def test20_delete(self):
        """Test method delete(index)"""
        clear()
        touch(1,1)
        touch(2,2)
        touch(3,3)
        oplisttest = delete(2)
        self.assertEqual(2, len(oplisttest))

    def test21_change(self):
        """Test method change(index1, index2)"""
        clear()
        touch(1,1)
        touch(2,2)
        touch(3,3)
        opright = Operation('touch', ((3,3),), 1, 1.0, 0, 0, 0)
        oplisttest = change(2, 3)
        optest = oplisttest[1]
        self.assertEqual(opright.optype, optest.optype)
        self.assertTupleEqual(opright.pointlist, optest.pointlist)
        self.assertEqual(opright.number, optest.number)
        self.assertEqual(opright.interval_time, optest.interval_time)
        self.assertEqual(opright.hold_time, optest.hold_time)
        self.assertEqual(opright.keyorstring, optest.keyorstring)
        self.assertEqual(opright.wait_time, optest.wait_time)

    def test22_save(self):
        """Test method save(save_name)"""
        touch(1,1)
        touch(2,2)
        self.assertTrue(save("unittestsave"))

    def test23_load(self):
        """Test method load(save_name)"""
        clear()
        touch(1,1)
        touch(2,2)
        save("unittestsave")
        oplisttest = load("unittestsave")
        opright1 = Operation('touch', ((1,1),), 1, 1.0, 0, 0, 0)
        opright2 = Operation('touch', ((2,2),), 1, 1.0, 0, 0, 0)
        optest1 = oplisttest[0]
        optest2 = oplisttest[1]
        self.assertEqual(opright1.optype, optest1.optype)
        self.assertTupleEqual(opright1.pointlist, optest1.pointlist)
        self.assertEqual(opright1.number, optest1.number)
        self.assertEqual(opright1.interval_time, optest1.interval_time)
        self.assertEqual(opright1.hold_time, optest1.hold_time)
        self.assertEqual(opright1.keyorstring, optest1.keyorstring)
        self.assertEqual(opright1.wait_time, optest1.wait_time)
        self.assertEqual(opright2.optype, optest2.optype)
        self.assertTupleEqual(opright2.pointlist, optest2.pointlist)
        self.assertEqual(opright2.number, optest2.number)
        self.assertEqual(opright2.interval_time, optest2.interval_time)
        self.assertEqual(opright2.hold_time, optest2.hold_time)
        self.assertEqual(opright2.keyorstring, optest2.keyorstring)
        self.assertEqual(opright2.wait_time, optest2.wait_time)

    def test24a_all_random(self):
        """Test method all_random(test_number=100)"""
        self.assertTrue(all_random(5))

    def test24b_all_random(self):
        """Test method all_random(test_number=100)"""
        self.assertTrue(all_random())

    def test25_close(self):
        """Test method close()"""
        self.assertTrue(close())
        
if __name__ == '__main__':
    test = unittest.TestSuite()
    test.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMonkeyFunc))
    file_path = "UnitTestReport.html"

    file_result = open(file_path, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result,
                                           title = u"单元测试报告",
                                           description = u"用例执行情况")
    runner.run(test)
    file_result.close()
