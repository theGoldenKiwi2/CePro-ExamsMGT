from flask_admin.contrib.sqla import ModelView

class UserView(ModelView):
    column_filters = ['email']
    column_searchable_list = ('email', 'password')
