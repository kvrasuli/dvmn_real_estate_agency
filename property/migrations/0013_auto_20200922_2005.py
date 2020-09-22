from django.db import migrations


def add_flats_to_owner_table(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats:
        owner, _ = Owner.objects.get_or_create(
            full_name=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
        )
        owner.flats.set([flat])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20200922_2005'),
    ]

    operations = [
         migrations.RunPython(add_flats_to_owner_table)
    ]
