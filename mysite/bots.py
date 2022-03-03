import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
import django
django.setup()
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from users.models import AuthUser
from posts.models import Post, Vote
import json
import asyncio
from faker import Faker
from random import randint, choice

fake = Faker()

with open('citate.json', 'r') as json_file:
    citate = json.load(json_file)



max_users = AuthUser.objects.count()
max_posts = Post.objects.count()


async def create_post():
    while True:
        global max_posts
        # await asyncio.sleep(randint(20,60))
        await asyncio.sleep(randint(2, 10))
        quote = citate[randint(0, len(citate)-1)]
        creator = AuthUser.objects.get(id=randint(1, max_users))
        post = Post(author=quote['autor'], text=quote['text'], creator=creator)
        post.save()
        max_posts = post.id
        print(f'create_post: {post}')


async def apply_vote():
    while True:
        await asyncio.sleep(randint(2, 5))
        post_id = randint(1, max_posts)
        vote = choice((-1, 1, 1, 1))
        user = AuthUser.objects.get(id=randint(3, max_users))
        old_vote = 0
        try:
            old_vote = Vote.objects.get(user=user, post_id=post_id).vote
        except ObjectDoesNotExist:
            pass
        print(f'vote: {post_id} > {vote}', end='')
        if old_vote > -1 and old_vote < 1:
            Vote.objects.update_or_create(user=user, post_id=post_id, defaults={
                'vote': old_vote + vote
            })
            Post.objects.filter(pk=post_id).update(votes=F("votes")+vote)
            print(' ... success')
        else:
            print(f' ... can not vote {vote}')


async def create_user():
    while True:
        global max_users
        # await asyncio.sleep(randint(180,360))
        await asyncio.sleep(randint(5, 10))
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f'{first_name.lower()}.{last_name.lower()}@{fake.domain_name()}'
        user_name = f'{first_name.lower()}{randint(70,99)}'
        user = AuthUser(username=user_name, email=email,
                        first_name=first_name, last_name=last_name)
        user.save()
        max_users = AuthUser.objects.count()
        print(f'create user: {user}')

loop = asyncio.get_event_loop()
tasks = asyncio.gather(
    # loop.create_task(create_user()),
    # loop.create_task(create_post()),
    loop.create_task(apply_vote())
)
loop.run_forever()

