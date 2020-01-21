#!/bin/bash
date -R
if test -f test.bin; then
        echo "bin file already exist. Skip"
else
        python3 gen.py 9
        date -R
fi
md5sum eratosthenes.9.bin
date -R
python3 prime.py 9
date -R
