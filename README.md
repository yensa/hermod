# Hermod


<p align="center">
<a href="https://pypi.python.org/pypi/hermod">
    <img src="https://img.shields.io/pypi/v/hermod.svg"
        alt = "Release Status">
</a>

<a href="https://github.com/yensa/hermod/actions">
    <img src="https://github.com/yensa/hermod/actions/workflows/main.yml/badge.svg?branch=main" alt="CI Status">
</a>

</p>

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
