function onStateChange() {
    const value = document.getElementById("selectType").value;
    if (value == 0) {
        document.getElementById('fileSelected').style.display = 'none';
    } else {
        document.getElementById('fileSelected').style.display = 'block';
    }
}

async function onHashing() {
    const value = document.getElementById("selectType").value;
    let type = '';
    let param = '';
    var filename = '';
    if (value == 0) {
        param = document.getElementById('string').value;
        type = '-s';

    } else {
        param = document.getElementById('fileSelected').files[0];
        type = '-f';
    }
    let result = await hash(type, param);
    document.getElementById('inputMD5').value = result['md5'];
    document.getElementById('inputMD4').value = result['md4'];
    document.getElementById('inputSHA1').value = result['sha1'];
    document.getElementById('inputSHA224').value = result['sha224'];
    document.getElementById('inputSHA256').value = result['sha256'];
    document.getElementById('inputSHA384').value = result['sha384'];
    document.getElementById('inputSHA512').value = result['sha512'];
    document.getElementById('inputCRC16').value = result['crc32'];
    document.getElementById('inputRIPEMD160').value = result['ripemd160'];
}

async function hash(type, param) {
    const formData = new FormData();
    formData.append('type', type);
    formData.append('param', param);
    const request = await fetch("http://localhost:5000/hash", {
        method: 'POST',
        body: formData
    })
    const response = await request.json()

    return response;
}