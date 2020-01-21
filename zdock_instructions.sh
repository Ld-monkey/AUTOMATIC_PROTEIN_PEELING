#!/bin/bash

echo "Zdock"

#test
#rm complex*
#rm *.out
#rm *_r.pdb
#rm *_l.pdb

export _POSIX2_VERSION=199209

ZDOCK = zdock_linux

cp $ZDOCK/uniCHARMM ./
cp $ZDOCK/create_lig ./

#sectionne seulement les atomes.
cat 1A19.pdb | grep ATOM > 1A2Patom.pdb

#Pour le docking on a besoin qu'une chaine la chaine A.
# Modifie en selectionnant la chaine A avec gedit

# On selection les atomes pour la 2eme structure.
cat 1A19.pdb | grep ATOM > 1A19Patom.pdb

# On selecitonne la chaine A avec gedit.

echo "Running zdock locally."

# Create new receptor and ligand pdb files xxx_r.pdb and xxx_l.pdb
echo "Create ligand and receptor pdb files."
$ZDOCK/mark_sur 1A2P_A.pdb 1BRS_r.pdb
$ZDOCK/mark_sur 1A19_A.pdb 1BRS_l.pdb

# Send the docking simulations.
$ZDOCK/zdock -R 1BRS_r.pdb -L 1BRS_l.pdb -o 1BRS_zdock.out

#Done
echo "Zdock done"

echo "Keep the top 15 solution"
# Keep the top 15 solutions N=15.
head -n 19 1BRS_zdock.out > 1BRS_zdock_15.out

#We can create pdb files for the top 15 docking solutions from the short Zdock
#output file.
echo "Create pdb files for the top 15 docking solutions."
perl $ZDOCK/create.pl 1BRS_zdock_15.out
echo "solutions done"

# fix atom record:
for fix_atom in  `ls complex*`;
do
    #echo $fix_atom
    cat $fix_atom | grep ATOM > $fix_atom.pdb;
done

