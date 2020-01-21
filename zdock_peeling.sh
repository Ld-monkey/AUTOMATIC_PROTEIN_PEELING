#!/bin/bash

export _POSIX2_VERSION=199209;
courant_directory=$(pwd)
ZDOCK=$courant_directory/zdock_linux/;

for folder_orign in  `ls output_zdock/`;
do
    echo $folder_orign;
    cd output_zdock/$folder_orign/pdb_zdock/
    #echo $(pwd)
    cp $ZDOCK/uniCHARMM ./
    cp $ZDOCK/create_lig ./
    for pdb_zdock in `ls *.pdb`;
    do
        echo "Running zdock locally.";
        echo "Create receptor pdb file.";
        echo $pdb_zdock;
        $ZDOCK/mark_sur "$pdb_zdock" $pdb_zdock"_r.pdb";
    done
    echo "Create ligand pdb file.";
    echo $pdb_zdock;
    $ZDOCK/mark_sur $pdb_zdock $pdb_zdock_l.pdb
done
cd $courant_directory
done

exit

cp $ZDOCK/uniCHARMM ./
cp $ZDOCK/create_lig ./

# for docking with zdock
for pdb_zdock in `ls output_zdock/*/*/*.pdb`;
do
    echo "Running zdock locally.";
    echo "Create receptor pdb file.";
    echo $pdb_zdock;
    $ZDOCK/mark_sur /$pdb_zdock /$pdb_zdock_r.pdb;
done
#echo "Create ligand pdb filE.";
#echo $pdb_zdock;
#$ZDOCK/mark_sur $pdb_zdock $pdb_zdock_l.pdb
#done
