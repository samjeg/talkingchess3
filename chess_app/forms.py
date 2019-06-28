from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ChessboardComment, Chessboard, UserProfileInfo


class UserCreateForm(UserCreationForm):

	class Meta:
		fields = ("username", "password1", "password2")
		model = get_user_model()

	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		self.fields["username"].label = "Username:"
		self.fields["username"].help_text = None
		self.fields["password1"].help_text = None
		self.fields["password2"].help_text = None


class ChessboardCommentForm(forms.Form):
	user = forms.ModelChoiceField(widget = forms.HiddenInput(), queryset=User.objects.all())
	chessboard = forms.ModelChoiceField(widget = forms.HiddenInput(), queryset=Chessboard.objects.all())
	comment = forms.CharField()
	comment_picture_path = forms.CharField(widget = forms.HiddenInput(), required=False)

	class Meta:
		fields = ("user", "chessboard", "comment", "comment_picture_path")
		model = ChessboardComment

	def __init__(self, *args, **kwargs):
		super(ChessboardCommentForm, self).__init__(*args, **kwargs)
		self.fields['comment'].widget.attrs['class'] = 'comment-input'

class ChessboardForm(forms.Form):
	player = forms.ModelChoiceField(widget = forms.HiddenInput(), queryset=UserProfileInfo.objects.all())
	user_input_state = forms.CharField()

	class Meta:
		fields = ("player", "user_input_state")
		model = Chessboard

	def __init__(self, *args, **kwargs):
		super(ChessboardForm, self).__init__(*args, **kwargs)
		self.fields['user_input_state'].widget.attrs['id'] = 'input_state'

