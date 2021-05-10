# Hermod

[![dev workflow](https://github.com/yensa/hermod/actions/workflows/dev.yml/badge.svg?branch=main)](https://github.com/yensa/hermod/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/yensa/hermod/branch/main/graph/badge.svg?token=L7Z4LYGMUT)](https://codecov.io/gh/yensa/hermod)
[![Requires.io](https://img.shields.io/requires/github/yensa/hermod)](https://requires.io/github/yensa/hermod/requirements/?branch=main)
[![PyPI](https://img.shields.io/pypi/v/hermod)](https://pypi.python.org/pypi/hermod)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hermod)](https://pypi.python.org/pypi/hermod)

Hermod is a package that generates .proto files out of your sqlalchemy models

* Free software: MIT
* Documentation: <https://yensa.github.io/hermod/>

## Features

### Convert sqlalchemy models to proto message

```python
from hermod import model_to_message, Message

message = model_to_message(MyModel)

assert isinstance(message, Message)

print(message.to_string())
```

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage) project template.
