import webbrowser
import requests
import re
import sys
import os
import requests
import re
import json
from colorama import init , Fore, Back, Style
init()

#Menu
def byebye():
    try:

        choice = int(input("\nChoose your IETF Document:\n 1 - Request for Comments (RFC):\n 2 - Best current practice (BCP):\n 3 - Internet Standard (STD):\n 4 - Save Document: \n 5 - Exit \n\n "))
        if choice == 1:
            rfcmenu()
        elif choice == 2:
            bcpmain()
        elif choice == 3:
            stdmain()
        elif choice == 4:
            savemain()
        elif choice == 5:
            sys.exit(0)
        else:
            print("Invalid input.")
            sys.exit()
    except ValueError:
        print("Invalid input.")
        sys.exit()

def savemain():
    try:
        save_choice = int(input("\nChoose your IETF Document to Save:\n 1 - Request for Comments (RFC):\n 2 - Best current practice (BCP):\n 3 - Internet Standard (STD):\n 4 - Exit \n"))
        if save_choice == 1:
            rfcsave()
        elif save_choice == 2:
            bcpsave()
        elif save_choice == 3:
            stdsave()
        elif save_choice == 4:
            byebye()
        else:
            print("Invalid input.")
            sys.exit()
    except ValueError:
        print("Invalid input.")
        sys.exit()

def rfcmenu():
    try:
        save_choice = int(input("\nChoose your Option:\n 1 - Open the Request for Comments (RFC):\n 2 - View the Request for Comments (RFC) Information:\n 3 - Back to Menu \n\n "))
        if save_choice == 1:
            rfcmain()
        elif save_choice == 2:
            rfcjson()
        elif save_choice == 3:
            byebye()
        else:
            print("Invalid input.")
            sys.exit()
    except ValueError:
        print("Invalid input.")
        sys.exit()










#RFC Intro
def rfc_intro():
    print('\033[36m' +
    """
██████╗ ███████╗ ██████╗    ██╗   ██╗██╗███████╗██╗    ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝    ██║   ██║██║██╔════╝██║    ██║██╔════╝██╔══██╗
██████╔╝█████╗  ██║         ██║   ██║██║█████╗  ██║ █╗ ██║█████╗  ██████╔╝
██╔══██╗██╔══╝  ██║         ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║██╔══╝  ██╔══██╗
██║  ██║██║     ╚██████╗     ╚████╔╝ ██║███████╗╚███╔███╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝      ╚═════╝      ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                
    """
    )
    print(Style.RESET_ALL)


#RFC Main
def rfcmain():
    rfc_intro()
    url = "https://tools.ietf.org/html/rfc"
    number = input("Enter the RFC number: ")

    if not re.match("^[0-9]{0,4}$", number):
        print("Error! Only RFC from 1-9999 allowed")
        byebye()

    try:
        webbrowser.open_new(url + number)
        byebye()
    except Exception as e:
        print(repr(e))

#RFC Save PDF
def rfcsave():
    rfc_intro()
    save_url = "https://tools.ietf.org/pdf/rfc"
    number = input("Enter the RFC number: ")
    comp_url = save_url + number + ".pdf"
    myfile = requests.get(comp_url, allow_redirects=True)

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    open(desktop + '\RFC' + (number) + '.pdf', 'wb').write(myfile.content)
    byebye()

#RFC Json
def rfcjson():
    rfc = input("Enter the RFC number: ")
    comp_url = (("https://www.rfc-editor.org/rfc/") + "rfc" + rfc + ".json")

    page_rfc_json = requests.get(comp_url)
    data = page_rfc_json.json()

    rfc_title = (data["title"])
    rfc_authors = (data["authors"])
    rfc_page_count = (data["page_count"])
    print('\033[36m' + "Title: " + rfc_title)
    print("Authors: " + (str(rfc_authors)))
    print("Page Count: " + rfc_page_count)
    print(Style.RESET_ALL)
    byebye()

#End RFC





#BCP Intro
def bcp_intro():
    print('\033[36m' +
    """
██████╗  ██████╗██████╗     ██╗   ██╗██╗███████╗██╗    ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗    ██║   ██║██║██╔════╝██║    ██║██╔════╝██╔══██╗
██████╔╝██║     ██████╔╝    ██║   ██║██║█████╗  ██║ █╗ ██║█████╗  ██████╔╝
██╔══██╗██║     ██╔═══╝     ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║██╔══╝  ██╔══██╗
██████╔╝╚██████╗██║          ╚████╔╝ ██║███████╗╚███╔███╔╝███████╗██║  ██║
╚═════╝  ╚═════╝╚═╝           ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                                                                                                              
    """
    )
    print(Style.RESET_ALL)


#BCP Main
def bcpmain():
    bcp_intro()
    url = "https://tools.ietf.org/html/bcp"
    number = input("Enter the BCP number: ")

    if not re.match("^[0-9]{0,3}$", number):
        print("Error! Only BCP from 1-999 allowed")
        byebye()

    try:
        webbrowser.open_new(url + number)
        byebye()
    except Exception as e:
        print(repr(e))


#BCP Save PDF
def bcpsave():
    bcp_intro()
    save_url = "https://tools.ietf.org/pdf/bcp"
    number = input("Enter the BCP number: ")
    comp_url = save_url + number + ".pdf"
    myfile = requests.get(comp_url, allow_redirects=True)

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    open(desktop + '\BCP' + (number) + '.pdf', 'wb').write(myfile.content)
    byebye()

#End BCP

#STD Intro
def std_intro():
    print('\033[36m' +
    """
██╗███╗   ██╗████████╗███████╗██████╗ ███╗   ██╗███████╗████████╗    ███████╗████████╗ █████╗ ███╗   ██╗██████╗  █████╗ ██████╗ ██████╗ ███████╗
██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔════╝╚══██╔══╝    ██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██╔██╗ ██║█████╗     ██║       ███████╗   ██║   ███████║██╔██╗ ██║██║  ██║███████║██████╔╝██║  ██║███████╗
██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝     ██║       ╚════██║   ██║   ██╔══██║██║╚██╗██║██║  ██║██╔══██║██╔══██╗██║  ██║╚════██║
██║██║ ╚████║   ██║   ███████╗██║  ██║██║ ╚████║███████╗   ██║       ███████║   ██║   ██║  ██║██║ ╚████║██████╔╝██║  ██║██║  ██║██████╔╝███████║
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝       ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝
                                                                                                                                                                 
    """
    )
    print(Style.RESET_ALL)


#STD Main
def stdmain():
    std_intro()
    url = "https://tools.ietf.org/html/std"
    number = input("Enter the STD number: ")

    if not re.match("^[0-9]{0,2}$", number):
        print("Error! Only STD from 1-99 allowed")
        byebye()

    try:
        webbrowser.open_new(url + number)
        byebye()
    except Exception as e:
        print(repr(e))

#STD Save PDF
def stdsave():
    std_intro()
    save_url = "https://tools.ietf.org/pdf/std"
    number = input("Enter the STD number: ")
    comp_url = save_url + number + ".pdf"
    myfile = requests.get(comp_url, allow_redirects=True)

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    open(desktop + '\STD' + (number) + '.pdf', 'wb').write(myfile.content)

    byebye()

#End STD

print('\033[36m' +
"""
██████  ███████╗████████╗███████╗
  ██║   ██╔════╝╚══██╔══╝██╔════╝
  ██║   █████╗     ██║   █████╗  
  ██║   ██╔══╝     ██║   ██╔══╝  
██████║ ███████╗   ██║   ██║     
╚═════╝ ╚══════╝   ╚═╝   ╚═╝     
"""
)
print(Style.RESET_ALL)


try:
    choice = int(input("\nChoose your IETF Document:\n 1 - Request for Comments (RFC):\n 2 - Best current practice (BCP):\n 3 - Internet Standard (STD):\n 4 - Save Document \n 5 - Exit \n\n "))
    if choice == 1:
        rfcmenu()
    elif choice == 2:
        bcpmain()
    elif choice == 3:
        stdmain()
    elif choice == 4:
        savemain()
    elif choice == 5:
        sys.exit
    else:
        print("Invalid input.")
        sys.exit()
except ValueError:
    print("Invalid input.")
    sys.exit()
