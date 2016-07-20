from core.models import *
from github import Github, Event, NamedUser

g = Github(client_id='f9c6481ee856e215c0a0',
           client_secret='3d066e249bfe454bb30ca9102945d1cf247e6110')


def is_git_user(username):
    try:
        u = g.get_user(username)
        if u:
            return True
    except Exception:
        return False


def add_user_data(user_name):
    events = g.get_user(user_name).get_events()
    email = g.get_user(user_name).email
    if email == "None":
        email = ""
    i = 0

    to_delete = Data.objects.filter(gitUser=GitUser.objects.filter(username=user_name))
    if to_delete.count() != 0:
        delete_user_data(user_name)

    git_user_record = GitUser.objects.filter(username=user_name)[0]
    for event in events:
        if event.type == "PushEvent":
            i += 1
            record = Data(gitUser=git_user_record, event_type="Commit",
                          created_at=event.created_at, repository=event.repo.name,
                          description=event.payload['commits'][0]['message'])
            record.full_clean()
            record.save()
        if i == 50:
            break
    return i, email


def delete_user_data(user_name):
    to_delete = Data.objects.filter(gitUser=GitUser.objects.filter(username=user_name))
    for row in to_delete:
        row.delete()
