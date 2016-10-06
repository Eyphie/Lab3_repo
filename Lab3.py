from UserId import IdFromUsername
from Friends import Friends

user = IdFromUsername('id3668084')
user_id = user.execute()

friends_client = Friends(user_id)
friends = friends_client.execute()

for (age, count) in friends:
    print('{} {}'.format(int(age), '#' * count))
