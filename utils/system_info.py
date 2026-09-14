import platform
import psutil


def get_system_info():
    return {
        "sistema": platform.system(),
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent
    }