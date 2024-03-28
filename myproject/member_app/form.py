from django import forms

from member_app.models import MemberModel


class MemberForm(forms.ModelForm):
    class Meta:
        model = MemberModel
        fields = ['address_member']