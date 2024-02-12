from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        label = " Author",
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control mb-2",
                "placeholder": "Your Name"
            }
        )
    )

    content = forms.CharField(
        label = "Content",
        widget = forms.Textarea(
            attrs = {
                "class": "form-control mb-4",
                "placeholder": "Leave a comment!"
            }
        )
    )
    