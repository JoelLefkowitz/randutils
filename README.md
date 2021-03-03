# Randutils

Random generators and selection utilities.

## Status

| Source     | Shields                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Project    | ![release][release_shield] ![license][license_shield] ![dependents][dependents_shield]                             |
| Health     | ![travis][travis_shield] ![codacy][codacy_shield] ![coverage][coverage_shield] ![readthedocs][readthedocs_shield]  |
| Repository | ![issues][issues_shield] ![pulls][pulls_shield]                                                                    |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]           |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield] |

## Installation

```bash
pip install randutils
```

## Tests

To run unit tests:

```bash
grunt tests:unit
```

To generate a coverage report:

```bash
grunt tests:coverage
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

To generate the sphinx configuration:

```bash
grunt docs:generate
```

Then build the documentation:

```bash
grunt docs:build
```

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

Before commiting new code:

```bash
grunt precommit
```

This will run linters, formaters, generate a test coverage report and the sphinx configuration.

## Versioning

This repository adheres to semantic versioning standards.
For more inforamtion on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][joellefkowitz]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Github links -->

[pulls]: https://github.com/JoelLefkowitz/randutils/pulls
[issues]: https://github.com/JoelLefkowitz/randutils/issues

<!-- External links -->

[readthedocs]: https://randutils.readthedocs.io/en/latest/
[semver]: http://semver.org/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->

[joellefkowitz]: https://github.com/JoelLefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/randutils
[license_shield]: https://img.shields.io/github/license/joellefkowitz/randutils
[dependents_shield]: https://img.shields.io/librariesio/dependent-repos/pypi/randutils

<!-- Health shields -->

[travis_shield]: https://img.shields.io/travis/joellefkowitz/randutils
[codacy_shield]: https://img.shields.io/codacy/coverage/randutils
[coverage_shield]: https://img.shields.io/codacy/grade/randutils
[readthedocs_shield]: https://img.shields.io/readthedocs/randutils

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/randutils
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/randutils

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/randutils
[python_versions_shield]: https://img.shields.io/pypi/pyversions/randutils
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/randutils

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/randutils
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/randutils
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/randutils
