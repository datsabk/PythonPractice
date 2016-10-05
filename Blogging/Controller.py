import web
from Model import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = [
    '/', 'home',
    '/register', 'register',
    '/postregistration', 'PostRegistration',
    '/login', 'Login',
    '/checklogin', 'Checklogin',
    '/Logout', 'Logout',
    '/post-activity', 'PostActivity'
]

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={"user": None})

session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout",globals={'session':session_data, 'current_user': session_data["user"]})


class home:
    def GET(self):
        posts_model = Posts.Posts()
        posts = posts_model.get_all_posts()

        return render.Home(posts)


class register:
    def GET(self):
        return render.Register()

class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


class Login:
    def GET(self):
        return render.Login()


class Checklogin:
    def POST(self):
        data = web.input()
        login_model =LoginModel.LoginModel()
        res = login_model.check_user(data)
        if res:
            session_data["user"]= res

        print(res)
        return res


class Logout:
    def GET(self):
        session['user']=None
        session_data['user']=None
        session.kill()
        return render.Login()


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']
        post_model = Posts.Posts()
        post_model.insert_post(data)
        return render.Home()


if __name__ == "__main__":
    app.run()
