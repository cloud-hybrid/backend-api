#!/bin/bash --posix

# @Task: https://docs.gitlab.com/ce/user/project/push_options.html
# ---> Document Table(s)
#

git config --global pull.rebase true
git config --global fetch.prune true

# --> To set up a Git alias for the merge when pipeline succeeds
# ... https://docs.gitlab.com/ce/user/project/push_options.html#push-options-for-merge-requests
# >>> git mwps origin <local-branch-name>
git config --global branch.mergeOptions "push -o merge_request.create -o merge_request.target=master -o merge_request.merge_when_pipeline_succeeds"

git config --global alias.push-merge-skip "git push -o ci.skip"

git push \
    -o merge_request.create \
    -o merge_request.target="${1}" \
    -o merge_request.title="${3}" \
    -o merge_request.description="${4}" \
    -o merge_request.remove_source_branch \
    origin "${2}"

git push --set-upstream origin Development -o merge_request.create

# Merging #

git status  && git checkout Development

git merge master

git checkout master

git merge Development

git branch --delete Development \
    && git branch Development \
    && git checkout Development
