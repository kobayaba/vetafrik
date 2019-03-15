from django.forms import ModelForm,TextInput,EmailInput
from .models import Contact
from django.forms.utils import ErrorList


class ContactForm(ModelForm):
	class Meta:
		model=Contact
		fields=['name','email']
		



class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])