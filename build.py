from enum import Enum
from datetime import datetime
import os, sys, shutil

path = {
    "egg_hub_export" : "../Voyager-Indexes/egg-hub-exports/",
    "trice_export"   : "../Voyager-Indexes/trice-exports/",
    "egg_hub"        : "../Voyager-MTG.github.io",
    "egg_hub_sets"   : "../Voyager-MTG.github.io/sets",
    "trice_sets"     : "../Voyager-Field-Builder/sets/",
    "trice_merged"   : "../Voyager-Field-Builder/export/",
    "field_builder"  : "../Voyager-Field-Builder/",
    "voyager_data"   : "../Voyager/tricedata/",
    "voyager"        : "../Voyager/"
}

def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.
    
    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

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

print("Moving files to Voyager")

try:
    shutil.rmtree(path["voyager_data"])
except Exception as e:
    print(e)


try:
    shutil.copytree(path["trice_merged"], path["voyager_data"])
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

print("Built Voyager!")

#region Git

print("Git stuff")
print("------------------------------\n")

date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

pushgit(path['field_builder'])
pushgit(path["voyager"])
pushgit(path["egg_hub"])