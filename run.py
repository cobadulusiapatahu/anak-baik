from flask.cli import with_appcontext
from app import create_app, db
from app.models import Task, Reward, Kid
import click

app = create_app()


def populate_sample_data():
    # Sample tasks
    tasks = [
        Task(name="Brush teeth", points=5, icon="brush_teeth.svg"),
        Task(name="Make bed", points=10, icon="make_bed.svg"),
        Task(name="Do homework", points=20, icon="homework.svg")
    ]

    # Sample rewards
    rewards = [
        Reward(name="30 min screen time", cost=50, icon="screen_time.svg"),
        Reward(name="Choose dinner", cost=100, icon="dinner.svg"),
        Reward(name="New toy", cost=500, icon="toy.svg")
    ]

    db.session.bulk_save_objects(tasks + rewards)
    db.session.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    db.drop_all()
    db.create_all()
    populate_sample_data()
    click.echo('Initialized the database.')


app.cli.add_command(init_db_command)

if __name__ == '__main__':
    app.run(debug=True)
