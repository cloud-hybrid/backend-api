import hashlib

USERNAME = "Segmentational"
EMAIL = "jacob.sanders@cloudhybrid.io"
DISPLAY = "Segmentational"
PASSWORD = hashlib.sha256("{}".format("Kn0wledge!").encode("UTF-8")).hexdigest()
RESET = None

EXECUTION_LITE = """INSERT INTO user VALUES ("{UID}","{USERNAME}","{EMAIL}","{DISPLAY}","{PASSWORD}","{RESET}")""".format(
    UID = 0,
    USERNAME = USERNAME,
    EMAIL = EMAIL,
    DISPLAY = DISPLAY,
    PASSWORD = PASSWORD,
    RESET = RESET
)

EXECUTION_MYSQL = """INSERT INTO user
    (UID, username, email, display, password, reset) VALUES 
    ("{UID}","{USERNAME}","{EMAIL}","{DISPLAY}","{PASSWORD}","{RESET}")""".format(
        UID = 0,
        USERNAME = USERNAME,
        EMAIL = EMAIL,
        DISPLAY = DISPLAY,
        PASSWORD = PASSWORD,
        RESET = RESET)

USERNAME_MYSQL = "root"
PASSWORD_MYSQL = PASSWORD
PASSWORD_MYSQL_ADMIN = "Kn0wledge!"