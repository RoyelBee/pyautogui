

import pyautogui as pag
import time

# # ------------------------------------------------------------------------
# # ----------------- Search google.com ------------------------------------
# # ------------------------------------------------------------------------

# #  Click chrome browser in the task
pag.click(x=528, y=1058)

# # Click url tab
pag.click(x=290, y=71)

## --------- Write text and search it -------------------------------------
pag.typewrite('www.google.com')
pag.typewrite(['enter'])
time.sleep(4)
## ---------------- Go to google and select search button -----------------
pag.click(x=670, y=502)
pag.typewrite('transcom limited')
pag.typewrite(['enter'])

# # ---- Finally go to transcombd.com -------------------------------------
time.sleep(3)
pag.click(x=286, y=398)


# print(pag.position())