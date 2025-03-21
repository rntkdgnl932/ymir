import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def boss_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    import pytesseract
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos, text_check_get, text_check_get_black_white
    from action import out_check, juljun_off, juljun_on, juljun_check, confirm_all, attack_check, bag_open, fix_bag
    from game_check import move_check, dun_check
    from get_item import get_item_start, get_event, get_pass, get_sangjum_gyohwan
    from potion import potion_buy
    from chango import go_chango, chango_start, chango_maul_auction
    from request import request_get, request_start
    from clean_screen import clean_screen_go
    from dungeon import dungeon_in, random_spot_dun, dungeon_hondon_folk
    from boonhae_collection import collection_start, boonhae_start
    from auction_game import auction_in, auction_low_num, auction_qun_num, auction_start
    from migoong import migoong_start

    print("boss_check")

    try:


        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boss\\already_arrive_notice.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(390, 500, 600, 600, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("already_arrive_notice", imgs_)


        

    except Exception as e:
        print(e)
        return 0


