import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check
    from game_check import move_check

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

    except Exception as e:
        print(e)
        return 0

def send_message(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=payload)
    return response

