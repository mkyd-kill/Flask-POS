from flask import Blueprint, render_template

error = Blueprint('errors', __name__)

# Bad Request
@error.app_errorhandler(400)
def page_not_found(e):
    return render_template("errors/400.html"), 400

# Unauthorized access
@error.app_errorhandler(401)
def page_not_found(e):
    return render_template('errors/401.html'), 401

# Forbidden URL only admin accessible
@error.app_errorhandler(403)
def page_not_found(e):
    return render_template("errors/403.html"), 403

# Invalid URL input
@error.app_errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404

# Method not allowed
@error.app_errorhandler(405)
def page_not_found(e):
    return render_template('errors/405.html'), 405

# request time out
@error.app_errorhandler(408)
def page_not_found(e):
    return render_template('errors/408.html'), 408


# Internal Server Error
@error.app_errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html'), 500

# Bad Gateway connection
@error.app_errorhandler(502)
def page_not_found(e):
    return render_template('errors/502.html'), 502

# Gateway connection timeout
@error.app_errorhandler(504)
def page_not_found(e):
    return render_template('errors/504.html'), 504