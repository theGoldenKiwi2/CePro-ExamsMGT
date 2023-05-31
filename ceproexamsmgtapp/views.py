from flask_admin.contrib.appengine import ModelView


class UserView(ModelView):
    column_filters = ['email']
    column_searchable_list = ('email', 'password')
