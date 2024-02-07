from LinkMLFormbuilder.formbuilder import getSlotFormCode
from LinkMLFormbuilder.slot_code_generators import *
from LinkMLFormbuilder.utils import extractDescription, extractSlotName
from test_fixtures import *
from test_fixtures_full_files import *
from utils import *

def test_simple_int_slot(yamlfile, default_range, simple_int_slot, simple_int_slot_expected):
    assert normalize(getSlotFormCode(simple_int_slot, yamlfile, default_range, [], 1)) == normalize(simple_int_slot_expected)
    assert normalize(getNumberSlotCode(simple_int_slot, extractDescription(simple_int_slot), "required", simple_int_slot.get("name"), extractSlotName(simple_int_slot))) == normalize(simple_int_slot_expected)

def test_simple_datetime_slot(yamlfile, default_range, simple_datetime_slot, simple_datetime_slot_expected):
    assert normalize(getSlotFormCode(simple_datetime_slot, yamlfile, default_range, [], 1)) == normalize(simple_datetime_slot_expected)
    assert normalize(getStringSlotCode(extractDescription(simple_datetime_slot), "required", simple_datetime_slot.get("name"), extractSlotName(simple_datetime_slot), simple_datetime_slot)) == normalize(simple_datetime_slot_expected)

def test_simple_enum_slot(yamlfile, default_range, simple_enum_slot, simple_enum_slot_expected):
    assert normalize(getSlotFormCode(simple_enum_slot, yamlfile, default_range, [], 1)) == normalize(simple_enum_slot_expected)
    assert normalize(getEnumSlotCode(simple_enum_slot, yamlfile, extractDescription(simple_enum_slot), "", simple_enum_slot.get("name"), extractSlotName(simple_enum_slot))) == normalize(simple_enum_slot_expected)

def test_simple_float_slot(yamlfile, default_range, simple_float_slot, simple_float_slot_expected):
    assert normalize(getSlotFormCode(simple_float_slot, yamlfile, default_range, [], 1)) == normalize(simple_float_slot_expected)
    assert normalize(getNumberSlotCode(simple_float_slot, extractDescription(simple_float_slot), "", simple_float_slot.get("name"), extractSlotName(simple_float_slot))) == normalize(simple_float_slot_expected)

def test_simple_textarea_slot(yamlfile, default_range, simple_textarea_slot, simple_textarea_slot_expected):
    assert normalize(getSlotFormCode(simple_textarea_slot, yamlfile, default_range, [], 1)) == normalize(simple_textarea_slot_expected)
    assert normalize(getTextareaSlotCode(extractDescription(simple_textarea_slot), "", simple_textarea_slot.get("name"), extractSlotName(simple_textarea_slot), simple_textarea_slot)) == normalize(simple_textarea_slot_expected)

def test_simple_boolean_slot(yaml_patient_partial, default_range, simple_boolean_slot, simple_boolean_slot_expected):
    assert normalize(getSlotFormCode(simple_boolean_slot, yaml_patient_partial, default_range, [], 1)) == normalize(simple_boolean_slot_expected)
    assert normalize(getBooleanSlotCode(extractDescription(simple_boolean_slot), "", simple_boolean_slot.get("name"), extractSlotName(simple_boolean_slot))) == normalize(simple_boolean_slot_expected)

def test_simple_int_slot_default_range(default_range_yaml_integer, simple_int_slot_default_range_expected, default_range_slot):
    assert normalize(getSlotFormCode(default_range_slot, default_range_yaml_integer, "integer", [], 1)) == normalize(simple_int_slot_default_range_expected)

def test_simple_float_slot_default_range(default_range_yaml_float, simple_float_slot_default_range_expected, default_range_slot):
    assert normalize(getSlotFormCode(default_range_slot, default_range_yaml_float, "float", [], 1)) == normalize(simple_float_slot_default_range_expected)

def test_simple_string_slot_default_range(default_range_yaml_string, simple_textarea_slot_default_range_expected, default_range_slot):
    assert normalize(getSlotFormCode(default_range_slot, default_range_yaml_string, "string", [], 1)) == normalize(simple_textarea_slot_default_range_expected)

def test_simple_boolean_slot_default_range(default_range_yaml_boolean, simple_boolean_slot_default_range_expected, default_range_slot):
    print(getSlotFormCode(default_range_slot, default_range_yaml_boolean, "boolean", [], 1))
    assert normalize(getSlotFormCode(default_range_slot, default_range_yaml_boolean, "boolean", [], 1)) == normalize(simple_boolean_slot_default_range_expected)

def test_simple_datetime_slot_default_range(default_range_yaml_datetime, simple_datetime_slot_default_range_expected, default_range_slot):
    assert normalize(getSlotFormCode(default_range_slot, default_range_yaml_datetime, "datetime", [], 1)) == normalize(simple_datetime_slot_default_range_expected)

def test_dynamic_enum_slot(yamlfile, default_range, dynamic_enum_slot, dynamic_enum_slot_expected):
    assert normalize(getSlotFormCode(dynamic_enum_slot, yamlfile, default_range, [], 1)) == normalize(dynamic_enum_slot_expected)
    assert normalize(getEnumSlotCode(dynamic_enum_slot, yamlfile, extractDescription(dynamic_enum_slot), "", dynamic_enum_slot.get("name"), extractSlotName(dynamic_enum_slot))) == normalize(dynamic_enum_slot_expected)

def test_inlined_static_enum_slot(yamlfile, default_range, inlined_static_enum_slot, inlined_static_enum_slot_expected):
    assert normalize(getSlotFormCode(inlined_static_enum_slot, yamlfile, default_range, [], 1)) == normalize(inlined_static_enum_slot_expected)
    assert normalize(getInlineEnumSlotCode(inlined_static_enum_slot, extractDescription(inlined_static_enum_slot), "", inlined_static_enum_slot.get("name"), extractSlotName(inlined_static_enum_slot))) == normalize(inlined_static_enum_slot_expected)

def test_inlined_dynamic_enum_slot(yamlfile, default_range, inlined_dynamic_enum_slot, inlined_dynamic_enum_slot_expected):
    assert normalize(getSlotFormCode(inlined_dynamic_enum_slot, yamlfile, default_range, [], 1)) == normalize(inlined_dynamic_enum_slot_expected)
    assert normalize(getInlineEnumSlotCode(inlined_dynamic_enum_slot, extractDescription(inlined_dynamic_enum_slot), "", inlined_dynamic_enum_slot.get("name"), extractSlotName(inlined_dynamic_enum_slot))) == normalize(inlined_dynamic_enum_slot_expected)

def test_min_and_max_range_int_slot(min_and_max_range_int_slot, min_and_max_range_int_slot_expected):
    assert normalize(getNumberSlotCode(min_and_max_range_int_slot, extractDescription(min_and_max_range_int_slot), "required", min_and_max_range_int_slot.get("name"), extractSlotName(min_and_max_range_int_slot))) == normalize(min_and_max_range_int_slot_expected)

def test_min_range_int_slot(min_range_int_slot, min_range_int_slot_expected):
    assert normalize(getNumberSlotCode(min_range_int_slot, extractDescription(min_range_int_slot), "required", min_range_int_slot.get("name"), extractSlotName(min_range_int_slot))) == normalize(min_range_int_slot_expected)

def test_max_range_int_slot(max_range_int_slot, max_range_int_slot_expected):
    assert normalize(getNumberSlotCode(max_range_int_slot, extractDescription(max_range_int_slot), "required", max_range_int_slot.get("name"), extractSlotName(max_range_int_slot))) == normalize(max_range_int_slot_expected)

def test_multivalued_int_slot(multivalued_int_slot, multivalued_int_slot_expected):
    assert normalize(getNumberSlotCode(multivalued_int_slot, extractDescription(multivalued_int_slot), "required", multivalued_int_slot.get("name"), extractSlotName(multivalued_int_slot))) == normalize(multivalued_int_slot_expected)

def test_multivalued_textarea_slot(multivalued_textarea_slot, multivalued_textarea_slot_expected):
    assert normalize(getTextareaSlotCode(extractDescription(multivalued_textarea_slot), "", multivalued_textarea_slot.get("name"), extractSlotName(multivalued_textarea_slot), multivalued_textarea_slot)) == normalize(multivalued_textarea_slot_expected)

def test_multivalued_datetime_slot(multivalued_datetime_slot, multivalued_datetime_slot_expected):
    assert normalize(getStringSlotCode(extractDescription(multivalued_datetime_slot), "required", multivalued_datetime_slot.get("name"), extractSlotName(multivalued_datetime_slot), multivalued_datetime_slot)) == normalize(multivalued_datetime_slot_expected)
