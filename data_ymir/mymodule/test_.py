import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos
    from action import out_check, juljun_off, juljun_on, juljun_check, confirm_all, attack_check
    from game_check import move_check
    from get_item import get_item_start
    from potion import potion_buy
    from chango import go_chango, chango_start
    from request import request_get, request_start
    from clean_screen import clean_screen_go

    print("test")
    cla = "one"

    plus = 0


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

        # request_get(cla, "외뢰_1")

        # request_start(cla, "외뢰_1")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\end_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 630, 630, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("end_btn")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\cancle_all\\cancle_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(340, 540, 480, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("cancle_btn")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\juljun\\juljun_middle_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(280, 920, 680, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("juljun_potion")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\click_request_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(835, 135, 920, 190, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("click_request_btn", imgs_)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\request_complete_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(835, 135, 920, 190, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("request_complete_btn", imgs_)

        prohibition = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prohibition"
        prohibition_list = os.listdir(prohibition)

        complete = False

        # 의뢰_1 => 이둔골짜기
        # 의뢰_2 => 레이븐스홀
        # 의뢰_3 => 아스가르드성
        # 의뢰_4 => 헤르모드의갈림길

        data = "의뢰_1"

        result_request_step = data.split("_")
        y_reg_1 = 140
        # result_request_step[1] => step
        if result_request_step[1] == "1":
            print("의뢰_이둔골짜기")
        elif result_request_step[1] == "2":
            print("레이븐스홀")
            y_reg_1 = 175
        elif result_request_step[1] == "3":
            print("아스가르드성")
            y_reg_1 = 215
        elif result_request_step[1] == "4":
            print("헤르모드의갈림길")
            y_reg_1 = 250

        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("request_get_count", is_spot_count)
            if is_spot_count > 15:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("quest", imgs_)

                click_pos_2(60, y_reg_1, cla)
                time.sleep(0.5)
                click_pos_2(60, y_reg_1, cla)
                time.sleep(0.5)

                # 여기서 분별 잘해서 받도록 하자
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\complete_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(770, 130, 910, 190, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("complete_1", imgs_)
                    is_spot = True
                    complete = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prerequisites.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(770, 130, 910, 190, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("prerequisites", imgs_)
                        is_spot = True
                        complete = True
                    else:
                        ##############//////////////////####################
                        # 아랫값 정하기
                        y_reg_3 = 1040

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\complete_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 130, 910, y_reg_3, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("complete_1", imgs_)
                            y_reg_3 = imgs_.y

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prerequisites.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 130, 910, y_reg_3, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("prerequisites", imgs_)
                            if y_reg_3 > imgs_.y:
                                y_reg_3 = imgs_.y

                        print("y_reg_3", y_reg_3)
                        if y_reg_3 < 190:
                            complete = True
                        else:
                            y_scan_1 = 50  # 120
                            y_scan_2 = 120  # 190

                            click_y = 85  # 155

                            for s in range(10):
                                y_scan_1 += 70
                                y_scan_2 += 70
                                click_y += 70
                                print("y_scan_1, y_scan_2, click_y", y_scan_1, y_scan_2, click_y)
                                if y_scan_2 > y_reg_3:
                                    complete = True

                                    break
                                else:
                                    is_prohibition_y = 200
                                    is_prohibition = False
                                    for i in range(len(prohibition_list)):
                                        result_prohibition_list = prohibition_list[i].split(".")
                                        read_data = result_prohibition_list[0]
                                        print("read_data", read_data)
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prohibition\\" + str(
                                            read_data) + ".PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(210, y_scan_1, 460, y_scan_2, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            print("prohibition_list", imgs_)
                                            is_prohibition = True
                                    # 금지 안되어 있으면 클릭하고
                                    if is_prohibition == False:
                                        click_pos_2(840, click_y, cla)
                                        break
                                    # 금지 되어 있으면 다음꺼 클릭하기 위함인데
                                    # y_reg_3 이건 완료 또는 불가능한 최소값
                                    # 그래서 이번에 금지된것이고, y_scan_1, y_scan_2 의 범주내에 최소값이 있으면 퀘스트 완료로 간주
                                    else:

                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\complete_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(770, y_scan_1, 910, y_scan_2, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            print("complete? complete_1", imgs_)
                                            complete = True
                                        else:
                                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prerequisites.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(770, y_scan_1, 910, y_scan_2, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                print("complete? prerequisites", imgs_)
                                                complete = True
                        if complete == False:
                            # 이제 수락 받으러 가는 길
                            for i in range(50):
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\quest.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("quest", imgs_)
                                    click_pos_2(815, click_y, cla)
                                else:
                                    result_confirm = confirm_all(cla)
                                    if result_confirm == False:
                                        move_check(cla)
                                    else:
                                        break
                                time.sleep(1)

                            for i in range(10):
                                confirm_all(cla)

                                result_attacl_check = attack_check(cla)
                                if result_attacl_check == False:
                                    juljun_off(cla)
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\click_request_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(835, 135, 900, 190, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("click_request_btn", imgs_)
                                        click_pos_reg(imgs_.x - 70, imgs_.y, cla)
                                        juljun_on(cla)
                                else:
                                    break
                                time.sleep(1)

                        is_spot = True

                    # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\move_btn.PNG"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set_(770, y_reg_2, 910, y_reg_3, cla, img, 0.85)
                    # if imgs_ is not None and imgs_ != False:
                    #     print("move_btn", imgs_)


            else:
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\safe_map_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 60, 70, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\maul_in_request_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 50, 170, 200, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("maul_in_request_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)

                            for r in range(10):
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\quest.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("quest", imgs_)
                                    break
                                time.sleep(0.5)

                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\jabhwa_sangin_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                drag_pos(90, 75, 90, 180, cla)
                            else:
                                click_pos_2(190, 55, cla)
                                time.sleep(1)

                    QTest.qWait(1000)

            QTest.qWait(1000)
        if complete == True:
            print("add 하거라")
        else:
            print("에라다")
        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\bag_auction_item.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_for = imgs_set_for(730, 110, 960, 1000, cla, img, 0.8)
        # if imgs_for is not None and imgs_for != False:
        #     print("bag_auction_item", imgs_for)
        #
        #     if len(imgs_for) > 0:
        #         for i in range(len(imgs_for)):
        #             click_pos_reg(imgs_for[i][0] - 15, imgs_for[i][1] + 15, cla)
        #             time.sleep(1)


        ####################### file list#################################
        # out_potion = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\out"
        # out_list = os.listdir(out_potion)
        # for i in range(len(out_list)):
        #     result_file_list = out_list[i].split(".")
        #     read_data = result_file_list[0]
        #     print("read_data", read_data)

    except Exception as e:
        print(e)
        return 0

def send_message(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=payload)
    return response

