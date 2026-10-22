"""Environment report used in Lab 1 and in every project README."""
import platform
from importlib import metadata

PACKAGES = ("numpy", "pandas", "matplotlib", "scikit-learn", "biopython", "pytest")


def package_version(name: str) -> str | None:
    """Return the installed version of a package, or None if it is missing."""
    raise NotImplementedError("TODO: implement package_version")


def check_environment(packages: tuple[str, ...] = PACKAGES) -> dict:
    """Return the Python version, operating system and package versions."""
    raise NotImplementedError("TODO: implement check_environment")


if __name__ == "__main__":
    report = check_environment()
    print("Python:", report["python"], "on", report["platform"])
    for name, version in report["packages"].items():
        print(f"  {name:<14} {version or 'NOT INSTALLED'}")
