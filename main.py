import click

@click.command()
@click.option('--num', default=1, help='Number of servers that need to be in the simulation')
def take_input(num):
    print(num)

if __name__ == '__main__':
    take_input()

