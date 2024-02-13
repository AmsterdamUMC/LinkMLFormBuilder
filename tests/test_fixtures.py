import pytest
import yaml

# The LinkML slot syntax is incomplete in these fixtures, this is on purpose as in real-world cases this is the format the called functions will receive

# getSlotFormCode
@pytest.fixture(scope='session')
def default_range():
    return "string"

@pytest.fixture(scope='session')
def default_range_slot():
    return yaml.safe_load('''
        default_range_slot:
        name: default_range_slot
        title: Default range slot
        description: Default range slot description
''')

@pytest.fixture(scope='session')
def simple_int_slot():
    return yaml.safe_load('''
    name: systolic_pressure
    title: Systolic pressure
    required: true
    description: Systolic pressure in mmHg
    definition_uri: snomed:271649006
    range: integer
    unit: 
        exact_mappings: 
            - snomed:259018001
    ''')

@pytest.fixture(scope='session')
def simple_int_slot_expected():
    return '''<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="systolic_pressure-addon">Systolic pressure</span>
      <input type="number" class="form-control" id="systolic_pressure" aria-describedby="systolic_pressure-addon systolic_pressure-description" required>
    </div>
    <div class="form-text" id="systolic_pressure-description">Systolic pressure in mmHg </div>
  </div>'''

@pytest.fixture(scope='session')
def simple_int_slot_default_range_expected():
    return '''<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="default_range_slot-addon">Default range slot</span>
      <input type="number" class="form-control" id="default_range_slot" aria-describedby="default_range_slot-addon default_range_slot-description">
    </div>
    <div class="form-text" id="default_range_slot-description">Default range slot description</div>
  </div>'''

@pytest.fixture(scope='session')
def min_and_max_range_int_slot():
    return yaml.safe_load('''
    name: systolic_pressure
    title: Systolic pressure
    required: true
    minimum_value: 0
    maximum_value: 250
    description: Systolic pressure in mmHg
    definition_uri: snomed:271649006
    range: integer
    unit: 
        exact_mappings: 
            - snomed:259018001
    ''')

@pytest.fixture(scope='session')
def min_and_max_range_int_slot_expected():
    return '''<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="systolic_pressure-addon">Systolic pressure</span>
      <input type="number" class="form-control" id="systolic_pressure" aria-describedby="systolic_pressure-addon systolic_pressure-description" required>
    </div>
    <div class="form-text" id="systolic_pressure-description">Systolic pressure in mmHg The value for this field should be between 0 and 250</div>
  </div>'''

@pytest.fixture(scope='session')
def min_range_int_slot():
    return yaml.safe_load('''
    name: systolic_pressure
    title: Systolic pressure
    required: true
    minimum_value: 0
    description: Systolic pressure in mmHg
    definition_uri: snomed:271649006
    range: integer
    unit: 
        exact_mappings: 
            - snomed:259018001
    ''')

@pytest.fixture(scope='session')
def min_range_int_slot_expected():
    return '''<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="systolic_pressure-addon">Systolic pressure</span>
      <input type="number" class="form-control" id="systolic_pressure" aria-describedby="systolic_pressure-addon systolic_pressure-description" required>
    </div>
    <div class="form-text" id="systolic_pressure-description">Systolic pressure in mmHg The value for this field should be equal to or greater than 0</div>
  </div>'''

@pytest.fixture(scope='session')
def max_range_int_slot():
    return yaml.safe_load('''
    name: systolic_pressure
    title: Systolic pressure
    required: true
    maximum_value: 250
    description: Systolic pressure in mmHg
    definition_uri: snomed:271649006
    range: integer
    unit: 
        exact_mappings: 
            - snomed:259018001
    ''')

@pytest.fixture(scope='session')
def max_range_int_slot_expected():
    return '''<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="systolic_pressure-addon">Systolic pressure</span>
      <input type="number" class="form-control" id="systolic_pressure" aria-describedby="systolic_pressure-addon systolic_pressure-description" required>
    </div>
    <div class="form-text" id="systolic_pressure-description">Systolic pressure in mmHg The value for this field should be equal to or smaller than 250</div>
  </div>'''

@pytest.fixture(scope='session')
def multivalued_int_slot():
    return yaml.safe_load('''
    name: systolic_pressure
    title: Systolic pressure
    required: true
    multivalued: true
    maximum_cardinality: 3
    description: Systolic pressure in mmHg
    definition_uri: snomed:271649006
    range: integer
    unit: 
        exact_mappings: 
            - snomed:259018001
    ''')

@pytest.fixture(scope='session')
def multivalued_int_slot_expected():
    return '''<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="systolic_pressure-addon">Systolic pressure</span>
      <input type="number" class="form-control" id="systolic_pressure" aria-describedby="systolic_pressure-addon systolic_pressure-description" required>
    </div>
    <div class="input-group">
      <span class="input-group-text hideField" id="systolic_pressure-addon">Systolic pressure</span>
      <input type="number" class="form-control" id="systolic_pressure2" aria-describedby="systolic_pressure-addon systolic_pressure-description">
    </div>
    <div class="input-group">
      <span class="input-group-text hideField" id="systolic_pressure-addon">Systolic pressure</span>
      <input type="number" class="form-control" id="systolic_pressure3" aria-describedby="systolic_pressure-addon systolic_pressure-description">
    </div>
    <div class="form-text" id="systolic_pressure-description">Systolic pressure in mmHg This field requires at least 1 value(s)</div>
  </div>'''

@pytest.fixture(scope='session')
def simple_datetime_slot():
    return yaml.safe_load('''
    name: measurement_datetime
    title: Measurement datetime
    required: true
    description: The date and time at which the measurement took place
    definition_uri: snomed:118575009
    range: datetime
    ''')

@pytest.fixture(scope='session')
def simple_datetime_slot_expected():
    return '''<div class="mb-3">
    <div class="input-group">
    <span class="input-group-text" id="measurement_datetime-addon">Measurement datetime</span>
    <input type="text" class="form-control" id="measurement_datetime" aria-describedby="measurement_datetime-addon measurement_datetime-description" required>
    </div>
    <div class="form-text" id="measurement_datetime-description">The date and time at which the measurement took place</div>
</div>'''

@pytest.fixture(scope='session')
def multivalued_datetime_slot():
    return yaml.safe_load('''
    name: measurement_datetime
    title: Measurement datetime
    required: true
    multivalued: true
    maximum_cardinality: 3
    description: The date and time at which the measurement took place
    definition_uri: snomed:118575009
    range: datetime
    ''')

@pytest.fixture(scope='session')
def multivalued_datetime_slot_expected():
    return '''<div class="mb-3">
    <div class="input-group">
    <span class="input-group-text" id="measurement_datetime-addon">Measurement datetime</span>
    <input type="text" class="form-control" id="measurement_datetime" aria-describedby="measurement_datetime-addon measurement_datetime-description" required>
    </div>
    <div class="input-group">
    <span class="input-group-text hideField" id="measurement_datetime-addon">Measurement datetime</span>
    <input type="text" class="form-control" id="measurement_datetime2" aria-describedby="measurement_datetime-addon measurement_datetime-description">
    </div>
    <div class="input-group">
    <span class="input-group-text hideField" id="measurement_datetime-addon">Measurement datetime</span>
    <input type="text" class="form-control" id="measurement_datetime3" aria-describedby="measurement_datetime-addon measurement_datetime-description">
    </div>
    <div class="form-text" id="measurement_datetime-description">The date and time at which the measurement took place This field requires at least 1 value(s)</div>
</div>'''

@pytest.fixture(scope='session')
def simple_datetime_slot_default_range_expected():
    return '''<div class="mb-3">
    <div class="input-group">
    <span class="input-group-text" id="default_range_slot-addon">Default range slot</span>
    <input type="text" class="form-control" id="default_range_slot" aria-describedby="default_range_slot-addon default_range_slot-description">
    </div>
    <div class="form-text" id="default_range_slot-description">Default range slot description</div>
</div>'''

@pytest.fixture(scope='session')
def simple_enum_slot():
    return yaml.safe_load('''
    name: measurement_location
    title: Measurement location
    description: The anatomical location of the blood pressure cuff on the patient during the measurement
    definition_uri: snomed:758637006
    values_from:
        - measurement_location_valueset 
    ''')

@pytest.fixture(scope='session')
def simple_enum_slot_expected():
    return '''<div class="mb-3">
        <div class="input-group">
<span class="input-group-text">Measurement location</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="measurement_location-description">The anatomical location of the blood pressure cuff on the patient during the measurement</div>
<div class='answer-options'>
<span class='values-from'>Measurement location valueset:</span>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="upper_arm_structure" >
                <label class="form-check-label" for="upper_arm_structure">Upper arm structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="right_upper_arm_structure" >
                <label class="form-check-label" for="right_upper_arm_structure">Right upper arm structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="left_upper_arm_structure" >
                <label class="form-check-label" for="left_upper_arm_structure">Left upper arm structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="thigh_structure" >
                <label class="form-check-label" for="thigh_structure">Thigh structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="right_thigh_structure" >
                <label class="form-check-label" for="right_thigh_structure">Right thigh structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_ valueset" id="left_thigh_structure" >
                <label class="form-check-label" for="left_thigh_structure">Left thigh structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="wrist_region_structure" >
                <label class="form-check-label" for="wrist_region_structure">Wrist region structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="right_wrist_region_structure" >
                <label class="form-check-label" for="right_wrist_region_structure">Right wrist region structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="left_wrist_region_structure" >
                <label class="form-check-label" for="left_wrist_region_structure">Left wrist region structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="finger_structure" >
                <label class="form-check-label" for="finger_structure">Finger structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="ankle_region_structure" >
                <label class="form-check-label" for="ankle_region_structure">Ankle region structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="right_ankle_region_structure" >
                <label class="form-check-label" for="right_ankle_region_structure">Right ankle region structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="left_ankle_region_structure" >
                <label class="form-check-label" for="left_ankle_region_structure">Left ankle region structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="toe_structure" >
                <label class="form-check-label" for="toe_structure">Toe structure</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Measurement_location_valueset" id="intra-arterial" >
                <label class="form-check-label" for="intra-arterial">Intra-arterial</label></div>
</div>
</div>'''

@pytest.fixture(scope='session')
def dynamic_enum_slot():
    return yaml.safe_load('''
    name: diastolic_endpoint
    title: Diastolic endpoint
    description: The diastolic endpoint, also called Korotkoff sounds
    definition_uri: snomed:85549003
    values_from:
        - diastolic_endpoint_valueset
''')

@pytest.fixture(scope='session')
def dynamic_enum_slot_expected():
    return '''<div class="mb-3">
        <div class="input-group">
<span class="input-group-text">Diastolic endpoint</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="diastolic_endpoint-description">The diastolic endpoint, also called Korotkoff sounds</div>
<div class='answer-options'>
<span class='values-from-dynamic'>Diastolic endpoint valueset:</span>
<textarea rows="6" class="form-control" id="diastolic_endpoint_valueset"></textarea>
</div>
</div>'''

@pytest.fixture(scope='session')
def inlined_static_enum_slot():
    return yaml.safe_load('''
    name: patient_body_position
    title: Patient body position
    description: The position of the patient's body during the measurement
    definition_uri: snomed:424724000
    enum_range:
        permissible_values:
            sitting position:
                meaning: snomed:33586001
            lying position:
                meaning: snomed:102538003
            standing position:
                meaning: snomed:10904000
            tilted position:
                meaning: snomed:272587006
            trendelenburg position:
                meaning: snomed:34106002
''')

@pytest.fixture(scope='session')
def inlined_static_enum_slot_expected():
    return '''
    <div class="mb-3">
        <div class="input-group">
<span class="input-group-text">Patient body position</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="patient_body_position-description">The position of the patient's body during the measurement</div>
<div class='answer-options'>
<span class='values-from'>Patient body position valueset:</span>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Patient_body_position_valueset" id="sitting_position" >
                <label class="form-check-label" for="sitting_position">Sitting position</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Patient_body_position_valueset" id="lying_position" >
                <label class="form-check-label" for="lying_position">Lying position</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Patient_body_position_valueset" id="standing_position" >
                <label class="form-check-label" for="standing_position">Standing position</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Patient_body_position_valueset" id="tilted_position" >
                <label class="form-check-label" for="tilted_position">Tilted position</label></div>
<div class="form-check">
                <input class="form-check-input" type="radio" name="Patient_body_position_valueset" id="trendelenburg_position" >
                <label class="form-check-label" for="trendelenburg_position">Trendelenburg position</label></div>
</div>
</div>
'''

@pytest.fixture(scope='session')
def inlined_dynamic_enum_slot():
    return yaml.safe_load('''
    name: diastolic_endpoint2
    title: Diastolic endpoint2
    description: The diastolic endpoint, also called Korotkoff sounds
    definition_uri: snomed:85549003
    enum_range: 
        reachable_from:
            source_ontology: snomed
            source_nodes:
                - snomed:272108007
            include_self: false
            relationship_types:
                - rdfs:subClassOf
''')

@pytest.fixture(scope='session')
def inlined_dynamic_enum_slot_expected():
    return '''<div class="mb-3">
        <div class="input-group">
<span class="input-group-text">Diastolic endpoint2</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="diastolic_endpoint2-description">The diastolic endpoint, also called Korotkoff sounds</div>
<div class='answer-options'>
<span class='values-from-dynamic'>Diastolic endpoint2 valueset:</span>
<textarea rows="6" class="form-control" id="Diastolic_endpoint2_valueset"></textarea>
</div>
</div>'''

@pytest.fixture(scope='session')
def simple_float_slot():
    return yaml.safe_load('''
    name: mean_arterial_pressure
    title: Mean arterial pressure
    description: The average arterial pressure throughout one cardiac cycle, systole, and diastole in mmHg
    definition_uri: snomed:1285244000
    unit: 
    exact_mappings:
        - snomed:259018001
    range: float
    ''')

@pytest.fixture(scope='session')
def simple_float_slot_expected():
    return '''<div class="mb-3">
<div class="input-group">
    <span class="input-group-text" id="mean_arterial_pressure-addon">Mean arterial pressure</span>
    <input type="number" class="form-control" id="mean_arterial_pressure" aria-describedby="mean_arterial_pressure-addon mean_arterial_pressure-description" >
</div>
<div class="form-text" id="mean_arterial_pressure-description">The average arterial pressure throughout one cardiac cycle, systole, and diastole in mmHg </div>
</div>'''

@pytest.fixture(scope='session')
def simple_float_slot_default_range_expected():
    return '''<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="default_range_slot-addon">Default range slot</span>
      <input type="number" class="form-control" id="default_range_slot" aria-describedby="default_range_slot-addon default_range_slot-description">
    </div>
    <div class="form-text" id="default_range_slot-description">Default range slot description</div>
  </div>'''

@pytest.fixture(scope='session')
def simple_textarea_slot():
    return yaml.safe_load('''
    name: explanatory_statement
    title: Explanatory statement
    description: Additional information that cannot be coded
    definition_uri: snomed:900000000000519001
    range: string
    ''')

@pytest.fixture(scope='session')
def simple_textarea_slot_expected():
    return '''<div class="mb-3">
<div class="input-group">
    <span class="input-group-text" id="explanatory_statement-addon">Explanatory statement</span>
    <textarea rows="6" class="form-control" id="explanatory_statement" aria-describedby="explanatory_statement-addon explanatory_statement-description" ></textarea>
</div>
<div class="form-text" id="explanatory_statement-description">Additional information that cannot be coded</div>
</div>'''

@pytest.fixture(scope='session')
def multivalued_textarea_slot():
    return yaml.safe_load('''
    name: explanatory_statement
    title: Explanatory statement
    description: Additional information that cannot be coded
    multivalued: true
    maximum_cardinality: 3
    definition_uri: snomed:900000000000519001
    range: string
    ''')

@pytest.fixture(scope='session')
def multivalued_textarea_slot_expected():
    return '''<div class="mb-3">
<div class="input-group">
    <span class="input-group-text" id="explanatory_statement-addon">Explanatory statement</span>
    <textarea rows="6" class="form-control" id="explanatory_statement" aria-describedby="explanatory_statement-addon explanatory_statement-description" ></textarea>
</div>
<div class="input-group">
    <span class="input-group-text hideField" id="explanatory_statement-addon">Explanatory statement</span>
    <textarea rows="6" class="form-control" id="explanatory_statement2" aria-describedby="explanatory_statement-addon explanatory_statement-description" ></textarea>
</div>
<div class="input-group">
    <span class="input-group-text hideField" id="explanatory_statement-addon">Explanatory statement</span>
    <textarea rows="6" class="form-control" id="explanatory_statement3" aria-describedby="explanatory_statement-addon explanatory_statement-description"></textarea>
</div>
<div class="form-text" id="explanatory_statement-description">Additional information that cannot be coded This field requires at least 1 value(s)</div>
</div>'''


@pytest.fixture(scope='session')
def simple_textarea_slot_default_range_expected():
    return '''<div class="mb-3">
<div class="input-group">
    <span class="input-group-text" id="default_range_slot-addon">Default range slot</span>
    <textarea rows="6" class="form-control" id="default_range_slot" aria-describedby="default_range_slot-addon default_range_slot-description" ></textarea>
</div>
<div class="form-text" id="default_range_slot-description">Default range slot description</div>
</div>'''

@pytest.fixture(scope='session')
def simple_boolean_slot():
    return yaml.safe_load('''
    source: 2.16.840.1.113883.2.4.3.11.60.40.1.0.1.31
    name: nl_zorg_Patient_MeerlingIndicator
    title: MeerlingIndicator
    structured_aliases:
        - literal_form: MeerlingIndicator
        - literal_form: MultipleBirthIndicator
    range: boolean
    ''')

@pytest.fixture(scope='session')
def simple_boolean_slot_expected():
    return '''<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">MeerlingIndicator (MeerlingIndicator / MultipleBirthIndicator)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_Patient_MeerlingIndicator-description"></div>
<div class='answer-options'>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="nl_zorg_Patient_MeerlingIndicator" id="True" >
                  <label class="form-check-label" for="True">True</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="nl_zorg_Patient_MeerlingIndicator" id="False" >
                  <label class="form-check-label" for="False">False</label></div>
</div>
</div>'''

@pytest.fixture(scope='session')
def simple_boolean_slot_default_range_expected():
    return '''<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">Default range slot</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="default_range_slot-description">Default range slot description</div>
<div class='answer-options'>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="default_range_slot" id="True" >
                  <label class="form-check-label" for="True">True</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="default_range_slot" id="False" >
                  <label class="form-check-label" for="False">False</label></div>
</div>
</div>'''

# extractDescription
@pytest.fixture(scope='session')
def simple_description_slot():
    return yaml.safe_load('''
        name: simple_description
        title: Simple description
        description: A simple description
        range: string
''')

@pytest.fixture(scope='session')
def simple_description_slot_expected():
    return "A simple description"

@pytest.fixture(scope='session')
def alt_description_slot():
    return yaml.safe_load('''
        name: alt_description
        title: Alternative descriptions
        alt_descriptions:
            - description: This is an alternative description
            - description: And another one
            - description: I don't have any inspiration for this
        range: string
''')

@pytest.fixture(scope='session')
def alt_description_slot_expected():
    return "(This is an alternative description / And another one / I don't have any inspiration for this)"

@pytest.fixture(scope='session')
def both_descriptions_slot():
    return yaml.safe_load('''
        name: both_descriptions
        title: Both descriptions
        description: This slot has both a description and multiple alt_descriptions
        alt_descriptions:
            - description: This is an alternative description
            - description: Normally, I'd add a source field, but Python doesn't like that
            - description: test
        range: string
''')

@pytest.fixture(scope = 'session')
def both_descriptions_slot_expected():
    return "This slot has both a description and multiple alt_descriptions (This is an alternative description / Normally, I'd add a source field, but Python doesn't like that / test)"

@pytest.fixture(scope='session')
def not_normal_description_slot():
    return yaml.safe_load('''
        name: not_normal_description
        title: Not normal description
        description: <b>This has some <img ...> tags </b>here<div> and there<span>, very annoying </span> </div>
        alt_descriptions:
            - description: <i> in the alts too </i>
        range: string
''')

@pytest.fixture(scope='session')
def not_normal_description_expected():
    return "This has some tags here and there, very annoying (in the alts too)"

# extractSlotName
@pytest.fixture(scope='session')
def multivalued_singular_name_slot():
    return yaml.safe_load('''
        name: multivalued_singular_name_slot
        title: Multivalued singular name slot
        multivalued: False
        singular_name: single name
        range: string
''')

@pytest.fixture(scope='session')
def multivalued_singular_name_slot_expected():
    return "single name"

@pytest.fixture(scope='session')
def cardinality_one_singular_name_slot():
    return yaml.safe_load('''
        name: cardinality_one_singular_name_slot
        title: Cardinality one singular name slot
        maximum_cardinality: 1
        singular_name: single name
        range: string
''')

@pytest.fixture(scope='session')
def cardinality_one_singular_name_slot_expected():
    return "single name"

@pytest.fixture(scope='session')
def absent_singular_name_slot():
    return yaml.safe_load('''
        name: absent_singular_name_slot
        title: Absent singular name slot
        multivalued: False
        maximum_cardinality: 1
        range: string
''')

@pytest.fixture(scope='session')
def absent_singular_name_slot_expected():
    return "Absent singular name slot"

@pytest.fixture(scope='session')
def multivalued_true_singular_name_slot():
    return yaml.safe_load('''
        name: multivalued_singular_name_slot
        title: Multivalued singular name slot
        multivalued: True
        singular_name: single name
        range: string
''')

@pytest.fixture(scope = 'session')
def multivalued_true_singular_name_slot_expected():
    return "Multivalued singular name slot"

@pytest.fixture(scope='session')
def maximum_cardinality_two_singular_name_slot():
    return yaml.safe_load('''
        name: multivalued_singular_name_slot
        title: Multivalued singular name slot
        maximum_cardinality: 2
        singular_name: single name
        range: string
''')

@pytest.fixture(scope='session')
def maximum_cardinality_two_singular_name_slot_expected():
    return "Multivalued singular name slot"

@pytest.fixture(scope='session')
def title_present_slot():
    return yaml.safe_load('''
        name: title_present
        title: Title present
        range: string
''')

@pytest.fixture(scope='session')
def title_present_slot_expected():
    return "Title present"

@pytest.fixture(scope='session')
def title_absent_slot():
    return yaml.safe_load('''
        name: title_absent
        range: string
''')

@pytest.fixture(scope='session')
def title_absent_slot_expected():
    return "title_absent"

@pytest.fixture(scope='session')
def title_present_aliases_slot():
    return yaml.safe_load('''
        name: title_present
        title: Title present
        aliases:
            - alias1
            - alias2
        range: string
''')

@pytest.fixture(scope='session')
def title_present_aliases_slot_expected():
    return "Title present (alias1 / alias2)"

@pytest.fixture(scope='session')
def title_present_structured_aliases_slot():
    return yaml.safe_load('''
        name: title_present
        title: Title present
        structured_aliases:
            - title: title1
            - title: title2
              literal_form: lit_form1
            - literal_form: lit_form2
        range: string
''')

@pytest.fixture(scope='session')
def title_present_structured_aliases_slot_expected():
    return "Title present (title1 / title2 / lit_form2)"

@pytest.fixture(scope='session')
def title_present_local_names_slot():
    return yaml.safe_load('''
        name: title_present
        title: Title present
        local_names:
            - local_name_value: loc1
            - local_name_value: loc2
        range: string
''')

@pytest.fixture(scope='session')
def title_present_local_names_slot_expected():
    return "Title present (loc1 / loc2)"

@pytest.fixture(scope='session')
def title_present_aliases_structured_aliases_local_names_slot():
    return yaml.safe_load('''
        name: title_present
        title: Title present
        aliases:
            - alias1
            - alias2
        structured_aliases:
            - title: title1
            - title: title2
              literal_form: lit_form1
            - literal_form: lit_form2
        local_names:
            - local_name_value: loc1
            - local_name_value: loc2
        range: string
''')

@pytest.fixture(scope='session')
def title_present_aliases_structured_aliases_local_names_slot_expected():
    return "Title present (alias1 / alias2 / title1 / title2 / lit_form2 / loc1 / loc2)"

@pytest.fixture(scope='session')
def title_absent_aliases_slot():
    return yaml.safe_load('''
        name: title_absent
        aliases:
            - alias1
            - alias2
        range: string
''')

@pytest.fixture(scope='session')
def title_absent_aliases_slot_expected():
    return "title_absent (alias1 / alias2)"

@pytest.fixture(scope='session')
def title_absent_structured_aliases_slot():
    return yaml.safe_load('''
        name: title_absent
        structured_aliases:
            - title: title1
            - title: title2
              literal_form: lit_form1
            - literal_form: lit_form2
        range: string
''')

@pytest.fixture(scope='session')
def title_absent_structured_aliases_slot_expected():
    return "title_absent (title1 / title2 / lit_form2)"

@pytest.fixture(scope='session')
def title_absent_local_names_slot():
    return yaml.safe_load('''
        name: title_absent
        local_names:
            - local_name_value: loc1
            - local_name_value: loc2
        range: string
''')

@pytest.fixture(scope='session')
def title_absent_local_names_slot_expected():
    return "title_absent (loc1 / loc2)"

@pytest.fixture(scope='session')
def title_absent_aliases_structured_aliases_local_names_slot():
    return yaml.safe_load('''
        name: title_absent
        aliases:
            - alias1
            - alias2
        structured_aliases:
            - title: title1
            - title: title2
              literal_form: lit_form1
            - literal_form: lit_form2
        local_names:
            - local_name_value: loc1
            - local_name_value: loc2
        range: string
''')

@pytest.fixture(scope='session')
def title_absent_aliases_structured_aliases_local_names_slot_expected():
    return "title_absent (alias1 / alias2 / title1 / title2 / lit_form2 / loc1 / loc2)"

# capitalizeLabel
@pytest.fixture(scope='session')
def capitalize_label_source():
    return "capitalize this"

@pytest.fixture(scope='session')
def capitalize_label_expected():
    return "Capitalize this"

@pytest.fixture(scope='session')
def capitalize_label_source2():
    return "caPiTaLiZe ThIs"

@pytest.fixture(scope='session')
def capitalize_label_expected2():
    return "CaPiTaLiZe ThIs"

@pytest.fixture(scope='session')
def capitalize_label_empty():
    return ""

@pytest.fixture(scope='session')
def capitalize_label_empty_expected():
    return ""
