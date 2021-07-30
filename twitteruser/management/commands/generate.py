from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
from twitteruser.models import TwitUser
from tweet.models import Tweet
import subprocess


class Command(BaseCommand):
  def handle(self, *args, **options):
    new_secret_key = get_random_secret_key()

    with open('./twitterclone/.env', 'w') as f:
      f.write(f"SECRET_KEY='{new_secret_key}'")
    with open('.gitignore', 'a') as f:
      f.write('.env')

    subprocess.run(['git', 'rm', '-r', '--cached', 'twitterclone/.env'])
    subprocess.run(['python', 'manage.py', 'migrate'])
    subprocess.run(['git', 'add', '.gitignore'])

    TwitUser.objects.bulk_create([
      TwitUser(username='RossKelly', first_name='Ross', last_name='Kelly', email='RossKelly@email.com', password='RossKelly'),
      TwitUser(username='MackJames', first_name='Mack', last_name='James', email='MackJames@email.com', password='MackJames'),
      TwitUser(username='OpalObrien', first_name='Opal', last_name='Obrien', email='OpalObrien@email.com', password='OpalObrien'),
      TwitUser(username='FrancisFrank', first_name='Francis', last_name='Frank', email='FrancisFrank@email.com', password='FrancisFrank'),
      TwitUser(username='DomingoWalsh', first_name='Domingo', last_name='Walsh', email='DomingoWalsh@email.com', password='DomingoWalsh'),
    ])
    Tweet.objects.bulk_create([
      Tweet(tweet='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam iaculis, diam a efficitur egestas, dolor.', posted_by=TwitUser.objects.get(username='RossKelly')),
      Tweet(tweet='Integer in turpis vel leo hendrerit scelerisque. Fusce mattis, augue at interdum aliquet, orci dui.', posted_by=TwitUser.objects.get(username='RossKelly')),
      Tweet(tweet='Cras id mollis dui, ut posuere risus. Aliquam tortor eros, accumsan in lacus vitae, gravida.', posted_by=TwitUser.objects.get(username='MackJames')),
      Tweet(tweet='Curabitur felis ex, finibus et convallis in, euismod eu dui. Integer eget interdum lectus. Nullam', posted_by=TwitUser.objects.get(username='MackJames')),
      Tweet(tweet='In a nunc eget massa semper lacinia. Quisque felis libero, rutrum vel molestie nec, accumsan.', posted_by=TwitUser.objects.get(username='OpalObrien')),
      Tweet(tweet='Maecenas ut libero ullamcorper, dapibus risus a, pretium quam. Praesent faucibus aliquam mauris vel vehicula', posted_by=TwitUser.objects.get(username='OpalObrien')),
      Tweet(tweet='Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec metus augue.', posted_by=TwitUser.objects.get(username='FrancisFrank')),
      Tweet(tweet='Donec ornare ipsum ex, consequat condimentum tellus egestas vitae. Nulla nunc nibh, lobortis eget mi.', posted_by=TwitUser.objects.get(username='FrancisFrank')),
      Tweet(tweet='Donec porta erat sodales, pharetra velit vel, ultricies ex. Sed quis eros et magna consectetur.', posted_by=TwitUser.objects.get(username='DomingoWalsh')),
      Tweet(tweet='Mauris efficitur odio ex. Donec sed semper metus. Fusce congue et velit ac pretium. Curabitur.', posted_by=TwitUser.objects.get(username='DomingoWalsh')),
    ])

