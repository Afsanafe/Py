import click

@click.command() # what does this decorator do
def cli():
    click.echo('Hello, world!')