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

```bash
$ find ~/git/gists -mindepth 1 -maxdepth 1 -exec bash -l -c 'gist-description $(gist-id) "$(basename "{}")"' \;
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>