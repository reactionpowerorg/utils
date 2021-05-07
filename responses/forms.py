from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Responses


class responses(forms.Form):
    CHOICES = [('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5'), ]
    # your_name = forms.CharField(label='Your name', max_length=100)
    goal = forms.CharField(label='What is your top goal for the next month?', max_length=300)
    highlights = forms.CharField(label="What's new, good, or most improved for you last month?",
                                 max_length=300)
    lowlights = forms.CharField(label="What is your biggest obstacle?", max_length=300)
    wload = forms.CharField(label="How was your work load last month? (overburdened, satisfactory, underworked)",
                            max_length=300)
    goal_obst = forms.CharField(label="In one word, what’s standing in between you and your biggest goal?",
                                max_length=300)
    m_tip = forms.CharField(label="Monthly Tip: What do you think we should do better/improve on?", max_length=300)
    rating = forms.ChoiceField(label="On a scale of 1-5, what is your morale?", choices=CHOICES,
                               widget=forms.RadioSelect)


class Responses_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Responses_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = Responses
        exclude = ('id', 'employee',)

