def default_character(request):
  if not request.user.is_anonymous() and request.user.is_authenticated:
    c = request.user.character_set.get(is_default=True)
    return {'default_character': c}
  else:
    return {}
