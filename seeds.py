from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

db.add_all([
    User(username='zencoh', email='zencoh@email.com', password='password123'),
    User(username='betaTester', email='btester@email.com', password='password123'),
    User(username='testUser', email='tuser@email.com', password='password123'),
    User(username='pixelPerformer', email='pperformer@email.com', password='password123'),
    User(username='enigmaEvaluator', email='eevaluator@email.com', password='password123'),
])

db.commit()

db.close()