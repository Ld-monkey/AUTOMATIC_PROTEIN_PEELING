# coding : utf-8

"""
@author : Zygnematophyce
Master II BIB - 2019 2020
Projet Deep Learning
"""

import os
import math

if __name__ == "__main__":
    print("Association pu-protéine")


    #liste de toute les fichiers dans output_zdock/
    list_folder = os.listdir("output_zdock/")

    #list des chemins relatifs de tous les pdb de pu proteine.
    list_final_pu_protein = []

    for folder_name in list_folder:
        #print(folder_name)
        #liste de toute les pdb associés avec leurs pu.
        folder_name = "output_zdock/"+folder_name
        #print(folder_name)
        list_protein_pu = os.listdir(folder_name)
        for name in list_protein_pu:
            if name[-4:] == ".pdb":
                name = folder_name+"/"+name
                list_final_pu_protein.append(name)
            else :
                pass

    # Cette fois si on lit le fichier chaque association de pu - protein

    mega_list=[]
    matrix_list = []

    # Faire 2 chaines 1 liste de chaine M et une liste de chaine I.
    #[[[1, 'M', 'ASP', '81.517', '40.107', '35.071'],....,
    # [1, 'B', 'LYS', '83.231', '4.613', '45.663'],...]]
    numero_list=0
    tmp_chain = None
    var_chain = None
    for path_pdb in list_final_pu_protein:
        with open(path_pdb, "r") as pdb_file:
            matrix_list=[]
            numero_list += 1
            for line in pdb_file:
                if line.startswith("ATOM") and line[12:16].strip() == "CA":
                    #print("coucou")
                    #print("var chain = %",var_chain,"tmp_chain",tmp_chain)
                    #print(type(var_chain))
                    #print(type(tmp_chain))
                    #print(id(var_chain))
                    #print(id(tmp_chain))
                    if tmp_chain == var_chain:
                        print("prout")
                        mini_list=[]
                        # Pour le numero de liste
                        mini_list.append(numero_list)
                        # Pour la chaine:
                        mini_list.append(line[21:23].strip())
                        # Pour AA :
                        mini_list.append(line[17:20].strip())
                        # Pour x
                        mini_list.append(line[30:38].strip())
                        # Pour y
                        mini_list.append(line[38:46].strip())
                        # Pour z
                        mini_list.append(line[46:54].strip())

                        # Ajoute la mini_list dans la matrix_list
                        matrix_list.append(mini_list)

                        # Variable de chaine
                        var_chain = line[21:23].strip()


                    print("var chain = %",var_chain,"tmp_chain",tmp_chain)

                    # Variable de chaine
                    var_chain = line[21:23].strip()


                    # Condition pour départager les chaines
                    if (tmp_chain == None):
                        tmp_chain = line[21:23].strip()

                    # au moment ou la chaine a changé.
                    if (tmp_chain != var_chain):
                        print("ok")
                        #ajoute une seconde table pour cette chaine
                        mini_list_second=[]
                        # Pour le numero de liste
                        mini_list_second.append(numero_list)
                        # Pour la chaine:
                        mini_list_second.append(line[21:23].strip())
                        # Pour AA :
                        mini_list_second.append(line[17:20].strip())
                        # Pour x
                        mini_list_second.append(line[30:38].strip())
                        # Pour y
                        mini_list_second.append(line[38:46].strip())
                        # Pour z
                        mini_list_second.append(line[46:54].strip())

                        # ajoute la mini_list_second dans la matrix_list
                        matrix_list.append(mini_list_second)

            # Ajoute a la mega_list la matrix_list
            mega_list.append(matrix_list)

    #[[[1, 'M', 'ASP', '81.517', '40.107', '35.071'],....,
    # [1, 'B', 'LYS', '83.231', '4.613', '45.663'],...]]
    #print(matrix_list)

    def euclidian_distance(xa, ya, za, xb, yb, zb, cutoff = 0.5):
        distance = math.sqrt(( (xb - xa)**2 + (yb - ya)**2 + (zb - za)**2 ))
        if distance <= cutoff:
            print(distance)
            return True
        else:
            return False

    # compare entre chaine si il y a deux acides aminés qui sont en contact.
    # et mettre dans une liste l'ensemble de ces composés par paire.

    # Afficher la liste complete.
    #print(mega_list)
    
    #for i in range(0, len(mega_list), 1):
        #print(mega_list[i])

    # Afficher la chain A et la chaine B
    print(mega_list[0][:])

    count_section = 

    print(mega_list[0][2])
