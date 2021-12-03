#!/bin/bash

if [ ! -e $1 ]; then
    echo "No such svg file"
fi

# ファイル名生成
base_path=$1

for ((i=1 ; i<360 ; i++))
do
    # 三桁にゼロ埋め
    add_zero_i=000${i}
    zero_padding_i="${add_zero_i: -3}"

    # 新しいファイルパス
    new_path=${base_path/000/${zero_padding_i}}

    # 痴漢 and 別名保存
    sed -e 's/rotate(0, 50, 50)/rotate('$i', 50, 50)/g' ${base_path} > ${new_path}
done
