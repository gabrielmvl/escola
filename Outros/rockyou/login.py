import pyautogui as auto
import time
import csv

def timer(tempo):
    time.sleep(tempo)

arquivo = ""

def digitar(item):
    auto.write(item, interval=0.001)
    auto.hotkey('enter')
    auto.hotkey('ctrl', 'a')
    auto.hotkey('del')
    timer(1)

with open(arquivo, "r", encoding="UTF-8") as f:
    file = csv.reader(f, delimiter=';')
    timer(3)
    for line in file:
        num = line[0]
        digitar(num)