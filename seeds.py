from app.models import User, Post, Comment, Vote
from app.db import Session, Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

db.add_all([
    User(username='alamonda1', email='vete@alv.com', password='contra123123'),
    User(username='auser2', email='some@mail.com', password='contra123123'),
    User(username='otro3', email='thisdude@fake.com', password='contra123123'),
    User(username='and4', email='elden@ring.com', password='contra123123')
])

db.commit()

db.add_all([
    Post(title='Blasrekroajsdf', post_url='something.com', user_id=1),
    Post(title='sef2efsdfa', post_url='fake.com', user_id=2),
    Post(title='LSdfowjf asodfka osdf', post_url='yes.com', user_id=3),
    Post(title='Hello There', post_url='no.com', user_id=4),
    Post(title='General Kenobi', post_url='lalala.com', user_id=2)
])

db.commit()

db.add_all([
  Comment(comment_text='Nunc rhoncus dui vel sem.', user_id=1, post_id=2),
  Comment(comment_text='Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.', user_id=1, post_id=3),
  Comment(comment_text='Aliquam erat volutpat. In congue.', user_id=2, post_id=1),
  Comment(comment_text='Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.', user_id=2, post_id=3),
  Comment(comment_text='In hac habitasse platea dictumst.', user_id=3, post_id=3)
])

db.commit()

db.add_all([
  Vote(user_id=1, post_id=2),
  Vote(user_id=1, post_id=4),
  Vote(user_id=2, post_id=4),
  Vote(user_id=3, post_id=4),
  Vote(user_id=4, post_id=2)
])
db.commit()

db.close()