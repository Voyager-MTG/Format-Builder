from enum import Enum
from datetime import datetime
import os, sys, shutil

format_ = "Voyager"

path = {
    "egg_hub_export"  : f"../{format_}-Indexes/1.exports/egg",
    "trice_export"    : f"../{format_}-Indexes/1.exports/trice",
    "indexes"         : f"../{format_}-Indexes/",
    "egg_hub"         : f"../{format_}-MTG.github.io",
    "egg_hub_sets"    : f"../{format_}-MTG.github.io/sets",
    "trice_sets"      : f"../{format_}-Field-Builder/sets/",
    "trice_merged"    : f"../{format_}-Field-Builder/export/",
    "field_builder"   : f"../{format_}-Field-Builder/",
    "format_data"     : f"../{format_}/tricedata/",
    "format"          : f"../{format_}/"
}


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            # print("copying", s, d)
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def pushgit(dir):
    os.chdir(dir)
    os.system("git add -A")
    os.system("git commit -m " + datetime.today().strftime('%Y-%m-%d_%H:%M:%S'))
    os.system("git push origin main")

# region Export mse 

print("EXPORTING FROM MSE")
print("Running indexes export script\n------------------------------")
os.chdir(path["indexes"])
os.system("python export.py")

# region Trice

print("BUILDING TRICE FILES\n")
print("Copying data from trice-export")
try:
    shutil.rmtree(path["trice_sets"])
except Exception as e:
    print(e)


try:
    shutil.copytree(path["trice_export"], path["trice_sets"])
except Exception as e:
    print(e)

print("Running trice-merge\n------------------------------")
os.chdir(path["field_builder"])
os.system(f"python trice-merge/merge.py")
print("------------------------------")

print(f"Moving files to {format_}")

try:
    shutil.rmtree(path["format_data"])
except Exception as e:
    print(e)


try:
    shutil.copytree(path["trice_merged"], path["format_data"])
except Exception as e:
    print(e)

#region Egg Hub

print("BUILDING EGG HUB\n")
print("Copying files from egg-hub-export")

os.chdir(path["egg_hub"])
try: 
    shutil.rmtree("sets")
except:
    print("removed sets!")

try:
    copytree(path["egg_hub_export"], "sets")
except Exception as e:
    print(e)

try:
    copytree(path["egg_hub_export"], "sets")
except Exception as e:
    print(e)

print("Running build_site\n------------------------------")
os.chdir(path["egg_hub"])
os.system("python scripts/build_site.py")
print("------------------------------\n")

print(f"Built {format_}!")

#region Git

print("Pushing to git repos")
print("------------------------------\n")

date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

pushgit(path["indexes"])
pushgit(path['field_builder'])
pushgit(path["format"]) # "{format_}".format_(format_)
pushgit(path["egg_hub"])