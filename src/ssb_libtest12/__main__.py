"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """SSB Libtest12."""


if __name__ == "__main__":
    main(prog_name="ssb-libtest12")  # pragma: no cover
