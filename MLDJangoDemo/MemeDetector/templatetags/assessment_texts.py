from django import template

register = template.Library()

#Ideally this would go in a model to make editing in production easier
#The texts are short and rarely ever will change so this is a good enough solution


CONST_TEXTS = {
    85: 'Definitely a meme!',
    70: 'This is most likely a meme.',
    50: 'This seems to be a meme.',
    40: 'This doesn\'t seem to be a meme.',
    20: 'This doesn\'t seem to be a meme.',
    0: 'Definitely not a meme!'
}


@register.filter
def textbyscore(score):
    if score >= 85:
        return CONST_TEXTS[85]
    elif score > 70:
        return CONST_TEXTS[70]
    elif score > 50:
        return CONST_TEXTS[50]
    elif score > 40:
        return CONST_TEXTS[40]
    elif score > 20:
        return CONST_TEXTS[20]
    else:
        return CONST_TEXTS[0]
