import platform
import psutil
import os
import cpuinfo
from multiprocessing import freeze_support
from colorama import Fore, init
freeze_support()

init(autoreset=True)

cat_ascii = r"""       
⠀⠀⠀         

⠀⠀⠀  ⠟⠷⠆⣠⠋⠀⠀⠀⢸⣿
⠀⠀⠀⣿⡄⠀⠀⠀⠈⠀⠀⠀⠀⣾⡿
⠀⠀⠀ ⣿⣦⡀⠀⠀⠀⠀⢀⣾
⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⡿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⢠⠏⡆⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣀⡀
⠀⠀⠀⠀⠀⡟⢦⡀⠇⠀⠀⣀⠞⠀⠀⠘⡀⢀⡠⠚⣉⠤⠂⠀⠀⠀⠈⠙⢦⡀
⠀⠀⠀⠀⠀⡇⠀⠉⠒⠊⠁⠀⠀⠀⠀⠀⠘⢧⠔⣉⠤⠒⠒⠉⠉⠀⠀⠀⠀⠹⣆
⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⣤⠶⠶⢶⡄⠀⠀⠀⠀⢹⡆
⠀⣀⠤⠒⠒⢺⠒⠀⠀⠀⠀⠀⠀⠀⠀⠤⠊⠀⢸⠀⡿⠀⡀⠀⣀⡟⠀⠀⠀⠀⢸⡇
⠈⠀⠀⣠⠴⠚⢯⡀⠐⠒⠚⠉⠀⢶⠂⠀⣀⠜⠀⢿⡀⠉⠚⠉⠀⠀⠀⠀⣠⠟
⠀⠠⠊⠀⠀⠀⠀⠙⠂⣴⠒⠒⣲⢔⠉⠉⣹⣞⣉⣈⠿⢦⣀⣀⣀⣠⡴⠟⠀⠀⠀
"""

cat_ascii_lines = cat_ascii.splitlines()


def fetch_system_info(): 
   
    system_info_lines = [

        Fore.CYAN + "=" * 30,
        Fore.CYAN + "          Meowfetch!",
        Fore.CYAN + "=" * 30,
        f"{Fore.LIGHTMAGENTA_EX}Username: {Fore.WHITE}{os.getlogin()}",
        f"{Fore.LIGHTMAGENTA_EX}Operating System: {Fore.WHITE}{platform.system()} {platform.release()}",
        f"{Fore.LIGHTMAGENTA_EX}Architecture: {Fore.WHITE}{platform.machine()}",
        f"{Fore.LIGHTMAGENTA_EX}Processor: {Fore.WHITE}{cpuinfo.get_cpu_info()['brand_raw']}",
        f"{Fore.LIGHTMAGENTA_EX}CPU Cores: {Fore.WHITE}(Threads: {psutil.cpu_count(logical=True)}) (Cores: {psutil.cpu_count(logical=False)})",
        f"{Fore.LIGHTMAGENTA_EX}CPU Frequency: {Fore.WHITE}{psutil.cpu_freq().current:.2f} MHz"
    ]
    
    ram_info = psutil.virtual_memory()
    system_info_lines.append(f"{Fore.LIGHTMAGENTA_EX}Total RAM: {Fore.WHITE}{ram_info.total / (1024  ** 3):.2f} GB")
    
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            for i, gpu in enumerate(gpus):
                system_info_lines.append(f"{Fore.LIGHTMAGENTA_EX}GPU {i + 1}: {Fore.WHITE}{gpu.name}, {gpu.memoryTotal / 1024:.2f} GB")
        else:
            system_info_lines.append(f"{Fore.LIGHTMAGENTA_EX}GPU: {Fore.WHITE}No GPU detected")
    except ImportError:
        system_info_lines.append(f"{Fore.LIGHTMAGENTA_EX}GPU Info: {Fore.WHITE}GPUtil not installed (run 'pip install gputil')")
    
    partitions = psutil.disk_partitions()
    for partition in partitions:
        disk_info = psutil.disk_usage(partition.mountpoint)
        system_info_lines.append(f"{Fore.LIGHTMAGENTA_EX}Disk {partition.device}: {Fore.WHITE}{disk_info.total / (1024 ** 3):.2f} GB (Available: {disk_info.free / (1024 ** 3):.2f} GB)")

    system_info_lines.append(Fore.CYAN + "=" * 30)

    
    max_lines = max(len(cat_ascii_lines), len(system_info_lines))

    
    while len(cat_ascii_lines) < max_lines:
        cat_ascii_lines.append("")

    while len(system_info_lines) < max_lines:
        system_info_lines.append("")

    
    for info_line, ascii_line in zip(system_info_lines, cat_ascii_lines):
        print(f"{info_line:<60} {Fore.MAGENTA}{ascii_line}")

    print(Fore.GREEN + "\nPress Enter to exit...")
    input()

if __name__ == "__main__":
    fetch_system_info()