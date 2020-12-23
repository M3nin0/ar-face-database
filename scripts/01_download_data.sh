#!/bin/bash

mkdir -p dbfs

wget http://cbcsl.ece.ohio-state.edu/protected-dir/dbf1.tar.tar
wget http://cbcsl.ece.ohio-state.edu/protected-dir/dbf2.tar
wget http://cbcsl.ece.ohio-state.edu/protected-dir/dbf3.tar
wget http://cbcsl.ece.ohio-state.edu/protected-dir/dbf4.tar
wget http://cbcsl.ece.ohio-state.edu/protected-dir/dbf5.tar
wget http://cbcsl.ece.ohio-state.edu/protected-dir/dbf6.tar.Z
wget http://cbcsl.ece.ohio-state.edu/protected-dir/dbf7.tar.Z
wget http://cbcsl.ece.ohio-state.edu/protected-dir/dbf8.tar.Z

# prepare dbf1
mv dbf1.tar.tar dbf1.tar
tar -xvf dbf1.tar
uncompress dbf1/*.Z

mv dbf1.tar dbfs/

# prepare dbf2
tar -xvf dbf2.tar
uncompress dbf2/*.Z

mv dbf2.tar dbfs/

# prepare dbf3
tar -xvf dbf3.tar
uncompress dbf3/*.Z

mv dbf3.tar dbfs/

# prepare dbf4
tar -xvf dbf4.tar
uncompress dbf4/*.Z

mv dbf4.tar dbfs/

# prepare dbf5
tar -xvf dbf5.tar
uncompress dbf5/*.Z

mv dbf5.tar dbfs/

# prepare dbf6
uncompress dbf6.tar.Z
tar -xvf dbf6.tar

mv dbf6.tar dbfs/

# prepare dbf7
uncompress dbf7.tar.Z
tar -xvf dbf7.tar

mv dbf7.tar dbfs/

# prepare dbf8
uncompress dbf8.tar.Z
tar -xvf dbf8.tar

mv dbf8.tar dbfs/

# merge files
mkdir -p merge
mv {dbf1,dbf2,dbf3,dbf4,dbf5}/*.raw merge
mv {dbfaces6,dbfaces7,dbfaces8}/*.raw merge

# remove old files
rm -rf {dbf1,dbf2,dbf3,dbf4,dbf5,dbfaces6,dbfaces7,dbfaces8}

# Convert .raw files to .jpeg
# Adapted from: https://github.com/matheustguimaraes/organize-AR-face-db.git
mkdir -p ar_out
python raw2jpeg.py
