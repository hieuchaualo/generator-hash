import string, sys
import hashlib, binascii
import zlib;
import os
from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
from flask import jsonify
from Crypto.Hash import MD2

app = Flask(__name__)

@app.route('/hash', methods=['GET', 'POST'])
def hash():
    type = request.form['type']
    if type == '-s':
        param = request.form['param']
        input_str = param
        
        rMd5 = hashlib.md5(input_str.encode())
        rMd4 = hashlib.new('md4', input_str.encode())
        rSha1 = hashlib.new('sha1', input_str.encode())
        rSha224 = hashlib.sha224(input_str.encode())
        rSha256 = hashlib.sha256(input_str.encode())
        rSha384 = hashlib.new('sha384', input_str.encode())
        rSha512 = hashlib.new('sha512', input_str.encode())
        rRipeMd160 = hashlib.new('ripemd160', input_str.encode())
        rCrc32 = zlib.crc32(input_str.encode())
        # rPanama = hashlib.new('panama', input_str.encode())
        # rTiger = hashlib.new('tiger', input_str.encode())
        rMd2 = MD2.new(input_str.encode())
        # rMd2 = rMd2.update()
        # rAdler32 = hashlib.new('adler32', input_str.encode())
        # rCrc32 = hashlib.new('crc32', input_str.encode())
        return jsonify(
            md5=rMd5.hexdigest(),
            md4=rMd4.hexdigest(),
            sha1=rSha1.hexdigest(),
            sha224=rSha224.hexdigest(),
            sha256=rSha256.hexdigest(),
            sha384=rSha384.hexdigest(),
            sha512=rSha512.hexdigest(),
            ripemd160=rRipeMd160.hexdigest(),
            crc32=hex( rCrc32% (1<<32)),
            # rPanama=panama.hexdigest(),
            # tiger=rTiger.hexdigest(),
            md2=rMd2.hexdigest(),
            # adler32=rAdler32.hexdigest(),
            # crc32=rCrc32.hexdigest(),
        )
        
    elif type =='-f' :
        param = request.files['param']
        if param.filename:
            # fn = os.getcwd() + os.path.basename(param.filename)
            rMd5 = hashlib.md5(param.read())
            rMd4 = hashlib.new('md4', param.read())
            rSha1 = hashlib.new('sha1', param.read())
            rSha224 = hashlib.sha224(param.read())
            rSha256 = hashlib.sha256(param.read())
            rSha384 = hashlib.new('sha384', param.read())
            rSha512 = hashlib.new('sha512', param.read())
            rRipeMd160 = hashlib.new('ripemd160', param.read())
            rCrc32 = zlib.crc32('crc32', param.read())
            rMd2 = MD2.new(param.read())
            # rMd2 = rMd2.update()
            # print(r.hexdigest())
            return jsonify(
            md5=rMd5.hexdigest(),
            md4=rMd4.hexdigest(),
            sha1=rSha1.hexdigest(),
            sha224=rSha224.hexdigest(),
            sha256=rSha256.hexdigest(),
            sha384=rSha384.hexdigest(),
            sha512=rSha512.hexdigest(),
            ripemd160=rRipeMd160.hexdigest(),
            crc32=hex( rCrc32% (1<<32)),
            # rPanama=panama.hexdigest(),
            # tiger=rTiger.hexdigest(),
            md2=rMd2.hexdigest(),
            # adler32=rAdler32.hexdigest(),
            # crc32=rCrc32.hexdigest(),
            )
        else:
            return jsonify(failed='file does not exits')
    else :
        return jsonify(failed='maybe incorrect syntax')


@app.route('/read', methods=['GET', 'POST'])
def readString():
    path = request.form['path']
    fstring = []
    min = 4
    with open(path, errors="ignore") as f:
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                fstring.append(result)
            result = ""
        return jsonify(
            string=fstring
        )

if __name__ == "__main__":
    app.run(debug = True)