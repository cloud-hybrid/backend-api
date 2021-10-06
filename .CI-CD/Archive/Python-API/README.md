---
Author: Jacob B. Sanders
Description: Axon User Manual, Licensing, Notice(s) & Copyright
Difficulty: Intermediate Understanding of Cloud Technology, Programming, & Core Business Concepts
Type: Technical & Legal Documentation
Updated: 09-14-2020
---

# 20r - _Server & Technology Information_

![Environment-Badge](.../Badges/Environment-POSIX.svg)
![Python-Badge](.../Badges/Language-Python-3.svg)
![Status-Badge](.../Badges/Status-Online.svg)

Cloud-Hybrid Performance Monitoring, Server APIs, & Nexus Connection Driver(s)

> __Proprietary Notice__
>
> The following source file(s) contains confidential, proprietary information. Unauthorized use is strictly prohibited. No portions may be accessed, copied, reproduced, or incorporated outside of this domain without Cloud Hybrid (LLC.)'s written consent.
>
> Special permissions have been givin to Cloud Hybrid LLC.'s established partners and associated namespaces; such permissions are limited to access, usage, and revisioning. Under no circumstances can such namespaces claim ownership or copyright the source code created by Cloud Hybrid LLC., Jacob B. Sanders, or other established entities regardless of closed/open-source contribution(s).
> 
> However, usage and further development of such source code can continue as long as *copyright notices remain* and derived applications are limited to **internal-use only**.
>
> Please contact [jacob.sanders@cloudhybrid.io](jacob.sanders@cloudhybrid.io) for further copyright, contact, and authorization information.

***

![Header-Diagram](.../Documentation/Images/Online-Gaming-Infrastructure.png)

***

## Table of Contents ##

[[_TOC_]]

## Overview ##

**Cloud Hybrid LLC.** is a *Limited Liability Company* owned and founded by Jacob B. Sanders (Null Byte, Segmentational, etc.). Cloud Hybrid provides various cloud-related services, source code, products, development APIs, & other *Technology & Infrastructure* with a number of partners and/or affilates. Consequently, always ensure to include **any and all copyright notices**. Jacob B. Sanders promotes open-source contribution(s) & dedicates **countless hours *almost* everyday to open-source projects, research, and development**.

90% of the time, all that is required is to include *a simple reference to Cloud Hybrid's or Jacob B. Sanders' source code* in a publically accessible, often times online location, and to include any *inline copyright definitions* -- let the following serve as various `source` (*inline*) references:

### Inline Licensing References ###

<details><summary><strong>Bash (POSIX)</code></strong></summary>



```bash
#!/bin/bash --posix

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:   *.*  -*- #

# License - BSD 3-Clause License

# ...
# ... The Idea is Simple [^1]
# ... --------------------------------------------------------------------
# ... Publish & Share Information Online and Make Available Everyone.
# ...    — Dick K.P. Yue, Professor, MIT School of Enineering
# ...

# 
# ========================================================================
# [Executable-Title-Name] | [Synopsis]
# ========================================================================
# - Author:   Jacob B. Sanders
# - Notice:   Copyright 2020
# - License:  BSD 3-Clause License
# 
# [Description ... ]
#
# Reference List & Source(s)
# ------------------------------------------------------------------------
# [1] - [MIT Open Source]: https://ocw.mit.edu/help/get-started-with-ocw/
#

# ------------------------------------------------------------------------
# Global Declarations
# ------------------------------------------------------------------------

CWD="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
SYSTEM="$(uname)"
ARGUMENTS="3"

# ------------------------------------------------------------------------
# Terminal Formatting & Output 
# ------------------------------------------------------------------------

EOM="\33[0m"

BOLD="\33[1m"
ITALIC="\33[3m"
LINK="\33[4m"
BLINK="\33[5m"
UNDERLINE="\033[4m"
SELECTED="\33[7m"
DIM="\33[2m"

R="\33[91m"
G="\33[32m"
B="\33[34m"

Error ()        { printf "${R}%s${EOM}\n" "${@}"; sleep 1.0; }
Auxiliary ()    { printf "${B}%s${EOM}\n" "${@}"; sleep 1.0; }
Success ()      { printf "${G}%s${EOM}\n" "${@}"; sleep 1.0; }

Print ()        { printf "${EOM}%s${EOM}\n" "${@}"; sleep 1.0; }

#
# ------------------------------------------------------------------------
# *.Properties Parsing (OOP Function)
# ------------------------------------------------------------------------
# 
# --- Example-File.Properties ---
# 
# ... #!/bin/bash --posix
# ...
# ... # -*- Coding: UTF-8 -*- #
# ... # -*- System: Linux -*- #
# ... # -*- Usage:   *.*  -*- #
# ... 
# ... # ===================================================================
# ... # Global Environment Properties
# ... # ===================================================================
# ...
# ... Global.Company.Name="Global-Enterprises"
# ...
#
# ($) OOP "Global.Company.Name"
# >>> Global-Enterprises
#

OOP () {
    grep "${1}" ${CWD}/Environment.Properties \
        | cut -d'=' -f2 | \
            sed -e 's/^"//' -e 's/"$//'
}

# ========================================================================
# Primary Entry-Point & Main Function(s)
# ========================================================================

Main () { # --> [Insert-Code-Here] 
    Print "Starting ${CWD}" && \
        Auxiliary "  - Input: ${@}"

    if [[ "${?}" == "0" ]]; then
        Success "${@} - Successful (${?})" \
            && return 0
    elif [[ "${?}" == "130" ]]; then
        Auxiliary "${@} - User Signal EXIT (${?})" \
            && return 0
    else
        local _SIGINT=${?}
        Error "${@} - Non-Zero Response (${_SIGINT})" \
            && return ${_SIGINT}
    fi
}

Main ${@} && Success "${#} exit ${?}
```

</details>

Under the Cloud Hybrid namespace exists various software programs, APIs, and other technology stacks. In addition to these various softwares is ***Server Infrastructure***. Cloud Hybrid is investing such self-owned infrastructure, dynamic-cloud space, and implementing aforementioned technologies for 20r.

Such investments are being made, and at large, in hope 20r can eventually become profitable where staff members are paid for their services and contribututions.

However, given the vast amount of <u>programing & development</u> required -- any programs made under the Cloud Hybrid namespace may or may not be open-source and should be assumed owned by Cloud Hybrid. Such _**does not include the development of the website and gaming servers**_. Development time & server management is simply a good-faith-investment, and consequently the ownership of such is and always will be 20r, but some of the backend services, such as the server dashboard, is ultimately owned by Cloud Hybrid.

Therefore,

> __Proprietary Notice__
>
> The following source file(s) contains confidential, proprietary information. Unauthorized use is strictly prohibited. No portions may be accessed, copied, reproduced, or incorporated outside of this domain without Cloud Hybrid (LLC.)'s written consent.
>
> Special permissions have been givin to Cloud Hybrid LLC.'s established partners and associated namespaces; such permissions are limited to access, usage, and revisioning. Under no circumstances can such namespaces claim ownership or copyright the source code created by Cloud Hybrid LLC. or Jacob B. Sanders. However, usage and further development of such source code can continue as long as copyright notices remain and derived applications are limited to internal-use only.
>
> Please contact [jacob.sanders@cloudhybrid.io](jacob.sanders@cloudhybrid.io) for further copyright, contact, and authorization information.

---

## Task Board ##

- [ ] Make `Constants.py` a Jinja File
  - [ ] Replace Domains/FQDN with Argument *Passable via `Virtualize.Bash`

## Project and Development Management ##

### Styles ###

![Project-Management-Styles-Infographic](.../Documentation/Images/Project-Management-Styles.jpeg)

Development & Project Management styles have taken various forms and consequently attributed various names over the last two-three decades:

1. Water-Fall
2. Agile
3. DevOps

While such information may or may not be prevalent to select *Technology & Infrastructure* users, Cloud Hybrid employs **DevOps Code & Project Management** methodologies. As a much simplified infographic, an organization's targetted DevOps interests should include:

![DevOps-Target-Enterprise-Interests](.../Documentation/Images/DevOps-Target-Interests.png)

## Installation & Usage ##

```bash
echo "Y" | ./Virtualize.Bash
```

## Security and Authentication ##

**Quick References**

- [JWT RFC Development](https://tools.ietf.org/html/rfc7519#section-7.1)
- [JWT RFC Definition](https://tools.ietf.org/html/rfc7519#section-10.1)
- [JWK RFC Overview](https://tools.ietf.org/html/rfc7517)

### JSON Web Tokens ###

[JWT-Article](https://medium.com/swlh/why-do-we-need-the-json-web-token-jwt-in-the-modern-web-8490a7284482)

JSON Web Token (JWT) is an open standard (RFC 7519) that defines a way for transmitting authentication claims & select query information between two parties: an _issuer_ and an _audience_. Communication is safe because each token issued is digitally signed, communicated via HTTPs (encrypted TLS), and programmatically validated.

Each token is **_self-contained_** -- meaning that all the information needed for authentication & endpoint/access validation is cryptographically stored in the seemingly-random, extensive encoded text string. As an example,

- `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJRCI6MSwiSXNzdWVyIjoiU2VnbWVudGF0aW9uYWwiLCJUeXBlIjoiSldUIiwiQWxnb3JpdGhtIjoiSFMyNTYiLCJVc2FnZSI6IldlYi1BcHBsaWNhdGlvbiIsIlRpbWUiOiIyMDIwLTA1LTI2IDExOjIzOjIwLjI3NDkyOSIsIkV4cGlyYXRpb24iOiIyMDIwLTA1LTI2IDExOjM4OjIwLjI3NTMwMSIsIlZhbGlkYXRvciI6IkNsb3VkLUh5YnJpZCIsIkpUSSI6Ik1FRTFRamhHUXpjdE1EUXhRVFJGUkRRdFFqZ3pOemd3UmtZdFJURTFSalE1T1RnPSJ9.DsXu7bnLv-aG3O_FbKLpQgj1lpAJBqRf9MWNULnnCL0`

Upon closer examination, the JWT is seen as a single, larger representation composed of *exactly three smaller strings* seperated via *exactly two periods* (`.`):

1. `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9`
2. `eyJJRCI6MSwiSXNzdWVyIjoiU2VnbWVudGF0aW9uYWwiLCJUeXBlIjoiSldUIiwiQWxnb3JpdGhtIjoiSFMyNTYiLCJVc2FnZSI6IldlYi1BcHBsaWNhdGlvbiIsIlRpbWUiOiIyMDIwLTA1LTI2IDExOjIzOjIwLjI3NDkyOSIsIkV4cGlyYXRpb24iOiIyMDIwLTA1LTI2IDExOjM4OjIwLjI3NTMwMSIsIlZhbGlkYXRvciI6IkNsb3VkLUh5YnJpZCIsIkpUSSI6Ik1FRTFRamhHUXpjdE1EUXhRVFJGUkRRdFFqZ3pOemd3UmtZdFJURTFSalE1T1RnPSJ9`
3. `DsXu7bnLv-aG3O_FbKLpQgj1lpAJBqRf9MWNULnnCL0`

Each segment of the JSON Web Token, in addition to being required, is respectively named:

1. Header
2. Payload
3. Signature

### Global Standardization ###

The internet drafts define the following standard fields ("claims") that can be used inside a JWT claim set:

| **Code** | **Name** | **Description** |
|:--------:|:--------:|:----------------|
| `iss` | Issuer | Identifies principal that issued the JWT. |
| `sub` | Subject | Identifies the subject of the JWT. |
| `aud` | Audience | Identifies the recipients that the JWT is intended for. Each principal intended to process the JWT must identify itself with a value in the audience claim. If the principal processing the claim does not  identify itself with a value in the aud claim when this claim is present, then the JWT must be rejected. |
| `exp` | Expiration Time | Identifies the expiration time on and after which the JWT must not be accepted for processing. The value must be a NumericDate:[9] either an integer or decimal, representing seconds past 1970-01-01 | 00:00:00Z. |
| `nbf` | Not Before | Identifies the time on which the JWT will start to be accepted for processing. The value must be a NumericDate. |
| `iat` | Issued at | Identifies the time at which the JWT was issued. The value must be a NumericDate. |
| `jti` | JWT ID | Case sensitive unique identifier of the token even among different issuers. |

## Resources & Cloud Infrastructure ##

![Server-Example](.../Documentation/Images/Server-Virtual-Machines-Example.png)

The meaning of Server Infrastructure is a general, blanketed term used to reference everything related to servers. Server infrastructure includes the programming, automation, and management of physical or virtual machines, containers, and gaming servers. An important note regarding gaming servers: they're simply a *process* or *service* that *runs on a server* -- game servers are not the actual physical servers or virtual machines, but just an executed program.

### Server Definition(s) ###

The term **server**, while misleadingly often being referenced in complex contexts, simply refers to a **computer program or process**.

Servers are usually provisioned using physical hardware, containerization technologies, a virtualization hypervisor, or any clustered combination. When a server is provisioned using resources other than physical hardware components, the server may in addition be referenced as a **Virtual Private Server** or **Container** where the difference is somewhere in between the specific build processes & the engineer's implementation.

> Please awknowledge the aforementioned definitions are heavily dependent upon *context* -- i.e. if discussion is taking place while managing a fleet of virtual machines or playing a video game.

Diving more into the hardware-side of server terminology, **Processes** -- or perhaps *service(s)* -- are the instances of a computer program that are executed by one or more threads of a processor (CPU). Processes hold the executable code and manage such related *activities* -- which also may or may not be *a server **instance** in select context(s)*. Take the Gaming Industry as an example: what is often coined *Server* is really just a simple executable instruction (process).

Finally, summarizing the terms and definitions:

- **_Server_**: A Physical or Virtual Machine with a subsequent Operating System.
- **_Dedicated Gaming Server_**: Networking process(es) or service(s) that allow server-client interactions.
- **_Process_ (Service)**: Instances of a computer program.

### Management vs Administration ###

**Infrastructure (Cloud Resource) Management** is different and typically much more involved when compared to **server-administration**. Specifically, administration is more about manually adjusting service-level settings such as removing a previous user from a dedicated gaming server, or perhaps defining a small configuration file that adds another *server process* on top of already existing ones. In contrast, management of cloud resources almost always comes down to a lower level where a user may be defining the automation behind powering a server-cluster on or off, adding a new FQDN, or simply removing a hard-drive from a given system. 

But, while such differences exists, such roles should not be treated any differently and **does not mean seperated responsibility**. Two individuals working as either an administrator or as a cloud manager both need to know how to perform one-another's responsibiilites as personal availabilities are always subject to quick, and perhaps inconvenient change.

## Automation and Deployments ##

![CI-CD-Test-Infographic](.../Documentation/Images/AWS-Deployment-Environment.png)

**Continuous Integration** (CI) works to integrate code provided by developers in a shared repository. Developers share the new code in a **Merge** (Pull) **Request**. The request triggers a pipeline to *build*, *test*, and *validate* the new code prior to merging the changes within your repository.

The practice of **Continuous Delivery** (CD) ensures the delivery of CI validated code to an application by means of a structured deployment pipeline.

Together, *CI and CD act to accelerate* how quickly a team can deliver results for customers and stakeholders. CI helps catch and reduce bugs early in the development cycle, and CD moves verified code to the application(s) faster.

CI and CD must work seamlessly together in order for a team to build fast and effectively, as well as being critical to ensuring a fully optimized development practice.

### Continuous Integration ###

**Continuous Integration** is the practice of merging all the code that is being produced by developers. The merging usually takes place several times a day in a shared repository. From within the repository, or production environment, building and automated testing are carried out that ensure no integration issues and the early identification of any problems.

### Continuous Delivery ###

**Continuous Delivery** adds that the software can be released to production at any time, often by automatically pushing changes to a *staging system*.

### Continuous Deployment ###

**Continuous Deployment** goes further and pushes changes to production automatically.

### Automated Architectures ###

Cloud Hybrid uses a specific architecture of automation & code-store called *GitLab* -- https://gitlab.cloudhybrid.io.

CI/CD is a part of GitLab, but GitLab is also a web application with an API that stores its *state* in a database. It manages projects (repositories) and build-pipeleines via commandline and GUI interfaces.

GitLab's web application and APIs can be further built upon by adding additional compute, i.e. servers or infrastructure, to the system:

![Runners](./.Artifacts/Assets/Images/DevOps/Architectures.png)

Such can be seen as an example of *Dynamic Scaling*, also called *Autoscaling*. The idea of dynamically-changing computer systems plays an important part in development, time-management, and the success of an idea, product, or the success of a company. Therefore, computer dynamics is also the driving force behind the management and development of Cloud Hybrid's products & services, and consquently the organization's relationship with affliates and partners.

## Server & Resource Access ##

There are often times many ways to access a server -- remotely, physically, virtually, or otherwise.

### Secure Socket Shell (SSH) ###

> While Cloud Hybrid & perhaps select others may be working on APIs and programs that are *projected* to facilitate and make working with servers & applicable services easier, fulfillment does take considerable development time in addition to successive automation.
> 
> These same programs are generally prioritized by the API's ability to be used accross *as many servers or resources as possible* -- therefore, specific and/or limited "Automation", "Products", "Bots", "APIs", "Projects", etc. may be queued for a while. At the time of writing, Jacob B. Sanders states some development-related requests may not hit the task-board until a projected *eight months from now*. 
> 
> However, priority can always be further discussed with leadership.
> 
> But with additional support and help, as is assumed via reading such documentation, learning how to use **SSH** puts contributors in a position to perform -- at the very least -- almost all server-specific functions & configurations. Please do continue for *SSH* specifics & guided information regarding accessing server resources.

SSH is a cryptographic communications protocol that gives users a secure channel over an otherwise open, unencrypted network -- such does also include the **Internet**. SSH comes installed as default on many different distributions & Operating Systems. 

Windows, for example, usually comes with the *ability* to communicate via SSH; however, most Windows administrators will opt for a Linux device/VM or install a program called [**PuTTY**](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

If a user may be a **beginner** or considered an **entry-level** server administrator, *SSH will be the default server-access method*. Unless a user has a *strong programming background* **and** *a need for automation*, management of server resources in any cloud environment should be done via *SSH* -- perhaps a web-based console if applicable.

### Windows-Server ###

There does exist an exception: **Windows-Server**. 

Specifically, **Windows-Server** is an exception to what may or may not be a user's default server-access method. For informational
purposes, *Windows* server administrators will often use a protocol called **RDP** rather than *SSH* when working
within Microsoft environments or servers.

However, Cloud-Hybrid *does not make use of any Windows-derived distribution(s)* for any *Technology & Infrastructure* resources. 
There is of little reason outside of a user's experience -- to a fault, however, where learning how to use a Terminal (Command Prompt)
needs to be practiced anyways.

Any request for a Windows server will be denied given the associated costs & cloud integration involvements.

## Storage ##

Files and other entities that *may* require storage are stored in cloud resource called an [**S3 Bucket**](https://en.wikipedia.org/wiki/Amazon_S3).


- [Cloud-Hybrid-Storage](http://cloud-hybrid.s3-website.us-east-2.amazonaws.com/)
- [20r-Storage](http://20r.s3-website.us-east-2.amazonaws.com/)
