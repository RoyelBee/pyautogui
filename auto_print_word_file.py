import pyautogui as pag
import time 

time.sleep(5)
# # Click windows start icon ------------------
pag.click(x=14, y=1053)
time.sleep(2)
pag.typewrite('word')
time.sleep(2)
pag.click(x=157, y=580)

time.sleep(10)
# # Select blank page -------------------
pag.click(x=363, y=248)

time.sleep(10)
pag.click(x=500, y=300)
pag.typewrite('Hello, This is a automated printed text. Please ignore it  ')
time.sleep(1)

# # ----- click file options ------------------
pag.click(x=38, y=54)
time.sleep(2)

# # -------- Click Print button ---------------
pag.click(x=67, y=492)
time.sleep(2)

# # -- Print document ---------------------
pag.click(x=268, y=177)

print(pag.position())