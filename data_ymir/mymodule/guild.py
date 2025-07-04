import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def guild_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check
    from chango import chango_start

    print("guild_start")

    try:
        guild_check(cla)

    except Exception as e:
        print(e)
        return 0

def guild_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import menu_open_pure
    from boonhae_collection import boonhae_collection_start
    try:
        print("guild_check")

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : guild")

                #####################
                # 지원
                # 아직 모름
                #####################

                #####################
                # 기술
                #####################
                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\guild_money_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 300, 540, 360, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("guild_money_title", imgs_)
                        click_pos_2(540, 740, cla)
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild_skill.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("title : guild_skill")
                            click_pos_2(240, 540, cla)
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(835, 365, cla)
                                time.sleep(1)
                    QTest.qWait(500)
                for i in range(35):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 570, 480, 620, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("cancle 1", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\guild_money_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 300, 540, 360, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("guild_money_title", imgs_)
                            click_pos_2(540, 740, cla)
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild_skill.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("title : guild_skill")
                                click_pos_2(240, 540, cla)
                            else:
                                click_pos_2(835, 365, cla)
                                time.sleep(1)
                    QTest.qWait(500)
                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("title : guild")
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\guild_money_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 300, 540, 360, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("guild_money_title", imgs_)
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\cancle.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(340, 570, 480, 760, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("cancle", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\cancle2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(340, 570, 480, 760, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("cancle 2", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild_skill.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("title : guild_skill")
                                click_pos_2(30, 50, cla)

                    QTest.qWait(1000)

                #####################
                # 활동
                #####################
                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\anymore_aim_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 500, 600, 600, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("anymore_aim_notice", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\anymore_get_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 500, 600, 600, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("anymore_get_notice", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild_hwaldong.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("title : guild_hwaldong")
                                click_pos_2(870, 1010, cla)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(765, 365, cla)
                    QTest.qWait(500)

                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\anymore_aim_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 500, 600, 600, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("anymore_aim_notice", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\anymore_get_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 500, 600, 600, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("anymore_get_notice", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild_hwaldong.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("title : guild_hwaldong")
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\all_get_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(720, 970, 860, 1030, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    click_pos_2(55, 145, cla)
                    QTest.qWait(500)

                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("title : guild")
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild_hwaldong.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("title : guild")
                            click_pos_2(30, 50, cla)


                    QTest.qWait(1000)




                #####################
                # 창고[기부]
                #####################
                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\anymore_donation_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 500, 600, 600, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("anymore_donation_notice", imgs_)

                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\donation_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 570, 630, 630, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("donation_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\guild_donation_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 300, 540, 390, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("guild_donation_title", imgs_)

                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\donation_money.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(420, 420, 500, 500, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("donation_money", imgs_)

                                    click_pos_reg(695, 655, cla)

                                    time.sleep(0.5)

                                    click_pos_2(610, 710, cla)
                                else:
                                    click_pos_2(310, 390, cla)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    print("title : guild")
                                    click_pos_2(530, 275, cla)

                                QTest.qWait(1000)
                    QTest.qWait(500)
                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\guild_donation_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 300, 540, 390, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\cancle.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(270, 570, 480, 760, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("cancle", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\guild\\cancle2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(270, 570, 480, 760, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("cancle 2", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    QTest.qWait(1000)

                # if is_get == True:
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("title : guild")
                            click_pos_2(30, 50, cla)
                    QTest.qWait(1000)

                is_get = True




            else:
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\guild.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\guild.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_guild")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0





