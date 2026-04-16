---
description: Run python tests with pytest - [ files ]
agent: build
permission:
  bash:
    pytest *: allow
  edit: ask
---

## overview

* Run python tests with pytest


## context

* tests in pytest located in the ./app/tests folder

## tasks

1. Run the tests with the `pytest` command in the root project dir and show warnings any failures.
  + if $ARGUMENTS is set, pass it to pytest (e.g. `pytest $ARGUMENTS`).
2. Focus on the failing tests and warnings , then suggest fixes.