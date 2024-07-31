import os
import shutil
import subprocess

path = "/boot/grub/themes/"
grub_path = "/etc/default/grub"

def check_sudo():
    if os.geteuid() != 0:
        print("This script requires superuser privileges. Please run with sudo.")
        exit()

def backup_grub_conf():
    print("Creating a backup copy of grub config!")
    
    if not os.path.exists(grub_path):
        print(f"{grub_path} does not exist!")
        exit()

    script_directory = os.path.dirname(os.path.abspath(__file__))
    backup_directory = os.path.join(script_directory, 'backup')

    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
        print(f"Backup directory created at {backup_directory}")
    try:
        shutil.copy(grub_path, backup_directory)
        print(f"Backup of grub config created at {os.path.join(backup_directory, os.path.basename(grub_path))}")
    except Exception as e:
        print(f"An error occurred while creating the backup: {e}")
        exit()


def apply_theme(theme_name):
    theme_path = os.path.join(path, theme_name, "theme.txt")
    if not os.path.exists(theme_path):
        print(f"{theme_path} does not exist!")
        exit()
    backup_grub_conf()
    try:
        with open(grub_path, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        print(f"Error reading grub config: {e}")
        exit()
    for i, line in enumerate(lines):
        if line.startswith("GRUB_THEME="):
            lines[i] = f'GRUB_THEME="{theme_path}"\n'
            break
    try:
        with open(grub_path, 'w') as file:
            file.writelines(lines)
        print(f"Theme {theme_name} applied successfully!")
    except Exception as e:
        print(f"Error writing to grub config: {e}")
        exit()
    try:
        subprocess.run(['grub-mkconfig', '-o', '/boot/grub/grub.cfg'], check=True)
        print("grub-mkconfig executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error executing grub-mkconfig: {e}")
        exit()


def get_themes(path):
    try:
        if not os.path.exists(path):
            print(f"Path {path} doesn't exists.")
            return

        folder_names = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

        if not folder_names:
            print(f"You have no themes installed in {path}.")
            return
        
        return folder_names
    
    except Exception as e:
        print(f"Error occurred: {e}")

def askuser():
    print("Available themes: ")
    folder_names = get_themes(path)
    c = 1
    for folder in folder_names:
        print(f"({c}) {folder}")
        c+=1
    print("Please select the theme you want to use: ")
    choice = input()
    if(int(choice) >= c or int(choice) < 0):
        print("Bad input!")
        exit()
    print(f"You have selected the theme {folder_names[int(choice)-1]}, do you want to apply this theme? (y/n)")
    apply = input()
    if(apply == "y" or apply == "Y"):
        apply_theme(folder_names[int(choice)-1])
    else:
        exit()

check_sudo()
askuser()