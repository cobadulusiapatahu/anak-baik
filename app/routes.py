import os
from flask import render_template, request, redirect, url_for, current_app
from werkzeug.utils import secure_filename
from app import db
from app.models import Kid, Task, Reward

from flask import Blueprint

bp = Blueprint('main', __name__)


@bp.route('/')
def dashboard():
    kids = Kid.query.all()
    return render_template('dashboard.html', kids=kids)


@bp.route('/kid/<int:kid_id>')
def kid_profile(kid_id):
    kid = db.get_or_404(Kid, kid_id)
    tasks = Task.query.all()
    rewards = Reward.query.all()
    return render_template('kid_profile.html', kid=kid, tasks=tasks, rewards=rewards)


@bp.route('/add_points/<int:kid_id>/<int:task_id>', methods=['POST'])
def add_points(kid_id, task_id):
    kid = db.get_or_404(Kid, kid_id)
    task = db.get_or_404(Task, task_id)
    kid.points += task.points
    db.session.commit()
    return redirect(url_for('main.kid_profile', kid_id=kid_id))


@bp.route('/redeem_reward/<int:kid_id>/<int:reward_id>', methods=['POST'])
def redeem_reward(kid_id, reward_id):
    kid = db.get_or_404(Kid, kid_id)
    reward = db.get_or_404(Reward, reward_id)
    if kid.points >= reward.cost:
        kid.points -= reward.cost
        db.session.commit()
    return redirect(url_for('main.kid_profile', kid_id=kid_id))


@bp.route('/add_kid', methods=['GET', 'POST'])
def add_kid():
    if request.method == 'POST':
        name = request.form['name']
        photo = request.files['photo']
        if photo:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(
                current_app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = 'default_kid.svg'
        new_kid = Kid(name=name, photo=filename)
        db.session.add(new_kid)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('add_kid.html')
