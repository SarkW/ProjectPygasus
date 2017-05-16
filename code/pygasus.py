# Requires Python 3

import urllib.request
import os

class Package:
    def __init__(self, package_title = 'noname'):
        self._title = package_title
        self._files = []

    def add_file(self, url, file_name):
        self._files.append([url, file_name])

    def download(self):
        print("     Downloading " + self._title + " Please Wait....")
        # Set up wget client
        for file in self._files:
            urllib.request.urlretrieve (file[0], file[1])

        print("Succesfully Downloaded...... :-)")

def draw_menu():
    # Setting up the design of the Console Interface

    # Console.ForegroundColor = ConsoleColor.DarkCyan;
    print("    ________________________________________________                          ")
    print("    |                                               |                         ")
    print("    | Project Pygasus - The Xbox One homebrew client|                         ")
    print("    |_______________________________________________|                         ")
    print("                                                                          ")
    print("\033[0m")
    print("\033[1;31;10m ")
    print("     # Note: Files are downloaded into the ~/homebrew folder (homebrew inside your")
    print("     user home). More information can be located in the README file.")
    print("\033[0m")
    print("\033[1;36;10m ")
    print("                                                                          ")
    print("     ---------------------------------------                                     ")
    print("    |                                       |")
    print("    |   [Emulators for Xbox One]            |")
    print("    |1.Chip8     - (Chip 8 Games)           |")
    print("    |2.Nesbox    - (NES,SNES,GEN,GB,GBC,GBA)|")
    print("    |3.PSX-BOX   - (PS1 *Work in Progress*) |")
    print("    |4.PPSSPP    - (PSP Games)              |")
    print("    |5.VBA10     - (GBA Games)              |")
    print("    |6.Win64e10  - (N64 Games)              |")
    print("    |                                       | ")
    print("    |                                       | ")
    print("    |   [Xbox One Indie Games]              |")
    print("    |7.Dungeon Run - 2D Zelda Clone         |")
    print("    |                                       |")
    print("    |   [Tutorials]                         |")
    print("    |8.Sideloading apps                     |")
    print("     ---------------------------------------")
    print("\033[0m")

def show_tutorial():
    print(" ");
    print(" ");
    print("     [1.] Go to your Xbox One console and restart it into developer mode if it is not already")
    print(" ")
    print("     [2.] Click on settings and you will see a menu that at the top shows Xbox Device Portal")
    print(" ")
    print("     [3.] Make sure that the option that says \"Enable Xbox Device Portal is ticked\" ")
    print(" ")
    print("     In addition you make sure \"Require authentication to access Xbox Device Portal\" is checked")
    print("     you will want to set up a username and a password.")
    print(" ")
    print("     [4.] Once finished go back to Dev Home and make note of your Xbox IP Address along with the ")
    print("     port number listed at the bottom right corner it will look something like 192.168.37.8:11224 ")
    print("     (Yours may be different) Open up your web browser and type in https:// followed by your IP ")
    print("     and port number so for example https://192.168.37.8:11224 alternatively you can also enter")
    print("     https://XboxOne:11224 for example. Once you log in you may receive a warning about the security")
    print("     certificate. Go ahead and proceed anyways.")
    print(" ")
    print("     [5.] You will now be greeted with a menu that says \"my games and apps\" near the top.  ")
    print("     From Here it's rather simple just click Add and choose file. You will then select your chosen appx file.")
    print("     add your dependencies if their are any, so go ahead and press next and your chosen app will install and deploy")

def setup_packages():
    # Could be changed to fetch the list of packages from a file or from an url
    # but if so, in order to make the whole program extendible, the menu above
    # should also be generated based on an external source.
    packages = []

    home = os.path.expanduser("~")

    # Chip 8 package
    chip8 = Package("Chip8")
    chip8.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBbWpNQ19hUlc4RnM", home + "/homebrew/CHIP8_XBOX_ONE_V3.rar")
    packages.append(chip8)

    # Nesbox package
    nesbox = Package("Nesbox")
    nesbox.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBcW9xMWw0Wlg2UjQ", home + "/homebrew/NESBOX+RELEASE2+APPX+PKG.rar")
    packages.append(nesbox)

    # PSX-BOX package
    psxbox = Package("PSX-BOX")
    psxbox.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBckdaXzJ0U0dSMVE", home + "/homebrew/psx-box-master.zip")
    packages.append(psxbox)

    # PPSSPP package
    ppsspp = Package("PPPSSPP")
    ppsspp.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBRlk3N1BHQkpRYmM", home + "/homebrew/PPSSPP+Release+APPX+PKG.rar")
    packages.append(ppsspp)

    # VBA10 package
    vba10 = Package("VBA10")
    vba10.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBb25qVjJQRE1iUEE", home + "/homebrew/VBA10_1.22.197.0_Test.rar")
    packages.append(vba10)

    # Win64e10 package
    win64e10 = Package("Win64e10")
    win64e10.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBTWJPeWhZU0hXRTQ", home + "/homebrew/Win64e10+PKG.rar")
    packages.append(win64e10)

    # Dungeon Run package
    dungeon_run = Package("Dungeon Run")
    dungeon_run.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBdmRJajZYazVFR0k", home + "/homebrew/DungeonRUN1.rar")
    dungeon_run.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBeVo2Y29NMWNJT2c", home + "/homebrew/DungeonRUN2.rar")
    dungeon_run.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBbGFUN1JvT0t1cWs", home + "/homebrew/DungeonRUN3.rar")
    dungeon_run.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBMk1tbHJObUNXQnM", home + "/homebrew/DungeonRun4.rar")
    dungeon_run.add_file("https://drive.google.com/uc?export=download&id=0B6C6WFjsJozBWjBtb1pOVVJId3c", home + "/homebrew/DungeonRun_README")
    packages.append(dungeon_run)

    return packages


# Main Program
# Create homebrew folder if it does not exist
home = os.path.expanduser("~")
if not os.path.isdir(home + "/homebrew"):
    os.mkdir(home + "/homebrew")

packages = setup_packages()
draw_menu()
menu_choice = int(input())
if not 1 <= menu_choice <= 8:
    print("     Exception! Invalid Input Try Again")
    exit()

if menu_choice == 8:
    show_tutorial()
else:
    packages[menu_choice - 1].download()

