from time import sleep
from pywinauto.application import Application
app = Application(backend="win32").start(r'C:\E20-II\HAP42\CODE\hap42.exe')


# Clicks OK
app.ThunderRT6FormDC['AfxWnd40'].OK.click()



# Clicks into "Spaces" (2&3 both work on Bootcamp for some reason)
app.ThunderRT6FormDC.ListView.select(3).click_input(double=True)

# Clicks into "New default space"
app.ThunderRT6FormDC.ListView.select(0).click_input(double=True)
app.ThunderRT6FormDC['Space Properties - [Default Space]'].print_control_identifiers(depth=2)


# Control Identifiers
# app.ThunderRT6FormDC.print_control_identifiers()
# app.ThunderRT6FormDC['ListView'].print_control_identifiers()

# Extra Testing Code
# dlg = app.windows()
# app.dlg['Dialog2'].OK.click()
# set_window("HAP42 - [Untitled]", 12)
# print (app.ThunderRT6FormDC.ListView1.select(3).index())