![Alt text](diffi.drawio.svg)

docker build -t monimageubuntu .

openssl dhparam -out dhparams.pem 2048

openssl genpkey -paramfile dhparams.pem -out privatekey1.pem/

openssl pkey -in privatekey1.pem -pubout -out publickey1.pem

openssl genpkey -paramfile dhparams.pem -out privatekey2.pem/

openssl pkey -in privatekey2.pem -pubout -out publickey2.pem

openssl pkeyutl -derive -inkey privatekey1.pem -peerkey publickey2.pem -out sharedkey1.bin/

openssl pkeyutl -derive -inkey privatekey2.pem -peerkey publickey1.pem -out sharedkey2.bin

diff sharedkey1.bin sharedkey2.bin && echo "Les clés partagées sont identiques" || echo "Les clés partagées sont différentes"
