from LinkMLFormbuilder.utils import extractDescription, extractSlotName, capitalizeLabel
from utils import *
from test_fixtures import *
from test_fixtures_full_files import *

# extractDescription
def test_simple_descriptions(simple_description_slot, simple_description_slot_expected):
    assert normalize(extractDescription(simple_description_slot)) == normalize(simple_description_slot_expected)

def test_alt_descriptions(alt_description_slot, alt_description_slot_expected):
    assert normalize(extractDescription(alt_description_slot)) == normalize(alt_description_slot_expected)

def test_both_descriptions(both_descriptions_slot, both_descriptions_slot_expected):
    assert normalize(extractDescription(both_descriptions_slot)) == normalize(both_descriptions_slot_expected)

def test_normalize_descriptions(not_normal_description_slot, not_normal_description_expected):
    assert normalize(extractDescription(not_normal_description_slot)) == normalize(not_normal_description_expected)

# extractSlotName
def test_multivalued_singular_name(multivalued_singular_name_slot, multivalued_singular_name_slot_expected):
    assert extractSlotName(multivalued_singular_name_slot) == multivalued_singular_name_slot_expected

def test_cardinality_one_singular_name(cardinality_one_singular_name_slot, cardinality_one_singular_name_slot_expected):
    assert extractSlotName(cardinality_one_singular_name_slot) == cardinality_one_singular_name_slot_expected
    
def test_absent_singular_name(absent_singular_name_slot, absent_singular_name_slot_expected):
    assert extractSlotName(absent_singular_name_slot) == absent_singular_name_slot_expected

def test_multivalued_true_singular_name(multivalued_true_singular_name_slot, multivalued_true_singular_name_slot_expected):
    assert extractSlotName(multivalued_true_singular_name_slot) == multivalued_true_singular_name_slot_expected

def test_maximum_cardinality_two_singular_name(maximum_cardinality_two_singular_name_slot, maximum_cardinality_two_singular_name_slot_expected):
    assert extractSlotName(maximum_cardinality_two_singular_name_slot) == maximum_cardinality_two_singular_name_slot_expected

def test_title_present(title_present_slot, title_present_slot_expected):
    assert extractSlotName(title_present_slot) == title_present_slot_expected

def test_title_absent(title_absent_slot, title_absent_slot_expected):
    assert extractSlotName(title_absent_slot) == title_absent_slot_expected

def test_title_present_aliases(title_present_aliases_slot, title_present_aliases_slot_expected):
    assert extractSlotName(title_present_aliases_slot) == title_present_aliases_slot_expected

def test_title_present_structured_aliases(title_present_structured_aliases_slot, title_present_structured_aliases_slot_expected):
    assert extractSlotName(title_present_structured_aliases_slot) == title_present_structured_aliases_slot_expected

def test_title_present_local_names(title_present_local_names_slot, title_present_local_names_slot_expected):
    assert extractSlotName(title_present_local_names_slot) == title_present_local_names_slot_expected

def test_title_present_aliases_structured_aliases_local_names(title_present_aliases_structured_aliases_local_names_slot, title_present_aliases_structured_aliases_local_names_slot_expected):
    assert extractSlotName(title_present_aliases_structured_aliases_local_names_slot) == title_present_aliases_structured_aliases_local_names_slot_expected

def test_title_absent_aliases(title_absent_aliases_slot, title_absent_aliases_slot_expected):
    assert extractSlotName(title_absent_aliases_slot) == title_absent_aliases_slot_expected

def test_title_absent_structured_aliases(title_absent_structured_aliases_slot, title_absent_structured_aliases_slot_expected):
    assert extractSlotName(title_absent_structured_aliases_slot) == title_absent_structured_aliases_slot_expected

def test_title_absent_local_names(title_absent_local_names_slot, title_absent_local_names_slot_expected):
    assert extractSlotName(title_absent_local_names_slot) == title_absent_local_names_slot_expected

def test_title_absent_aliases_structured_aliases_local_names(title_absent_aliases_structured_aliases_local_names_slot, title_absent_aliases_structured_aliases_local_names_slot_expected):
    assert extractSlotName(title_absent_aliases_structured_aliases_local_names_slot) == title_absent_aliases_structured_aliases_local_names_slot_expected

def test_capitalize_label(capitalize_label_source, capitalize_label_expected):
    assert capitalizeLabel(capitalize_label_source) == capitalize_label_expected

def test_capitalize_label2(capitalize_label_source2, capitalize_label_expected2):
    assert capitalizeLabel(capitalize_label_source2) == capitalize_label_expected2

def test_capitalize_label_empty(capitalize_label_empty, capitalize_label_empty_expected):
    assert capitalizeLabel(capitalize_label_empty) == capitalize_label_empty_expected
