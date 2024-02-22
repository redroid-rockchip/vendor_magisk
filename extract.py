#!/usr/bin/env python3
import atexit
import os.path
import re
import shutil
import subprocess
import zipfile


def main():
    current_path = os.path.dirname(os.path.abspath(__file__))
    apk_path = os.path.join(current_path, "magisk.apk")
    unzip_path = os.path.join(current_path, "temp")
    overlay_path = os.path.join(current_path, "rootfs")
    overlay_magisk_path = os.path.join(overlay_path, "vendor", "etc", "init", "ksigam")
    overlay_init_path = os.path.join(overlay_path, "vendor", "etc", "init", "ksigam.rc")

    shutil.rmtree(unzip_path, ignore_errors=True)
    os.makedirs(unzip_path, exist_ok=True)
    atexit.register(shutil.rmtree, unzip_path, ignore_errors=True)

    print("==> Extracting archive...")
    with zipfile.ZipFile(apk_path) as z:
        z.extractall(unzip_path)

    shutil.rmtree(overlay_path, ignore_errors=True)
    os.makedirs(overlay_magisk_path, exist_ok=True)

    print("==> Installing magisk now ...")
    lib64_path = os.path.join(unzip_path, "lib", "arm64-v8a")
    for parent, dirnames, filenames in os.walk(lib64_path):
        for filename in filenames:
            so_path = os.path.join(lib64_path, filename)
            so_name = re.search(r"lib(.*)\.so", filename)
            target_path = os.path.join(overlay_magisk_path, so_name.group(1))
            shutil.copyfile(so_path, target_path)
            subprocess.check_call(["chmod", "+x", target_path])

    lib32_path = os.path.join(unzip_path, "lib", "armeabi-v7a")
    shutil.copyfile(os.path.join(lib32_path, "libmagisk32.so"), os.path.join(overlay_magisk_path, "magisk32"))


if __name__ == '__main__':
    main()
