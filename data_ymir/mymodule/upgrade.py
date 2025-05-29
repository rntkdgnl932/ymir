import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

this_point_x_plus = 80

def upgrade_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check
    from chango import chango_start

    print("upgrade_start")

    try:
        jejak_start(cla)
        artifact_check(cla)

    except Exception as e:
        print(e)
        return 0

def jejak_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import menu_open_pure
    from boonhae_collection import boonhae_collection_start
    try:
        print("jejak_start")

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\jejak.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : jejak")

                # 제일 먼저 골동품

                for i in range(2):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\goldongpoom_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 100, 140, 900, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("goldongpoom_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(1000)

                result_make = jejak_make(cla)

                if result_make == False:
                    # 두번째로 아티팩트
                    for i in range(2):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\artifact_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 100, 140, 900, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("artifact_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(1000)

                    result_make = jejak_make(cla)

                    if result_make == False:
                        is_get = True
                    else:
                        is_get_count = 0
                else:
                    is_get_count = 0



            else:
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\jejak.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\jejak.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_jejak")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def jejak_make(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import menu_open_pure
    from boonhae_collection import boonhae_collection_start
    try:
        print("jejak_make")

        make = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\0_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(320, 110, 370, 900, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("0_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
            click_pos_2(720, 1015, cla)
            make = True
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\0_1_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(320, 110, 370, 900, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("0_1_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
                click_pos_2(720, 1015, cla)
                make = True

        for i in range(20):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\jejak_ing_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 300, 800, 400, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("jejak_ing_1", imgs_)
                break
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\jejak_ing_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 980, 800, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("jejak_ing_2", imgs_)
                    break
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\item_lack_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 400, 640, 440, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("item_lack_notice", imgs_)
                        make = False
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\jejak_result_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 400, 640, 540, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("jejak_result_notice", imgs_)
                            break
            time.sleep(0.1)
        if make == True:
            for i in range(10):
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\jejak_ing_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 300, 800, 400, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("jejak_ing_1", imgs_)
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\jejak_ing_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 980, 800, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("jejak_ing_2", imgs_)
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\jejak\\jejak_result_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 400, 640, 540, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("jejak_result_notice", imgs_)
                            click_pos_2(600, 800, cla)
                            break
                time.sleep(1)
        else:
            print("못 만듦")
        print("make", make)

        return make
    except Exception as e:
        print(e)
        return 0


def artifact_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import menu_open_pure
    from boonhae_collection import boonhae_collection_start
    try:
        print("artifact_check")

        this_point_x = 640 + this_point_x_plus
        this_point_y = 508
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\artifact.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : artifact")

                is_point = False
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\artifact\\art_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 300, 860, 860, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("art_point_1 :", imgs_)
                    click_pos_reg(imgs_.x + 80, imgs_.y, cla)
                    is_point = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\artifact\\art_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 300, 860, 860, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("art_point_2 :", imgs_)
                        click_pos_reg(imgs_.x + 80, imgs_.y, cla)
                        is_point = True

                if is_point == True:
                    for i in range(5):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("clean_screen close_1 : ", imgs_)
                            click_pos_2(555, 715, cla)
                            break
                        QTest.qWait(1000)
                    for i in range(5):
                        met = True
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\upgrade\\artifact\\condition_not_met_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(360, 510, 550, 580, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("condition_not_met_notice", imgs_)
                            met = False
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("clean_screen close_1 : ", imgs_)
                                click_pos_2(555, 715, cla)
                            else:
                                break
                        QTest.qWait(500)
                    if met == False:
                        for i in range(5):
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                break
                            QTest.qWait(500)


                else:
                    is_get = True
            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\artifact.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_2")
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0



