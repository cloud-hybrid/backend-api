#!/usr/bin/env python3

# -*- Coding: UTF-8 -*-
# -*- System: Linux -*-
# -*- Usage:   *.*  -*-

# Copyright:    Public Domain
# License:      BSD 3-Clause License
# Creator:      Jacob B. Sanders

gitlab.development.cloud-technology.io

ssh-keygen -b 521 -t ECDSA -f "${1}" -C "${SIGNATURE}" -N ""

aws ssm put-parameter --name "Nexus-UI-Target-VPC" \
    --description "Environment VPC-ID" \
    --value "vpc-a2fe3dc9" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "Nexus-UI-Subnets" \
    --description "VPC Dependent Subnet(s)" \
    --value "subnet-35fe7679, subnet-61ba9b1b, subnet-4216fd29" \
        --type "StringList" \
            --overwrite

aws ssm put-parameter --name "Nexus-UI-Target-Subnet-Singleton" \
    --description "VPC Default, Singleton Subnet" \
    --value "subnet-35fe7679" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "Nexus-UI-Subnet-A" \
    --description "VPC Dependent Subnet(s) [A]" \
    --value "subnet-35fe7679" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "Nexus-UI-Subnet-B" \
    --description "VPC Dependent Subnet(s) [B]" \
    --value "subnet-61ba9b1b" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "Nexus-UI-Subnet-C" \
    --description "VPC Dependent Subnet(s) [C]" \
    --value "subnet-4216fd29" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "Nexus-UI-AWS-Account-ID" \
    --description "Nexus-UI Environment Account-ID" \
    --value "983281742669" \
        --type "String" \
            --overwrite
