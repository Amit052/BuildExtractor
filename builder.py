
global full_build, build_name, Tic_name, t1, t2, t3, t4, full_build
full_build = ""
Tic_name = ""
import os
import threading
import subprocess
import time


def get_g_folder(path, t):
    if not "zip" in t.lower():
        t += ".zip"
    file_list = os.listdir(path)
    for file in file_list:
        if t.lower() in file.lower():
            return (os.path.join(path, file), file.upper()[:-5])
        elif "layout" in file.lower():
            return get_g_folder(path + os.sep + file, t)


def extract_path(path, dest):
    global full_build
    if not "eng" in dest:
        full_build += dest + "\n"
    subprocess.call(r'"C:\Program Files\7-Zip\7z.exe" x ' + path + ' -o' + dest)



t1 = t2 = t3 = t4 = ""

s = "| Build extractor by Amit Maor |"
for i in s:
    print("-", end="", flush=True)
print("\n" + s)
for i in s:
    print("-", end="", flush=True)

proset = input('\nProset: ')
eng = input('Eng: ')
bts = input('BT for sustain: ')
bt_hrp = input('BT for HrP: ')

if proset != "" and proset != "0":

    args = get_g_folder(proset, 'g')
    Tic_name = args[1]
    dest = r"DESTINATION_PATH" + Tic_name + os.sep + Tic_name + "g"
    t1 = threading.Thread(target=extract_path, args=(args[0], dest))

if eng != "" and eng != "0":
    dest = r"DESTINATION_PATH" + Tic_name + os.sep + "eng/"
    args = get_g_folder(eng, 'eng')
    t2 = threading.Thread(target=extract_path, args=(args[0], dest))

if bts != "" and bts != "0":
    dest = r"DESTINATION_PATH"
    args = get_g_folder(bts, 'g')
    t3 = threading.Thread(target=extract_path, args=(args[0], dest + args[1]))


if bt_hrp != "" and bt_hrp != "0":
    dest = r"DESTINATION_PATH"
    args = get_g_folder(bt_hrp, 'g')
    t4 = threading.Thread(target=extract_path, args=(args[0], dest + args[1]))

flag_arr =[]
if not isinstance(t1, str):
    t1.start()
    flag_arr.append(1)
if not isinstance(t2, str):
    t2.start()
    flag_arr.append(1)
if not isinstance(t3, str):
    t3.start()
    flag_arr.append(1)
if not isinstance(t4, str):
    t4.start()
    flag_arr.append(1)
print("Extracting data")
while (not isinstance(t1, str) and t1.isAlive()) or (not isinstance(t2, str) and t2.isAlive()) or (not isinstance(t3, str) and t3.isAlive()) or (not isinstance(t4, str) and t4.isAlive()):
    print(".", end="", flush=True)
    time.sleep(1)
if Tic_name == "":
    Tic_name = "tmp"


full_build = full_build.replace(r'/', '\\')

tmp = open(Tic_name + ".txt", 'w')
tmp.write(full_build)
tmp.close()
input("Press any key to exit...")

