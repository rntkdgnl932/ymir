import sys
import os
import time
import requests
from PyQt5.QtTest import *
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
        imgs_ = imgs_set_(0, 60, 880, 930, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("long_time")
            why = "장시간 1????"
            line_to_me(cla, why)
            # 다시 시작
            macro_out(cla)
            time.sleep(1)
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\jangsigan_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 60, 880, 930, cla, img, 0.7)
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
        macro_out = False
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\server_fix_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(290, 420, 660, 660, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("server_fix_1")
            macro_out = True
            why = "서버 점검"
        else:
            # 게임접속 실패
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\login_failed.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(290, 420, 800, 800, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("login_failed")
                macro_out = True
                why = "게임접속실패"

        if macro_out == True:
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

        is__move = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\check\\move\\move_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(60, 90, 120, 150, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:

            is__move = True

            is_ = False
            is_count = 0
            is_not_count = 0
            while is_ is False:


                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\check\\move\\move_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 90, 120, 150, cla, img, 0.95)
                if imgs_ is not None and imgs_ != False:
                    print("move_2", imgs_)
                    is_count += 1
                    is_not_count = 0
                    if is_count > 300:
                        is_ = True
                else:
                    is_not_count += 1
                    if is_not_count > 3:
                        is_ = True



                time.sleep(1)

        return is__move
    except Exception as e:
        print(e)
        return 0

def loading_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import macro_out
    from massenger import line_to_me
    try:

        is_loading = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\loading\\loading.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(870, 940, 960, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:

            is_loading = True

            is_ = False
            is_count = 0
            is_not_count = 0
            while is_ is False:


                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\loading\\loading.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(870, 940, 960, 1040, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:

                    if is_count % 5 == 0:
                        print("loading...", str(is_count), "초" ,imgs_)
                    is_count += 1
                    is_not_count = 0
                    if is_count > 300:
                        is_ = True
                        why = "로딩하는데 300초 이상 걸렸다."
                        line_to_me(cla, why)
                        macro_out(cla)
                else:
                    is_not_count += 1
                    if is_not_count > 3:
                        is_ = True



                time.sleep(1)

        return is_loading
    except Exception as e:
        print(e)
        return 0

def error_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import macro_out
    from massenger import line_to_me
    try:
        is_err = False
        for i in range(5):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\move_ticket_lack_notice.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 30, 550, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("move_ticket_lack_notice")
                why = "이동서 부족하다는 에러"
                line_to_me(cla, why)
                macro_out(cla)
                break
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chaejib\\not_complete_quest_notice.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(340, 380, 600, 470, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("not_complete_quest_notice", imgs_)
                    is_err = True
                    break

            time.sleep(0.2)
        return is_err
    except Exception as e:
        print(e)
        return 0


def error_check2(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import macro_out
    from massenger import line_to_me
    try:
        black_screen = False

        for i in range(5):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\pakit_gamji_notice.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 30, 960, 1040, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("pakit_gamji_notice")
                why = "비정상적인 패킷 감지했다는 에러"
                line_to_me(cla, why)
                macro_out(cla)
                break
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\black_screen.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 1)
                if imgs_ is not None and imgs_ != False:
                    print("black_screen")
                    black_screen = True
                    break
            time.sleep(0.2)
        black_screen_count = 0
        while black_screen is True:

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\black_screen.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 1)
            if imgs_ is not None and imgs_ != False:
                black_screen_count += 1
                print("black_screen =>", black_screen_count, "초")
                if black_screen_count > 300:
                    why = "블랙스크린이다"
                    line_to_me(cla, why)
                    macro_out(cla)
            else:
                black_screen = False
            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0


def dun_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:

        is_dun = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\out_dun_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(160, 30, 230, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("out_dun_1", imgs_)
            is_dun = True
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\out_dun_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(160, 30, 230, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("out_dun_2", imgs_)
                is_dun = True



        return is_dun
    except Exception as e:
        print(e)
        return 0


