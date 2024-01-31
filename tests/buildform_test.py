import os
from test_fixtures import *
from test_fixtures_full_files import *
from utils import *
from LinkMLFormbuilder.formbuilder import buildForm

def test_patient_partial_form(yaml_patient_partial, patient_partial_form_expected):
    assert normalize(buildForm(yaml_patient_partial, True, "cwd", "default", True)) == normalize(patient_partial_form_expected)
    os.remove(os.path.join(os.getcwd(), "Zorginformatiebouwstenen_(ZIB)_2020.html"))

def test_three_zibs_form(yaml_3ZIB_complex, three_zibs_form_expected):
    assert normalize(buildForm(yaml_3ZIB_complex, True, "cwd", "default", True)) == normalize(three_zibs_form_expected)
    os.remove(os.path.join(os.getcwd(), "3Zorginformatiebouwstenen_(ZIB)_2020.html"))