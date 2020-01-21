#!/bin/bash

echo "select only true interaction between pu and protein."

# output for results.
mkdir output_interactions
mkdir output_zdock
mkdir pu_no_interactions

for file_chain in `ls all_chains/*`;
do
    for file_pdb in `ls 1qfw/pdb/*pdb`;
    do
        echo all_chains/$file_chain $file_pdb;
        python interactions_PU_protein.py $file_chain $file_pdb
    done
done

#move in output_interactions folder.

#for move_file in `ls *.pdb`;
#do
#    echo $move_file;
#    mv $move_file output_interactions/$move_file
#done

#remove empty folder
for folder in `ls output_zdock/`;
do
    echo "------------"
    #echo $folder
    if [ ! "$(ls -A output_zdock/$folder)" ]
    then
        echo "$folder is empty!"
        echo "remove $folder"
        rm -r output_zdock/$folder
    else
        echo "$folder is not empty"
    fi;
done

exit

# for each chain
for zdock in `ls output_zdock/*/*pdb`;
do
    echo $zdock;
    python break_protein_chain.py $zdock;
done


# for docking with zdock
for pdb_zdock in `ls output_zdock/*/*/*.pdb`;
do
    export _POSIX2_VERSION=199209;
    ZDOCK=zdock_linux/;
    $ZDOCK/zdock
    echo "Running zdock locally.";
    echo "Create receptor pdb file.";
    echo $pdb_zdock;
    $ZDOCK/mark_sur $pdb_zdock ($pdb_zdock)_r.pdb
done
    echo "Create ligand pdb filE.";
    echo $pdb_zdock;
    $ZDOCK/mark_sur $pdb_zdock $pdb_zdock_l.pdb
done


