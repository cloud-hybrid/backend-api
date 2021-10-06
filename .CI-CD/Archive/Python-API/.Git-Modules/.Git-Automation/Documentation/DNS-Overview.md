---
NS Servers
    - `ns-533.awsdns-02.net`
    - `ns-134.awsdns-16.com`
    - `ns-1677.awsdns-17.co.uk`
    - `ns-1057.awsdns-04.org`
Domain Name
    - `20r.gg`
Hosted Zone ID
    - `ZDANI33QUNJTZ`
---

# Domain Name Translation #

DNS is a hierarchical distributed database that stores
IP addresses and translatable data -- allowing the *world
wide web* to look-up organizational resources through a common
and easy to understand domain name.

Various public systems contains such directories of DNS
domain names that translate to numeric IP addresses used
by computers to communicate with each other. For example,
when users type a URL into a browser, DNS converts the URL
into an IP address of a web server associated with that
name. The DNS directories are stored and distributed around
the world on domain name servers that are updated regularly.

The following concepts are useful when working with DNS.

## Table of Contents ##

<!-- [[_TOC_]] -->

- [Domain Name Translation](#domain-name-translation)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Authoritative Servers](#authoritative-servers)
    - [Recursive Resolvers](#recursive-resolvers)
  - [Zones](#zones)
    - [Public Zone](#public-zone)
    - [Private Zone](#private-zone)
    - [Delegated subzone](#delegated-subzone)
    - [Split Horizon Zone](#split-horizon-zone)
  - [DNS Records](#dns-records)
    - [Delegation of Subdomains](#delegation-of-subdomains)
  - [Registrar](#registrar)
  - [DNSSEC](#dnssec)
  - [References and Global Standards](#references-and-global-standards)

<!-- /TOC -->


## Overview ##

A DNS server stores a database of domain names and processes
domain names based on DNS queries that come from a client in
a network.

### Authoritative Servers ###

An authoritative server is a server that holds the DNS name records,
such as A, AAAA, CNAME, etc. A non-authoritative server constructs a
cache file based on previous queries for domains. It does not hold
original name records.

### Recursive Resolvers ###

A recursive resolver is the server that sends a query to the authoritative
or non-authoritative server for resolution. A recursive resolver is so-
called because it performs each query for a given name and returns the final
result. In contrast to an iterative resolver, which only returns a referral
to the next DNS servers that might have the answer.

When resolving the name "google.com.", first the recursive resolver must
determine who is authoritative for "." (the root zone of the DNS). Then it
asks those name servers who is authoritative for ".com." ".gg", etc. Finally,
it asks those name servers who is authoritative for "google.com.", and the
rdata for the A record is returned to the client.

Below is an example of a recursive resolver in action here; running a dig +trace
on google.com, the recursive resolver performs the following action:

```bash
>>> $ dig +trace google.com
; <<>> DiG 9.11.5-P4-5.1-Debian <<>> +trace google.com
;; global options: +cmd
.           168383  IN  NS  a.root-servers.net.
.           168383  IN  NS  b.root-servers.net.
.           168383  IN  NS  c.root-servers.net.
.           168383  IN  NS  d.root-servers.net.
.           168383  IN  NS  e.root-servers.net.
.           168383  IN  NS  f.root-servers.net.
.           168383  IN  NS  g.root-servers.net.
.           168383  IN  NS  h.root-servers.net.
.           168383  IN  NS  i.root-servers.net.
.           168383  IN  NS  j.root-servers.net.
.           168383  IN  NS  k.root-servers.net.
.           168383  IN  NS  l.root-servers.net.
.           168383  IN  NS  m.root-servers.net.
.           168383  IN  RRSIG   NS 8 0 518400 20190810170000 20190728160000 59944 .
ITqCp5bSKwoG1P76GpNfDanh4fXxOtHuld5SJzEm9ez0U/K7kpmBm4TE
cw82zuqtZlqiGOuq+90KHJEhD1fdX3FujgDqe3kaY/41LgFIo76RBeMP
CorYg29lKQOBf7pLPiJWewFmnLsRXsvENzxNXl9mynX80EQSS2YlCWpr
47i2j5SFpGDzmxls7LinB4VvwVLhy0FPwBaVc5NVqQoFS5ZkfKXCUz8x
urExPT2OtPJeDiGzrQGmT6vDbYZtJRWWGK5tPIKZQyF/08YSJlrjebNa
1nKZVN8SsO8s7elz6JGmdoM6D/1ByLNFQmKvU55ikaVSnXylqixLbJQI 7LyQoA==
;; Received 525 bytes from 127.0.0.1#53(127.0.0.1) in 22 ms

com.            172800  IN  NS  a.gtld-servers.net.
com.            172800  IN  NS  b.gtld-servers.net.
com.            172800  IN  NS  c.gtld-servers.net.
com.            172800  IN  NS  d.gtld-servers.net.
com.            172800  IN  NS  e.gtld-servers.net.
com.            172800  IN  NS  f.gtld-servers.net.
com.            172800  IN  NS  g.gtld-servers.net.
com.            172800  IN  NS  h.gtld-servers.net.
com.            172800  IN  NS  i.gtld-servers.net.
com.            172800  IN  NS  j.gtld-servers.net.
com.            172800  IN  NS  k.gtld-servers.net.
com.            172800  IN  NS  l.gtld-servers.net.
com.            172800  IN  NS  m.gtld-servers.net.
com.            86400   IN  DS  30909 8 2
E2D3C916F6DEEAC73294E8268FB5885044A833FC5459588F4A9184CF C41A5766
com.            86400   IN  RRSIG   DS 8 1 86400 20190811170000 20190729160000 59944 .
KXPRdZspxd6hZYRFx3cj7Yp3d6HDzOG5CmoK46ZrrlKnZkCYMPKzyFQ2
15pA+jZ37MbQbhe6+S+C4AHWqv95DDsue85ha3ZmWGhnJxcLnDaL5Twp
Z/W/a+1cTHhhbMZua1riw74mqvzRAF1kVerj7jrvWnOAOZCh69Dr4AFJ
gRN4MAn+wCZDmPQCtkcGVJ9vyNV7Xra45B4ISqEo0xi8CXewp9cc+aW5
TSjFRhj1RM9d3k+3Mrq6AAV8dVgWofYTg6Ihph/SfoIx4TrTrEbgfdsv
MvuLPXvK6Y7oSh5WknbFduw7HQdo1jH3/QR54FORswBJT8VmYD7Zii88 tAjbRQ==
;; Received 1170 bytes from 192.58.128.30#53(j.root-servers.net) in 2 ms

google.com.     172800  IN  NS  ns2.google.com.
google.com.     172800  IN  NS  ns1.google.com.
google.com.     172800  IN  NS  ns3.google.com.
google.com.     172800  IN  NS  ns4.google.com.
CK0POJMG874LJREF7EFN8430QVIT8BSM.com. 86400 IN NSEC3 1 1 0 -
CK0Q1GIN43N1ARRC9OSM6QPQR81H5M9A NS SOA RRSIG DNSKEY NSEC3PARAM
CK0POJMG874LJREF7EFN8430QVIT8BSM.com. 86400 IN RRSIG NSEC3 8 2
86400 20190803044434 20190727033434 17708 com.
rMmiNL7bYvJpB3Bc+WnqS2iiczm2PwxBvJcl7SL/vcTj88GsxM1ycTSV
PsHZHxfrv1dv2C5BCSZ+mzeVBu8upLoeraQy+UVf3VXyt3i3rNGzcXYV
8HSrHcXrRoAJopFim3Ge1xdZ+uERg3cTIcN2tJxxkCeqt/EcUTqtQl8t EAc=
S84BDVKNH5AGDSI7F5J0O3NPRHU0G7JQ.com. 86400 IN NSEC3 1 1 0 -
S84CFH3A62N0FJPC5D9IJ2VJR71OGLV5 NS DS RRSIG
S84BDVKNH5AGDSI7F5J0O3NPRHU0G7JQ.com. 86400 IN RRSIG NSEC3
8 2 86400 20190804045723 20190728034723 17708 com.
jypPsaWVop9rzuf70CFYyiK0hliiJ+YYtkjgb3HVj9ICc57kLmv9DkvG
DddF5GBQpqNEakzyJtya179MAdDT7RhJB4XfmY6fu5I5QTeIjchfP5wt
7gU1AL7cqTmBAo2RWu62vtUytV09+O3KGFq5O+Cwr11dSTfq1yYyw6YW cMI=
;; Received 772 bytes from 192.41.162.30#53(l.gtld-servers.net) in 2 ms

google.com.     300 IN  A   172.217.7.14

```

Each DNS client queries a name server. A recursive resolver queries
other name servers, all the way up to a top level name server, if necessary.
The NS record for a zone on an upper-level name server directs the resolver
"down" to another name server, eventually reaching either a name server that
cached the zone or the authoritative server for the zone.

## Zones ##

### Public Zone ###

A public zone is visible to the internet. End-users can create DNS records in a
public zone to publish any number of service(s) on the internet. Users may create an A
record in a public zone called `example.com`.

### Private Zone ###

A private zone is any zone that cannot be queried over the public internet.

### Delegated subzone ###

DNS allows the owner of a zone to delegate a subdomain to a different name
server using NS records. Resolvers follow these records and send queries
for the subdomain to the target name server specified in the delegation.

### Split Horizon Zone ###

Split Horizon is a term to describe an instance when two zones, one to be
used by the internal network, the other used by the external network
(usually the internet), for the same domain are created. Split-horizon DNS
lets you serve different answers (different resource record sets) for the
same name depending on who is asking.

Example) A software engineer provides the development/staging version of an
application; split horizon occurs if the query comes from the development
network, and the production version of the application comes from the public
internet.

## DNS Records ##

|   Type    |                                  Description                                   |           Example           |
| :-------: | :----------------------------------------------------------------------------: | :-------------------------: |
|   **A**   |         *Address record, which maps host names to their IPv4 address.*         |        `3.168.18.5`         |
| **AAAA**  |      *IPv6 Address record, which maps host names to their IPv6 address.*       | `0:0:0:0:0:ffff:aca8:1001`  |
| **CNAME** |             *Canonical name record, which specifies alias names.*              |      `www.example.com`      |
|  **NS**   |  *Name server record, which delegates a DNS zone to an authoritative server.*  |     `ns-server-1.ex.io`     |
|           |                                                                                |     `ns-server-2.ex.io`     |
|           |                                                                                |     `ns-server-3.ex.io`     |
|           |                                                                                |     `ns-server-4.ex.io`     |
|           |                                                                                |     `ns-server-5.ex.io`     |
|  **PTR**  | *Pointer record, which defines a name associated with an IP address.*    <br>  | `1, website.gg, 3.168.18.5` |
|           |  *Start of authority, used to designate the primary name server and*     <br>  |                             |
|           |  *administrator responsible for a zone. Each zone hosted on a DNS*       <br>  |                             |
|           | *server must have an SOA (start of authority) record. You can modify*    <br>  |                             |
|           |  *the record as needed (for example, you can change the serial number*   <br>  |                             |
|           |          *to an arbitrary number to support date-based versioning).*           |                             |

### Delegation of Subdomains ###

When creating records, make sure that the NS and SOA records match each other.
Conflicting NS and SOA records can cause some resolvers to reject the delegation
as invalid and refuse to cache "NO DATA" responses to queries. This can result in
a large unexpected number of queries against your public managed zones by third-party
recursive resolvers when resolvers query your public managed zones for records that
do not exist.

Example: Suppose that there are two subdomains, example.com and subdomain.example.com.
The NS and SOA records for subdomain.example.com do not match. Neither of the zones contains
any AAAA records. When some third-party recursive resolvers query subdomain.example.com for an
AAAA record and receive a "NO DATA" response, if the resolvers detect the invalid delegation
of subdomain.example.com, they refuse to cache the non-existence of AAAA records in that zone.
The result is that they retry the queries. They query all the Cloud Console name servers, in
turn, for this information.

## Registrar ##

A domain name registrar is an organization that manages the reservation of internet
domain names for public zones. A registrar must be accredited by a generic top-level
domain (TLD) registry or a country code top-level domain (ccTLD) registry. This is how
"upper"-level name servers agree on SOA and update NS records for the zone to direct
requests to caching or authoritative name servers.

## DNSSEC ##

The Domain Name System Security Extension (DNSSEC) addresses vulnerabilities to DNS data.
It is a suite of IETF specifications to provide authentication of DNS data, authenticated
denial of existence, and data integrity to DNS clients (resolvers). In short, DNSSEC
provides a way for software to verify the origin of DNS data and validate that it has not
been modified in transit.

## References and Global Standards ##

- [Global DNS Standards](https://tools.ietf.org/html/rfc7719)
- [DNSSec Technical Documentation](https://tools.ietf.org/html/rfc4033)
