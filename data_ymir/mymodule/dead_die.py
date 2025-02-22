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
            is_dead = True

        if is_dead == True:
            # 스케쥴부터 불러오기
            result_schedule = myQuest_play_check(cla, "check")
            print("result_schedule", result_schedule)
            character_id = result_schedule[0][1]
            result_schedule_ = result_schedule[0][2]

            if result_schedule_ == "튜토육성":
                myQuest_play_add(cla, result_schedule_)

            potion_buy(cla)

    except Exception as e:
        print(e)
        return 0

