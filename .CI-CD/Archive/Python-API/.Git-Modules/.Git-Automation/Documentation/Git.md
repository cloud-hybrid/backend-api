### Pruning ###

> Git has a default disposition of keeping data unless it’s explicitly thrown away; 
> this extends to holding onto local references to branches on remotes that have themselves 
> deleted those branches.
> 
> If left to accumulate, these stale references might make performance worse on big and busy 
> repos that have a lot of branch churn, and e.g. make the output of commands like 
> `git branch -a --contains <commit>` needlessly verbose, as well as impacting anything else 
> that’ll work with the complete set of known references.

`git config remote.origin.prune true`

```toml
[fetch]
    prune = true
