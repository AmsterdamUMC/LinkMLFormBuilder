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

# the tests below require the user to manually delete the HTML files: personinfo.html and personinfo5.html. This is due to the file not being closed when errors are thrown

def test_tutorial1_yaml(tutorial1_yaml, tutorial1_yaml_expected):
    with pytest.raises(TypeError) as excinfo:
        buildForm(tutorial1_yaml, True, "cwd", "default", True)    
    assert tutorial1_yaml_expected in str(excinfo.value)
    
def test_tutorial1_no_name_yaml(tutorial1_no_name_yaml, tutorial1_no_name_yaml_expected):
    with pytest.raises(TypeError) as excinfo:
        buildForm(tutorial1_no_name_yaml, True, "cwd", "default", True)    
    assert tutorial1_no_name_yaml_expected in str(excinfo.value)

def test_tutorial5_yaml(tutorial5_yaml, tutorial5_yaml_expected):
    with pytest.raises(TypeError) as excinfo:
        buildForm(tutorial5_yaml, True, "cwd", "default", True)    
    assert tutorial5_yaml_expected in str(excinfo.value)
