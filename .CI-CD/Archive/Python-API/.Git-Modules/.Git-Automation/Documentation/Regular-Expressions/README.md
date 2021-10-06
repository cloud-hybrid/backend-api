---
Author: Jacob B. Sanders
Description: [...]
Difficulty: Intermediate
Type: Technical Documentation
Updated: [...]
License: BSD 3-Clause License
Copyright: 2020, Cloud-Hybrid & Affiliates
---

# Git-Commit Regular Expressions #

[**GitLab**](https://docs.gitlab.com/ee/push_rules/push_rules.html) has the ability to prevent commits
that fail to follow administrator-defined [*Push Rules*](
https://docs.gitlab.com/ee/push_rules/push_rules.html
). 

## Table of Contents ##

[[_TOC_]]

## Overview ##

Push rules provide git administrators additional control over repository updates through the use
of [*Regular Expressions*](https://www.regular-expressions.info). In short, A regular expression
-- or "*regex*", is a special text string for describing a search pattern.

For reference, push rules are *allowed* or *prevented* during the **commit hook**; a commit hook
consists of the following procedure:

`pre-commit → prepare-commit-msg → commit-msg → post-commit`

## Usage ##

For example, if an administrator wanted a automated way to track *Jira* stories via commit messages,
a regular expression defined as `JIRA\-\d+` would have the following effect:

```
# --> Commit Failure Example

git add . && git add *
git commit --message \
    "Bug-Fix: Corrected API Endpoint"
git push
...  ! [rejected] error: failed to push some refs to 
https://code.cloud-technology.io/CICD/Commit-Regular-Expressions.git
```

However, a successful commit message:

```
# --> Successful Commit Example

git add . && git add *
git commit --message \
    "Bug-Fix (JIRA-00000): Corrected API Endpoint"
git push
... Enumerating objects: 8, done.
... Counting objects: 100% (8/8), done.
... Delta compression using up to 6 threads
... Compressing objects: 100% (4/4), done.
... Writing objects: 100% (6/6), 1.28 KiB | 1.28 MiB/s, done.
... Total 6 (delta 1), reused 0 (delta 0)
... To https://code.cloud-technology.io/CICD/Commit-Regular-Expressions.git
...     53f1fc3..add0477  master -> master
```

## Standardized Reference ##

[Insert Table-Map (How to Read Table)]

| Pattern | Description | Alias(es) |
| ------ | ------ | ------ |
| **Revert**,    `U` | Reverts a previous commit | `[U]ndo`, `Reversion`, `Reverted`, `Mistake` |
| **Fix**,       `B` | Work towards bug-related code | `[B]ugfix`, `Bug-Fix`, `Hot-Fix`, `Hotfix` |
| **[F]eature**, `F` | **Creation** of a capability: implementation of a dependency, test, functionality | `Add`, `Added`, `Addition`, `Implementation` `Implemented` |
| **Bump**,      `V` | **Increase version**; i.e. updating a dependency | `[V]ersion`, `Release` |
| **[T]est**,    `T` | *Additions* or *refactoring* of anything **test-related** | `Unit`, `Interoperability`, `Stage` |
| **[B]uild**,   `B` | Build effects to *compilation or external dependencies* | *Not Applicable* |
| **No-Build**,  `X` | Build effects to *compilation or external dependencies* | *Not Applicable* |
| **C[I]**,      `I` | *Changes to CI configuration files and scripts* | *Under Further Consideration* |
| **[R]efactor**,`R` | A code change that **neither** fixes a *bug* nor adds a *feature* | `Refactoring`|
| **[S]tyle**,   `S` | Deprivation of _Refactor_ - *white space, semi-colons, etc* | `Styling`, `Styles`, `Markup` |
| **[O]ptimize**,`O` | Deprivation of _Refactor_ - *runtime, build optimizations* | `Optimizing`, `Optimization` | 
| **[D]ocument**,`D` | Deprivation of _Refactor_ - *code documentation* | `Documentation`, `README`, `Information`, `ILC`, `In-Line-Comment`, `In-Line-Comments`, `Clarification` |

### Pattern Effects ###

- **`Revert`**
    - [Insert Description of Pattern]
    - [Insert Description of Deployment Process]
    - [Insert Description of Side-Effects]
- **`Fix`**
    - **Description**: *[Insert Description of Pattern]*
    - **Automation**: *[Insert Description of Deployment Process]*
    - **Note**: *[Insert Description of Side-Effects]*
- **`Feature`**
    - **Description**: *[Insert Description of Pattern]*
    - **Automation**: *[Insert Description of Deployment Process]*
    - **Note**: *[Insert Description of Side-Effects]*
- **`Bump`**
    - **Description**: *[Insert Description of Pattern]*
    - **Automation**: *[Insert Description of Deployment Process]*
    - **Note**: *[Insert Description of Side-Effects]*
- **`Test`**
    - **Description**: *[Insert Description of Pattern]*
    - **Automation**: *[Insert Description of Deployment Process]*
    - **Note**: *[Insert Description of Side-Effects]*
- **`Build`**
    - **Description**: *[Insert Description of Pattern]*
    - **Automation**: *[Insert Description of Deployment Process]*
    - **Note**: *[Insert Description of Side-Effects]*
- **`CI`**
    - **Description**: *[Insert Description of Pattern]*
    - **Automation**: *[Insert Description of Deployment Process]*
    - **Note**: *[Insert Description of Side-Effects]*
- **`Refactor`**
    - **Description**: *[Insert Description of Pattern]*
    - **Automation**: *[Insert Description of Deployment Process]*
    - **Note**: *[Insert Description of Side-Effects]*
- **`Style`**
    - **Description**: *[Insert Description of Pattern]*
    - **Automation**: *[Insert Description of Deployment Process]*
    - **Note**: *[Insert Description of Side-Effects]*
- **`Optimize`**
    - **Description**: *[Insert Description of Pattern]*
    - **Automation**: *[Insert Description of Deployment Process]*
    - **Note**: *[Insert Description of Side-Effects]*
- **`Document`**
    - **Description**: *[Insert Description of Pattern]*
    - **Automation**: *[Insert Description of Deployment Process]*
    - **Note**: *[Insert Description of Side-Effects]*

### Examples ###

- [Simple Jira + Semantic Commit](https://regex101.com/r/4m0pea/1)
```regexp
/((Jira?(\-))([1-9][0-9]*)|((Feat|Fix|Chore|Refactor|Style|Test|Docs)(-|\ |)(\((\w{0,15})\))?))?(\:?(\ ))(.*\S.*)/gmi
```
