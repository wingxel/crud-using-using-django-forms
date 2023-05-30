from django.forms import ModelForm
from app.models import User


class AddUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__( *args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs["class"] = "form-control"
            visible_field.field.widget.attrs["placeholder"] = f"Enter {visible_field.label.lower()}"
    
    class Meta:
        model = User
        fields = ["username", "email", "location", "gender"]
