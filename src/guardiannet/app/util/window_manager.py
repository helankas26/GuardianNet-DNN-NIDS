import ctypes


class WindowManager:
    window = None
    scan = None
    scanWorker = None
    scanWorkerThread = None
    historyWorker = None
    historyWorkerThread = None
    appUserModelID = 'UOR.IDS.GuardianNet.v1'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appUserModelID)
