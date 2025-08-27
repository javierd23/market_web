from django import forms

plan_select = [
    ("pb", "Plan básico"),
    ("pe", "Plan esencial"),
    ("pi", "Plan intermedio"),
    ("pa", "Plan avanzado"),
    ("pp", "Plan premium"),
    ("pu", "Plan ultra"),
]

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={
            "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
        })
    )
    phone = forms.CharField(
        label="Teléfono",
        widget=forms.TextInput(attrs={
            "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
        })
    )
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
        })
    )
    plan = forms.ChoiceField(
        label="Plan",
        choices=plan_select,
        widget=forms.Select(attrs={
            "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none bg-white"
        })
    )
    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            "rows": 4,
            "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
        })
    )