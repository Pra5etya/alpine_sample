from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    key_func=get_remote_address,           # gunakan IP user
    default_limits=["100 per hour"],       # limit default semua route
    strategy="moving-window",              # hitungan sliding window
    storage_uri="memory://",               # simpan hitungan di memory
    headers_enabled=True                   # kirim header X-RateLimit
)

def create_app():
    # =================
    # 0. core
    # =================

    core = Flask(__name__, static_folder='static', template_folder='templates')
    limiter.init_app(core)

    # =================
    # 1. routes
    # =================
    from app.routes import register_routes
    register_routes(core)

    return core