import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog_orm.settings")
django.setup()

from home.models import Post,Coment


# post1 = Post(
#     name='hello',
#     content='vadym was here',
#     )
# post1.save()

# coment1 = Coment(
#     content ='hello',
#     post = post1
# )

# coment1.save()

post = Post.objects.get(id=1)
post.content = 'edited text'
post.save()
