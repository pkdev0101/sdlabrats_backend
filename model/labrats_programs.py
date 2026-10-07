""" San Diego LabRats program catalog.

The `slug` values are the contract with the frontend (sdlabrats_frontend _data/sdlabrats.yml
`programs[].slug`): contact forms send them as the `interest` of an inquiry.
"""

LABRATS_PROGRAMS = [
    {
        "slug": "afterschool",
        "name": "Afterschool at the STEM Discovery Center",
        "audience": "families",
        "grades": "K-3 and 4-8",
        "description": "A one-hour lab led by a scientist, then an hour of open maker space. Monthly sessions in Carlsbad.",
        "path": "/stem-discovery-center-2-3-2/",
    },
    {
        "slug": "camps",
        "name": "Break and summer camps",
        "audience": "families",
        "grades": "K-3 and 3-6",
        "description": "Half-day camps over Thanksgiving, winter, spring, and summer breaks with hands-on labs and maker space time.",
        "path": "/camps/",
    },
    {
        "slug": "assemblies",
        "name": "Assemblies and demo lab stations",
        "audience": "schools",
        "grades": "K-8",
        "description": "30- or 60-minute science shows, The Power of Science and Mysteries of Science, at your school or event.",
        "path": "/assemblies-demo-lab-stations/",
    },
    {
        "slug": "stem-at-home",
        "name": "STEM at Home",
        "audience": "families",
        "grades": "K-8",
        "description": "Free video labs and printable procedures using household materials.",
        "path": "/stemathome/",
    },
    {
        "slug": "courses-workshops",
        "name": "Courses and workshops",
        "audience": "schools",
        "grades": "K-2, 3-5, 6-8",
        "description": "Mobile Lab courses and workshops for classrooms, scout troops, and events across San Diego County.",
        "path": "/courses-workshops/",
    },
]

PROGRAM_SLUGS = frozenset(program["slug"] for program in LABRATS_PROGRAMS)
