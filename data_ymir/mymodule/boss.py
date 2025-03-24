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
    from function_game import imgs_set_

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


