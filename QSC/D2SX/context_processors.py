def leader_name_processor(request):
    if request.user.is_authenticated:
        return {'leader_name': request.user.get_full_name() or request.user.username}
    return {}
