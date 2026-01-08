from flask import Blueprint, render_template, render_template_string
from .data_routes import project_data
from .. import limiter  # ambil limiter dari app/__init__.py

# Blueprint
main_bp = Blueprint('main', __name__)

# =====================
# Routes
# =====================

@main_bp.route('/')
@limiter.limit("2 per 20 seconds")  # limit cepat untuk testing
def home():
    html = """
    <h1>Flask + Alpine.js Demo</h1>
    <ul>
        <li><a href='/counter'>Counter</a></li>
        <li><a href='/form'>Form Greeting</a></li>
        <li><a href='/cart'>Shopping Cart</a></li>
        <li><a href='/projects'>Project</a></li>
    </ul>
    """
    return render_template_string(html)

@main_bp.route('/counter')
def counter():
    return render_template('counter.html')

@main_bp.route('/form')
def form():
    return render_template('form.html')

@main_bp.route('/cart')
def cart():
    return render_template('cart.html')

@main_bp.route('/projects')
def projects():
    data = project_data()
    return render_template('projects.html', projects_param=data)

# =====================
# Error handler untuk rate limit
# =====================
@main_bp.errorhandler(429)
def ratelimit_handler(e):
    return render_template('429.html'), 429
