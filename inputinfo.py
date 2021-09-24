from time import sleep
from pywinauto.application import Application
app = Application(backend="win32").start(r'C:\E20-II\HAP42\CODE\hap42.exe')

# dlg = app.windows()
# app.dlg['Dialog2'].OK.click()

# Clicks OK
app.ThunderRT6FormDC['AfxWnd40'].OK.click()

# app.ThunderRT6FormDC.print_control_identifiers()
# app.ThunderRT6FormDC['ListView'].print_control_identifiers()

# Clicks into "Spaces"
app.ThunderRT6FormDC.ListView.select(3).click_input(double=True)

# Clicks into "New default space"
app.ThunderRT6FormDC.ListView.select(0).click_input(double=True)