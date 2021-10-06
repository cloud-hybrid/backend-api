# def generate():
#     __cn__ = request.args.get("common-name", default = "cloudhybrid.io")
#     __args__ = request.args.getlist("san")
#     return dict(enumerate([__cn__] + __args__))
#     CN = request.args.get("common-name", default = "cloudhybrid.io")
#     SANs = (self.parameters[0][1:])
#     enumSANs = "DNS.1 = {}".format(CN) + "\n" + "\n".join("DNS.{i} = {san}".format(i = _i + 2, san = value) for _i, value in enumerate(SANs))
#     strSANs = " ".join(_i for _i in SANs)

#     _config = """[req]
# distinguished_name = req_distinguished_name
# req_extensions = v3_req
# [req_distinguished_name]
# countryName = countryName
# countryName_default = US
# stateOrProvinceName = stateOrProvinceName
# stateOrProvinceName_default = Minnesota
# localityName = localityName
# localityName_default = Minneapolis
# organizationName = organizationName
# organizationName_default = Cloud Hybrid
# organizationalUnitName = organizationalUnitName
# organizationalUnitName_default = Engineering
# commonName = commonName
# commonName_default = {_default}
# [v3_req]
# subjectAltName = @alt_names
# [alt_names]
# {_DNS}
# """.format(_default = CN, _DNS = enumSANs)
    
#     with open("alts.cnf", "w") as f:
#         f.write(_config)

#         f.close()

#     f.close()

#     commands = {
#         "Generate-Key" : "openssl genrsa -out private-{_name}.key 2048".format(_name = CN),
        
#         "Generate-CSR" : "openssl req -newkey rsa:2048 -sha256 -nodes -keyout {_name}.key -out {_name}.csr -config alts.cnf -subj '/C=US/ST=Minnesota/L=Minneapolis/O=Cloud Hybrid/OU=Engineering/CN={_name}'".format(
#             _name = CN
#         ),

#         "Generate-CRT" : "openssl x509 -signkey {_name}.key -req -in {_name}.csr -req -days 365 -out {_name}.crt -extensions v3_req -extfile alts.cnf".format(_name = CN),
        
#         "View-CSR": "openssl req -text -noout -verify -in {}.csr".format(CN),
        
#         "View-Certificate": "openssl x509 -text -noout -in {}.crt".format(CN),

#         # "ACM-Upload" : "aws acm import-certificate --certificate file://{_dir}/{_name}.crt --private-key file://{_dir}/{_name}.key --profile dev --region us-east-1".format(_name = CN, _dir = os.getcwd())
#         "ACM-Upload" : "aws acm import-certificate --certificate file://{_dir}/{_name}.crt --private-key file://{_dir}/{_name}.key --profile prod --region us-east-1".format(_name = CN, _dir = os.getcwd())
#     }
#     _return = []
#     for command in list(commands.values()):
#         with subprocess.Popen(
#             shlex.split(command),
#             stdout = sys.stdout,
#             stdin = sys.stdout,
#             stderr = sys.stderr,
#             text = True,
#             shell = False,
#             start_new_session = False
#             ) as process:
#                 process.wait()
#                 process.poll()
        
#         _return.append(str(process))
    
#     eval("self.handler").content(_return)

#     os.remove("alts.cnf")
#     os.remove("private-{}.key".format(CN))