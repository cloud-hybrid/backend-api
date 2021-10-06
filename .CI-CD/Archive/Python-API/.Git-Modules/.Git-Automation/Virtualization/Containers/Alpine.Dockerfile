FROM alpine:latest

MAINTAINER Jacob B. Sanders <jacob.sanders@cloudhybrid.io>

ENV Y="\\n\\33[33m"
ENV X="\\33[0m\\n"

ENV LANG C.UTF-8
ENV SIGNATURE "Alpine-Auto-Generated-SSH-Signature"
ENV PYTHON_VERSION 3.8.5

EXPOSE 22

RUN echo -e "${Y} - Updating ${X}" \
    && apk update --verbose

RUN echo -e "${Y} - Installing Packages ${X}" \
    && apk add --no-cache       \
        build-base              \
            ca-certificates     \
            openssh             \
            libxml2             \
            docker              \
            openrc              \
            gnupg               \
            bash                \
            curl                \
            wget                \
            tree                \
            git                 \
            zip                 \
            jq

RUN echo -e "${Y} - Installing DOFD ${X}"   \
    && apk add --no-cache docker-cli        \
        && rc-update add docker boot

RUN echo -e "${Y} - Configuring SSH ${X}" \
    && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config                                                \
    && echo 'root:$1$FphroyUU$HCQN5Vmi9Ew7EdKNqPsSt/' | chpasswd -e                                                          \
    && sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config                                                                   \
    && sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_key/HostKey \/etc\/ssh\/ssh_host_key/g'                 /etc/ssh/sshd_config \
    && sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_rsa_key/HostKey \/etc\/ssh\/ssh_host_rsa_key/g'         /etc/ssh/sshd_config \
    && sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_dsa_key/HostKey \/etc\/ssh\/ssh_host_dsa_key/g'         /etc/ssh/sshd_config \
    && sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ecdsa_key/HostKey \/etc\/ssh\/ssh_host_ecdsa_key/g'     /etc/ssh/sshd_config \
    && sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ed25519_key/HostKey \/etc\/ssh\/ssh_host_ed25519_key/g' /etc/ssh/sshd_config \
    && /usr/bin/ssh-keygen -A \
        && ssh-keygen -b 521 -t ECDSA -f /etc/ssh/ssh_host_key -C "${SIGNATURE}" -N ""

RUN echo -e "${Y} - Adding Python-3 ${X}" \
    && apk add python3 \
        py3-pip --verbose

RUN echo -e "${Y} - Upgrading Python-3 Package Manager ${X}" \
    && python3 -m pip install pip \
        --upgrade

RUN echo -e "${Y} - Installing PIP Modules ${X}"    \
    && python3 -m pip install --ignore-installed    \
        wheel                                       \
        PyYaml                                      \
        docker-py                                   \
           virtualenv

# # =====================================================================================
# # Initialization
# # =====================================================================================

RUN mkdir -p /Cloud

COPY Public-Key /Cloud/Public-Key
COPY Docker.Properties /Cloud/Docker.Properties
COPY Entry-Point.Bash /Cloud/Entry-Point.Bash

RUN chmod a+x /Cloud/Docker.Properties && \
    chmod a+x /Cloud/Entry-Point.Bash

RUN echo -e "${Y} - Removing Cache ${X}" \
    && rm -rf /var/cache/apk/*

CMD ["/usr/sbin/sshd", "-D"]
