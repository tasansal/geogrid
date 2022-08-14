"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """GeoGrid."""


if __name__ == "__main__":
    main(prog_name="geogrid")  # pragma: no cover
