# CHANGELOG

<!--
All enhancements and changes will be documented in this file.  It adheres to
the structure of http://keepachangelog.com/ ,

This project adheres to Semantic Versioning (http://semver.org/).
-->

## Unreleased

See the fragment files in the [changelog.d/ directory](./changelog.d).

<!-- scriv-insert-here -->

<a id='changelog-21.0.0'></a>
## 21.0.0 — 2026-01-28

### Added

- Add support for the Ulmo release.

### Changed

- Bump the sentry-sdk version to 2.46.0

<a id='changelog-20.0.0'></a>
## v20.0.0 (2025-07-02)

### Added

- Support for the Teak release.

### Changed

- Update the sentry-sdk version to 2.29.1

## v19.0.0 (2024-12-18)

### Features

- Sumac release ([#3](https://github.com/eduNEXT/tutor-contrib-sentry/pull/3),
  [`0edf1cb`](https://github.com/eduNEXT/tutor-contrib-sentry/commit/0edf1cbef79872b474071df60f856dfa4b179056))


## v18.0.0 (2024-07-11)

### Bug Fixes

- Default sample_rate to 0.0
  ([`bc45e45`](https://github.com/eduNEXT/tutor-contrib-sentry/commit/bc45e4514c7df32223331a418d39a72e8049deca))

- Ignore oswrite error on uwsgi
  ([`70a17fd`](https://github.com/eduNEXT/tutor-contrib-sentry/commit/70a17fddaa16dfa49868abc92c31007b8feb06ff))

### Features

- Add sentry support on openedx
  ([`a520a4d`](https://github.com/eduNEXT/tutor-contrib-sentry/commit/a520a4d5c4134d761d2956eef5758690780c1f35))

- Allow to ignore exceptions by class type and regex
  ([`bcb0883`](https://github.com/eduNEXT/tutor-contrib-sentry/commit/bcb0883af813640208aeaf78ecb2ee633bb7077e))
