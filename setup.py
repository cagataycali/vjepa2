# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup, find_packages

NAME = "vjepa2"
VERSION = "0.0.2"
DESCRIPTION = "PyTorch code and models for V-JEPA 2 (community fork with MPS, ST-A², bugfixes)."
URL = "https://github.com/cagataycali/vjepa2"


def get_requirements():
    with open("./requirements.txt") as reqsf:
        reqs = [r.strip() for r in reqsf.readlines() if r.strip() and not r.startswith("#")]
    return reqs


if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        url=URL,
        python_requires=">=3.10",
        install_requires=get_requirements(),
        packages=find_packages(exclude=["notebooks", "scripts", "configs"]),
        package_dir={"vjepa2": "."},
        include_package_data=True,
    )
