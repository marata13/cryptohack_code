from pwn import *
import json
import Crypto.Util.number
import codecs

r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

received = json_recv()
while True:

    if received["type"] == "base64":
        base64_bytes = received["encoded"].encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decoded = message_bytes.decode('ascii')
    elif received["type"] == "hex":
        bytess = bytes.fromhex(received["encoded"])
        decoded = bytess.decode('ascii')
    elif received["type"] == "rot13":
        decoded = codecs.encode(received["encoded"], 'rot_13')
    elif received["type"] == "bigint":
        decoded = Crypto.Util.number.long_to_bytes(int(received["encoded"], base=16)).decode('ascii')
    elif received["type"] == "utf-8":
        b = []
        for i in range(len(received["encoded"])):
            c = received["encoded"][i].to_bytes(1, 'big')
            b.append(c.decode("utf-8"))
        decoded = "".join(b)



    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

    received = json_recv()
