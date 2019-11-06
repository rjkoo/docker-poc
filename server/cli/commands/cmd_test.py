import os
import subprocess

import click


@click.command()
@click.argument('path', default=os.path.join('app', 'tests'))
@click.option('--blueprint', default='')
def cli(path, blueprint):
    """
    Run tests with Pytest.

    :param path: Test path
    :return: Subprocess call result
    """
    bp = f"/{blueprint}"
    cmd = 'py.test {0}{1}'.format(path, bp)
    return subprocess.call(cmd, shell=True)
