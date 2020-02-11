# SRA221-PSU-Hozza

## Steps to working through the PKI Lab

1. Create your environment
```
cp /usr/lib/ssl/openssl.cnf ./
mkdir demoCA
cd demoCA
mkdir certs crl newcerts
touch index.txt serial
echo 1000 > serial
cd ..
```

2. Generate SSL Certificates
```
openssl req -new -x509 -keyout ca.key -out ca.crt -config openssl.cnf
openssl genrsa -aes128 -out server.key 1024
openssl rsa -in server.key -text
openssl req -new -key server.key -out server.csr -config openssl.cnf
openssl ca -in server.csr -out server.crt -cert ca.crt -keyfile ca.key -config openssl.cnf
```

3. Make web directories
```
sudo mkdir /var/www/sra221
cp index.html /var/www/sra221
```
