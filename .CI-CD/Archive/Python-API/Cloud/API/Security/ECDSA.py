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
    Generator = Blueprint("ECDSA", __name__)
    Route = Secure.Route + "ECDSA"
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
        """
        bits & size (Integer): Argument can be one of three elliptic curve sizes: 256,
            384 or 521 bits.  Attempting to use bit lengths other than these three
            values for ECDSA keys will fail.
        """
        with TDirectory() as Directory:
            UUID = uuid.uuid4()
            _File = None

            command = "ssh-keygen -b {} -t ECDSA -f {}/key-{} -C {} -N ''".format(
                String(Request.args.get("size",
                    default = Request.args.get("bits", default = 521))),
                Directory,
                UUID,
                Request.args.get("comment", default = "...")
            )

            subprocess.Popen(
                Spliter(command),
                stdin = subprocess.DEVNULL,
                stdout = subprocess.DEVNULL,
                stderr = subprocess.DEVNULL,
                shell = False
            ).wait()

            __ECDSA__ = {}

            Key = open("{}/key-{}".format(Directory, UUID), "w")

            __ECDSA__["Path"] = Key.name

            Key.write("\n")

            return Handler(__ECDSA__.get("Path"),
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
