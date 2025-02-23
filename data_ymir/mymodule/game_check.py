import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def check_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import confirm_all, macro_out
    from massenger import line_to_me
    try:
        print("game_check")

        # 장시간
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\long_time.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 880, 60, 930, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("long_time")
            why = "장시간 1????"
            line_to_me(cla, why)
            # 다시 시작
            macro_out(cla)
            time.sleep(1)
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\long_time2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 880, 60, 930, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                why = "장시간 2????"
                line_to_me(cla, why)
                macro_out(cla)
        # 캐릭터 선택
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\login_character_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(375, 410, 580, 470, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("login_character_title", imgs_)

            for i in range(5):
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\server_select_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(410, 550, 580, 610, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("server_select_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(830, 980, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                time.sleep(1)
        # 서버 점검
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\server_fix_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(290, 420, 660, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("server_fix_1")
            why = "서버 점검"
            line_to_me(cla, why)

            dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
            file_path = dir_path + "\\start.txt"
            # cla.txt
            cla_data = str(cla) + "cla"
            file_path2 = dir_path + "\\" + cla_data + ".txt"
            with open(file_path, "w", encoding='utf-8-sig') as file:
                data = 'no'
                file.write(str(data))
                time.sleep(0.2)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                data = cla
                file.write(str(data))
                time.sleep(0.2)
            os.execl(sys.executable, sys.executable, *sys.argv)

    except Exception as e:
        print(e)
        return 0


def move_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\check\\move\\move_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(60, 90, 120, 150, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:

            is_ = False
            is_count = 0
            is_not_count = 0
            while is_ is False:


                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\check\\move\\move_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 90, 120, 150, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("move_2", imgs_)
                    is_count += 1
                    is_not_count = 0
                    if is_count > 300:
                        is_ = True
                else:
                    is_not_count += 1
                    if is_not_count > 4:
                        is_ = True



                time.sleep(1)
    except Exception as e:
        print(e)
        return 0