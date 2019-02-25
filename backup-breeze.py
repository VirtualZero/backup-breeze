#!/usr/bin/python3

import os

def dependencies():
    """Attempts to install dependencies"""

    print(" \nChecking dependencies...\n ")

    try:
        os.system("sudo apt-get install python3-tk -y")

    except PermissionError:
        print("Please run backup-breeze with sudo privileges: 'sudo backup-breeze' ")
        exit(1)

    except Exception:
        print("Error ")
        exit(1)

try:
    from tkinter import *
    from tkinter import ttk
    import tkinter.messagebox
    import tkinter.filedialog

except Exception:
    dependencies()

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.filedialog

import tarfile

root = Tk()
root.title("Backup-BreEZe")

iPath = ""
oPath = ""

def askSourceDir():
    """Prompts user for the directory to backup"""

    global iPath
    iPath = tkinter.filedialog.askdirectory(title="Choose Directory")

    if not iPath:
        tkinter.messagebox.showinfo("Hint:", "You haven't selected a directory to backup yet.")

def askDestinationDir():
    """Prompts user for the location to save the backup to"""

    global oPath
    oPath = tkinter.filedialog.askdirectory(title="Choose Directory")

    if not oPath:
        tkinter.messagebox.showinfo("Hint:", "You haven't selected a place to store your backup yet.")

def makeBackup():
    """Creates a .tar.gz file from the user-selected directory,
    Moves the .tar.gz file to the user-selected destination directory"""

    global iPath
    global oPath
    
    if not iPath or not oPath:
        tkinter.messagebox.showinfo("Hint:", "You must select a directory to backup and a place to store the backup in.")

    else:
        answer = tkinter.messagebox.askquestion("Confirm", "Backup " + iPath + "?")

        if answer == "yes":
        
            try:
                with tarfile.open(iPath + ".tar.gz", mode="w:gz") as archive:
                    archive.add(iPath)

                    origBack = iPath + ".tar.gz"
                    
                    os.system("sudo mv " + origBack + " " + oPath)

                    displaySuccess()
                    
                    iPath = ""
                    oPath = ""
                    
            except FileNotFoundError:
                tkinter.messagebox.showinfo("File Not Found!", "Invalid parameter, exiting with status '1'")
                exit(1)
                
            except PermissionError:
                tkinter.messagebox.showinfo("Permission Error:", "Please run Backup-BreEZe with sudo privileges: 'sudo backup-breeze'")
                exit(1)

def displaySuccess():
    """Let's user know operation is complete"""
    
    tkinter.messagebox.showinfo("Status", "Successful Backup!")

def gui():
    """Opens the GUI interface, configuration of GUI"""

    global iPath
    global oPath

    sourceLabel = ttk.Label(text=" Backup this Directory:    ")
    sourceLabel.grid(row=0, column=0, sticky=E)

    destinationLabel = ttk.Label(text=" And Store it Here:    ")
    destinationLabel.grid(row=1, column=0, sticky=E)

    sourceButton = ttk.Button(root, text="Choose Directory", command=askSourceDir)
    sourceButton.grid(row=0, column=1, sticky=E)

    destinationButton = ttk.Button(root, text="Choose Directory", command =askDestinationDir)
    destinationButton.grid(row=1, column=1, sticky=E)

    exitButton = ttk.Button(root, text="Exit", command=root.quit)
    exitButton.grid(row=3, column=0, sticky=W)

    applyButton = ttk.Button(root, text="Apply", command=makeBackup)
    applyButton.grid(row=3, column=1, sticky=E)

    spaceLabel = ttk.Label(root, text="")
    spaceLabel.grid(row=2, columnspan=2)

def main():
    gui()

    root.mainloop()


if __name__ == "__main__":
    main()
