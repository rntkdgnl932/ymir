import time
# import os
import sys

from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def _stop_please(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_check
    from character_select_and_game_start import game_start_screen
    try:
        print("_stop_please")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(830, 980, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            result_schedule = myQuest_play_check(cla, "check")
            print("clean sreenresult_schedule", result_schedule)
            character_id = result_schedule[0][1]
            game_start_screen(cla, character_id)
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(830, 980, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                result_schedule = myQuest_play_check(cla, "check")
                print("clean sreenresult_schedule", result_schedule)
                character_id = result_schedule[0][1]
                game_start_screen(cla, character_id)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\18_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(70, 600, 350, 770, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("18_1")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\18_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(70, 600, 350, 770, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("18_2")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\18_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 350, 860, 410, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("18_3")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\event_1818.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 350, 860, 410, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("event_1818")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\18_4.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 350, 860, 410, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("18_4")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
        # full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("18_1")
        #     click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0



