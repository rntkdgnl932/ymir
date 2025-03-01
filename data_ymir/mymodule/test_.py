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
    from get_item import get_item_start, get_event, get_pass
    from potion import potion_buy
    from chango import go_chango, chango_start
    from request import request_get, request_start
    from clean_screen import clean_screen_go
    from dungeon import dungeon_in

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

        # request_get(cla, "외뢰_2")

        # request_start(cla, "외뢰_1")

        # dungeon_in(cla, "발할라_일반_혼돈_4")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\migoong\\out\\sbipa.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(20, 30, 200, 90, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("migoong out :",  imgs_)

        ran_x = random.randint(100, 200)
        print("result", ran_x)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\dun_complete.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(805, 255, 870, 320, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("dun_complete", imgs_)

        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_title_point_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(275, 380, 300, 720, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("event_title_point_1", imgs_)

        # prohibition = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prohibition"
        # prohibition_list = os.listdir(prohibition)
        #
        # for i in range(len(prohibition_list)):
        #     result_prohibition_list = prohibition_list[i].split(".")
        #     read_data = result_prohibition_list[0]
        #     print("read_data", read_data)
        #     full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prohibition\\" + str(
        #         read_data) + ".PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(210, 140, 460, 220, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         print("prohibition_list", str(read_data), imgs_)
        #         is_prohibition = True

        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\end_btn.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(480, 570, 630, 630, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("end_btn")
        #
        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prohibition\\15.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(210, 100, 460, 960, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("prohibition_list", imgs_)
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

