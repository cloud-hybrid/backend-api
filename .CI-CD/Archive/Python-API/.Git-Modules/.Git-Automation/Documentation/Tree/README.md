---
Author: Jacob B. Sanders
Description: What to include in GitLab documentation pages.
Updated: 04-25-2020
---

# Title #

![Environment-Badge](../../Badges/Environment-POSIX.svg)
![Release-Badge](../../Badges/Release-Alpha.svg)
![Status-Badge](../../Badges/Status-Online.svg)

An introduction -- without any additional header -- goes here.

## Overview ##

Overview:

- Feature or Use Case
- Intended Audience
- Context and Potential Prerequisites or Requirements
- Benefits vs. Alternatives

## Usage ##

Describe use cases and provide examples.

Also include `Help Output`

## Requirements ##

State any requirements for using the feature and/or following along with the instructions.

- A ...
- B ...
- C ... 

## Installation ##

Short excerpt.

- Step-By-Step Guide & Relevant Information

## API Topic ##

One-two sentence summary of endpoint.

### cURL Commands ###

- Use `https://gitlab.example.com/api/v4/` as an endpoint.
- Wherever needed use this personal access token: `<your_access_token>`.
- Always put the request first. `GET` is the default so you don't have to
  include it.
- Use double quotes to the URL when it includes additional parameters.
- Prefer to use examples using the personal access token and don't pass data of
  username and password.

| Methods                                         | Description                                           |
|:-------------------------------------------     |:------------------------------------------------------|
| `--header "PRIVATE-TOKEN: <your_access_token>"` | Use this method as is, whenever authentication needed |
| `--request POST`                                | Use this method when creating new objects             |
| `--request PUT`                                 | Use this method when updating existing objects        |
| `--request DELETE`                              | Use this method when removing existing objects        |

---
