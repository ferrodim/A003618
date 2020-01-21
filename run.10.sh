#!/bin/bash
date -R
if test -f test.bin; then
        echo "bin file already exist. Skip"
else
        python3 gen.py 10
        date -R
fi
md5sum eratosthenes.10.bin
date -R
python3 prime.py 10
date -R
