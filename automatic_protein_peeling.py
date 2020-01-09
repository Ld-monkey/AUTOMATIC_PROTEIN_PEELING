# coding : utf-8

"""
@autor : Zygnematophyce
Master II - 2019 2020
Projet Long
"""

import re
import robobrowser
import os

from robobrowser import RoboBrowser

if __name__ == "__main__":
    print("Automatics protein peeling")

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    print(THIS_FOLDER)
    my_file = os.path.join(THIS_FOLDER, "1qfw_Fv_Human_chorionic_gonadotropin.pdb")
    print(my_file)

    browser = RoboBrowser(history=True, parser = "html.parser")
    browser.open("https://www.dsimb.inserm.fr/dsimb_tools/peeling3/")

    form = browser.get_form()
    print(form)
    form['file_pdb'].value = my_file
    print(form)

    browser.submit_form(form)

    print(browser.parsed)

    print("Done")
