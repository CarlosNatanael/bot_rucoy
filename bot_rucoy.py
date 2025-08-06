import pyautogui
import cv2
import numpy as np
import time
import random

def encontrar_imagem(imagem_referencia, confianca=0.8):
    try:
        screenshot = pyautogui.screenshot()
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        template = cv2.imread(imagem_referencia, cv2.IMREAD_COLOR)
        if template is None:
            return None
            
        resultado = cv2.matchTemplate(screenshot_cv, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

        if max_val >= confianca:
            largura, altura = template.shape[1], template.shape[0]
            centro_x = max_loc[0] + largura // 2
            centro_y = max_loc[1] + altura // 2
            return (centro_x, centro_y)
        else:
            return None
    except Exception as e:
        print(f"Ocorreu um erro na função encontrar_imagem: {e}")
        return None
