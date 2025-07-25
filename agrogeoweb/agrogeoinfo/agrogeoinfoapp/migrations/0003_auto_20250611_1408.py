# Generated by Django 5.2 on 2025-06-11 14:08
from datetime import date

from django.db import migrations


def load_contact_data(apps, schema_editor):
    Organizations = apps.get_model('agrogeoinfoapp', 'Organizations')
    CV_OrganizationType = apps.get_model('agrogeoinfoapp', 'CV_OrganizationType')

    People = apps.get_model('agrogeoinfoapp', 'People')

    Affiliations = apps.get_model('agrogeoinfoapp', 'Affiliations')

    organization_type = CV_OrganizationType.objects.filter(term='university').first()

    organization = Organizations(
        organizationcode='WSU',
        organizationname='Washington State University',
        organizationdescription='A public land-grant research university in Pullman, Washington, United States',
        organizationlink='https://css.wsu.edu/',
        organizationtypecv=organization_type,
    )
    organization.save()

    contact_person = People(
        personfirstname='David',
        personlastname='Brown'
    )
    contact_person.save()

    affiliation = Affiliations(
        personid=contact_person,
        organizationid=organization,
        isprimaryorganizationcontact=True,
        affiliationstartdate=date(2002, 1, 1),
        primaryphone='509-332-2756',
        primaryemail='dave.brown@wsu.edu',
        primaryaddress='models.CharField(max_length=255, blank=True, null=True)',
        personlink='https://bsyse.wsu.edu/people/faculty/wsu-profile/dave.brown/'
    )
    affiliation.save()


class Migration(migrations.Migration):

    dependencies = [
        ("agrogeoinfoapp", "0002_auto_20250611_1156"),
    ]

    operations = [
        migrations.RunPython(load_contact_data)
    ]
