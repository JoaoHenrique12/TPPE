# Pytest

## Executing pytest.

Note that by default, pytest looks for files named test_*.py or *_test.py
in the specified directory.

Functions for tests must starts with test\_

```bash
$ pytest nome_arquivo_teste.py
$ pytest folder_with_test/
```
### Verbose option

Flags : -v, -vv, -vvv.

### Show output from std*
Flag -s

### Durations reports

pytest --durations=3

Show the 3 most slow tests.

## Plugins

### pytest-randomly

Shuffle the order of your tests execution.
Good for find if your code have stateful dependency.

### pytest-cov

Measure how well your tests cover your implementation.

## pytest-bdd

[link](https://pytest-bdd.readthedocs.io/en/latest/#bdd-library-for-the-pytest-runner).

[Gherkin language](https://docs.behat.org/en/v2.5/guides/1.gherkin.html).

## Marking tests

[REFERENCE](https://docs.pytest.org/en/7.1.x/example/markers.html)

Maybe you will need define marks, [how to define marks](https://docs.pytest.org/en/stable/how-to/mark.html).
Pytest have some default marks, to list it use: 

```bash
$ pytest --markers
```

Executing tests with a certain mark

```bash
$ pytest -m return_error
```

Executing tests that are not a certain mark

```bash
$ pytest -m "not return_error"
```
Executing tests with mark a or b. The same idea work's for and.

```bash
$ pytest -m "a or b"
```

### Mark nomark

Is a convention used in some projects to mark a test without marks.

### Filter by name

The -k option in pytest allows you to filter which tests to run based on their names, using a substring match.
And, or, not are keywords that work here just like marks.

```bash
pytest -k "always"
```
