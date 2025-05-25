import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def clean_screen_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from game_check import error_check2
    from action import out_check, macro_out
    from dead_die import dead_check
    from function_game import imgs_set_
    from massenger import line_to_me
    try:

        clean = False
        clean_count = 0

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\boohwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 900, 600, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("clean_screen_start : boohwal_btn")
            dead_check(cla)
        else:
            while clean is False:
                clean_count += 1
                print("clean_screen_start", clean_count)
                if clean_count > 2:
                    clean = True

                result_out = out_check(cla)
                QTest.qWait(1000)
                if result_out == True:
                    clean_screen_go(cla)
                    clean = True
                else:

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\check\\game_title_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, v_.now_cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        clean_screen_go(cla)
                        error_check2(cla)
                    else:
                        why = "게임 꺼짐"
                        line_to_me(cla, why)
                        macro_out(cla)


                QTest.qWait(1000)



    except Exception as e:
        print(e)
        return 0


def clean_screen_go(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import juljun_check, juljun_off, confirm_all, cancle_all, fix_bag
    from character_select_and_game_start import game_start_screen
    from schedule import myQuest_play_check
    from stop_event18 import _stop_please
    try:

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(500, 400, cla)
            result_schedule = myQuest_play_check(cla, "check")
            print("clean sreenresult_schedule", result_schedule)
            character_id = result_schedule[0][1]
            game_start_screen(cla, character_id)
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(500, 400, cla)
                result_schedule = myQuest_play_check(cla, "check")
                print("clean sreenresult_schedule", result_schedule)
                character_id = result_schedule[0][1]
                game_start_screen(cla, character_id)

            else:
                result_juljun = juljun_check(cla)
                if result_juljun == True:
                    juljun_off(cla)

                _stop_please(cla)

                confirm_all(cla)

                cancle_all(cla)


                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_for(0, 0, 960, 1040, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("clean_screen close_1 : ", imgs_)
                    if len(imgs_) > 0:
                        for i in range(len(imgs_)):
                            click_pos_reg(imgs_[i][0], imgs_[i][1], cla)
                            time.sleep(0.5)

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_for(0, 0, 960, 1040, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("clean_screen close_2 : ", imgs_)
                    if len(imgs_) > 0:
                        for i in range(len(imgs_)):
                            click_pos_reg(imgs_[i][0], imgs_[i][1], cla)
                            time.sleep(0.5)

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_for(0, 0, 960, 1040, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("clean_screen close_3 : ", imgs_)
                    if len(imgs_) > 0:
                        for i in range(len(imgs_)):
                            click_pos_reg(imgs_[i][0], imgs_[i][1], cla)
                            time.sleep(0.5)

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_for(0, 0, 550, 1040, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("clean_screen close_4 1 : ", imgs_)
                    if len(imgs_) > 0:
                        for i in range(len(imgs_)):
                            click_pos_reg(imgs_[i][0], imgs_[i][1], cla)
                            time.sleep(0.5)
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_for(610, 0, 960, 1040, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("clean_screen close_4 2 : ", imgs_)
                    if len(imgs_) > 0:
                        for i in range(len(imgs_)):
                            click_pos_reg(imgs_[i][0], imgs_[i][1], cla)
                            time.sleep(0.5)

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 550, 850, 650, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("clean_screen : menu_post")
                    click_pos_2(915, 50, cla)

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\event_1818.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_for(0, 0, 960, 1040, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("clean_screen event_1818 : ", imgs_)
                    if len(imgs_) > 0:
                        for i in range(len(imgs_)):
                            click_pos_reg(imgs_[i][0], imgs_[i][1], cla)
                            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0