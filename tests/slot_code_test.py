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
    assert normalize(getStringSlotCode(extractDescription(simple_datetime_slot), "required", simple_datetime_slot.get("name"), extractSlotName(simple_datetime_slot))) == normalize(simple_datetime_slot_expected)

def test_simple_enum_slot(yamlfile, default_range, simple_enum_slot, simple_enum_slot_expected):
    assert normalize(getSlotFormCode(simple_enum_slot, yamlfile, default_range, [], 1)) == normalize(simple_enum_slot_expected)
    assert normalize(getEnumSlotCode(simple_enum_slot, yamlfile, extractDescription(simple_enum_slot), "", simple_enum_slot.get("name"), extractSlotName(simple_enum_slot))) == normalize(simple_enum_slot_expected)

def test_simple_float_slot(yamlfile, default_range, simple_float_slot, simple_float_slot_expected):
    assert normalize(getSlotFormCode(simple_float_slot, yamlfile, default_range, [], 1)) == normalize(simple_float_slot_expected)
    assert normalize(getNumberSlotCode(simple_float_slot, extractDescription(simple_float_slot), "", simple_float_slot.get("name"), extractSlotName(simple_float_slot))) == normalize(simple_float_slot_expected)

def test_simple_textarea_slot(yamlfile, default_range, simple_textarea_slot, simple_textarea_slot_expected):
    assert normalize(getSlotFormCode(simple_textarea_slot, yamlfile, default_range, [], 1)) == normalize(simple_textarea_slot_expected)
    assert normalize(getTextareaSlotCode(extractDescription(simple_textarea_slot), "", simple_textarea_slot.get("name"), extractSlotName(simple_textarea_slot))) == normalize(simple_textarea_slot_expected)

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