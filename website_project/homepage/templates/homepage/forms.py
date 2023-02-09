'''from django import forms

class UserLoginForm(forms.Form):
    email = forms.EmailField(
     widget=forms.EmailField(
         attrs={
             'id':'LoginEmail',
             'type':'email',
             'class':'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id':'loginPassword',
                'type':'password',
                'class':'form-control'
            }
        )
    )
 
    
class UserRegisterForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id':'signupEmail',
                'type':'email',
                'class':'form-control'
                }
            )
    )
    
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'class':'form-control'
                }
            )
    )
    
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'class':'form-control'
                }
            )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs= {
                'id':'signupPassword',
                'type':'password',
                'class':'form-control'
            }
        )
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'class':'form-control'
                }
            )
    )
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']
'''
'''
VIEWS
# REGISTER USER
def registrarUsuario(request):
    signup_form = UserRegisterForm(request.POST or None)
    if signup_form.is_valid():
        email = signup_form.cleaned_data.get('email')
        first_name = signup_form.cleaned_data.get('first_name')
        last_name = signup_form.cleaned_data.get('last_name')
        password = signup_form.cleaned_data.get('password')
        try:
            user = get_user_model().objects.create(
                email = email,
                first_name = first_name,
                last_name = last_name,
                password = make_password(password),
                is_active = True
            )
            login(request, user)
            return redirect('/')
        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})

def iniciarSesión(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, email-email, password-password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente')
            return redirect('/')
        else:
            messages.warning(request, 'Correo electronico o contraseña invalida')    
        return render(request, '/')
'''
