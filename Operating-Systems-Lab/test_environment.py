import platform
import psutil

print("Operating System:", platform.system())
print("Python Version:", platform.python_version())
print("CPU Cores:", psutil.cpu_count())
print("Memory Available (GB):", round(psutil.virtual_memory().available / (1024**3), 2))
print("OS LAB PYTHON TEST PASSED")
