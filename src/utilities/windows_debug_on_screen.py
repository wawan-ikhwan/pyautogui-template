import tkinter as Tkinter
import win32api, win32con, pywintypes

class WindowsDebugScreen:
  def __init__(self):
    label = Tkinter.Label(text='Debug', font=('Consolas', 12), fg='lime', bg='green', justify=Tkinter.LEFT)
    label.master.overrideredirect(True)
    label.master.geometry("+20+20")
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "green")

    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
    exStyle: int = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    label.pack()
    self.label = label

  def hide_label(self):
    global windows_label
    self.label.master.withdraw()
    self.label.master.update()

  def show_label(self):
    global windows_label
    self.label.master.deiconify()
    self.label.master.update()

  def update_label(self, new_text):
    global windows_label
    self.label.config(text=new_text)
    self.label.master.update()
