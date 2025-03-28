import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def mission_start(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_
    from action import juljun_on, juljun_check, fix_bag, attack_check
    from potion import potion_check

    print("mission_start", data)
    # 임무_필드_2
    try:



        result_juljun = juljun_check(cla)
        if result_juljun == True:

            fix_bag(cla)

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\juljun_mission_ing.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 130, 890, 180, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("juljun_mission_ing")

                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\juljun_mission_ing.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(760, 130, 890, 180, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("자동임무 수행중....")

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_complete_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(730, 70, 890, 240, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("mission_complete_btn", cla)
                            mission_get(cla, data)
                            time.sleep(10)
                            juljun_on(cla)
                        else:
                            result_attack = attack_check(cla)
                            if result_attack == False:
                                mission_get(cla, data)
                                time.sleep(10)
                                juljun_on(cla)

                            result_buy = potion_check(cla)
                            if result_buy == True:
                                break
                    else:
                        break
                    time.sleep(5)
            else:
                mission_get(cla, data)
                time.sleep(10)
                juljun_on(cla)
        else:
            mission_get(cla, data)
            time.sleep(10)
            juljun_on(cla)

    except Exception as e:
        print(e)
        return 0

def mission_get(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos
    from action import out_check, juljun_off, juljun_on, juljun_check, menu_open, dun_out
    from get_item import get_item_start
    from schedule import myQuest_play_add
    from clean_screen import clean_screen_start

    print("mission_get")

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:

        juljun_off(cla)

        print('huhh')

        # 먼저 던전이면 나가기
        dun_out(cla)

        print('jiji')

        # 드래그 횟수
        drag_count = 0

        # 임무_필드_2
        result_data = data.split("_")

        # 세부클릭 미리 설정
        if result_data[1] == "필드":
            if int(result_data[2]) > 10:
                y_multiply = 1
            else:
                y_multiply = int(result_data[2])
        elif result_data[1] == "정예":
            if int(result_data[2]) > 7:
                y_multiply = 8
            else:
                y_multiply = int(result_data[2])
        elif result_data[1] == "미궁":
            if int(result_data[2]) > 4:
                y_multiply = 5
            else:
                y_multiply = int(result_data[2])

        y_click = 105 + (y_multiply * 35)


        get_complete = False

        is_get = False
        is_get_count = 0

        while is_get is False:
            is_get_count += 1
            if is_get_count > 20:
                is_get = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : mission")

                print("y_click", y_click)

                if get_complete == False:

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\all_get_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(820, 910, 950, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("all_get_btn")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\anymore_get_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(370, 510, 500, 570, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("anymore_get_notice")
                            get_complete = True
                            break
                        time.sleep(0.1)


                # 필드 또는 정예 클릭
                if result_data[1] == "필드":
                    click_pos_2(50, 85, cla)
                    time.sleep(0.2)
                    click_pos_2(50, 85, cla)
                    time.sleep(0.2)
                elif result_data[1] == "정예":
                    click_pos_2(150, 85, cla)
                    time.sleep(0.2)
                    click_pos_2(150, 85, cla)
                    time.sleep(0.2)
                elif result_data[1] == "미궁":
                    click_pos_2(250, 85, cla)
                    time.sleep(0.2)
                    click_pos_2(250, 85, cla)
                    time.sleep(0.2)

                # 세부클릭하기
                click_pos_2(60, y_click, cla)
                time.sleep(0.2)
                click_pos_2(60, y_click, cla)
                time.sleep(0.2)

                # 지믈쇠빼고 클릭하기기
                y_reg_1 = 110
                y_reg_2 = 990

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\give_up_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_give = imgs_set_for(760, 110, 850, 990, cla, img, 0.8)
                if imgs_give is not None and imgs_give != False:
                    print("give_up_btn", imgs_give)
                    if len(imgs_give) > 0:
                        result_for = len(imgs_give) - 1
                        y_reg_1 = imgs_give[result_for][1] + 30

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\complete_mission.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(220, 110, 540, 990, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("complete_mission")
                    y_reg_2 = imgs_.y - 10

                ##############################################
                ### 받기 시작 ###


                is_get_btn = False


                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\90.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_for = imgs_set_for(250, y_reg_1 + 20, 600, y_reg_2, cla, img, 0.85)
                if imgs_for is not None and imgs_for != False:
                    print("90", imgs_for)
                    if len(imgs_for) > 0:
                        for i in range(len(imgs_for)):
                            click_pos_reg(840 + plus, imgs_for[i][1] - 10, cla)
                            time.sleep(0.2)
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                is_get_btn = True
                                break
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    is_get_btn = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_end_notice.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(250, 500, 530, 570, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        is_get_btn = True
                                        break

                            time.sleep(0.2)
                if is_get_btn == False:
                    ### 포기 다시 파악

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\give_up_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_give = imgs_set_for(760, 110, 850, 990, cla, img, 0.8)
                    if imgs_give is not None and imgs_give != False:
                        print("give_up_btn", imgs_give)
                        if len(imgs_give) > 0:
                            result_for = len(imgs_give) - 1
                            y_reg_1 = imgs_give[result_for][1] + 30
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 570, 480, 620, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_get_btn = True

                    ###
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\60.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_for = imgs_set_for(250, y_reg_1 + 20, 600, y_reg_2, cla, img, 0.85)
                    if imgs_for is not None and imgs_for != False:
                        print("60", imgs_for)
                        if len(imgs_for) > 0:
                            for i in range(len(imgs_for)):
                                click_pos_reg(840 + plus, imgs_for[i][1] - 10, cla)
                                time.sleep(0.2)
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    is_get_btn = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        is_get_btn = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_end_notice.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(250, 500, 530, 570, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            is_get_btn = True
                                            break

                                time.sleep(0.2)
                if is_get_btn == False:
                    ### 포기 다시 파악

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\give_up_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_give = imgs_set_for(760, 110, 850, 990, cla, img, 0.8)
                    if imgs_give is not None and imgs_give != False:
                        print("give_up_btn", imgs_give)
                        if len(imgs_give) > 0:
                            result_for = len(imgs_give) - 1
                            y_reg_1 = imgs_give[result_for][1] + 30
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 570, 480, 620, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_get_btn = True

                    ###
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\120.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_for = imgs_set_for(250, y_reg_1 + 20, 600, y_reg_2, cla, img, 0.85)
                    if imgs_for is not None and imgs_for != False:
                        print("120", imgs_for)
                        if len(imgs_for) > 0:
                            for i in range(len(imgs_for)):
                                click_pos_reg(840 + plus, imgs_for[i][1] - 10, cla)
                                time.sleep(0.2)
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    is_get_btn = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        is_get_btn = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_end_notice.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(250, 500, 530, 570, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            is_get_btn = True
                                            break

                                time.sleep(0.2)
                if is_get_btn == False:
                    ### 포기 다시 파악

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\give_up_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_give = imgs_set_for(760, 110, 850, 990, cla, img, 0.8)
                    if imgs_give is not None and imgs_give != False:
                        print("give_up_btn", imgs_give)
                        if len(imgs_give) > 0:
                            result_for = len(imgs_give) - 1
                            y_reg_1 = imgs_give[result_for][1] + 30
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 570, 480, 620, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_get_btn = True
                    ###
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\160.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_for = imgs_set_for(250, y_reg_1 + 20, 600, y_reg_2, cla, img, 0.85)
                    if imgs_for is not None and imgs_for != False:
                        print("160", imgs_for)
                        if len(imgs_for) > 0:
                            for i in range(len(imgs_for)):
                                click_pos_reg(840 + plus, imgs_for[i][1] - 10, cla)
                                time.sleep(0.2)
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    is_get_btn = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        is_get_btn = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_end_notice.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(250, 500, 530, 570, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            is_get_btn = True
                                            break

                                time.sleep(0.2)
                if is_get_btn == False:
                    ### 포기 다시 파악

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\give_up_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_give = imgs_set_for(760, 110, 850, 990, cla, img, 0.8)
                    if imgs_give is not None and imgs_give != False:
                        print("give_up_btn", imgs_give)
                        if len(imgs_give) > 0:
                            result_for = len(imgs_give) - 1
                            y_reg_1 = imgs_give[result_for][1] + 30
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 570, 480, 620, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_get_btn = True
                    ###
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\240.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_for = imgs_set_for(250, y_reg_1 + 20, 600, y_reg_2, cla, img, 0.85)
                    if imgs_for is not None and imgs_for != False:
                        print("240", imgs_for)
                        if len(imgs_for) > 0:
                            for i in range(len(imgs_for)):
                                click_pos_reg(840 + plus, imgs_for[i][1] - 10, cla)
                                time.sleep(0.2)
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    is_get_btn = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        is_get_btn = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_end_notice.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(250, 500, 530, 570, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            is_get_btn = True
                                            break

                                time.sleep(0.2)
                if is_get_btn == False:
                    ### 포기 다시 파악

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\give_up_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_give = imgs_set_for(760, 110, 850, 990, cla, img, 0.8)
                    if imgs_give is not None and imgs_give != False:
                        print("give_up_btn", imgs_give)
                        if len(imgs_give) > 0:
                            result_for = len(imgs_give) - 1
                            y_reg_1 = imgs_give[result_for][1] + 30
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 570, 480, 620, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_get_btn = True
                    ###
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\320.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_for = imgs_set_for(250, y_reg_1 + 20, 600, y_reg_2, cla, img, 0.85)
                    if imgs_for is not None and imgs_for != False:
                        print("320", imgs_for)
                        if len(imgs_for) > 0:
                            for i in range(len(imgs_for)):
                                click_pos_reg(840 + plus, imgs_for[i][1] - 10, cla)
                                time.sleep(0.2)
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    is_get_btn = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\full_get_notice2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(330, 500, 530, 570, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        is_get_btn = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_end_notice.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(250, 500, 530, 570, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            is_get_btn = True
                                            break

                                time.sleep(0.2)
                ###
                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 570, 480, 620, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_get_btn = True
                    time.sleep(0.2)
                ##############################################

                if is_get_btn == True:
                    for i in range(10):

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_ing_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 320, 560, 400, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            is_get = True
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\jadong_start_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 980, 820, 1040, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)

                else:
                    drag_count += 1
                    print("drag_count : ", drag_count)
                    if drag_count < 3:
                        drag_pos(550, 810, 550, 200, cla)
                    else:
                        if int(result_data[2]) == 1:
                            y_click += 35
                        else:
                            y_click -= 35
                        if y_click < 140 or y_click > 285:
                            is_get = True
                            for i in range(10):

                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_ing_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 320, 560, 400, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    is_get = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\jadong_start_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(680, 980, 820, 1040, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)



                    time.sleep(1)
                if is_get == True:
                    # 자동진행 꾸욱

                    for i in range(10):

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_ing_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 320, 560, 400, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\anymore_jadong_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(370, 380, 600, 455, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                clean_screen_start(cla)
                                myQuest_play_add(cla, data)
                                break
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\have_not_mission_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 500, 560, 600, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    clean_screen_start(cla)
                                    myQuest_play_add(cla, data)
                                    break

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(620, 690, 730, 740, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:

                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\end_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(720, 690, 860, 740, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\mission_start_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(720, 690, 860, 740, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\off.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(620, 690, 730, 740, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                        time.sleep(1)
                    

            else:

                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\menu_mission.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 430, 520, 510, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_mission")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open(cla)
                    time.sleep(0.5)
                    QTest.qWait(1000)

            time.sleep(1)

    except Exception as e:
        print(e)
        return 0


def mission_get_complete(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg
    from action import menu_open, dun_out
    from clean_screen import clean_screen_start

    print("mission_get_complete")

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:

        # 먼저 던전이면 나가기
        dun_out(cla)

        # 드래그 횟수
        drag_count = 0

        # 임무_필드_2
        result_data = data.split("_")

        # 세부클릭 미리 설정
        if result_data[1] == "필드":
            if int(result_data[2]) > 10:
                y_multiply = 1
            else:
                y_multiply = int(result_data[2])
        elif result_data[1] == "정예":
            if int(result_data[2]) > 7:
                y_multiply = 8
            else:
                y_multiply = int(result_data[2])
        elif result_data[1] == "미궁":
            if int(result_data[2]) > 4:
                y_multiply = 5
            else:
                y_multiply = int(result_data[2])

        y_click = 105 + (y_multiply * 35)

        get_complete = False

        is_get = False
        is_get_count = 0

        while is_get is False:
            is_get_count += 1
            if is_get_count > 10:
                is_get = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : mission")

                print("y_click", y_click)

                if get_complete == False:

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\all_get_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(820, 910, 950, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("all_get_btn")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\anymore_get_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(370, 510, 500, 570, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("anymore_get_notice")
                            get_complete = True
                            break
                        time.sleep(0.1)

                if get_complete == True:
                    is_get = True

            else:
                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\mission\\menu_mission.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 430, 520, 510, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_mission")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open(cla)
                    time.sleep(0.5)
                    QTest.qWait(1000)

            time.sleep(1)
        clean_screen_start(cla)
    except Exception as e:
        print(e)
        return 0


