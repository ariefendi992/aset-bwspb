from django import forms
from .models import TanggulSungaiModel, FotoTanggulSungaiModel


class TanggulSungaiForm(forms.ModelForm):
    class Meta:
        model = TanggulSungaiModel
        fields = "__all__"
        labels = {
            "latitude": "lat1",
            "longitude": "long1",
            "latitude2": "lat2",
            "longitude2": "long2",
        }
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


class FotoTanggulSungaiForm(forms.ModelForm):
    class Meta:
        model = FotoTanggulSungaiModel
        fields = ["image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
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

    def cleaned_file(self):
        file = self.cleaned_data["file"]

        if not file.name.endswith(".xlsx"):
            raise forms.ValidationError("File harus format .xlsx")
        return file
