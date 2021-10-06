""" PEM
-------

Example)
    >>> GET http://127.0.0.1:5000/API/Certificate/PEM?common-name=example.io&san=san-example.io&san=www.san-example.io&san=admin.san-example.io

    >>> __cn__ = Request.args.get("common-name", default = "cloudhybrid.io")
    >>> __args__ = Request.args.getlist("san")
    >>> return dict(enumerate([__cn__] + __args__))

    >>> {
    >>>     "0": "san-example.io",
    >>>     "1": "www.san-example.io",
    >>>     "2": "admin.san-example.io"
    >>> }

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

BANNER = """\

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃              Cloud Hybrid - Security Notice             ┃
┃             --------------------------------            ┃
┃   The following source file(s) contains confidential,   ┃
┃  proprietary information. Unauthorized use is strictly  ┃
┃    prohibited. No portions may be copied, reproduced,   ┃
┃      or incorporated outside of this domain without     ┃
┃         Cloud Hybrid LLC's prior written consent.       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

"""

class File(Secure):
    Generator = Blueprint("SSH-Banner", __name__)
    Route = Secure.Route + "SSH-Banner"
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
    def generate():
        with TDirectory() as Directory:
            UUID = uuid.uuid4()

            _File = None

            with open("{}/SSH-Banner-{}".format(Directory, UUID), "a") as File:
                File.write(BANNER)
                _File = File.name

            return Handler(_File,
                mimetype = "text/plain" if Request.args.get("download", default = 1) == 1 \
                    or Request.args.get("download", default = 1) == "true" \
                        or Request.args.get("download", default = 1) == "True" \
                            or Request.args.get("download", default = 1) == True \
                                else "text/plain",
                attachment_filename = "{}".format(Request.args.get("filename", default = "SSH-Banner")),
                as_attachment = True if Request.args.get("download", default = 0) == 1 \
                    or Request.args.get("download", default = 0) == "true" \
                        or Request.args.get("download", default = 0) == "True" \
                            or Request.args.get("download", default = 0) == True \
                                else False,
                cache_timeout = 1.0)
