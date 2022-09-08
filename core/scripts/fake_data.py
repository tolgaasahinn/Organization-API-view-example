import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
import django

django.setup()

from accounts.models import UserModel
from faker import Faker
from organizations.models import Organization


def set_user_and_organization():
    type = ["Person", "Conglomerate", "KOBİ", "STK"]
    fake = Faker(["en_US"])
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f"{f_name.lower()}_{l_name.lower()}"
    email = f"{u_name}@{fake.domain_name()}"
    print(f_name, l_name, email)

    user_check = UserModel.objects.filter(username=u_name)
    while user_check.exists():
        u_name = u_name + str(random.randrange(1, 99))
        user_check = UserModel.objects.filter(username=u_name)
    user = User(
        username=u_name,
        first_name=f_name,
        last_name=l_name,
        email=email,
        is_staff=fake.boolean(chance_of_getting_true=20),
    )
    user.set_password("testing321..")
    user.save()
    # o_user = user
    o_name = f"{f_name.lower()}-{l_name.lower()}"
    o_type = random.choice(type)
    o_country = fake.country_code()
    o_url = fake.ascii_company_email()
    number = random.randint(100, 1000)
    organization = Organization(
        organisations_user=user,
        organisation_name=o_name,
        organization_type=o_type,
        country=o_country,
        organization_url=o_url,
        number_of_employees=number,
    )
    organization.save()
    print(o_name, o_type, o_country, o_url, number)
