import pyautogui as pp, time as t
t.sleep(5)
f=open("ss",'r')
for i in f:
    pp.typewrite(i)
    pp.press("enter")



