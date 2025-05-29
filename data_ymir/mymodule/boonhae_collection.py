import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def boonhae_collection_start(cla):


    try:

        print("boonhae_collection_start")

        collection_start(cla)

        boonhae_start(cla)

    except Exception as e:
        print(e)
        return 0


def collection_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, menu_open_pure
    from auction_game import auction_fast_start
    from clean_screen import clean_screen_start

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

                # 장비 6강 콜렉하기
                # 일반
                print("일반 6강")
                collection_upgrade(cla, 180)
                # 고급
                print("고급 6강")
                collection_upgrade(cla, 215)



                is_get = True
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\touch_me_close_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 980, 600, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("touch_me_close_notice", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
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

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_collection")
                                click_pos_reg(imgs_.x, imgs_.y - 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(0.5)
                    QTest.qWait(1000)
                if is_in == False:
                    is_get = True

            time.sleep(1)
        clean_screen_start(cla)
    except Exception as e:
        print(e)
        return 0



def collection_upgrade(cla, y_click):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, menu_open_pure
    from game_check import move_check
    from clean_screen import clean_screen_start

    try:
        print("collection_upgrade")

        this_point_x = 635
        this_point_y = 510
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 20:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : collection")

                click_pos_2(350, 85, cla)
                time.sleep(0.5)
                click_pos_2(80, y_click, cla)
                time.sleep(0.2)
                click_pos_2(80, y_click, cla)


                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\plus_6_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 160, 680, 1030, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("plus_6_1", imgs_)
                    click_pos_reg(imgs_.x - 15, imgs_.y - 15, cla)
                    upgrade = True
                    upgrade_count = 0

                    while upgrade is True:
                        upgrade_count += 1
                        if upgrade_count > 20:
                            upgrade = False

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\touch_me_close_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 980, 600, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("touch_me_close_notice", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            upgrade = False
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\daejangan.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 30, 200, 100, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("daejangan", imgs_)

                                is_stone = False
                                for i in range(4):
                                    stone = i + 1
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\ganghwa_stone_" + str(
                                        stone) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(700, 130, 960, 300, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("ganghwa_stone_", str(stone), imgs_)
                                        is_stone = True
                                        break

                                if is_stone == True:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\upgrade_checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(545, 950, 585, 1000, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("upgrade_checked", imgs_)
                                        for i in range(10):
                                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\touch_me_close_notice.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(380, 980, 600, 1040, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                break
                                            else:
                                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\ganghwa_btn.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(380, 980, 600, 1040, cla, img, 0.85)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("ganghwa_btn", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                            QTest.qWait(1000)


                                    else:
                                        click_pos_2(580, 975, cla)
                                else:
                                    upgrade = False

                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\upgrade_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(700, 930, 770, 1000, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("upgrade_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\plus_6_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(360, 160, 680, 1030, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("plus_6_1", imgs_)
                                        click_pos_reg(imgs_.x - 15, imgs_.y - 15, cla)
                        QTest.qWait(1000)

                    if upgrade == False:
                        # 업그레이드 후조치



                        print("ok")

                        is_collec = False

                        for i in range(5):
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\touch_me_close_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 980, 600, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("touch_me_close_notice", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)


                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\registration_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(750, 980, 880, 1030, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\registration_btn_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 690, 630, 760, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    is_collec = True
                                break
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\daejangan.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(20, 50, cla)

                            time.sleep(1)

                        if is_collec == False:
                            is_get = True
                            for i in range(5):
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\daejangan.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(20, 50, cla)
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\collection.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                time.sleep(1)
                else:
                    is_get = True
                    for i in range(5):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\daejangan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(20, 50, cla)
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                break
                        time.sleep(1)



            else:

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

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_collection")
                                click_pos_reg(imgs_.x, imgs_.y - 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(0.5)
                    QTest.qWait(1000)
                if is_in == False:
                    is_get = True

            time.sleep(1)
    except Exception as e:
        print(e)
        return 0

def boonhae_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import bag_open, cancle_all
    from game_check import move_check
    from clean_screen import clean_screen_start

    try:
        print("boonhae_start")



        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\boonhae_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(510, 310, 610, 375, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("boonhae_title")
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\not_checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(450, 460, 485, 500, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("not_checked common")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                if v_.onCollection_high == True:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\not_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(510, 460, 560, 500, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("not_checked high")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\boonhae_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(510, 310, 610, 375, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(625, 555, cla)
                    else:
                        is_get = True
                    time.sleep(0.5)

                if is_get == False:
                    cancle_all(cla)
                    is_get = True
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\bag_refresh_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(770, 980, 870, 1040, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("bag_refresh_btn")
                    click_pos_reg(imgs_.x, imgs_.y, cla)


                else:
                    bag_open(cla)

            time.sleep(1)

        clean_screen_start(cla)
    except Exception as e:
        print(e)
        return 0

