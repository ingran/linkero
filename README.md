# Linkero

[![Build Status](https://travis-ci.org/ingran/linkero.svg?branch=master)](https://travis-ci.org/ingran/linkero)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2b63ba733fed4213b97361f0593d3a3b)](https://www.codacy.com/app/RDCH106/linkero?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ingran/linkero&amp;utm_campaign=Badge_Grade)

<!-- ![logo](http://ingran.es:8081/uploads/project/avatar/22/Link_Slash.png) -->

Framework focused in Restful API development for external requests powered by [Ingran Engineering](https://ingran.es) under [AGPL-3.0](https://github.com/RDCH106/linkero/blob/master/LICENSE) license.

Linkero is compatible with Python-2 and Python-3.

### What can I do with Linkero?

- Run REST API server
- Mount your Python developments or wrappers as API REST service. Only spend time developing your APIs behaviour.
- Add new APIs easily to already existing gateway development.
- Generate Public APIs.
- Generate Private APIs.
    - Security using user and password authentication.
    - Security using token.
    - Grant privileges to desired APIs or only a group of calls of API to specific users.
- User accounts persistence using SQLite DB.
- Integration with other WSGI (Web Server Gateway Interface):
    - [Gevent](https://github.com/gevent/gevent)
    - [Waitress](https://github.com/Pylons/waitress)

### Intallation

You can install or upgrade linkero with:

`$ pip install linkero --upgrade`

Or you can install from source with:

```
$ git clone https://github.com/ingran/linkero.git --recursive
$ cd linkero
$ pip install .
```

### **Documentation**

More information available in the **[WIKI](https://github.com/ingran/linkero/wiki/home)**.

### **Contribution**

Check the **[Contributing](https://github.com/ingran/linkero/blob/master/CONTRIBUTING.md)** guide.
