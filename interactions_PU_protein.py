# coding : utf-8

"""
@author : Zygnematophyce
Master II BIB - 2019 2020
Projet Deep Learning
"""

#condition : si c'est la meme chaine quitter directement [ ]

#testinteraction = interfaceResidues("all",cA="c. "+chains[0]+"\"", cB="c. "+chains[1]+"\"", cutoff=0.5, selName="test")
#testinteraction = interfaceResidues(\"all\",cA=\"c. ",chains[0],"\", cB=\"c. "+chains[1]+"\", cutoff=0.5, selName=\"test\")

#select truc1, all
#cmd.save("result1.pdb", "truc1")
#cmd.save("output_zdock/"+models[0] +models[1]+".pdb", "all")

import os
import sys

if __name__ == "__main__":
    print("Interraction between PU and protein")

    try:
        #path_file = "modified_1qfw_Fv_Human_chorionic_gonadotropin_M.pdb"
        #path_pu = "1qfw/pdb/in_PU0_1-110.pdb"
        path_file = str(sys.argv[1])
        path_pu = str(sys.argv[2])
    except IndexError:
        sys.exit("Erreur dans l'indexage des arguments")

    file_pdb = open(path_file,"r")
    #print(file_pdb.readline())
    chain_1=file_pdb.readline()
    verif_same_chain=file_pdb.readline()
    chain_1=chain_1[21:22]
    verif_same_chain=verif_same_chain[21:22]
    print(verif_same_chain)
    if chain_1 != verif_same_chain:
        chain_1 = verif_same_chain
    print(chain_1)
    print(verif_same_chain)
    file_pdb.close()

    file_pu=open(path_pu,"r")
    chain_2=file_pu.readline()
    chain_2=chain_2[21:22]
    verif_same_pu_chain=file_pu.readline()
    verif_same_pu_chain=verif_same_pu_chain[21:22]
    if chain_2 != verif_same_pu_chain:
        print("petite bug de decoupage")
        chain_2=verif_same_pu_chain
    print(chain_2)
    print(verif_same_pu_chain)
    file_pu.close()

    input_pymol = open("pymol_interaction_pu.pml", "w")
    input_pymol.write("load "+path_file+"\n")
    input_pymol.write("load "+path_pu+"\n")
    filename = path_file[:-4]
    file_pu = path_pu[:-4]

    print(os.path.basename(filename))
    print(os.path.basename(file_pu))
    firtname_folder=os.path.basename(filename)
    lastname_folder=os.path.basename(file_pu)
    name_folder="output_zdock/"+firtname_folder+lastname_folder

    name_folder_2="pu_no_interactions"

    print("the name folder is ",name_folder)
    print("--------------")
    try:
        os.mkdir(name_folder)
    except OSError:
        print ("Creation of the directory %s failed" % name_folder)
    else:
        print ("Successfully created the directory %s " % name_folder)

    input_pymol.write("chains = cmd.get_chains()\n")
    input_pymol.write("print(chains)\n")
    input_pymol.write("models=cmd.get_names()\n")
    input_pymol.write("run InterfaceResidues.py\n")
    input_pymol.write("testinteraction = interfaceResidues(\"all\",cA=\"c. "+chain_1+"\", cB=\"c. "+chain_2+"\", cutoff=0.5, selName=\"test\")\n")
    input_pymol.write("if(len(chains)==1):quit\n")
    #input_pymol.write("show sticks, test\n")
    #input_pymol.write("if (cmd.count_atoms(\"test\")==0):cmd.delete(\"test\")\n")
    input_pymol.write("if (cmd.count_atoms(\"test\")==0):cmd.save(\""+name_folder_2+"/"+"\"+models[0] +"+"models[1]+"+"'.pdb'"+", \"all\")\n")

    #input_pymol.write("if (cmd.count_atoms(\"test\")!=0):cmd.save(models[0] +"+"models[1]+"+"'.pdb'"+", \"test\")\n")
    #input_pymol.write("if (cmd.count_atoms(\"test\")!=0):cmd.save(\"output_interactions/\"+models[0] +"+"models[1]+"+"'.pdb'"+", \"test\")\n")
    #input_pymol.write("if (cmd.count_atoms(\"test\")!=0):cmd.save(\""+name_folder+"\"+models[0] +"+"models[1]+"+"'.pdb'"+", \"test\")\n")
    input_pymol.write("if (cmd.count_atoms(\"test\")!=0):cmd.save(\""+name_folder+"/"+"\"+models[0] +"+"models[1]+"+"'.pdb'"+", \"all\")\n")
    #"output_zdock/"+
    #""output_interactions/"+
    input_pymol.write("quit\n")
    input_pymol.close()
    os.system("pymol -p pymol_interaction_pu.pml")


