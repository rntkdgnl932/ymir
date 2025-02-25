import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dead_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check
    from game_check import move_check
    from potion import potion_buy
    from schedule import myQuest_play_check, myQuest_play_add

    try:
        print("dead_check")

        is_dead = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\boohwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 900, 600, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_btn")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_dead = True

        if is_dead == True:
            # 스케쥴부터 불러오기
            dead_after(cla)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dead_die\\out_dead_point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 850, 560, 900, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out_dead_point", imgs_)
            dead_recovery(cla)

    except Exception as e:
        print(e)
        return 0



def dead_after(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check
    from game_check import move_check
    from potion import potion_buy
    from schedule import myQuest_play_check, myQuest_play_add

    try:
        print("dead_after")

        # 스케쥴부터 불러오기
        result_schedule = myQuest_play_check(cla, "check")
        print("result_schedule", result_schedule)
        character_id = result_schedule[0][1]
        result_schedule_ = result_schedule[0][2]

        if result_schedule_ == "튜토육성" or "의뢰" in result_schedule_:
            myQuest_play_add(cla, result_schedule_)

        potion_buy(cla)

    except Exception as e:
        print(e)
        return 0



def dead_recovery(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start

    try:
        print("dead_recovery")

        # 스케쥴부터 불러오기
        is_recovery = False
        is_recovery_count = 0
        while is_recovery is False:
            is_recovery_count += 1
            if is_recovery_count > 7:
                is_recovery = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dead_die\\exp_recover_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("exp_recover_title", imgs_)

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dead_die\\exp.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 60, 100, 120, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("exp", imgs_)

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dead_die\\free_recover.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 920, 230, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("free_recover", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        click_pos_2(100, 850, cla)
                        time.sleep(0.5)
                        click_pos_2(150, 945, cla)
                        time.sleep(0.5)
                else:
                    clean_screen_start(cla)
                    is_recovery = True
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dead_die\\out_dead_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 850, 560, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("out_dead_point", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0


