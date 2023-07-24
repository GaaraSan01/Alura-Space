from django import forms

class LoginForm(forms.Form):
    user_login = forms.CharField(
        label= 'Digite o seu usuário...',
        required=True,
        max_length=30,
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Vinicius H.'
            }
        )
    )
    user_password = forms.CharField(
        label= 'Digite sua senha...',
        required=True,
        max_length=30,
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha...'
            }
        )
    )


class CadatroForm(forms.Form):
    user_name = forms.CharField(
        label='Digite seu nome:',
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Vinicius H.'
            }
        )
    )
    user_email = forms.EmailField(
        label='Digite seu e-mail...',
        required=True,
        max_length=30,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.:  viniciush@gmail.com'
            }
        )
    )
    user_password = forms.CharField(
        label='Digite sua senha:',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digitar senha...'
            }
        )
    )
    user_confirm_password = forms.CharField(
        label='Confirme sua senha:',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar senha...'
            }
        )
    )
    def clean_user_name(self):
        nome = self.cleaned_data.get('user_name')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não é possivel inserir espaços dentro do campo usuário!')   
            else:
                return nome
    def clean_user_confirm_password(self):
        senha_1 = self.cleaned_data.get('user_password')
        senha_2 = self.cleaned_data.get('user_confirm_password')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas não coinscidem')
            else: 
                return senha_2