import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2
    import os
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check, macro_out
    from game_check import move_check
    from massenger import line_to_me
    try:
        print("tuto_start")

        result_out = out_check(cla)
        if result_out == True:
            out_check(cla)
            tuto_go(cla)
        else:
            # 미션 실패시 알람하기
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\mission_failed.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 180, 530, 230, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("mission_failed")
                why = "미션실패했다 정비해보자"
                line_to_me(cla, why)

                macro_out(cla)


            # 실수로 메뉴 클릭시....
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("menu_post")
                click_pos_2(920, 55, cla)
            else:
                tuto_story(cla)
            tuto_skip(cla)

    except Exception as e:
        print(e)
        return 0


def tuto_go(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import confirm_all, out_check
    from game_check import move_check
    try:

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\tuto_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(830, 90, 860, 140, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            is_tuto = False
            is_tuto_count = 0
            while is_tuto is False:


                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\tuto_ing.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(830, 90, 860, 140, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("tuto_ing", imgs_)
                    move_check(cla)
                    is_tuto_count = 0

                else:
                    print("물음표?")

                    clicked = False
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\ready_quest.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(830, 60, 960, 130, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("tuto_go : ready_quest")
                        clicked = True

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\ready_quest2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(830, 60, 960, 130, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("tuto_go : ready_quest")
                        clicked = True
                    if clicked == True:
                        tuto_click(cla)
                    else:
                        is_tuto_count += 1
                        if is_tuto_count > 3:
                            is_tuto = True
                        tuto_skip(cla)
                time.sleep(1)

        else:
            tuto_click(cla)
            tuto_story(cla)
    except Exception as e:
        print(e)
        return 0

def tuto_click(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import confirm_all, out_check
    from game_check import move_check
    try:

        is_tuto = False
        is_tuto_count = 0
        while is_tuto is False:
            is_tuto_count += 1
            if is_tuto_count > 10:
                is_tuto = True

            clicked = False


            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\ready_quest2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(830, 60, 960, 130, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("ready_quest2")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clicked = True
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\ready_quest.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(830, 60, 960, 130, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("ready_quest")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    clicked = True

            if clicked == True:
                im_move_not = False

                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\im_move_not.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 480, 660, 600, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("im_move_not")
                        im_move_not = True
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\segesoo.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(415, 95, 660, 170, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("segesoo")
                            im_move_not = True
                            break
                    time.sleep(0.1)
                if im_move_not == True:
                    click_pos_2(800, 115, cla)
                    is_tuto = True

                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\quest_gesipan_notice_300_90_650_160.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 90, 650, 160, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("quest_gesipan_notice_300_90_650_160")
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\quest_gesipan_notice_10_50_170_215.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 50, 170, 215, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                        time.sleep(0.1)



                else:
                    print("빠른이동 오케이하기")
                    is_tuto = True
                    for i in range(5):
                        result_confirm = confirm_all(cla)
                        if result_confirm == True:
                            break
                        QTest.qWait(1000)
            else:
                print("물음표??")
                result_out = out_check(cla)
                if result_out == True:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\tuto_ing.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(830, 90, 860, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("tuto_ing", imgs_)
                    else:
                        click_pos_2(800, 115, cla)
                        is_tuto = True
                else:
                    tuto_skip(cla)
            time.sleep(1)
    except Exception as e:
        print(e)
        return 0
def tuto_skip(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:
        skip_result = False
        is_skip = False
        is_skip_count = 0
        while is_skip is False:
            is_skip_count += 1
            if is_skip_count > 10:
                is_skip = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\skip\\skip_top_right_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(830, 30, 960, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("skip_top_right_1")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_skip = True
                skip_result = True
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\skip\\skip_top_right_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(830, 30, 960, 80, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("skip_top_right_2")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_skip = True
                    skip_result = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\skip\\screen_touch_bottom.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 720, 600, 1040, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("screen_touch_bottom")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_skip = True
                        skip_result = True
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\skip\\screen_touch_bottom2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 720, 600, 1040, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("screen_touch_bottom")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            is_skip = True
                            skip_result = True

            time.sleep(1)
        return skip_result
    except Exception as e:
        print(e)
        return 0


def tuto_story(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    from massenger import line_to_me
    from action import confirm_all, out_check, macro_out
    try:
        is_stroy = False
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\disir.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("title : disir")
            is_stroy = True
            click_pos_2(895, 1010, cla)
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\jejak.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : jejak")
                is_stroy = True

                for i in range(20):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\jejak_result_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 410, 550, 500, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(480, 750, cla)

                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\jejak_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(610, 980, 820, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\cancle_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(610, 980, 820, 1040, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("제작중")
                                time.sleep(2)
                    time.sleep(1)
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\balkeyly.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("title : balkeyly")
                    click_pos_2(830, 200, cla)
                    time.sleep(1)
                    click_pos_2(860, 1010, cla)
                    time.sleep(1)
                    is_stroy = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\daejangan.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("title : daejangan")

                        for i in range(20):
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\safe_ganghwa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(340, 950, 500, 990, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(480, 1010, cla)
                                break
                            else:
                                click_pos_2(740, 170, cla)
                            time.sleep(1)

                        for i in range(20):
                            result_skip = tuto_skip(cla)
                            if result_skip == True:
                                break

                            time.sleep(1)
                        is_stroy = True
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\dongbanja.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("title : dongbanja")
                            is_stroy = True
                            click_pos_2(895, 1010, cla)
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\out_gesipan.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 240, 960, 800, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("title : out_gesipan")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\quest.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("title : quest")
            why = "의뢰"
            click_pos_2(810, 155, cla)
            # line_to_me(cla, why)
            time.sleep(2)

            for i in range(20):

                result_out = out_check(cla)
                if result_out == True:

                    result_confirm = confirm_all(cla)
                    if result_confirm == True:
                        break
                else:
                    result_skip = tuto_skip(cla)
                    if result_skip == True:
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\quest.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(810, 155, cla)
                            is_stroy = True
                            break
                time.sleep(1)
        else:
            # 버섯스프
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\bag_refresh_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 980, 870, 1040, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("bag_refresh_btn")

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\busut_supe.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(720, 110, 960, 1000, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("busut_supe", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    is_stroy = True

            else:
                # 사가
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\saga.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:

                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\saga_story_ravenshall_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 330, 840, 380, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            why = "수동해야 한다"
                            line_to_me(cla, why)
                            macro_out(cla)
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\saga.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(145, 525, cla)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\saga_story_ravenshall_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(740, 330, 840, 380, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                        time.sleep(1)
        if is_stroy == True:
            clean_screen_start(cla)
    except Exception as e:
        print(e)
        return 0