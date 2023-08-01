import click


def output_info(msg):
    click.echo(click.style(msg, fg='green'))


def output_warning(msg):
    click.echo(click.style(msg, fg='yellow'))


def output_error(msg):
    click.echo(click.style(msg, fg='red'))


