from .forms import UserLoginForm, UserRegisterForm

def login_form(request):
    login_form = UserLoginForm()
    signup_form = UserRegisterForm()
    return {
        'loginForm': login_form,
        'signupForm': signup_form
    }