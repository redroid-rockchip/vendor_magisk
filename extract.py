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

    shutil.rmtree(unzip_path, ignore_errors=True)
    os.makedirs(unzip_path, exist_ok=True)
    atexit.register(shutil.rmtree, unzip_path, ignore_errors=True)

    print("==> Extracting archive ...")
    with zipfile.ZipFile(apk_path) as z:
        z.extractall(unzip_path)

    ########################################################
    ########################################################
    print("==> Installing magisk（arm64） now ...")
    overlay_path = os.path.join(current_path, "arm64", "magisk")
    shutil.rmtree(overlay_path, ignore_errors=True)
    os.makedirs(overlay_path, exist_ok=True)

    lib64_path = os.path.join(unzip_path, "lib", "arm64-v8a")
    for parent, dirnames, filenames in os.walk(lib64_path):
        for filename in filenames:
            so_path = os.path.join(lib64_path, filename)
            so_name = re.search(r"lib(.*)\.so", filename)
            target_path = os.path.join(overlay_path, so_name.group(1))
            shutil.copyfile(so_path, target_path)
            subprocess.check_call(["chmod", "+x", target_path])

    lib32_path = os.path.join(unzip_path, "lib", "armeabi-v7a")
    shutil.copyfile(os.path.join(lib32_path, "libmagisk32.so"), os.path.join(overlay_path, "magisk32"))

    ########################################################
    ########################################################
    print("==> Installing magisk（arm64_only） now ...")
    overlay_path = os.path.join(current_path, "arm64_only", "magisk")
    shutil.rmtree(overlay_path, ignore_errors=True)
    os.makedirs(overlay_path, exist_ok=True)

    lib64_path = os.path.join(unzip_path, "lib", "arm64-v8a")
    for parent, dirnames, filenames in os.walk(lib64_path):
        for filename in filenames:
            so_path = os.path.join(lib64_path, filename)
            so_name = re.search(r"lib(.*)\.so", filename)
            target_path = os.path.join(overlay_path, so_name.group(1))
            shutil.copyfile(so_path, target_path)
            subprocess.check_call(["chmod", "+x", target_path])

    ########################################################
    ########################################################
    print("==> Installing magisk（x86_64） now ...")
    overlay_path = os.path.join(current_path, "x86_64", "magisk")
    shutil.rmtree(overlay_path, ignore_errors=True)
    os.makedirs(overlay_path, exist_ok=True)

    lib64_path = os.path.join(unzip_path, "lib", "arm64-v8a")
    for parent, dirnames, filenames in os.walk(lib64_path):
        for filename in filenames:
            so_path = os.path.join(lib64_path, filename)
            so_name = re.search(r"lib(.*)\.so", filename)
            target_path = os.path.join(overlay_path, so_name.group(1))
            shutil.copyfile(so_path, target_path)
            subprocess.check_call(["chmod", "+x", target_path])

    lib32_path = os.path.join(unzip_path, "lib", "x86")
    shutil.copyfile(os.path.join(lib32_path, "libmagisk32.so"), os.path.join(overlay_path, "magisk32"))

    ########################################################
    ########################################################
    print("==> Installing magisk（x86_64_only） now ...")
    overlay_path = os.path.join(current_path, "x86_64_only", "magisk")
    shutil.rmtree(overlay_path, ignore_errors=True)
    os.makedirs(overlay_path, exist_ok=True)

    lib64_path = os.path.join(unzip_path, "lib", "x86_64")
    for parent, dirnames, filenames in os.walk(lib64_path):
        for filename in filenames:
            so_path = os.path.join(lib64_path, filename)
            so_name = re.search(r"lib(.*)\.so", filename)
            target_path = os.path.join(overlay_path, so_name.group(1))
            shutil.copyfile(so_path, target_path)
            subprocess.check_call(["chmod", "+x", target_path])


if __name__ == '__main__':
    main()
