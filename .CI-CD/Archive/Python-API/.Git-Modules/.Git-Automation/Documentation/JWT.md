# JWT Authentication Tokens #

## Table of Contents ##

[[_TOC_]]

## Overview ##

[JWT-Article](https://medium.com/swlh/why-do-we-need-the-json-web-token-jwt-in-the-modern-web-8490a7284482)

JSON Web Token (JWT) is an open standard (RFC 7519) that defines a way for transmitting 
authentication claims & select query information between two parties: an _issuer_ and an _audience_.
Communication is safe because each token issued is digitally signed, so the consumer can verify if 
the token is authentic or has been forged.

Each token is self-contained, this means it contains all information needed to allow or deny any 
given requests to an API.

A JSON Web Token is essentially a long encoded text string. This string is composed of three smaller 
parts, separated by a dot sign. Such parts are defined:

- Header
- Payload
- Signature

![JWT-Stateless-HTTP-Example](./.Artifacts/Assets/Images/HTTP-API-Stateless-Example-1.png)

Therefore, the format becomes:

- `[H]eader.[P]ayload.[S]ignature`

## Standardization ##

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

## References ##
- [JWT RFC](https://tools.ietf.org/html/rfc7519#section-10.1)
- [JWK RFC](https://tools.ietf.org/html/rfc7517)
- [Creating JWTs](https://tools.ietf.org/html/rfc7519#section-7.1)