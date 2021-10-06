# Nexus-API #

*The **Nexus** Cloud-Technology API*

[[_TOC_]]

## Overview ##

Cloud-Technology's API is a set of HTTP endpoints that adhere to RESTful design principles and CRUD
actions with predictable URIs. It uses standard HTTP response codes & messages. The
API has consistent and well-formed JSON communication patterns with cursor-based, variable pagination
to simplify list handling. Error messages are descriptive and easy to understand.

All functional endpoints a part of the Cloud-Technology customer portal are accessible via the API, enabling Users to
script complex unattended scenarios with any tool capable of HTTP.

## Setup & Usage ##

### Requirements ###

- PIP-3
- OpenSSL
- Python3.9+
- PostgreSQL 13
    - [UUID-OSCP](https://www.postgresql.org/docs/13/uuid-ossp.html) (Extension)
- MongoDB *or* DocumentDB

1. **Set the *Source* Repository URL** (Subject to Change):
    ```bash
    export URL="*.API.git"
    ```
2. **Clone the Repository**:
    ```bash
    git clone "${URL}"
    ```
3. **Change Working Directories & Update PIP**:
    ```bash
    cd ./API && python3 -m pip install pip --upgrade
    ```
4. **Enable a Virtual Environment**:
    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```
5. **Initialize a Hash Token**:
    ```bash
    export HASH_KEY="$(python3 -c "import secrets, sys; sys.stdout.write(secrets.token_urlsafe(32))")"
    ```
6. **Create `Environment.ini`**:
    ```ini
    [Database]
    PostgreSQL  = ****************************************************
    Mongo       = *********************************************************************************
    
    Secret      =
        %(PostgreSQL)s
        %(Mongo)s
    
    [Authentication]
    Token       = [Step-1-Hash-Token]
    Algorithm   = HS256
    Expiration  = 60
    
    Secret      =
        %(Token)s
    
    [Gitlab]
    URL         = gitlab.cloud.technology.io
    Username    = **************
    Token       = ********************
    
    Secret      =
        %(Token)s
        %(Username)s
    
    [Github]
    Username    = **************
    Token       = ****************************************
    
    Secret      =
        %(Token)s
        %(Username)s
    ```
7. **Lastly**:
    ```bash
    python3 -m pip install --use-feature in-tree-build --force --upgrade . && Nexus-API --Debug Server --TLS
    ```
    - Optionally, Developers & Contributors ***can and should*** run `Nexus-API` *in Development-Mode*:
        ```bash
        python3 -m API --Debug Server --TLS 
        ```

Please reach out to Jacob Sanders for additional details, permissions, and for help
getting started.

## Releases ##

1. **Create a `requirements.txt` File**.
    ```bash
    python3 -m pip freeze > requirements.txt
    ```
2. **Zip `.venv` Dependencies**.
   1. MacOS:
       ```bash
       zip Virtual-Environment.Darwin.zip -r .venv
       ```
   2. Ubuntu || Debian:
       ```bash
       zip Virtual-Environment.Debian.zip -r .venv
       ```
   3. CentOS 8, CentOS Stream, Fedora, RHEL:
       ```bash
       zip Virtual-Environment.Fedora.zip -r .venv
       ```
3. **Clean File Structure**.
    ```bash
    rm -r -f Artifact/Build
    rm -r -f Artifact/Distribution
    ```
4. **Compile Source Distribution**.
    ```bash
    python3 setup.py sdist
    ```
5. **Compile Wheel**.
    ```bash
    python3 setup.py bdist_wheel
    ```
6. **Copy State Object(s)**.
    ```bash
    cp VERSION ./Artifact
    cp requirements.txt ./Artifact
    cp Environment.ini ./Artifact
    
    cp *.py ./Artifact
    cp *.whl ./Artifact
    cp *.zip ./Artifact
    
    cp Key.PEM ./Artifact
    
    cp *.crt ./Artifact
    cp *.key ./Artifact
    cp *.pem ./Artifact
    
    cp LICENSE ./Artifact
    
    cp setup.py ./Artifact
    
    cp Install-Certificate.py ./Artifact
    ```
7. **Zip Artifact(s)**.
    ```bash
    zip Artifacts.zip -r ./Artifact
    ```
8. **Move Artifacts.zip to Target-Version**.
    ```bash
    mv Artifacts.zip ./$(cat VERSION).zip
    ```
9. **Force Add ./$(cat VERSION).zip to `git`**.
    ```bash
    git add --force ./$(cat VERSION).zip
    ```
 
## Debugging ##

### SSL Verification Failure ###

```log
urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)
```

**Run `python[3] Install-Certificate.py`**.

---

### MongoDB Setup (MacOS) ###

#### Requirements ####

- Brew

1. **Tap MongoDB**:
   ```bash
   brew tap mongodb/brew
   ```
1. **Install**:
   ```bash
   brew install mongodb-community@4.4
   ```

---

## Clustering ##

<details>

<summary>
    <strong>
        Service Management
    </strong>
</summary>

In the production environment, an "EKS" (AWS Elastic K8s Service) cluster
exists; please refer to the following section(s) regarding state management.

### EC2 Instance Access ###

**AWS-Shell CLI Generation**

- [Official AWS Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair)

```bash
aws ec2 create-key-pair --key-name "Nexus-API-EKS-Instance-Key"  \
    --query "KeyMaterial" --output text > \
        ~/.ssh/Nexus-API-EKS-Instance.PEM

chmod 400 ~/.ssh/Nexus-API-EKS-Instance.PEM
```

### Security Group ###

```bash
export ID="sg-0213ebb7f4ea54257"
export OWNER="983281742669"
export VPC_ID="vpc-a2fe3dc9"

export NAME="Nexus-API-EKS-Security-Group"
```

### Provisioning ###

![EKS Screenshot of Gitlab Provisioning Form](./Artifact/EKS-Screenshot-Form.png)

### Service Token Look-Up ###

```bash
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.20.4/2021-04-12/bin/darwin/amd64/kubectl
openssl sha1 -sha256 kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
echo 'export PATH=$PATH:$HOME/bin' >> ~/.profile
kubectl version --short --client

brew unlink eksctl || true

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

brew tap weaveworks/tap
brew install weaveworks/tap/eksctl
brew upgrade eksctl && brew link --overwrite eksctl

eksctl version

printf "%s" "Nexus-API-EKS-Cluster"                           > Cluster.Name
printf "%s" "Nexus-K8s-Service-EKS-Cluster-Development-Stack" > Cluster.Stack-Name

printf "%s" "$(aws sts get-caller-identity | jq -r .Account)" > Cluster.Account
printf "%s" "$(aws eks get-token --cluster-name "${CLUSTER}" --output "json" | jq -r ".status.token" --)" \
                                                              > Cluster.Token
printf "%s" "cluster.{certificateAuthorityData: certificateAuthority.data}.certificateAuthorityData" \
                                                              > Cluster.CA.Query
printf "%s" "$(aws eks describe-cluster --name "$(cat Cluster.Name)" --output "text" --query "$(cat Cluster.CA.Query)" | base64 --decode)" \
                                                              > Cluster.CA
printf "%s" "arn:aws:iam::$(cat Cluster.Account):user/Segmentational" > Cluster.Role
#printf "%s" "$(aws cloudformation describe-stack-resources --stack-name Nexus-K8s-Service-EKS-Cluster-Development-Stack | jq -r ".StackResources[-2].PhysicalResourceId")" \
#                                                              > Cluster.Role
aws eks update-kubeconfig --region "us-east-2" --name "${CLUSTER}" --role-arn "$(cat Cluster.Role)"

export TOKEN="$(aws eks get-token --cluster-name "${CLUSTER}" --output "json" | jq -r ".status.token" --)"
export CA="$(aws eks describe-cluster --name "${CLUSTER}" --output "text" --query "${CERTIFICATE}" | base64 --decode)"

# ... aws eks describe-cluster --name "${CLUSTER}" --output "text" --query "${CERTIFICATE}" | base64 --decode | pbcopy

# ... https://aws.amazon.com/premiumsupport/knowledge-center/eks-cluster-connection
```

</details>

---

## IDE Environment Variables ##

- `$USER_HOME$`: TTY Home Directory
- `$PROJECT_DIR$`: Where the Project is Located
- `$MODULE_DIR$`: The Directory where Module Configuration Files (IML) are Located

## References ##

### Contributors ###

- [*Contributors.md*](./Artifact/CONTRIBUTING.md)

### Time-Zones ###
|...|...|....|
|--- |--- |--- |
|Hawaii Time|Alaska Time|Pacific Time|
|Thursday, 6/24/2021, 9:20 AM, HST|Thursday, 6/24/2021, 11:20 AM, AKDT|Thursday 6/24/2021, 12:20 PM, PDT|
|Mountain Time|Central Time|Eastern Time|
|Thursday, 6/24/20211:20 PM, MDT|Thursday 6/24/20212:20 PM, CDT|Thursday 6/24/2021, 3:20 PM, EDT|

### Pipeline Environment Variables ###

<details>

<summary>
    <strong>
        Variables Table
    </strong>
</summary>

| Variable                                      | GitLab | Runner | Description                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------|--------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CHAT_CHANNEL`                                | 10.6   | all    | Source chat channel which triggered the [ChatOps](../chatops/README.md) command                                                                                                                                                                                                                                                                            |
| `CHAT_INPUT`                                  | 10.6   | all    | Additional arguments passed in the [ChatOps](../chatops/README.md) command                                                                                                                                                                                                                                                                                 |
| `CI`                                          | all    | 0.4    | Mark that job is executed in CI environment                                                                                                                                                                                                                                                                                                                |
| `CI_API_V4_URL`                               | 11.7   | all    | The GitLab API v4 root URL                                                                                                                                                                                                                                                                                                                                 |
| `CI_BUILDS_DIR`                               | all    | 11.10  | Top-level directory where builds are executed.                                                                                                                                                                                                                                                                                                             |
| `CI_COMMIT_BEFORE_SHA`                        | 11.2   | all    | The previous latest commit present on a branch. Is always `0000000000000000000000000000000000000000` in pipelines for merge requests.                                                                                                                                                                                                           |
| `CI_COMMIT_DESCRIPTION`                       | 10.8   | all    | The description of the commit: the message without first line, if the title is shorter than 100 characters; full message in other case.                                                                                                                                                                                                                    |
| `CI_COMMIT_MESSAGE`                           | 10.8   | all    | The full commit message.                                                                                                                                                                                                                                                                                                                                   |
| `CI_COMMIT_REF_NAME`                          | 9.0    | all    | The branch or tag name for which project is built                                                                                                                                                                                                                                                                                                          |
| `CI_COMMIT_REF_PROTECTED`                     | 11.11  | all    | `true` if the job is running on a protected reference, `false` if not                                                                                                                                                                                                                                                                                                               |
| `CI_COMMIT_REF_SLUG`                          | 9.0    | all    | `$CI_COMMIT_REF_NAME` lowercased, shortened to 63 bytes, and with everything except `0-9` and `a-z` replaced with `-`. No leading / trailing `-`. Use in URLs, host names and domain names.                                                                                                                                                                |
| `CI_COMMIT_SHA`                               | 9.0    | all    | The commit revision for which project is built                                                                                                                                                                                                                                                                                                             |
| `CI_COMMIT_SHORT_SHA`                         | 11.7   | all    | The first eight characters of `CI_COMMIT_SHA`                                                                                                                                                                                                                                                                                                              |
| `CI_COMMIT_BRANCH`                            | 12.6   | 0.5    | The commit branch name. Present only when building branches.                                                                                                                                                                                                                                                                                                      |
| `CI_COMMIT_TAG`                               | 9.0    | 0.5    | The commit tag name. Present only when building tags.                                                                                                                                                                                                                                                                                                      |
| `CI_COMMIT_TITLE`                             | 10.8   | all    | The title of the commit - the full first line of the message                                                                                                                                                                                                                                                                                               |
| `CI_COMMIT_TIMESTAMP`                         | 13.4   | all    | The timestamp of the commit in the ISO 8601 format.                                                                                                                                                                                                                                                                                               |
| `CI_CONCURRENT_ID`                            | all    | 11.10  | Unique ID of build execution within a single executor.                                                                                                                                                                                                                                                                                                     |
| `CI_CONCURRENT_PROJECT_ID`                    | all    | 11.10  | Unique ID of build execution within a single executor and project.                                                                                                                                                                                                                                                                                         |
| `CI_CONFIG_PATH`                              | 9.4    | 0.5    | The path to CI configuration file. Defaults to `.gitlab-ci.yml`                                                                                                                                                                                                                                                                                                   |
| `CI_DEBUG_TRACE`                              | all    | 1.7    | Whether [debug logging (tracing)](README.md#debug-logging) is enabled                                                                                                                                                                                                                                                                                      |
| `CI_DEFAULT_BRANCH`                           | 12.4   | all    | The name of the default branch for the project.                                                                                                                                                                                                                                                                                                            |
| `CI_DEPLOY_FREEZE`                            | 13.2   | all    | Included with the value `true` if the pipeline runs during a [deploy freeze window](../../user/project/releases/index.md#prevent-unintentional-releases-by-setting-a-deploy-freeze).                                                                                                                                                                                                                                    |
| `CI_DEPLOY_PASSWORD`                          | 10.8   | all    | Authentication password of the [GitLab Deploy Token](../../user/project/deploy_tokens/index.md#gitlab-deploy-token), only present if the Project has one related.                                                                                                                                                                                                                                    |
| `CI_DEPLOY_USER`                              | 10.8   | all    | Authentication username of the [GitLab Deploy Token](../../user/project/deploy_tokens/index.md#gitlab-deploy-token), only present if the Project has one related.                                                                                                                                                                                                                                    |
| `CI_DISPOSABLE_ENVIRONMENT`                   | all    | 10.1   | Marks that the job is executed in a disposable environment (something that is created only for this job and disposed of/destroyed after the execution - all executors except `shell` and `ssh`). If the environment is disposable, it is set to true, otherwise it is not defined at all.                                                                  |
| `CI_ENVIRONMENT_NAME`                         | 8.15   | all    | The name of the environment for this job. Only present if [`environment:name`](../yaml/README.md#environmentname) is set.                                                                                                                                                                                                                                  |
| `CI_ENVIRONMENT_SLUG`                         | 8.15   | all    | A simplified version of the environment name, suitable for inclusion in DNS, URLs, Kubernetes labels, etc. Only present if [`environment:name`](../yaml/README.md#environmentname) is set.                                                                                                                                                                 |
| `CI_ENVIRONMENT_URL`                          | 9.3    | all    | The URL of the environment for this job. Only present if [`environment:url`](../yaml/README.md#environmenturl) is set.                                                                                                                                                                                                                                     |
| `CI_EXTERNAL_PULL_REQUEST_IID`                | 12.3   | all    | Pull Request ID from GitHub if the [pipelines are for external pull requests](../ci_cd_for_external_repos/index.md#pipelines-for-external-pull-requests). Available only if `only: [external_pull_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the pull request is open.                                                                                                         |
| `CI_EXTERNAL_PULL_REQUEST_SOURCE_REPOSITORY`  | 13.3   | all    | The source repository name of the pull request if [the pipelines are for external pull requests](../ci_cd_for_external_repos/index.md#pipelines-for-external-pull-requests). Available only if `only: [external_pull_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the pull request is open.                                                                                          |
| `CI_EXTERNAL_PULL_REQUEST_TARGET_REPOSITORY`  | 13.3   | all    | The target repository name of the pull request if [the pipelines are for external pull requests](../ci_cd_for_external_repos/index.md#pipelines-for-external-pull-requests). Available only if `only: [external_pull_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the pull request is open.                                                                                          |
| `CI_EXTERNAL_PULL_REQUEST_SOURCE_BRANCH_NAME` | 12.3   | all    | The source branch name of the pull request if [the pipelines are for external pull requests](../ci_cd_for_external_repos/index.md#pipelines-for-external-pull-requests). Available only if `only: [external_pull_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the pull request is open.                                                                                          |
| `CI_EXTERNAL_PULL_REQUEST_SOURCE_BRANCH_SHA`  | 12.3   | all    | The HEAD SHA of the source branch of the pull request if [the pipelines are for external pull requests](../ci_cd_for_external_repos/index.md#pipelines-for-external-pull-requests). Available only if `only: [external_pull_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the pull request is open.                                                                               |
| `CI_EXTERNAL_PULL_REQUEST_TARGET_BRANCH_NAME` | 12.3   | all    | The target branch name of the pull request if [the pipelines are for external pull requests](../ci_cd_for_external_repos/index.md#pipelines-for-external-pull-requests). Available only if `only: [external_pull_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the pull request is open.                                                                                          |
| `CI_EXTERNAL_PULL_REQUEST_TARGET_BRANCH_SHA`  | 12.3   | all    | The HEAD SHA of the target branch of the pull request if [the pipelines are for external pull requests](../ci_cd_for_external_repos/index.md#pipelines-for-external-pull-requests). Available only if `only: [external_pull_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the pull request is open.                                                                               |
| `CI_HAS_OPEN_REQUIREMENTS`                    | 13.1   | all    | Included with the value `true` only if the pipeline's project has any open [requirements](../../user/project/requirements/index.md). Not included if there are no open requirements for the pipeline's project.                                                                                                                                                                                        |
| `CI_JOB_ID`                                   | 9.0    | all    | The unique ID of the current job that GitLab CI/CD uses internally                                                                                                                                                                                                                                                                                            |
| `CI_JOB_IMAGE`                                | 12.9   | 12.9   | The name of the image running the CI job                                                                                                                                                                                                                                                                                                                   |
| `CI_JOB_MANUAL`                               | 8.12   | all    | The flag to indicate that job was manually started                                                                                                                                                                                                                                                                                                         |
| `CI_JOB_NAME`                                 | 9.0    | 0.5    | The name of the job as defined in `.gitlab-ci.yml`                                                                                                                                                                                                                                                                                                         |
| `CI_JOB_STAGE`                                | 9.0    | 0.5    | The name of the stage as defined in `.gitlab-ci.yml`                                                                                                                                                                                                                                                                                                       |
| `CI_JOB_TOKEN`                                | 9.0    | 1.2    | Token used for authenticating with the [GitLab Container Registry](../../user/packages/container_registry/index.md), downloading [dependent repositories](../../user/project/new_ci_build_permissions_model.md#dependent-repositories), and accessing [GitLab-managed Terraform state](../../user/infrastructure/index.md#gitlab-managed-terraform-state).         |
| `CI_JOB_JWT`                                  | 12.10  | all    | RS256 JSON web token that can be used for authenticating with third party systems that support JWT authentication, for example [HashiCorp's Vault](../secrets/index.md). |
| `CI_JOB_URL`                                  | 11.1   | 0.5    | Job details URL                                                                                                                                                                                                                                                                                                                                            |
| `CI_KUBERNETES_ACTIVE`                        | 13.0   | all    | Included with the value `true` only if the pipeline has a Kubernetes cluster available for deployments. Not included if no cluster is available. Can be used as an alternative to [`only:kubernetes`/`except:kubernetes`](../yaml/README.md#onlykubernetesexceptkubernetes) with [`rules:if`](../yaml/README.md#rulesif)                                    |
| `CI_MERGE_REQUEST_ASSIGNEES`                  | 11.9   | all    | Comma-separated list of username(s) of assignee(s) for the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                              |
| `CI_MERGE_REQUEST_ID`                         | 11.6   | all    | The instance-level ID of the merge request. Only available if [the pipelines are for merge requests](../merge_request_pipelines/index.md) and the merge request is created.                                                                                                                                                           |
| `CI_MERGE_REQUEST_IID`                        | 11.6   | all    | The project-level IID (internal ID) of the merge request. Only available If [the pipelines are for merge requests](../merge_request_pipelines/index.md) and the merge request is created.                                                                                                                                                          |
| `CI_MERGE_REQUEST_LABELS`                     | 11.9   | all    | Comma-separated label names of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                                                      |
| `CI_MERGE_REQUEST_MILESTONE`                  | 11.9   | all    | The milestone title of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                                                              |
| `CI_MERGE_REQUEST_PROJECT_ID`                 | 11.6   | all    | The ID of the project of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                                                            |
| `CI_MERGE_REQUEST_PROJECT_PATH`               | 11.6   | all    | The path of the project of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md) (e.g. `namespace/awesome-project`). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                       |
| `CI_MERGE_REQUEST_PROJECT_URL`                | 11.6   | all    | The URL of the project of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md) (e.g. `http://192.168.10.15:3000/namespace/awesome-project`). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                              |
| `CI_MERGE_REQUEST_REF_PATH`                   | 11.6   | all    | The ref path of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). (e.g. `refs/merge-requests/1/head`). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                                |
| `CI_MERGE_REQUEST_SOURCE_BRANCH_NAME`         | 11.6   | all    | The source branch name of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                                                           |
| `CI_MERGE_REQUEST_SOURCE_BRANCH_SHA`          | 11.9   | all    | The HEAD SHA of the source branch of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used, the merge request is created, and the pipeline is a [merged result pipeline](../merge_request_pipelines/pipelines_for_merged_results/index.md). **(PREMIUM)**   |
| `CI_MERGE_REQUEST_SOURCE_PROJECT_ID`          | 11.6   | all    | The ID of the source project of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                                                     |
| `CI_MERGE_REQUEST_SOURCE_PROJECT_PATH`        | 11.6   | all    | The path of the source project of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                                                   |
| `CI_MERGE_REQUEST_SOURCE_PROJECT_URL`         | 11.6   | all    | The URL of the source project of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                                                    |
| `CI_MERGE_REQUEST_TARGET_BRANCH_NAME`         | 11.6   | all    | The target branch name of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                                                           |
| `CI_MERGE_REQUEST_TARGET_BRANCH_SHA`          | 11.9   | all    | The HEAD SHA of the target branch of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or [`rules`](../yaml/README.md#rules) syntax is used, the merge request is created, and the pipeline is a [merged result pipeline](../merge_request_pipelines/pipelines_for_merged_results/index.md). **(PREMIUM)**   |
| `CI_MERGE_REQUEST_TITLE`                      | 11.9   | all    | The title of the merge request if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Available only if `only: [merge_requests]` or  [`rules`](../yaml/README.md#rules) syntax is used and the merge request is created.                                                                                                                                                        |
| `CI_MERGE_REQUEST_EVENT_TYPE`                 | 12.3   | all    | The event type of the merge request, if [the pipelines are for merge requests](../merge_request_pipelines/index.md). Can be `detached`, `merged_result` or `merge_train`. |
| `CI_NODE_INDEX`                               | 11.5   | all    | Index of the job in the job set. If the job is not parallelized, this variable is not set.                                                                                                                                                                                                                                                                 |
| `CI_NODE_TOTAL`                               | 11.5   | all    | Total number of instances of this job running in parallel. If the job is not parallelized, this variable is set to `1`.                                                                                                                                                                                                                                    |
| `CI_PAGES_DOMAIN`                             | 11.8   | all    | The configured domain that hosts GitLab Pages.                                                                                                                                                                                                                                                                                                             |
| `CI_PAGES_URL`                                | 11.8   | all    | URL to GitLab Pages-built pages. Always belongs to a subdomain of `CI_PAGES_DOMAIN`.                                                                                                                                                                                                                                                                       |
| `CI_PIPELINE_ID`                              | 8.10   | all    | The instance-level ID of the current pipeline.                                                                                                                                                                                                                                                                                                             |
| `CI_PIPELINE_IID`                             | 11.0   | all    | The project-level IID (internal ID) of the current pipeline.                                                                                                                                                                                                                                                                                               |
| `CI_PIPELINE_SOURCE`                          | 10.0   | all    | Indicates how the pipeline was triggered. Possible options are: `push`, `web`, `schedule`, `api`, `external`, `chat`, `webide`, `merge_request_event`, `external_pull_request_event`, `parent_pipeline`, [`trigger`, or `pipeline`](../triggers/README.md#authentication-tokens) (renamed to `cross_project_pipeline` since 13.0). For pipelines created before GitLab 9.5, this is displayed as `unknown`. |
| `CI_PIPELINE_TRIGGERED`                       | all    | all    | The flag to indicate that job was [triggered](../triggers/README.md)                                                                                                                                                                                                                                                                                       |
| `CI_PIPELINE_URL`                             | 11.1   | 0.5    | Pipeline details URL                                                                                                                                                                                                                                                                                                                                       |
| `CI_PROJECT_DIR`                              | all    | all    | The full path where the repository is cloned and where the job is run. If the GitLab Runner `builds_dir` parameter is set, this variable is set relative to the value of `builds_dir`. For more information, see [Advanced configuration](https://docs.gitlab.com/runner/configuration/advanced-configuration.html#the-runners-section) for GitLab Runner. |
| `CI_PROJECT_ID`                               | all    | all    | The unique ID of the current project that GitLab CI/CD uses internally                                                                                                                                                                                                                                                                                        |
| `CI_PROJECT_NAME`                             | 8.10   | 0.5    | The name of the directory for the project that is currently being built. For example, if the project URL is `gitlab.example.com/group-name/project-1`, the `CI_PROJECT_NAME` would be `project-1`.                                                                                                                                                         |
| `CI_PROJECT_NAMESPACE`                        | 8.10   | 0.5    | The project namespace (username or group name) that is currently being built                                                                                                                                                                                                                                                                                |
| `CI_PROJECT_ROOT_NAMESPACE`                   | 13.2   | 0.5    | The **root** project namespace (username or group name) that is currently being built. For example, if `CI_PROJECT_NAME` is `root-group/child-group/grandchild-group`, `CI_PROJECT_ROOT_NAMESPACE` would be `root-group`.                                                                                                                                  |
| `CI_PROJECT_PATH`                             | 8.10   | 0.5    | The namespace with project name                                                                                                                                                                                                                                                                                                                            |
| `CI_PROJECT_PATH_SLUG`                        | 9.3    | all    | `$CI_PROJECT_PATH` lowercased and with everything except `0-9` and `a-z` replaced with `-`. Use in URLs and domain names.                                                                                                                                                                                                                                  |
| `CI_PROJECT_REPOSITORY_LANGUAGES`             | 12.3   | all    | Comma-separated, lowercased list of the languages used in the repository (e.g. `ruby,javascript,html,css`)                                                                                                                                                                                                                                                 |
| `CI_PROJECT_TITLE`                            | 12.4   | all    | The human-readable project name as displayed in the GitLab web interface.                                                                                                                                                                                                                                                                                  |
| `CI_PROJECT_URL`                              | 8.10   | 0.5    | The HTTP(S) address to access project                                                                                                                                                                                                                                                                                                                      |
| `CI_PROJECT_VISIBILITY`                       | 10.3   | all    | The project visibility (internal, private, public)                                                                                                                                                                                                                                                                                                         |
| `CI_REGISTRY`                                 | 8.10   | 0.5    | If the Container Registry is enabled it returns the address of GitLab's Container Registry. This variable includes a `:port` value if one has been specified in the registry configuration.                                                                                                                                                           |
| `CI_REGISTRY_IMAGE`                           | 8.10   | 0.5    | If the Container Registry is enabled for the project it returns the address of the registry tied to the specific project                                                                                                                                                                                                                                   |
| `CI_REGISTRY_PASSWORD`                        | 9.0    | all    | The password to use to push containers to the GitLab Container Registry, for the current project.                                                                                                                                                                                                                                                                |
| `CI_REGISTRY_USER`                            | 9.0    | all    | The username to use to push containers to the GitLab Container Registry, for the current project.                                                                                                                                                                                                                                                                 |
| `CI_REPOSITORY_URL`                           | 9.0    | all    | The URL to clone the Git repository                                                                                                                                                                                                                                                                                                                        |
| `CI_RUNNER_DESCRIPTION`                       | 8.10   | 0.5    | The description of the runner as saved in GitLab                                                                                                                                                                                                                                                                                                           |
| `CI_RUNNER_EXECUTABLE_ARCH`                   | all    | 10.6   | The OS/architecture of the GitLab Runner executable (note that this is not necessarily the same as the environment of the executor)                                                                                                                                                                                                                        |
| `CI_RUNNER_ID`                                | 8.10   | 0.5    | The unique ID of runner being used                                                                                                                                                                                                                                                                                                                         |
| `CI_RUNNER_REVISION`                          | all    | 10.6   | GitLab Runner revision that is executing the current job                                                                                                                                                                                                                                                                                                   |
| `CI_RUNNER_SHORT_TOKEN`                       | all    | 12.3   | First eight characters of the runner's token used to authenticate new job requests. Used as the runner's unique ID                                                                                                                                                                                                                                         |
| `CI_RUNNER_TAGS`                              | 8.10   | 0.5    | The defined runner tags                                                                                                                                                                                                                                                                                                                                    |
| `CI_RUNNER_VERSION`                           | all    | 10.6   | GitLab Runner version that is executing the current job                                                                                                                                                                                                                                                                                                    |
| `CI_SERVER`                                   | all    | all    | Mark that job is executed in CI environment                                                                                                                                                                                                                                                                                                                |
| `CI_SERVER_URL`                               | 12.7   | all    | The base URL of the GitLab instance, including protocol and port (like `https://gitlab.example.com:8080`)                                                                                                                                                                                                                                                           |
| `CI_SERVER_HOST`                              | 12.1   | all    | Host component of the GitLab instance URL, without protocol and port (like `gitlab.example.com`)                                                                                                                                                                                                                                                           |
| `CI_SERVER_PORT`                              | 12.8   | all    | Port component of the GitLab instance URL, without host and protocol (like `3000`)                                                                                                                                                                                                                                                                         |
| `CI_SERVER_PROTOCOL`                          | 12.8   | all    | Protocol component of the GitLab instance URL, without host and port (like `https`)                                                                                                                                                                                                                                                                        |
| `CI_SERVER_NAME`                              | all    | all    | The name of CI server that is used to coordinate jobs                                                                                                                                                                                                                                                                                                      |
| `CI_SERVER_REVISION`                          | all    | all    | GitLab revision that is used to schedule jobs                                                                                                                                                                                                                                                                                                              |
| `CI_SERVER_VERSION`                           | all    | all    | GitLab version that is used to schedule jobs                                                                                                                                                                                                                                                                                                               |
| `CI_SERVER_VERSION_MAJOR`                     | 11.4   | all    | GitLab version major component                                                                                                                                                                                                                                                                                                                             |
| `CI_SERVER_VERSION_MINOR`                     | 11.4   | all    | GitLab version minor component                                                                                                                                                                                                                                                                                                                             |
| `CI_SERVER_VERSION_PATCH`                     | 11.4   | all    | GitLab version patch component                                                                                                                                                                                                                                                                                                                             |
| `CI_SHARED_ENVIRONMENT`                       | all    | 10.1   | Marks that the job is executed in a shared environment (something that is persisted across CI invocations like `shell` or `ssh` executor). If the environment is shared, it is set to true, otherwise it is not defined at all.                                                                                                                            |
| `GITLAB_CI`                                   | all    | all    | Mark that job is executed in GitLab CI/CD environment                                                                                                                                                                                                                                                                                                         |
| `GITLAB_FEATURES`                             | 10.6   | all    | The comma separated list of licensed features available for your instance and plan                                                                                                                                                                                                                                                                         |
| `GITLAB_USER_EMAIL`                           | 8.12   | all    | The email of the user who started the job                                                                                                                                                                                                                                                                                                                  |
| `GITLAB_USER_ID`                              | 8.12   | all    | The ID of the user who started the job                                                                                                                                                                                                                                                                                                                     |
| `GITLAB_USER_LOGIN`                           | 10.0   | all    | The login username of the user who started the job                                                                                                                                                                                                                                                                                                         |
| `GITLAB_USER_NAME`                            | 10.0   | all    | The real name of the user who started the job                                                                                                                                                                                                                                                                                                              |

</details>

## Serverless Technologies ##

<details>

<summary>Fargate</summary>

**AWS Fargate** is a *serverless* compute engine for containers that works with both Amazon Elastic 
Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). Fargate makes it easy 
for you to focus on building your applications. Fargate removes the need to provision and manage 
servers, lets you specify and pay for resources per application, and improves security through 
application isolation by design.

Fargate allocates the right amount of compute, eliminating the need to choose instances and scale 
cluster capacity. You only pay for the resources required to run your containers, so there is no 
over-provisioning and paying for additional servers. Fargate runs each task or pod in its own kernel 
providing the tasks and pods their own isolated compute environment. This enables your application 
to have workload isolation and improved security by design. This is why customers such as Vanguard,
Accenture, Foursquare, and Ancestry have chosen to run their mission critical applications on 
Fargate.

</details>

### TLS Development Key(s) ###

<details>

<summary>
    <strong>
        OpenSSL CLI Instructions
    </strong>
</summary>

<br/>

```bash
#!/bin/bash --posix

#
# A CSR or Certificate Signing request is a block of encoded text that is given to a Certificate Authority
# when applying for an SSL Certificate. It is usually generated on the server where the certificate will be
# installed and contains information that will be included in the certificate such as the organization name,
# common name (domain name), locality, and country. It also contains the public key that will be included in
# the certificate. A private key is usually created at the same time that you create the CSR, making a key pair.
#
# CSRs are generally encoded using ASN.1 according to the PKCS #10 specification.
#

# ... export SUB="/C=US/ST=MN/O=Cloud Technology LLC./CN=localhost/subjectAltName=DNS:*.nexus.cloud-technology.io,DNS:nexus.cloud-technology.io,localhost,0.0.0.0"
# ...
# ... openssl req -x509 -newkey rsa:8192 -nodes -sha256   \
# ...     -days 365 -passin "pass:Development"            \
# ...         -subj "${SUB}" -keyout Development.key      \
# ...             -out Development.pem

# --> Debian & Ubuntu
# ... sudo apt install libnss3-tools --yes

# --> OS Agnostic
cat << "EOF" | tee Development.conf
[ req ]
prompt              = no
default_bits        = 2048
default_keyfile     = Development.pem
distinguished_name  = subject
req_extensions      = req_ext
x509_extensions     = x509_ext
string_mask         = utf8only

# RFC 4514, RFC 4519

[ subject ]
countryName              = US
stateOrProvinceName      = MN
localityName             = Minneapolis
organizationName         = Localhost

# Friendly Name

commonName          = Development Certificate
emailAddress        = development@localhost.com

[ x509_ext ]

subjectKeyIdentifier        = hash
authorityKeyIdentifier      = keyid,issuer
basicConstraints        = CA:FALSE
keyUsage                = digitalSignature, keyEncipherment
subjectAltName          = @alternate_names
nsComment               = "OpenSSL Generated Certificate"

# RFC 5280, Section 4.2.1.12 makes EKU optional

[ req_ext ]

subjectKeyIdentifier        = hash

basicConstraints            = CA:FALSE
keyUsage                    = digitalSignature, keyEncipherment
subjectAltName              = @alternate_names
nsComment                   = "OpenSSL Generated Certificate"

# CA/Browser Baseline Requirements, Appendix (B)(3)(G)

[ alternate_names ]

DNS.1       = localhost
DNS.7       = 127.0.0.1

# IPv6 localhost
# DNS.8     = ::1
EOF

openssl req -config Development.conf -new -x509 -sha256 -newkey rsa:2048 -nodes \
    -days "1024" -keyout "Development.key" -out "Development.crt"

openssl pkcs12 -export -out "Development.pfx" -inkey "Development.key" -in "Development.crt"

# --> MacOS Only
# ... sudo security -v add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain Development.crt

# --> Debian & Ubuntu
# ... pk12util -d "sql:${HOME}/.pki/nssdb" -i Development.pfx
# ... certutil -d sql:$HOME/.pki/nssdb -A -t "P,," -n "Development Certificate" -i Development.crt

# Reference
#   - https://stackoverflow.com/questions/7580508/getting-chrome-to-accept-self-signed-localhost-certificate
```

</details>

## Finding Process via Port ##

```bash
 lsof -i :3000
```
