from django.core.management.base import BaseCommand
from faker import Faker
from user_auth.models import User


class Command(BaseCommand):
    help = 'Create fake users using Faker'

    def add_arguments(self, parser):

        parser.add_argument(
            'num_users',
            type=int,
            nargs='?',  # Makes it optional, defaults to 1000
            default=1000,
            help='Number of users to create'
        )

    def handle(self,*args, **options):
        num_users = options['num_users']

        fake = Faker('en_IN')  # This locale will generate Indian names

        created_emails = set()  # Track generated emails to avoid duplicates

        for i in range(num_users):
            email = fake.unique.email()  # Ensure unique emails are generated

            # Check for duplicates before saving
            while email in created_emails:
                email = fake.unique.email()

            created_emails.add(email)  # Add the email to the set
            first_name = fake.first_name()
            last_name = fake.last_name()
            mobile_number = fake.phone_number()

            user = User(
                first_name=first_name,
                last_name=last_name,
                age=fake.random_int(min=18, max=50),
                email=email,
                mobile_number=mobile_number,
                is_active=True,
                is_phone_verified=fake.boolean(chance_of_getting_true=50),
                is_email_verified=fake.boolean(chance_of_getting_true=50)
            )
            user.save()