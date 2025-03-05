import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def boonhae_collection_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check
    from game_check import move_check
    from get_item import get_item_start


    try:
        print("boonhae_collection_start")
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\out_zero_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(615, 970, 680, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("out_zero_potion")


    except Exception as e:
        print(e)
        return 0


def collection_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, menu_open
    from game_check import move_check
    from get_item import get_item_start

    try:
        print("collection_start")

        this_point_x = 635
        this_point_y = 510
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : collection")

                for i in range(20):
                    # 장비 이전까지

                    is__point = False

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\collection_title_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 60, 300, 105, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("collection_title_point_1", imgs_)
                        is__point = True
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\collection_title_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 60, 300, 105, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("collection_title_point_2", imgs_)
                            is__point = True

                    if is__point == True:
                        click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                        time.sleep(0.5)

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\collection_des_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(100, 100, 160, 400, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("collection_des_point_1", imgs_)
                            click_pos_reg(imgs_.x - 50, imgs_.y + 5, cla)
                            time.sleep(0.5)

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\collection_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 150, 680, 1030, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("collection_point_1", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            time.sleep(0.5)

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\registration_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(750, 980, 880, 1030, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\registration_btn_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(490, 690, 630, 760, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                    else:
                        break

                    QTest.qWait(1000)
                for i in range(20):

                    is__point = False

                    # 장비는 고급까지
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\collection_title_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 60, 510, 105, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("collection_title_point_1", imgs_)
                        is__point = True
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\collection_title_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 60, 510, 105, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("collection_title_point_2", imgs_)
                            is__point = True

                    if is__point == True:

                        click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                        time.sleep(0.5)

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\collection_des_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(100, 150, 160, 220, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("collection_des_point_1", imgs_)
                            click_pos_reg(imgs_.x - 50, imgs_.y + 5, cla)
                            time.sleep(0.5)

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\collection_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 150, 680, 1030, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("collection_point_1", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                time.sleep(0.5)

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\registration_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(750, 980, 880, 1030, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\registration_btn_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 690, 630, 760, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                        else:
                            break
                    else:
                        break
                    QTest.qWait(1000)





                is_get = True
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\collection.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(20, 50, cla)
                    else:
                        break
                    time.sleep(1)

            else:
                menu_open(cla)
                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\collection.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                          this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_2")
                            click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

