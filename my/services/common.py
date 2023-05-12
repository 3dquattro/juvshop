from my.models import Address, Profile
from my.tables import AddressTable
from my.forms import ProfileForm


"""
Function returns profile for user
Input: user
Output: Profile object
"""


def get_profile(user: object):
    return Profile.objects.get(user=user)


"""
Function returns context for addresses index-page
Input: user
Output: dictionary with django_tables2 table
"""


def addresses_index_context(user: object) -> dict:
    profile = get_profile(user)
    addresses = Address.objects.filter(profile=profile).all()
    table = AddressTable(addresses)
    return {"table": table}


"""
Function returns context for index profile page
(form for updating profile)
Input: user
Output: dictionary containing Django form for model Profile
"""


def profile_index_get_context(user: object) -> dict:
    profile, created = Profile.objects.get_or_create(user=user)
    return {"form": ProfileForm(instance=profile)}


"""
Procedure that handles post method of profile index page
Input: user, post (POST variables storage)
Output: None
"""


def profile_index_post_logic(user, post):
    profile = get_profile(user)
    form = ProfileForm(post, instance=profile)
    if form.is_valid():
        form.save()
    return
