from apm_models import models_info
import subprocess
import os


root_path = os.getcwd()
all_models = {**models_info['Copter'], **models_info['Plane'], **models_info['VTOL']}

def run_sitl(model: str = "quad", speedup: int = 1, home: str = "21.667195,39.180198,0,340", port: int = 5760, sysid: int = 1):
    binary = all_models[model]['binary']
    params = all_models[model]['param_files']
    cmd = f"{binary}.exe --synthetic-clock --model {model} --defaults {params} --speedup {speedup} --home {home} --base-port {port}"
    subprocess.Popen(cmd)


def check_port_availability():
    pass


def main():
    pass


if __name__ == "__main__":
    pass