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

SSHD = """\
# === Authentication === #
PasswordAuthentication no
ChallengeResponseAuthentication no
UsePAM yes

# === Session Display === #
X11Forwarding yes
AcceptEnv LANG LC_*

# === Daily Message === #
PrintMotd no

# === Subsystem Service(s) === #
Subsystem       sftp    /usr/lib/openssh/sftp-server
"""

DEFAULT = """\
# This is the sshd server system-wide configuration file.  See
# sshd_config(5) for more information.

# This sshd was compiled with PATH=/usr/bin:/bin:/usr/sbin:/sbin

# The strategy used for options in the default sshd_config shipped with
# OpenSSH is to specify options with their default value where
# possible, but leave them commented.  Uncommented options override the
# default value.

#Port 22
#AddressFamily any
#ListenAddress 0.0.0.0
#ListenAddress ::

#HostKey /etc/ssh/ssh_host_rsa_key
#HostKey /etc/ssh/ssh_host_ecdsa_key
#HostKey /etc/ssh/ssh_host_ed25519_key

# Ciphers and keying
#RekeyLimit default none

# Logging
#SyslogFacility AUTH
#LogLevel INFO

# Authentication:

#LoginGraceTime 2m
#PermitRootLogin prohibit-password
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10

#PubkeyAuthentication yes

# Expect .ssh/authorized_keys2 to be disregarded by default in future.
#AuthorizedKeysFile	.ssh/authorized_keys .ssh/authorized_keys2

#AuthorizedPrincipalsFile none

#AuthorizedKeysCommand none
#AuthorizedKeysCommandUser nobody

# For this to work you will also need host keys in /etc/ssh/ssh_known_hosts
#HostbasedAuthentication no
# Change to yes if you don't trust ~/.ssh/known_hosts for
# HostbasedAuthentication
#IgnoreUserKnownHosts no
# Don't read the user's ~/.rhosts and ~/.shosts files
#IgnoreRhosts yes

# To disable tunneled clear text passwords, change to no here!
PasswordAuthentication no
#PermitEmptyPasswords no

# Change to yes to enable challenge-response passwords (beware issues with
# some PAM modules and threads)
ChallengeResponseAuthentication no

# Kerberos options
#KerberosAuthentication no
#KerberosOrLocalPasswd yes
#KerberosTicketCleanup yes
#KerberosGetAFSToken no

# GSSAPI options
#GSSAPIAuthentication no
#GSSAPICleanupCredentials yes
#GSSAPIStrictAcceptorCheck yes
#GSSAPIKeyExchange no

# Set this to 'yes' to enable PAM authentication, account processing,
# and session processing. If this is enabled, PAM authentication will
# be allowed through the ChallengeResponseAuthentication and
# PasswordAuthentication.  Depending on your PAM configuration,
# PAM authentication via ChallengeResponseAuthentication may bypass
# the setting of "PermitRootLogin without-password".
# If you just want the PAM account and session checks to run without
# PAM authentication, then enable this but set PasswordAuthentication
# and ChallengeResponseAuthentication to 'no'.
UsePAM yes

#AllowAgentForwarding yes
#AllowTcpForwarding yes
#GatewayPorts no
X11Forwarding yes
#X11DisplayOffset 10
#X11UseLocalhost yes
#PermitTTY yes
PrintMotd no
#PrintLastLog yes
#TCPKeepAlive yes
#UseLogin no
#PermitUserEnvironment no
#Compression delayed
#ClientAliveInterval 0
#ClientAliveCountMax 3
#UseDNS no
#PidFile /var/run/sshd.pid
#MaxStartups 10:30:100
#PermitTunnel no
#ChrootDirectory none
#VersionAddendum none

# no default banner path
#Banner none

# Allow client to pass locale environment variables
AcceptEnv LANG LC_*

# override default of no subsystems
Subsystem	sftp	/usr/lib/openssh/sftp-server

# Example of overriding settings on a per-user basis
#Match User anoncvs
#	X11Forwarding no
#	AllowTcpForwarding no
#	PermitTTY no
#	ForceCommand cvs server
"""

class File(Secure):
    Generator = Blueprint("SSH-Settings", __name__)
    Route = Secure.Route + "SSH-Settings"
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

            if Request.args.get("default", default = 0) == "True" or \
            Request.args.get("default", default = 0) == "true" or \
            Request.args.get("default", default = 0) == "1" or \
            Request.args.get("default", default = 0) == 1 or \
            Request.args.get("Default", default = 0) == "True" or \
            Request.args.get("Default", default = 0) == "true" or \
            Request.args.get("Default", default = 0) == "1" or \
            Request.args.get("Default", default = 0) == 1:
                with open("{}/SSH-Settings-{}".format(Directory, UUID), "a") as File:
                    File.write(DEFAULT)
                    _File = File.name
            else:
                with open("{}/SSH-Settings-{}".format(Directory, UUID), "a") as File:
                    File.write(SSHD)
                    _File = File.name

            return Handler(_File,
                mimetype = "text/plain" if Request.args.get("download", default = 1) == 1 \
                    or Request.args.get("download", default = 1) == "true" \
                        or Request.args.get("download", default = 1) == "True" \
                            or Request.args.get("download", default = 1) == True \
                                else "text/plain",
                attachment_filename = "{}".format(Request.args.get("filename", default = "sshd_config")),
                as_attachment = True if Request.args.get("download", default = 0) == 1 \
                    or Request.args.get("download", default = 0) == "true" \
                        or Request.args.get("download", default = 0) == "True" \
                            or Request.args.get("download", default = 0) == True \
                                else False,
                cache_timeout = 1.0)
