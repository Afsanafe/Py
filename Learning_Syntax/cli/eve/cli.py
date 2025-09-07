import click

                # Without this decorator cli() would just be a normal python function
@click.command() # this decorator basically says “Treat the function cli as a command-line entry point.”
def cli():
    click.echo('Hello, world!')