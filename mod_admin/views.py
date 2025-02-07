from . import admin
@admin.route('/')
def admin_index():
    return "hello admin "