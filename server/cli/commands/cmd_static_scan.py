import subprocess
import click

@click.command()
def cli():
    """
    Run a static scan of the python code base inside the 'app' directory.
    :return: Subprocess call result
    """
    cmd = 'bandit -r -x __pycache__ app/'
    return subprocess.call(cmd, shell=True)
