from flask import (Blueprint, send_from_directory, abort)

from .helper_file import (
    is_trusted_referer,
    is_allowed_file,
    is_safe_path,
    ALLOWED_IMAGE_EXTENSIONS,
)

file_bp = Blueprint('file', __name__)

# ✅ Route: images
@file_bp.route('/images/<path:filename>')
def protected_image(filename):
    print(f"\n[Assets] Filename requested: {filename}")

    if not (is_safe_path(filename) and is_allowed_file(filename, ALLOWED_IMAGE_EXTENSIONS)):
        abort(403)

    if not is_trusted_referer():
        abort(403)

    return send_from_directory('private/images', filename)
