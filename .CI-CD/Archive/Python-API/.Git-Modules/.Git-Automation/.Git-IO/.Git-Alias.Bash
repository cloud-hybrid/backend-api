alias git-update="git add --all && git commit -m '$( echo "[WIP]:[Build] - $(uuidgen)" )' && git push"
alias git-commit='echo -n "Commit Summary [ENTER]: " && read COMMIT && git add . && git commit -m "${COMMIT}" && git push'
alias gcp='echo -n "Commit Summary [ENTER]: " && read COMMIT && git add . && git commit -m "${COMMIT}" && git push'
alias git-submodule-update="git submodule update --remote --force"
