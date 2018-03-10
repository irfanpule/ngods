def path_file_save(session_key, count=0):
    return f"tmp/{session_key}-{count}.ods"


def get_session_key(request):
    if not request.session.session_key:
        request.session.save()
    return request.session.session_key