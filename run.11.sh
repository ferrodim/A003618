#!/bin/bash
date -R
if test -f test.bin; then
        echo "bin file already exist. Skip"
else
        python3 gen.py 11
        date -R
fi
md5sum eratosthenes.11.bin
date -R
python3 prime.py 11
date -R
