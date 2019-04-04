# -*- coding: utf-8 -*-
import sys
sys.path.append(r"E:\dontstop\testfile")
import test

resolution_x = 540 # 分辨率
resolution_y = 960 # 分辨率
package_name = 'com.Jelly.JellyFish' # JellyFish 包名
activity_name = 'com.unity3d.player.UnityPlayerActivity' # JellyFish 活动名

test1 = test.Test()
test1.connect(resolution_x, resolution_y) # 连接模拟器
test1.open_app(package_name, activity_name) # 打开待测试游戏
test1.random_touch(20, 2) # 随机点击测试，点击20次，间隔2秒
test1.random_drag(20, 3) # 随机滑动测试，滑动20次，间隔3秒
