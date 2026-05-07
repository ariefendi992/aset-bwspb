from django import forms
from .models import DataAbsahModel


class AbsahForm(forms.ModelForm):
    class Meta:
        model = DataAbsahModel
        fields = "__all__"
        # widgets = {
        #     "latitude": forms.TextInput(attrs={"type": "text"}),
        #     "longitude": forms.TextInput(attrs={"type": "text"}),
        # }
        exclude = ["created_by", "updated_by"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            css_class = ""
            if isinstance(field.widget, forms.Select):
                css_class = "form-select"
            elif isinstance(field.widget, forms.CheckboxInput):
                css_class = "form-check-input"
            else:
                css_class = "form-control"

            if self.is_bound:
                if self.errors.get(name):
                    css_class += " is-invalid"
                else:
                    css_class += " is-valid"

            field.widget.attrs.update({"class": css_class})


class UploadExcelForm(forms.Form):
    file = forms.FileField(
        label="Pilih File",
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control", "accept": ".xlsx"}
        ),
    )
    # widgets = {
    #     "file": forms.TextInput(attrs={"class": "form-control", "accept": ".xlsx"})
    # }

    def cleaned_file(self):
        file = self.cleaned_data["file"]

        if not file.name.endswith(".xlsx"):
            raise forms.ValidationError("File harus format .xlsx")
        return file
