import ctypes


class WindowManager:
    window = None
    scan = None
    scanWorker = None
    workerThread = None
    appUserModelID = 'UOR.IDS.GuardianNet.v1'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appUserModelID)
