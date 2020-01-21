# coding : utf-8

"""
@author : Zygnematophyce
Master II BIB - 2019 2020
Projet Deep Learning
"""

import os
import sys

if __name__ == "__main__":
    print("Split chain protein")

    #path_file = "modified_1qfw_Fv_Human_chorionic_gonadotropin.pdb"
    try:
        path_file = str(sys.argv[1])
    except IndexError:
        sys.exit("Erreur dans l'indexage des arguments")

    folder_name=os.path.dirname(path_file)

    # create pdb_zdock folder
    #print(folder_name)
    full_name = folder_name+"/pdb_zdock"
    #print(full_name)
    try:
        os.mkdir(full_name)
    except OSError:
        print ("Creation of the directory %s failed" % full_name)
    else:
        print ("Successfully created the directory %s " % full_name)

    input_pymol = open("pymol_tmp.pml", "w")
    input_pymol.write("load "+path_file+"\n")
    filename = path_file[:-4]
    input_pymol.write("split_chains \n")
    input_pymol.write("models=cmd.get_names()\n")
    input_pymol.write("for i in range(1,len(models)):print(models[i])\n")
    #input_pymol.write("for i in range(1,len(models)):cmd.save(models[i] +"+"'.pdb'"+", models[i]"+")\n")
    #for i in range(1,len(models)):cmd.save("output_zdock/modified_1qfw_Fv_Human_chorionic_gonadotropin_Iin_PU0_1-110/pdb_zdock/"+models[i] +'.pdb', models[i])
    input_pymol.write("for i in range(1,len(models)):cmd.save(\""+full_name+"/\"+models[i] +"+"'.pdb'"+", models[i]"+")\n")
    #input_pymol.write("if (cmd.count_atoms(\"test\")!=0):cmd.save(\""+name_folder+"/"+"\"+models[0] +"+"models[1]+"+"'.pdb'"+", \"all\")\n")
    #input_pymol.write("quit")
    input_pymol.close()
    os.system("pymol -p pymol_tmp.pml")


