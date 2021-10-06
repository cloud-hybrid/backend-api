export SUB="/C=US/ST=MN/O=Cloud Technology LLC./CN=localhost/subjectAltName=DNS:*.nexus.cloud-technology.io,DNS:nexus.cloud-technology.io,localhost,*.localhost,0.0.0.0"

openssl req -x509 -newkey rsa:8192 -nodes -sha256   \
    -days 365 -passin "pass:Development"            \
        -subj "${SUB}" -keyout Development.key      \
            -out Development.pem

openssl req -config Development.conf -new -x509 -sha256 -newkey rsa:2048 -nodes -keyout Development.key -days 1024 -out Development.crt
openssl pkcs12 -export -out Development.pfx -inkey Development.key -in Development.crt

# MacOS
# sudo security -v add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain Development.crt

# Ubuntu LTS 20.04
# sudo apt install libnss3-tools --yes
# pk12util -d "sql:${HOME}/.pki/nssdb" -i Development.pfx
# certutil -d sql:$HOME/.pki/nssdb -A -t "P,," -n "Development Certificate" -i Development.crt

# https://stackoverflow.com/questions/7580508/getting-chrome-to-accept-self-signed-localhost-certificate
