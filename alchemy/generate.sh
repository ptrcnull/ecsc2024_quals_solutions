#!/bin/sh

secrets_file="./secret.bin"
flag_file="./flag.txt"

if [ ! -f "$flag_file" ]; then
    echo "FLAG FILE MISSING !"
    exit -1
fi

rm "$secrets_file"
if [ ! -f "$secrets_file" ]; then
    dd if=/dev/urandom of="$secrets_file" bs=14 count=1 2>/dev/null
fi

secret=`cat $secrets_file`

# AES enc
enc_aes=`openssl enc -aes-256-cbc -pbkdf2 -iter 1000001 -salt -a -A -kfile "$secrets_file" -in $flag_file`


# Gen SHA512 xor key
sha512="$secret`echo -n "$secret" | sha512sum | cut -d' ' -f1`"

echo "enc_aes: $(echo $enc_aes)" #| xxd -ps)"
echo "sha512: $(echo $sha512)" #| xxd -ps)"

# xor
perl -e '@a=split("", $ARGV[0]); @b=split("", $ARGV[1]); print unpack "H2", chr(ord(shift @a)^ord(shift @b)) while @a; print "\n"' "$sha512" "$enc_aes"  
