import ctypes


class WindowManager:
    window = None
    appUserModelID = 'UOR.IDS.GuardianNet.v1'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appUserModelID)
