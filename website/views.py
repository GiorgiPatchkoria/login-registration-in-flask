from flask import Blueprint, redirect, render_template, request, flash
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods= ['POST', 'GET'])
@login_required
def home():
    return render_template('home.html', user=current_user)
