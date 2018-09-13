# word-frequency-counter-tests

Repo with tests for lab #1.

Running tests:
```
python -m unittest discover -p "*_test.py" -s .
``` 

## Что делать если в родительском репозитории есть изменения и они мне нужны?

1. Создаем `upstream` таргет в репозитории:
```
git remote add upstream https://github.com/fipl-hse/word-frequency-counter-tests
git fetch upstream
git merge upstream/master
```
