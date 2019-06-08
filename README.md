<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/gist-description.svg?maxAge=3600)](https://pypi.org/project/gist-description/)
[![](https://img.shields.io/npm/v/gist-description.svg?maxAge=3600)](https://www.npmjs.com/package/gist-description)
[![Travis](https://api.travis-ci.org/looking-for-a-job/gist-description.svg?branch=master)](https://travis-ci.org/looking-for-a-job/gist-description/)

#### Installation
```bash
$ [sudo] npm i -g gist-description
```
```bash
$ [sudo] pip install gist-description
```

#### Config
```bash
$ export GITHUB_TOKEN="<GITHUB_TOKEN>"
```

#### Scripts usage
```bash
usage: gist-description id [description]
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
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>