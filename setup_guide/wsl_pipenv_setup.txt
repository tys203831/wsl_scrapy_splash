https://stackoverflow.com/questions/52540121/make-pipenv-create-the-virtualenv-in-the-same-folder#answer-60234402

1. Just make empty folder inside your project and name it .venv and pipenv will use this folder.

2. Use either `python3 -m pipenv install` or `python -m pipenv install`