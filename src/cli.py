import click

from simple_day.model import SimpleHabit


@click.command()
def create_scheme():
    SimpleHabit().create_table(read_capacity_units=1, write_capacity_units=1)


if __name__ == '__main__':
    create_scheme()
