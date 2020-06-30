<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/gist-description.svg?maxAge=3600)](https://pypi.org/project/gist-description/)
[![](https://img.shields.io/npm/v/gist-description.svg?maxAge=3600)](https://www.npmjs.com/package/gist-description)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/gist-description/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/gist-description/actions)

### Installation
```bash
$ [sudo] pip install gist-description
```

```bash
$ [sudo] npm i -g gist-description
```

#### Config
```bash
$ export GITHUB_TOKEN="<GITHUB_TOKEN>"
```

#### Examples
```bash
$ gist-description <id> "new description"
$ gist-description <id>
new description
```

update multiple gists description
```bash
$ pip install gist-id
```

a) folder name as description
```bash
find ~/git/gists -type d -maxdepth 1 -exec bash -l -c 'id=$(gist-id "$0"); desc="$(basename "$0")"; [[ -n $id ]] && gist-description $id $desc' {} \;
```

b) `description.txt` as description
```bash
$ find ~/git/gists -type d -maxdepth 1 -exec bash -l -c 'id=$(gist-id "$0"); desc="$(cat description.txt 2> /dev/null)"; [[ -n $id ]] && [[ -n $desc ]] && gist-description $id $desc' {} \;
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>