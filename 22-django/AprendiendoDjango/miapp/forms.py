from django import forms

from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Titulo",
        max_length=40,
        required=False,
        widget = forms.TextInput(
            attrs={
                'placeholder':'titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$','El título solo lleva letras y números')
        ]

    )


    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea
    )

    content.widget.attrs.update({
        'placeholder':'titulo',
        'class': 'contenido_form_article',
        'id':'contenido_form'
    })

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = '¿Publicado?',
        choices = public_options
    )