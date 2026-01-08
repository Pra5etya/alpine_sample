from flask import Blueprint, render_template, render_template_string
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.exceptions import HTTPException
from .data_routes import project_data

# Blueprint
main_bp = Blueprint('main', __name__)

# Limiter khusus blueprint
limiter = Limiter(get_remote_address, app=main_bp)

# =====================
# Routes
# =====================

@main_bp.route('/')
@limiter.limit("5 per minute")  # Rate limit 5 request per menit
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
    # load data
    data = project_data()
    return render_template('projects.html', projects_param=data)

# =====================
# Error handler untuk rate limit
# =====================
@main_bp.errorhandler(429)
def ratelimit_handler(e):
    # Bisa kembalikan template custom
    return render_template('429.html', error=e.description), 429
