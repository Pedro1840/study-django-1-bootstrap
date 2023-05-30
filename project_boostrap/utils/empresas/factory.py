from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_recipe():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'created_at': fake.date_time(),
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/brazil,rio' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())