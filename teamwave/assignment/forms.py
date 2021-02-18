from django import forms

class ItemListForm(forms.Form):
    BOOL_CHOICES    =   ((True, True), (False, False), (None, ''))
    ORDER_CHOICES   =   (('desc','desc'), ('asc','asc'))
    SORT_CHOICES    =   (('activity','activity'),('votes','votes'),('creation','creation'),('relevance','relevance'))

    page        = forms.IntegerField(widget=forms.TextInput, required=False)
    page_size   = forms.IntegerField(widget=forms.TextInput, required=False)
    accepted    = forms.ChoiceField(widget=forms.Select(), choices=BOOL_CHOICES, initial='', required=False)
    wiki        = forms.ChoiceField(widget=forms.Select(), choices=BOOL_CHOICES, initial='', required=False)
    closed      = forms.ChoiceField(widget=forms.Select(), choices=BOOL_CHOICES, initial='', required=False)
    migrated    = forms.ChoiceField(widget=forms.Select(), choices=BOOL_CHOICES, initial='', required=False)
    notice      = forms.ChoiceField(widget=forms.Select(), choices=BOOL_CHOICES, initial='', required=False)
    order       = forms.ChoiceField(widget=forms.Select(), choices=ORDER_CHOICES, required=False)
    sort        = forms.ChoiceField(widget=forms.Select(), choices=SORT_CHOICES, required=False)
    fromdate    = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    todate      = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    min         = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    max         = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    q           = forms.IntegerField(widget=forms.TextInput, required=False)
    answers     = forms.IntegerField(widget=forms.TextInput, required=False)
    body        = forms.IntegerField(widget=forms.TextInput, required=False)
    nottagged   = forms.IntegerField(widget=forms.TextInput, required=False)
    tagged      = forms.IntegerField(widget=forms.TextInput, required=False)
    title       = forms.IntegerField(widget=forms.TextInput, required=False)
    user        = forms.IntegerField(widget=forms.TextInput, required=False)
    url         = forms.URLField(required=False)
    views       = forms.IntegerField(widget=forms.TextInput, required=False)

    