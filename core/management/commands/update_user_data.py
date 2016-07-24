from django.core.management.base import BaseCommand
from core import models
from github import Github



class Command(BaseCommand):
    help = "Updating git users data."

    def handle(self, *args, **options):
        g = Github(client_id='f9c6481ee856e215c0a0',
           client_secret='3d066e249bfe454bb30ca9102945d1cf247e6110')
        for i in models.GitUser.username:
            events = g.get_user(i).get_events()
            commits = 0

            to_delete = models.Data.objects.filter(gitUser=models.GitUser.objects.filter(username=i))
            if to_delete.count() != 0:
                for row in to_delete:
                    row.delete()

            git_record = models.GitUser.objects.filter(username=i)[0]

            for event in events:
                if event.type == "PushEvent":
                    commits += 1
                    record = models.Data(gitUser=git_record, event_type="Commit",
                        created_at=event.created_at, repository=event.repo.name,
                        description=event.payload['commits'][0]['message'])
                    record.full_clean()
                    record.save()
                if commits == 50:
                    break
