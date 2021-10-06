#!/usr/bin/env bash --posix

declare PRE="Nexus-API"

aws ssm put-parameter --name "${PRE}-Target-VPC" \
    --description "Environment VPC-ID" \
    --value "vpc-a2fe3dc9" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "${PRE}-Subnets" \
    --description "VPC Dependent Subnet(s)" \
    --value "subnet-35fe7679, subnet-61ba9b1b, subnet-4216fd29" \
        --type "StringList" \
            --overwrite

aws ssm put-parameter --name "${PRE}-Target-Subnet-Singleton" \
    --description "VPC Default, Singleton Subnet" \
    --value "subnet-35fe7679" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "${PRE}-Subnet-A" \
    --description "VPC Dependent Subnet(s) [A]" \
    --value "subnet-35fe7679" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "${PRE}-Subnet-B" \
    --description "VPC Dependent Subnet(s) [B]" \
    --value "subnet-61ba9b1b" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "${PRE}-Subnet-C" \
    --description "VPC Dependent Subnet(s) [C]" \
    --value "subnet-4216fd29" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "${PRE}-AWS-Account-ID" \
    --description "${PRE} Environment Account-ID" \
    --value "983281742669" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "${PRE}-Container-Image-ID" \
    --description "${PRE} CI-Deployable" \
    --value "983281742669.dkr.ecr.us-east-2.amazonaws.com/nexus-api:latest" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "${PRE}-Service-Name" \
    --description "${PRE} Functional Service Port" \
    --value "Nexus-API-Service" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "${PRE}-Container-Port" \
    --description "${PRE} Functional Service Port" \
    --value "3000" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "${PRE}-ALB-Port" \
    --description "${PRE} Load-Balancer Connection Port" \
    --value "3000" \
        --type "String" \
            --overwrite

aws ssm put-parameter --name "${PRE}-SSL-Certificate" \
    --description "${PRE} TLS + SSL Certificate Resource ARN" \
    --value "arn:aws:acm:us-east-2:983281742669:certificate/6b219c7f-2741-4757-8126-3babca2ae759" \
        --type "String" \
            --overwrite
