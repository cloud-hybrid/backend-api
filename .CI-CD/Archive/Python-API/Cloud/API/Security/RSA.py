""" PEM
-------

Example)
    In order to successfully generate and copy a public key to a target server:

    ssh-keygen -y -f key.pem > key.pub
        --> Generates a public key from a given private key.

    ssh-copy-id -f -i key snow@192.168.1.5
        --> Copies the newly created public-key to a target server.

    ssh -i key.pem snow@192.168.1.5
        --> Successfully connects to a target server using a given `key.pem` file.

"""

from . import *

class File(Secure):
    Generator = Blueprint("RSA", __name__)
    Route = Secure.Route + "RSA"
    Methods = Secure.Methods

    Description = """\
       ... ... ...
    """

    Metadata    = {**{
        "Description"   : "{}".format(Description),
        "Title"         : "{}".format(Generator.name.replace("-", " ").title()),
        "Generator"     : "{}".format(Generator.name),
        "Page"          : "{}".format(Generator.name.casefold())
    }, **Secure.Metadata}

    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

    @Method
    @Generator.route(Route, methods = Methods)
    @Authenticate
    def generate():
        with TDirectory() as Directory:
            UUID = uuid.uuid4()
            _File = None

            command = "ssh-keygen -b {} -t rsa -f {}/key-{} -C {} -N ''".format(
                String(Request.args.get("size", default = 4096)),
                Directory,
                UUID,
                Request.args.get("comment", default = U"...")
            )

            subprocess.Popen(
                Spliter(command),
                stdin = subprocess.DEVNULL,
                stdout = subprocess.DEVNULL,
                stderr = subprocess.DEVNULL,
                shell = False
            ).wait()

            with open("{}/key-{}".format(Directory, UUID), "a") as File:
                File.write("\n")
                _File = File.name

            return Handler(_File,
                mimetype = "application/pkcs8" if Request.args.get("download", default = 1) == 1 \
                    or Request.args.get("download", default = 1) == "true" \
                        or Request.args.get("download", default = 1) == "True" \
                            or Request.args.get("download", default = 1) == True \
                                else "text/plain",
                attachment_filename = "{}".format(Request.args.get("filename", default = "RSA-Key")),
                as_attachment = True if Request.args.get("download", default = 1) == 1 \
                    or Request.args.get("download", default = 1) == "true" \
                        or Request.args.get("download", default = 1) == "True" \
                            or Request.args.get("download", default = 1) == True \
                                else False,
                cache_timeout = 1.0)
