# [[Template-Name]](https://code.cloud-technology.io/Automata/Template) #

- [ ] @Task - Update `README.md` to Better Reflect [***Discord-Bot-Template***](https://code.cloud-technology.io/Discord/Bot-Template)

> __Proprietary Notice__
>
> The following source file(s) contains confidential, proprietary information. Unauthorized use is strictly prohibited.
> No portions may be accessed, copied, reproduced, or incorporated outside of this domain without Cloud Hybrid (LLC.)'s
> written consent.
>
> Special permissions have been given to Cloud Hybrid LLC.'s established partners and associated namespaces; such 
> permissions are limited to access, usage, and revisioning. Under no circumstances can such namespaces claim ownership
> or copyright the source code created by Cloud Hybrid LLC. or Jacob Sanders. However, usage and further development of
> such source code can continue as long as copyright notices remain and derived applications are limited to internal-use
> only.
>
> Please contact [Jacob B. Sanders](mainto:jacob.sanders@cloudhybrid.io) for further copyright, contact, and
> authorization information.

## Table of Contents ##

[[_TOC_]]

## Overview ##

In order to use *Cloud Technology's* [**Git-Template**](https://code.cloud-technology.io/Automata/Git-Template):

- Use the [**Automated**](#automated-initialization) Bash Script
- Clone & [*Configure*](#manual-usage) the `Git-Template` Repository 

## Automated Initialization ##

1. **Clone**: 
    ```bash
    export URL="https://code.cloud-technology.io/"
    git clone --recurse-submodules "${URL}/Automata/Git-Template.git" \
        && git init . && mv Git-Template .Imports
    ```
1. **Initialize Modular Imports**:
    ```bash
    git submodule add --force ./.Imports \
       && git submodule update --init    \
           --recursive
    ```
1. **Set the *Target* Remote Repository**:
    - *Example:* `https://code.cloud-technology.io/Infrastructure/MacOS-Server.git` <br> <br>
    ```bash
    echo -n "Remote URL (Append '.git' to the URI) [ENTER]: " \
        && read TARGET && export TARGET
    ````
1. **Update `.gitmodules`**:
    ```bash
    cat << 'EOF' > .gitmodules
    #!/usr/bin/env file .

    # -*- Coding: UTF-8 -*-
    # -*- System: Linux -*-
    # -*- Usage:   *.*  -*-
    
    # Owner:    Jacob B. Sanders
    # License:  BSD 3-Clause License
    # Website:  code.cloud-technology.io
    
    #
    # Copyright 2020, Jacob B. Sanders - Cloud Hybrid LLC. & Affiliates
    #
    # Redistribution and use in source and binary forms, with or without modification, are permitted
    # provided that the following conditions are met:
    #
    # 1.  Redistributions of source code must retain the above copyright notice, this list of
    #     conditions and the following disclaimer.
    #
    # 2.   Redistributions in binary form must reproduce the above copyright notice, this list of
    #      conditions and the following disclaimer in the documentation and/or other materials
    #      provided with the distribution.
    #
    # 3.  Neither the name of the copyright holder nor the names of its contributors may be used
    #     to endorse or promote products derived from this software without specific prior written
    #     permission.
    #
    # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
    # OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
    # AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER
    # OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
    # CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    # SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    # THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
    # OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
    # OF SUCH DAMAGE.
    #
    
    #
    # =================================================================================================
    # Git Modules
    # =================================================================================================
    #
    
    [submodule ".Imports"]
        path = .Imports
        url = https://code.cloud-technology.io/Automata/Git-Template.git
        active = true

    EOF
    ```
1. **Git Configuration**:
    ```bash
    git lfs install && git config "lfs.${TARGET}/info/lfs.locksverify" true
    git lfs track "*.psd" \
        && git lfs track "*.zip" \
            && git lfs track "*.rar" \
                && git lfs track "*.app" \
                    && git lfs track "*.iso" \
                        && git lfs track "*.jar" \
                            && git lfs track "*.mp4" 
    
    git add --all && git commit -m "Git Initialization"
   
    git remote add origin "${TARGET}"

    git checkout -B Development
    
    git push --set-upstream "${TARGET}" "Development"
    ```
   
### Usage ###

[Setup](#setup), [System Requirements](#requirements) & [Dependencies](#linux-dependencies)

1. Upgrade Python-PIP:
    `python3 -m pip install pip --upgrade`
    - Windows: `py -m pip install pip --upgrade`
1. Install Virtual Environment Package(s):
    `python3 -m pip install virtualenv`
    - Windows: `py -m pip install --user virtualenv`
1. Setup Virtual Environment:
    `python3 -m virtualenv .venv`
    - Windows: `py -m venv .venv`
1. Activate Virtual Environment:
    `source ./.venv/bin/activate` 
    - Windows: `./.venv/Scripts/activate.bat` 
1. Install Package Dependencies:
    `python -m pip install --requirement Dependencies`

```bash
python3 -m [Example-Python-Executable] --Example-Key "Example-Value"
```
   
### Requirements ###

<u>[**Git-SCM**](https://git-scm.com)</u>

> Git is a *free and open source* **distributed version control system** designed to handle everything 
> from small to very large projects with speed and efficiency.
- [Windows 10](https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/Git-2.28.0-64-bit.exe)
- [MacOS](https://git-scm.com/download/mac) - `xcode-select --install`
- [Alpine](https://git-scm.com/download/linux) - `apk add bash && apk add git`
- [Debian & Ubuntu](https://git-scm.com/download/linux) - `sudo apt-get install git --yes`
- [CentOS (8+) & Fedora](https://git-scm.com/download/linux) - `sudo dnf install -y git`

#### Linux Dependencies ####

- [`libffi`](https://github.com/libffi/libffi)
- [`libnacl`](https://github.com/saltstack/libnacl)
- [`python3-dev`](https://packages.debian.org/python3-dev)

**Debian & Ubuntu**
```bash
sudo apt install libffi-dev libnacl-dev python3-dev --yes
```
 
**Fedora & CentOS**
```bash
sudo dnf install -y libffi-dev libnacl-dev python3-dev
```

## Example `README.md` Sections ##

### Usage ###

[Setup](#setup), [System Requirements](#requirements) & [Dependencies](#linux-dependencies)

1. Upgrade Python-PIP:
    `python3 -m pip install pip --upgrade`
    - Windows: `py -m pip install pip --upgrade`
1. Install Virtual Environment Package(s):
    `python3 -m pip install virtualenv`
    - Windows: `py -m pip install --user virtualenv`
1. Setup Virtual Environment:
    `python3 -m virtualenv .venv`
    - Windows: `py -m venv .venv`
1. Activate Virtual Environment:
    `source ./.venv/bin/activate` 
    - Windows: `./.venv/Scripts/activate.bat` 
1. Install Package Dependencies:
    `python -m pip install --requirement Dependencies`

```bash
python3 -m [Example-Python-Executable] --Example-Key "Example-Value"
```

### Requirements ###

<u>[**Git-SCM**](https://git-scm.com)</u>

> Git is a *free and open source* **distributed version control system** designed to handle everything 
> from small to very large projects with speed and efficiency.
- [Windows 10](https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/Git-2.28.0-64-bit.exe)
- [MacOS](https://git-scm.com/download/mac) - `xcode-select --install`
- [Alpine](https://git-scm.com/download/linux) - `apk add bash && apk add git`
- [Debian & Ubuntu](https://git-scm.com/download/linux) - `sudo apt-get install git --yes`
- [CentOS (8+) & Fedora](https://git-scm.com/download/linux) - `sudo dnf install -y git`

### Dependencies ###

- [`libffi`](https://github.com/libffi/libffi)
- [`libnacl`](https://github.com/saltstack/libnacl)
- [`python3-dev`](https://packages.debian.org/python3-dev)

#### Debian & Ubuntu ####

```bash
sudo apt install libffi-dev libnacl-dev python3-dev --yes
```

#### Fedora & CentOS ####

```bash
sudo dnf install -y libffi-dev libnacl-dev python3-dev
```

---
---
---

## Git Modules ##

***Module(s) Initialization***

```bash
git submodule update --init --force --recursive
```

### [`.IO`](https://code.cloud-technology.io/Automata/.IO) ###

[*Module Description*]

**Initialize `.IO`**

```bash
git submodule add --force https://code.cloud-technology.io/Automata/.IO.git .IO \
    && git submodule update --init --force --recursive .IO
```

***

### [`Git-Ignore`](https://github.com/github/gitignore.git) ###

[*Module Description*]

**Initialize `Git-Ignore`**

```bash
git submodule add --force https://github.com/github/gitignore.git .Git-Ignore \
    && git submodule update --init --force --recursive .Git-Ignore
```

***
w
### [`Badge-Generator`](https://code.cloud-technology.io/Automata/Badge-Generator.git) ###

[*Module Description*]

**Initialize `Badge-Generator`**

```bash
git submodule add --force https://code.cloud-technology.io/Automata/Badge-Generator.git .Badges \
    && git submodule update --init --force --recursive .Badges
```

***


