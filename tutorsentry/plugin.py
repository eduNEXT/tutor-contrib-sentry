from __future__ import annotations

import os
from glob import glob

import importlib_resources
from tutor import hooks

from .__about__ import __version__

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        ("SENTRY_VERSION", __version__),
        ("SENTRY_DSN", ""),
        # The setting SENTRY_IGNORED_ERRORS is a list of rules that defines which exceptions to ignore.
        # An example below:
        # SENTRY_IGNORED_ERRORS = ['AuthFailedError']
        # Every rule support only 2 keys for now:
        ("SENTRY_IGNORED_ERRORS", []),
        ("SENTRY_ENVIRONMENT", "production"),
        # Extra initialization options for sentry
        ("SENTRY_EXTRA_ARGS", {"traces_sample_rate": 0.0, "profiles_sample_rate": 0.0}),
    ]
)

hooks.Filters.ENV_TEMPLATE_ROOTS.add_items(
    # Root paths for template files, relative to the project root.
    [
        str(importlib_resources.files("tutorsentry") / "templates"),
    ]
)

for path in glob(str(importlib_resources.files("tutorsentry") / "patches" / "*")):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))
