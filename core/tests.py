import datetime
from django.test import TestCase
from core.models import *
from github import Github


class CoreModelsTest(TestCase):

    # def test_create_git_user(self):
    #     # user = User.objects.create_user("litel")
    #     n = 10
    #     for i in range(n):
    #         gu = GitUser(
    #         username="git user {}".format(i),
    #         email="userMail{}@mail.col".format(i),
    #         )
    #         gu.full_clean()
    #         gu.save()
    #
    #     print("test_create_git_user - OK")
    #
    #     self.assertEquals(GitUser.objects.count(), n)

    # def test_create_group(self):
    #     g1 = Group(
    #     name="group1 name",
    #     admin="Myself",
    #     created_at="2016-06-30",
    #     )
    #     g1.full_clean()
    #     g1.save()
    #
    #     g2 = Group(
    #     name="group2 name",
    #     admin="Myself",
    #     created_at="2016-06-30",
    #     )
    #     g2.full_clean()
    #     g2.save()
    #
    #     g3 = Group(
    #     name="group name",
    #     admin="Myself",
    #     created_at="2016-06-30",
    #     )
    #     g3.full_clean()
    #     g3.save()
    #
    #     gu1 = g1.git_users.create(username="git user 1", email="userMail@mail.col")
    #     gu1.full_clean()
    #     gu1.save()
    #
    #     g2.git_users.add(gu1)
    #     g2.full_clean()
    #     g2.save()
    #
    #     g3.git_users.add(gu1)
    #     g3.full_clean()
    #     g3.save()
    #
    #     gu2 = g1.git_users.create(username="git user 2", email="userMail@mail.col")
    #     gu2.full_clean()
    #     gu2.save()
    #
    #     g2.git_users.add(gu2)
    #     g2.full_clean()
    #     g2.save()
    #
    #     print(Group.objects.count())
    #     print(GitUser.objects.count())
    #
    #     print("test_create_group - OK2")
    #
    #     self.assertEquals(Group.objects.count(), 3)
    #     self.assertEquals(GitUser.objects.count(), 2)

    # def test_create_data(self):
    #     g = Github(client_id='f9c6481ee856e215c0a0',
    #                client_secret='3d066e249bfe454bb30ca9102945d1cf247e6110')
    #     events = g.get_user("litelx").get_events()
    #     i = 0
    #     git_record = GitUser(username="litelx", email='joli@gmail.com')
    #     git_record.full_clean()
    #     git_record.save()
    #
    #     y = GitUser.objects.filter(username="litelx")
    #     for event in events:
    #         if event.type == "PushEvent":
    #             i += 1
    #             record = Data(gitUser=y[0], event_type="Commit",
    #                           created_at=event.created_at, repository=event.repo.name,
    #                           description=event.payload['commits'][0]['message'])
    #             record.full_clean()
    #             record.save()
    #         if i == 50:
    #             break
    #     print("total = ", Data.objects.count())
    #
    #
    # def test_delete_data(self):
    #     g = Github(client_id='f9c6481ee856e215c0a0', client_secret='3d066e249bfe454bb30ca9102945d1cf247e6110')
    #     user_nm1 = "litelx"
    #     user_nm2 = "nonzero"
    #     events = g.get_user(user_nm1).get_events()
    #     i = 0
    #     git_record = GitUser(username=user_nm1, email='joli@gmail.com')
    #     git_record.full_clean()
    #     git_record.save()
    #
    #     git_record2 = GitUser(username=user_nm2, email='joli@gmail.com')
    #     git_record2.full_clean()
    #     git_record2.save()
    #
    #     git_record3 = GitUser(username="miacaplan", email='joli@gmail.com')
    #     git_record3.full_clean()
    #     git_record3.save()
    #
    #     for event in events:
    #         if event.type == "PushEvent":
    #             i += 1
    #             record = Data(gitUser=GitUser.objects.filter(username=user_nm1)[0], event_type="Commit", created_at=event.created_at, repository=event.repo.name, description=event.payload['commits'][0]['message'])
    #             record.full_clean()
    #             record.save()
    #             record = Data(gitUser=GitUser.objects.filter(username=user_nm2)[0], event_type="Commit", created_at=event.created_at, repository=event.repo.name, description=event.payload['commits'][0]['message'])
    #             record.full_clean()
    #             record.save()
    #             record = Data(gitUser=GitUser.objects.filter(username="miacaplan")[0], event_type="Commit", created_at=event.created_at, repository=event.repo.name, description=event.payload['commits'][0]['message'])
    #             record.full_clean()
    #             record.save()
    #         if i == 50:
    #             break
    #
    #     fr = []
    #     r = Data.objects.filter(gitUser=git_record)
    #     r2 = Data.objects.filter(gitUser=git_record2)
    #     r3 = Data.objects.filter(gitUser=git_record3)
    #     print(r.count())
    #     fr = r | r2
    #     fr |= r3
    #     print(fr.count())
    #
    #     '''
    #         r2 = Data.objects.filter((Q(gitUser=users[0]) | Q(gitUser=users[1]))
    #         we got up to 50 data rows in database
    #     '''
    #     to_delete = Data.objects.filter(gitUser=GitUser.objects.filter(username="pp"))
    #     for row in to_delete:
    #         row.delete()
    #
    def test_db(self):
        g1 = Group(
            name="group1 name",
            admin="Myself",
            created_at="2016-06-30",
        )
        g1.full_clean()
        g1.save()

        g2 = Group(
            name="group2 name",
            admin="Myself",
            created_at="2016-06-30",
        )
        g2.full_clean()
        g2.save()

        gu1 = g1.git_users.create(username="litelx", email="userMail@mail.col")
        gu1.full_clean()
        gu1.save()

        gu2 = g1.git_users.create(username="nonzero", email="userMail@mail.col")
        gu2.full_clean()
        gu2.save()

        gu3 = g2.git_users.create(username="miakaplan", email="userMail@mail.col")
        gu3.full_clean()
        gu3.save()


