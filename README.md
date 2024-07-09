# Celery plugin for [Tutor](https://docs.tutor.edly.io)

A tutor plugin to integration Open edX with Sentry.

## Installation

```shell
pip install git+https://github.com/eduNEXT/tutor-contrib-sentry
```

## Usage

```shell
tutor plugins enable sentry
```

## Configuration

This plugin supports the following settings:

- `SENTRY_DSN`: The sentry DSN used for ingestion.
- `SENTRY_IGNORED_ERRORS`: A list of strings with exceptions types to ignore, e.g: `['AuthFailedError']`.
- `SENTRY_ENVIRONMENT`: The sentry environment. Defaults to `production`.
- `SENTRY_EXTRA_ARGS`: A dictionary with extra arguments for the sentry SDK. e.g:

```yaml
SENTRY_EXTRA_ARGS:
  traces_sample_rate: 1.0
  profiles_sample_rate: 0.0
```

### Recommendations

On production we recommend adjusting both `traces_sample_rate` and `profiles_sample_rate` as those
can impact performance. See the [sentry configuration options](https://docs.sentry.io/platforms/python/configuration/options/) for more information


### License

This software is licensed under the terms of the AGPLv3.
