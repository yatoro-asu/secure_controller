# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard


def main() -> None:
    passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)
    total_count = passcards.count()
    active_count = active_passcards.count()

    print('Все карточки пропусков:')
    print(passcards)
    print('\nВсе действующие карточки:')
    print(active_passcards)
    print('\nСтатистика:')
    print(f'Всего пропусков {total_count}')
    print(f'Активных пропусков {active_count}')

    if total_count:
        first_passcard = passcards[0]
        print('\nПример одного пропуска:')
        print(f'owner_name: {first_passcard.owner_name}')
        print(f'passcode: {first_passcard.passcode}')
        print(f'created_at: {first_passcard.created_at}')
        print(f'is_active: {first_passcard.is_active}')
    else:
        print('\nВ базе нет ни одного пропуска.')


if __name__ == '__main__':
    main()
