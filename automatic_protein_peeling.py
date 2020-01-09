# coding : utf-8

"""
@autor : Zygnematophyce
Master II - 2019 2020
Projet Long
"""
import requests
import os
import time

from zipfile import ZipFile 
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

    TIMER=0

    url = browser.url
    browser.open(url)

    condition = True
    while(condition == True):
        time.sleep(1.0)

        url = browser.url
        page = browser.parsed

        print("url = ",url)
        print(TIMER)
        TIMER = TIMER + 1

        # get links on page
        links = browser.get_links()

        peeling_path = url[:-12]+"peeling3d.zip"
        if (requests.head(peeling_path).status_code == 200):
            print("Exits")

            browser.open(peeling_path)

            with open("result_peeling3d.zip", "wb") as file:
                file.write(browser.response.content)

            # Extracting zip file.
            with ZipFile("result_peeling3d.zip", 'r') as zip:
                # printing all the contents of the zip file
                zip.printdir()

                # extracting all the files
                zip.extractall("peeling3d_1qfw_Fv_Human_chorionic_gonadotropin.pdb")
                print('Extracting Done!')
            condition = False


    print("Done")
