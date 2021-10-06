

### Formatting & Whitespace ###

Configuring the Correct `git` Line-Endings & BOM Configurations 
is Important for **Cross-Platform Development Compatability**.

- **Command**: `git config --global core.autocrlf true`
- **`.gitconfig`**:
    ```toml
    [core]; git config --global core.autocrlf true
    	autocrlf = true
    ```

### Git-Core Editor ###

`git` will occassionally prompt for user-input when a message is
required (i.e. during a merge request). The default is set to either `vim`
or `vi`.

*`Nano`* (Command-Line Text Editor)
- **Command**: `git config --global core.editor nano`
- **`.gitconfig`**:
    ```toml
    [core]; git config --global core.editor nano
        editor = 'nano'
    ```
*`VSCode`* (Application, GUI-based Text Editor)
- **Command**: `git config --global core.editor "'/Applications/Visual Studio Code.app/Contents/MacOS/Electron' -w"`
- **`.gitconfig`**:
    ```toml
    [core]; git config --global core.editor "'/Applications/Visual Studio Code.app/Contents/MacOS/Electron' -w"
	editor = '/Applications/Visual Studio Code.app/Contents/MacOS/Electron' -w
    ```
### Merge Strategy ###

`git config --local merge.ff only`

```toml
[merge]; git config --local merge.ff only
    ff = only
[branch "UAT"]; git config branch.UAT.mergeoptions  "--no-ff"
    mergeoptions = --no-ff
[branch "Staging"]; git config branch.Staging.mergeoptions  "--no-ff"
    mergeoptions = --no-f
[branch "Production"]; git config branch.Production.mergeoptions  "--no-ff"
    mergeoptions = --no-f
```

