import time
# import os
import sys

from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def _stop_please(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg
    from game_check import check_start
    try:
        print("_stop_please")

        is_18 = False
        while is_18 is False:
            is_18 = True

            check_start(cla)

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\18_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(70, 600, 350, 770, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("18_1")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_18 = False
                time.sleep(1)
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\18_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(70, 600, 350, 770, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("18_2")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_18 = False
                    time.sleep(1)
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\18_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 350, 860, 410, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("18_3")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_18 = False
                        time.sleep(1)
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\event_1818.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 350, 860, 410, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("event_1818")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            is_18 = False
                            time.sleep(1)
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\18_4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(790, 350, 860, 410, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("18_4")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                is_18 = False
                                time.sleep(1)
            time.sleep(1)

        print("stop plz, check_start")




    except Exception as e:
        print(e)
        return 0



