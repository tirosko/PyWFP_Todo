import datetime
import os

import click
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile('config.py', silent=True)
    app.config.from_mapping(SECRET_KEY='dev')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///event_database.db"

    class Base(DeclarativeBase):
        pass

    db = SQLAlchemy(model_class=Base)
    db.init_app(app)

    class Event(db.Model):
        date = mapped_column(db.String, primary_key=True)
        event = mapped_column(db.String)

    @click.command('init-db')
    def init_db_command():
        """Command for initializing the database"""
        with app.app_context():
            db.create_all()
            click.echo('Database created successfully')

    app.cli.add_command(init_db_command)

    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            # use timezone-aware datetime to avoid naive datetime warning
            db.session.add(Event(date=datetime.datetime.now(tz=datetime.timezone.utc).isoformat(),
                                 event=request.form['eventBox']))
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('home.html', eventsList=db.session.execute(db.select(Event).order_by(Event.date)).scalars())

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
