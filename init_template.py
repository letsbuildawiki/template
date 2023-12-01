"""Update the template with the project information."""

import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Self


@dataclass
class Folder:
    """Folder."""

    label: str
    directory: str

    def to_formatted_str(self: Self) -> str:
        """Return a formatted string."""
        return f"{{label: '{self.label}',autogenerate: {{ directory: '{self.directory}' }}}}"


@dataclass
class Project:
    """Project."""

    pretty_name: str
    repo_name: str
    folders: list[Folder]

    @classmethod
    def from_dict(cls: type[Self], data: dict) -> Self:
        """Create a project from a dictionary."""
        return cls(
            pretty_name=data["project"]["pretty_name"],
            repo_name=data["project"]["repo_name"],
            folders=[Folder(**folder) for folder in data["project"]["folders"]],
        )


def run() -> None:
    """Update the template with the project information."""
    project = Project.from_dict(tomllib.loads(Path("config.toml").read_text()))
    astro_config_text = Path("astro.config.mjs").read_text()
    astro_config_text = astro_config_text.replace("template", project.repo_name)
    astro_config_text = astro_config_text.replace("TEMPLATE", project.pretty_name)
    astro_config_text = astro_config_text.replace(
        "// sidebar-items",
        ",".join(folder.to_formatted_str() for folder in project.folders),
    )
    Path("astro.config.mjs").write_text(astro_config_text)


if __name__ == "__main__":
    run()
