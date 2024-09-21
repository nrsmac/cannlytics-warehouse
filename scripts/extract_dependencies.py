import sys
from pathlib import Path
import argparse

def load_toml(file_path: str) -> dict:
    """Load a TOML file and return the data as a dictionary."""
    import tomllib
    with open(file_path, "rb") as f:
        return tomllib.load(f)

def extract_dependencies(toml_data, group: str | None = None) -> dict:
    """Extract dependencies from a pyproject.toml file."""
    if group is None:
        dependencies = toml_data.get('tool', {}).get('poetry', {}).get('dependencies')
    else:
        dependencies = toml_data.get('tool', {}).get('poetry').get('group').get(group).get('dependencies')
        if not dependencies:
            raise ValueError(f"Group {group} not found")

    return dependencies

def generate_requirements(dependencies: dict) -> str:
    """Generate a requirements.txt file from a dictionary of dependencies."""
    requirements = []
    for name, spec in dependencies.items():
        requirements.append(f"{name}=={spec.replace('^','')}")
    
    return "\n".join(requirements)

def main(pyproject_file, group: str | None = None) -> None:
    """Load a pyproject.toml file and print the dependencies by group."""
    toml_data = load_toml(pyproject_file)
    deps = extract_dependencies(toml_data, group=group)
    print(generate_requirements(deps))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract dependencies from a pyproject.toml file.")
    parser.add_argument("group", nargs="?", default=None, help="The dependency group to extract (default: dependencies)")
    parser.add_argument("pyproject_file", nargs="?", default="./pyproject.toml", help="Path to the pyproject.toml file (default: ./pyproject.toml)")
    
    args = parser.parse_args()
    main(args.pyproject_file, args.group)