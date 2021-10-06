---
Author: Jacob B. Sanders
Description: What to include in GitLab documentation pages.
Updated: 04-25-2020
---

# Git Hooks #

![Environment-Badge](../../Badges/Environment-POSIX.svg)
![Release-Badge](../../Badges/Release-1.0.0.svg)
![Python-Badge](../../Badges/Language-Python-3.svg)
![Status-Badge](../../Badges/Status-Online.svg)

General GitLab documents, templates, automation packages, and overall programatic system entities.

> __Proprietary Notice__
>
> The following source file(s) contains confidential, proprietary information. Unauthorized use is strictly prohibited. No portions may be accessed, copied, reproduced, or incorporated outside of this domain without Cloud Hybrid (LLC.)'s written consent.
>
> Special permissions have been givin to Cloud Hybrid LLC.'s established partners and associated namespaces; such permissions are limited to access, usage, and revisioning. Under no circumstances can such namespaces claim ownership or copyright the source code created by Cloud Hybrid LLC. or Jacob Sanders. However, usage and further development of such source code can continue as long as copyright notices remain and derived applications are limited to internal-use only.
>
> Please contact [jacob.sanders@cloudhybrid.io](jacob.sanders@cloudhybrid.io) for further copyright, contact, and authorization information.

***

![Header-Diagram](./.Artifacts/Assets/Images/Online-Gaming-Infrastructure.png)

***

## Table of Contents ##

[[_TOC_]]

## Overview ##

**Cloud Hybrid LLC.** is a *Limited Liability Company* owned and founded by Jacob B. Sanders (Null Byte, Segmentational, etc.). Cloud Hybrid provides various cloud-related services and development with a number of partners and/or affilates -- one of which includes *20th Regiment of Foot*, or **20r**.

Under the Cloud Hybrid namespace exists various software programs, APIs, and other technology stacks. In addition to these various softwares is ***Server Infrastructure***. Cloud Hybrid is investing such self-owned infrastructure, dynamic-cloud space, and implementing aforementioned technologies for 20r.

Such investments are being made, and at large, in hope 20r can eventually become profitable where staff members are paid for their services and contribututions.

However, given the vast amount of <u>programing & development</u> required -- any programs made under the Cloud Hybrid namespace may or may not be open-source and should be assumed owned by Cloud Hybrid. Such services _**do not include the development of the website and gaming servers**_. Development time & server management is simply a good-faith-investment, and consequently the ownership of such is and always will be 20r, but some of the backend services, such as the server dashboard, is ultimately owned by Cloud Hybrid.

Therefore,

> __Proprietary Notice__
>
> The following source file(s) contains confidential, proprietary information. Unauthorized use is strictly prohibited. No portions may be accessed, copied, reproduced, or incorporated outside of this domain without Cloud Hybrid (LLC.)'s written consent.
>
> Special permissions have been givin to Cloud Hybrid LLC.'s established partners and associated namespaces; such permissions are limited to access, usage, and revisioning. Under no circumstances can such namespaces claim ownership or copyright the source code created by Cloud Hybrid LLC. or Jacob B. Sanders. However, usage and further development of such source code can continue as long as copyright notices remain and derived applications are limited to internal-use only.
>
> Please contact [jacob.sanders@cloudhybrid.io](jacob.sanders@cloudhybrid.io) for further copyright, contact, and authorization information.

### Modules ###

#### Add ####

```bash
git submodule add --force https://code.cloud-technology.io/CICD/Commit-Regular-Expressions.git \
    Regular-Expressions/Commit-Regular-Expressions

git submodule add --force https://github.com/google/re2.git \
    Regular-Expressions/re2
```

#### Remove ####

```bash
git submodule deinit --force --all
```

#### Update ####

```bash
REMOTE="https://code.cloud-technology.io/Automata/.IO"

git submodule update --force .IO        \
    && cd .IO && git pull "${REMOTE}"   \
    && cd ..
```
---

## Start-to-Finish ##

1. `python3 venv .venv`
1. `source .venv/bin/activate`
1. `python -m pip install --requirement Dependencies`
1. `python setup.py build 0 7 535 2450`
1. `python setup.py bdist_wheel`
1. `python -m pip wheel .IO/Distribution/Cloud-0.7.535-2450-py3-none-any.whl --wheel-dir .IO/Distribution/Wheel`
1. `python -m pip install .IO/Distribution/Cloud-0.7.535-2450-py3-none-any.whl`

## Programming Paradigms ##

OOP introduces two fundamental types of inheritance: implementation (class) inheritance and interface inheritance.7 Implementation inheritance defines an object's implementation in terms of another object's implementation. In contrast, interface inheritance enforces only object interface compatibility regardless, of implementation.

Hierarchical state machines introduce a third type of inheritance that is equally fundamental. We call this behavioral inheritance . To understand why hierarchy introduces inheritance and how it works, consider an empty (or transparent) substate nested within an arbitrary superstate. If such a substate becomes active it behaves in exactly the same way as its superstate, that is, it inherits the superstate's entire behavior. This is analogous to a subclass which does not introduce any new attributes or methods. An instance of such a subclass is indistinguishable from its superclass because, again, everything is inherited exactly.

This property of HSMs is fundamental because it requires only the differences from the superstate's behavior to be defined. One observes that all OO design principles (for example, the Liskov Substitution Principle) hold in HSM designs because one deals with inheritance in yet another form. The concept of behavioral inheritance describes the “is-a” (“is-in”) relationship between substates and superstates and should not be confused with inheritance of entire state models.3

The analogy between SOP and OOP goes further. Class instantiation and finalization is similar to entering and exiting a state. In both cases special methods are invoked: constructors and destructors for objects, entry and exit actions for states. Even the order of invocation of these methods is the same: constructors are invoked starting from most remote ancestor classes (destructors are invoked in reverse order), and entry actions are invoked starting from the topmost superstate (exit actions are invoked in reverse order).

A final similarity between OOP and SOP lies in the way they are most efficiently implemented. Although polymorphism can be implemented in many ways, virtually all C++ compilers implement it in the same way: by using function pointers grouped into virtual tables. In view of the deep analogy between SOP and OOP, it is therefore not surprising that arguably the most efficient implementation of HSMs is also based on function pointers grouped into states. These simple state objects define both behavior and hierarchy but are not specific to any particular instance of a state machine. The same holds for virtual functions, which are characteristics of the whole class rather than specific to any particular object instance. For this reason we observe that state objects could (and probably should) be placed in v-tables and be supported as a native language feature.

---

## Creating and Using SSH Keys ##

1. Navigate to https://cloudhybrid.io/API/Security/RSA to download new RSA key.
2. Copy the new SSH key to a known, private location.
3. Rename the key to a more fitting name.
4. Navigate into the directory where the SSH key is now stored.
5. Change the permissions: `chmod 400 RSA-Key`.
6. Create a public key: `ssh-keygen -y -f RSA-key > ./RSA-key.pub`.
7. Copy the public key into the target server: `ssh-copy-id -i RSA-Key username@169.0.0.1`.
8. Enter the server's password when prompted.
9. Attempt password-less login: `ssh -i RSA-key username@169.0.0.1`.

***

## JWT Authentication Tokens ##

[JWT-Article](https://medium.com/swlh/why-do-we-need-the-json-web-token-jwt-in-the-modern-web-8490a7284482)

JSON Web Token (JWT) is an open standard (RFC 7519) that defines a way for transmitting authentication claims & select query information between two parties: an _issuer_ and an _audience_. Communication is safe because each token issued is digitally signed, so the consumer can verify if the token is authentic or has been forged.

Each token is self-contained, this means it contains all information needed to allow or deny any given requests to an API.

A JSON Web Token is essentially a long encoded text string. This string is composed of three smaller parts, separated by a dot sign. Such parts are defined:

- Header
- Payload
- Signature

![JWT-Stateless-HTTP-Example](./.Artifacts/Assets/Images/HTTP-API-Stateless-Example-1.png)

Therefore, the format becomes:

- `[H]eader.[P]ayload.[S]ignature`


### Standardization ###

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

This section registers the "application/jwt" media type [RFC2046] in
   the "Media Types" registry [IANA.MediaTypes] in the manner described
   in RFC 6838 [RFC6838], which can be used to indicate that the content
   is a JWT.

   o  Type name: application
   o  Subtype name: jwt
   o  Required parameters: n/a
   o  Optional parameters: n/a
   o  Encoding considerations: 8bit; JWT values are encoded as a series
      of base64url-encoded values (some of which may be the empty
      string) separated by period ('.') characters.
   o  Security considerations: See the Security Considerations section
      of RFC 7519
   o  Interoperability considerations: n/a
   o  Published specification: RFC 7519
   o  Applications that use this media type: OpenID Connect, Mozilla
      Persona, Salesforce, Google, Android, Windows Azure, Amazon Web
      Services, and numerous others
   o  Fragment identifier considerations: n/a
   o  Additional information:

         Magic number(s): n/a
         File extension(s): n/a
         Macintosh file type code(s): n/a

   o  Person & email address to contact for further information:
      Michael B. Jones, mbj@microsoft.com
   o  Intended usage: COMMON
   o  Restrictions on usage: none
   o  Author: Michael B. Jones, mbj@microsoft.com
   o  Change controller: IESG
   o  Provisional registration?  No

### References ###
- [JWT RFC](https://tools.ietf.org/html/rfc7519#section-10.1)
- [JWK RFC](https://tools.ietf.org/html/rfc7517)
- [Creating JWTs](https://tools.ietf.org/html/rfc7519#section-7.1)

### Server & Gaming Infrastructure ###

![Server-Example](./.Artifacts/Assets/Images/Server-Virtual-Machines-Example.png)

The meaning of Server Infrastructure is a general, blanketed term used to reference everything related to servers. Server infrastructure includes the programming, automation, and management of physical or virtual machines, containers, and gaming servers. An important note regarding gaming servers: they're simply a *process* or *service* that *runs on a server* -- game servers are not the actual physical servers or virtual machines, but just an executed program.

### Server Definition(s) ###

The term server refers to a computer program or process, however, the term server can take on different definitions depending on a given context. At a high-level, a server is a virtual machine; virtual machines are encapsulated kernels (Operating Systems) that reside on a physical computer. Processes, also referenced as service(s), are the instances of a computer program that are executed by one or more threads of a processor (CPU). Processes contains the program code and its activity. Depending on the operating system, a process may be made up of multiple threads of execution that execute instructions concurrently.

In a separate context, as with the gaming industry, a server is -- fundamentally -- a multi-user networking connection that allows users to interact in real-time.

**Summarizing**:

<u>Server</u>: A Physical or Virtual Machine with a subsequent Operating System.

<u>Gaming Server</u>: Process(es) or service(s) that allow client-server-client interactions.

<u>Process</u> (*Service*): Instances of a computer program.

### Management vs Administration ###

Infrastructure management is different than that of administration. Specifically, administration is about defining and adjusting service-level settings such as adding an administrator to a dedicated gaming server. Management almost always comes down to a lower level where a user may be turning the actual server on or off, or spinning up a new dedicated gaming server on a VPS. Accessing server infrastructure is also a part of management where users need either RDP, SSH, or physical access to the machine in order to modify settings. Administration can usually be done while in game, but most administrative actions are also available via SSH or a similar connection(s).

Because Cloud Hybrid primarily uses Linux-based server infrastructure, management is done via SSH. Please visit the SSH section for further details.

***

## Automation and Deployments ##

![CI-CD-Test-Infographic](./.Artifacts/Assets/Images/DevOps/CI-CD-Test-Infographic.png)

**Continuous Integration** (CI) works to integrate code provided by developers in a shared repository. Developers share the new code in a **Merge** (Pull) **Request**. The request triggers a pipeline to *build*, *test*, and *validate* the new code prior to merging the changes within your repository.

The practice of **Continuous Delivery** (CD) ensures the delivery of CI validated code to an application by means of a structured deployment pipeline.

Together, *CI and CD act to accelerate* how quickly a team can deliver results for customers and stakeholders. CI helps catch and reduce bugs early in the development cycle, and CD moves verified code to the application(s) faster.

CI and CD must work seamlessly together in order for a team to build fast and effectively, as well as being critical to ensuring a fully optimized development practice.

### Continuous Integration ###

**Continuous Integration** is the practice of merging all the code that is being produced by developers. The merging usually takes place several times a day in a shared repository. From within the repository, or production environment, building and automated testing are carried out that ensure no integration issues and the early identification of any problems.

### Continuous Delivery ###

**Continuous Delivery** adds that the software can be released to production at any time, often by automatically pushing changes to a *staging system*.

### _Continuous Deployment_ ###

**Continuous Deployment** goes further and pushes changes to production automatically.

### Automated Architectures ###

Cloud Hybrid uses a specific architecture of automation & code-store called *GitLab* -- https://gitlab.cloudhybrid.io.

CI/CD is a part of GitLab, but GitLab is also a web application with an API that stores its *state* in a database. It manages projects (repositories) and build-pipeleines via commandline and GUI interfaces.

GitLab's web application and APIs can be further built upon by adding additional compute, i.e. servers or infrastructure, to the system:

![Runners](./.Artifacts/Assets/Images/DevOps/Architectures.png)

Such can be seen as an example of *Dynamic Scaling*, also called *Autoscaling*. The idea of dynamically-changing computer systems plays an important part in development, time-management, and the success of an idea, product, or the success of a company. Therefore, computer dynamics is also the driving force behind the management and development of Cloud Hybrid's products & services, and consquently the organization's relationship with affliates and partners.

***

## Accessing Server Infrastructure via SSH ##

### Overview ###

SSH is a cryptographic network protocol that gives users, particularly system administrators, a secure way to access a computer or server over an unsecured network (Internet). SSH provides strong authentication and encrypted data communications between two computers connecting over an open network. It is a secure alternative to the non-protected login protocols (such as telnet, rlogin) and insecure file transfer methods (such as FTP). SSH refers both to the cryptographic network protocol and to the suite of utilities that implement that protocol. An SSH server, by default, listens on the standard Transmission Control Protocol (TCP) port 22. In the context of the Development-Operations Manual, all servers (gaming and otherwise) are always SSH capable.

While Cloud Hybrid may be working on APIs and certain programs that ease server management, such automata can manually be accomplished via SSH. Unfortunately, working within SSH requires knowledge of shell-related technologies and a small amount programming syntax.

Therefore, the remainder of the *Accessing Server Infrastructure via SSH* section will demonstrate such SSH-related commands required for basic management of server infrastructure.

### Server Power Management ###

Restarting a server usually fixes most issues related to a failed service. For example, a game server such as Mordhau may begin to fail after being online for a few weeks or months -- resulting in multiple users being unable to join a game.

Restarting the server will often reinitialize the failed service and consequently correct itself upon reboot. In order to restart a Mordhau-Server,

...

...

...
