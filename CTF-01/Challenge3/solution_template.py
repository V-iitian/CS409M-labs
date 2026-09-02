from pwn import *

HOST = "10.129.6.191"
PORT = 8081

# Uncomment the 'process' line below when you want to test locally, uncomment the 'remote' line below when you want to execute your exploit on the server
#target = process(["python", "./server.py"])
target = remote(HOST, PORT)

def recvuntil(msg):
    resp = target.recvuntil(msg.encode()).decode()
    print(resp)
    return resp

def sendline(msg):
    print(msg)
    target.sendline(msg.encode())
    response = target.recvline().decode()
    print(f"Server response: {response}")
    return response

def recvline():
    resp = target.recvline().decode()
    print(resp)
    return resp

def recvall():
    resp = target.recvall().decode()
    print(resp)
    return resp


# ===== YOUR CODE BELOW =====


payload = b"a"*30000
payload = payload.hex()
# TODO: This variable should finally contain the hex-string you want to send
# ===== YOUR CODE ABOVE =====


recvuntil("string: ")
sendline(payload)

for level in range(100):
    recvuntil("c1: ")
    c1 = recvline().strip()

    recvuntil("c2: ")
    c2 = recvline().strip()
    
    recvuntil("c1 or c2: ")
    # ===== YOUR CODE BELOW =====
    # Write code here to decide whether to send c1 or c2
    # The variable c1 (which is of type str) contains the hex-encoded version of c1 returned by the server
    # The variable c2 (which is of type str) contains the hex-encoded version of c2 returned by the server
    c1_byte = bytes.fromhex(c1)
    c2_byte = bytes.fromhex(c2)
    if b"a" in c1_byte:
        guess = 2
    elif b"a" in c2_byte:
        guess = 1
    else:
        guess = 1
    # TODO: Set guess to 1 or 2 accordingly if you think the correct answer is c1 vs. c2 respectively
    # ===== YOUR CODE ABOVE =====
    response = sendline(f"c{guess}")
    if "Incorrect" in response:
        break


#recvall()
try:
    resp = target.recvall(timeout=5).decode()
except Exception as e:
    print("recvall issue:", e)
print(resp)
target.close()
