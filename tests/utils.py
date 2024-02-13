def normalize(org_string):
    return "".join(org_string.split())

def getDefaultRangeCode(default_range):
    return '''
    id: default_range_tests
    name: default_range_tests
    title: Default range tests
    prefixes:
        linkml: https://w3id.org/linkml
    default_range: {default_range}
                          
    classes:
        default_range_tests:
            name: default_range_tests
            slots:
                - default_range_slot
    slots:
        default_range_slot:
            name: default_range_slot
            title: Default range slot
            description: Default range slot description
'''.format(default_range=default_range)
