from django.core.exceptions import ObjectDoesNotExist

def default_character(request):
  if not request.user.is_anonymous() and request.user.is_authenticated:
    try:
      c = request.user.character_set.get(is_default=True)
    except ObjectDoesNotExist:
      c = None

    return {'default_character': c}
  else:
    return {}
