from dataclasses import fields
from django.forms import ModelForm
from app.models import User


class Util:
    @staticmethod
    def update_attrs(visible_field) -> None:
        visible_field.field.widget.attrs["class"] = "form-control db-form"
        visible_field.field.widget.attrs["placeholder"] = f"Enter {visible_field.label.lower()}"


class AddUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__( *args, **kwargs)
        for visible_field in self.visible_fields():
            Util.update_attrs(visible_field)
    
    class Meta:
        model = User
        fields = ["username", "email", "location", "gender"]


class UpdateUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            Util.update_attrs(visible_field)
    
    class Meta:
        model = User
        fields = ["username", "email", "location"]
