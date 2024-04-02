import pytest
import yaml
from utils import getDefaultRangeCode

# The LinkML slot syntax is incomplete in these fixtures, this is on purpose as in real-world cases this is the format the called functions will receive

@pytest.fixture(scope='session')
def yamlfile():
    return yaml.safe_load('''
    id: new_blood_pressure_model
    name: new_blood_pressure_model
    title: New blood pressure model
    last_updated_on: "2024-01-05T15:34:00"
    prefixes:
        snomed: http://snomed.info/sct/
        linkml: https://w3id.org/linkml/
        default_range: string
        default_prefix: snomed

    classes:
        blood_pressure:
            name: blood_pressure
            title: Blood pressure
            description: The procedure in which a patient's blood pressure is taken
            definition_uri: snomed:46973005
            last_updated_on: "2024-01-24T14:24:00"
            slots:
                - systolic_pressure
                - diastolic_pressure
                - measurement_datetime
                - measurement_location
                - diastolic_endpoint
                - diastolic_endpoint2
                - average_systolic_pressure
                - average_diastolic_pressure
                - patient_body_position
                - cuff_size
                - measurement_method
                - mean_arterial_pressure
                - pulse_pressure
                - explanatory_statement

    imports:
        - linkml:types

    slots:
        systolic_pressure:
            name: systolic_pressure
            title: Systolic pressure
            required: true
            description: Systolic pressure in mmHg
            definition_uri: snomed:271649006
            range: integer
            unit: 
            exact_mappings: 
                - snomed:259018001
        diastolic_pressure:
            name: diastolic_pressure
            title: Diastolic pressure
            required: true
            description: Diastolic pressure in mmHg
            definition_uri: snomed:271650006
            range: integer
            unit: 
            exact_mappings:
                - snomed:259018001
        measurement_datetime:
            name: measurement_datetime
            title: Measurement datetime
            required: true
            description: The date and time at which the measurement took place
            definition_uri: snomed:118575009
            range: datetime
        measurement_location:
            name: measurement_location
            title: Measurement location
            description: The anatomical location of the blood pressure cuff on the patient during the measurement
            definition_uri: snomed:758637006
            values_from:
                - measurement_location_valueset 
        diastolic_endpoint:
            name: diastolic_endpoint
            title: Diastolic endpoint
            description: The diastolic endpoint, also called Korotkoff sounds
            definition_uri: snomed:85549003
            values_from:
                - diastolic_endpoint_valueset
        diastolic_endpoint2:
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
        average_systolic_pressure:
            name: average_systolic_pressure
            title: Average systolic pressure
            description: The average of the systolic blood pressure values of this patient in mmHg
            definition_uri: snomed:314440001
            range: integer
            unit: 
            exact_mappings:
                - snomed:259018001
        average_diastolic_pressure:
            name: average_diastolic_pressure
            title: Average diastolic pressure
            description: The average of the diastolic blood pressure values of this patient in mmHg
            definition_uri: snomed:314453003
            range: integer
            unit: 
            exact_mappings:
                - snomed:259018001
        patient_body_position:
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
        cuff_size:
            name: cuff_size
            title: Cuff size
            description: Blood pressure cuff size
            definition_uri: snomed:722471002
            values_from:
                - cuff_size_valueset
        measurement_method:
            name: measurement_method
            title: Measurement method
            description: The method used to perform the blood pressure measurement
            definition_uri: snomed:370129005
            values_from:
                - measurement_method_valueset
        mean_arterial_pressure:
            name: mean_arterial_pressure
            title: Mean arterial pressure
            description: The average arterial pressure throughout one cardiac cycle, systole, and diastole in mmHg
            definition_uri: snomed:1285244000
            unit: 
            exact_mappings:
                - snomed:259018001
            range: float
        pulse_pressure:
            name: pulse_pressure
            title: Pulse pressure
            description: The difference between systolic and diastolic blood pressure in mmHg
            definition_uri: snomed:392571003 
            unit: 
            exact_mappings:
                - snomed:259018001
            range: integer
        explanatory_statement:
            name: explanatory_statement
            title: Explanatory statement
            description: Additional information that cannot be coded
            definition_uri: snomed:900000000000519001
            range: string

    enums:
        diastolic_endpoint_valueset:
            name: diastolic_endpoint_valueset
            title: Diastolic endpoint valueset
            reachable_from:
                source_ontology: snomed
                source_nodes:
                    - snomed:272108007
                include_self: false
                relationship_types:
                    - rdfs:subClassOf
        cuff_size_valueset:
            name: cuff_size_valueset
            title: Cuff size valueset
            permissible_values: 
                normal:
                    meaning: snomed:17621005
                large:
                    meaning: snomed:255509001
                small:
                    meaning: snomed:255507004
                extra large:
                    meaning: snomed:258262008
                child:
                    meaning: snomed:67822003
                young child:
                    meaning: snomed:74489007
                neonate:
                    meaning: snomed:133933007
        measurement_location_valueset:
            name: measurement_location_valueset
            title: Measurement location valueset
            permissible_values:
                upper arm structure:
                    meaning: snomed:40983000
                right upper arm structure:
                    meaning: snomed:368209003
                left upper arm structure:
                    meaning: snomed:368208006
                thigh structure:
                    meaning: snomed:68367000
                right thigh structure:
                    meaning: snomed:11207009
                left thigh structure:
                    meaning: snomed:61396006
                wrist region structure:
                    meaning: snomed:8205005
                right wrist region structure:
                    meaning: snomed:9736006
                left wrist region structure:
                    meaning: snomed:5951000
                finger structure:
                    meaning: snomed:7569003
                ankle region structure:
                    meaning: snomed:344001
                right ankle region structure:
                    meaning: snomed:6685009
                left ankle region structure:
                    meaning: snomed:51636004
                toe structure:
                    meaning: snomed:29707007
                intra-arterial:
                    meaning: snomed:229801003
        measurement_method_valueset:
            name: measurement_method_valueset
            title: Measurement method valueset
            permissible_values:
                non-invasive:
                    meaning: snomed:22762002
                measurement of blood pressure using cuff method:
                    meaning: snomed:371911009
                measurement of blood pressure using automatic blood pressure monitor:
                    meaning: snomed:17146006
                invasive: 
                    meaning: snomed:10179008
''')

@pytest.fixture(scope='session')
def yaml_patient_partial():
    return yaml.safe_load('''
    id: 2.16.840.1.113883.2.4.3.11.60.121
    name: Zorginformatiebouwstenen_(ZIB)_2020
    structured_aliases:
        - literal_form: Zorginformatiebouwstenen (ZIB) 2020
        - literal_form: Health and Care Information Models (HCIM) 2020
    last_updated_on: "2023-07-06T18:06:20"
    prefixes:
        zib2020bbr-: https://decor.nictiz.nl/ad/#/zib2020bbr-/ 
        snomed: https://browser.ihtsdotools.org/?perspective=full&conceptId1= 
        loinc: https://loinc.org/ 
        hl7: http://terminology.hl7.org/CodeSystem/v3- 
        vektis: https://www.vektis.nl/standaardisatie/codelijsten/ 
        rdfs: http://www.w3.org/2000/01/rdf-schema# 
        linkml: https://w3id.org/linkml/ 
    default_prefix: zib2020bbr-
    default_range: string

    classes:
        NlZorgPatientAdresgegevensContainer:
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.0.1.4
            name: NlZorgPatientAdresgegevensContainer
            description: Adresgegevens van de patiënt.
            alt_descriptions:
                - description: Patients address information.
                  source: Nictiz
            structured_aliases:
                - literal_form: Adresgegevens
                - literal_form: AddressInformation
            last_updated_on: "2020-09-01T00:00:00"
            slots:
                - nl_zorg_part_Adresgegevens_Huisnummer
                - nl_zorg_part_Adresgegevens_Huisnummerletter
                - nl_zorg_part_Adresgegevens_Huisnummertoevoeging
                - nl_zorg_part_Adresgegevens_AanduidingBijNummer
                - nl_zorg_part_Adresgegevens_Gemeente
                - nl_zorg_part_Adresgegevens_Land
        Nl.zorg.Patient:
            source: 2.16.840.1.113883.2.4.3.11.60.40.3.0.1
            name: Nl.zorg.Patient
            description: <p><b>Concept</b></p> <p>Een persoon die medische, psychische, paramedische of verpleegkundige zorg ontvangt. In sommige zorgsectoren wordt in plaats van de term patient de term client of deelnemer gebruikt.</p> <p><b>Purpose</b></p> <p>Het vastleggen van de relevante gegevens ten behoeve van identificatie van de patiënt, voor administratieve doeleinden en procesondersteuning.</p> <p><b>Evidence Base</b></p> <p>Hoewel de term Patiënt niet in alle zorgsectoren gebruikt wordt, is er niet voor gekozen de naam van de zib te wijzigen in Persoon als overkoepelende aanduiding voor patiënt, cliënt, deelnemer, etc. omdat het begrip Persoon breder is dan het hier bedoelde concept. Zorgverleners en Contactpersonen zijn uiteindelijk ook personen.<br/><br/>De naam en adresgegevens zijn gebaseerd op de gegevensset van de Gemeentelijk Basis Administratie (GBA) en op de Nederlandse implementatiehandleiding HL7v3 Basiscomponenten.<br/><br/>De gegevens die bij de wettelijk verplichte verificatie van een BSN door de SBV-Z worden opgeleverd zijn eveneens conform de GBA specificatie.<br/><br/>Daarnaast is bij het vaststellen van de set gekeken naar de in de AWBZ zorg gebruikte AZR (AWBZ-brede zorgregistratie) gegevensset.<br/><br/>Gebruik van patiënt- en persoonsgegevens dient te voldoen aan de Wet Bescherming Persoonsgegevens. In deze wet wordt beschreven dat het verboden is om niet-noodzakelijke persoonsgegevens te verwerken en dat op een nadenkende en fatsoenlijke wijze met verkregen persoonsgegevens omgegaan wordt (Kohnstamm, 2006). Patiëntgegevens vastgelegd in een (elektronisch) patiëntendossier of in een elektronisch bericht dienen in de context van de Wet Bescherming Persoonsgegevens beschouwd te worden. Daarnaast dienen gezondheidszorginstellingen te voldoen aan de norm Informatiebeveiliging NEN 7510. Het toezicht op naleving van de WBP ligt bij het college Bescherming persoonsgegevens (CBP). Voor het toezicht op de informatiebeveiliging in de zorg zijn het CBP en de Inspectie voor de gezondheidszorg (IGZ) gezamenlijk verantwoordelijk (CBP, IGZ, 2008).<br/>Om die redenen zijn een aantal persoonsgegevens, die in sommige landen als administratieve gegevens beschouwd worden, niet in deze bouwsteen maar in de bouwstenen voor de Sociale Anamnese opgenomen.</p> <p><b>Example Instances</b></p> <p><img src="http//decor.nictiz.nl/decor/data/projects/zib2020bbr/zib2020bbr-images/nl.zorg.Patient-3.2-ExampleInstances-366593607-1.png" alt="nl.zorg.Patient-3.2-ExampleInstances-366593607-1.png" style="width392px; height798px;"/></p> <p><b>Instructions</b></p> <p>Indien zowel een naam als een identificatienummer wordt meegegeven, moet, voor verificatiedoeleinden, de naam overeenkomen met de naam die bij het identifcatienummer geregistreerd is.</p> <p><b>References</b></p> <p>1. DCM Patientgegevens V0.91. [Online] Beschikbaar op http//www.nictiz.nl/uploaded/FILES/htmlcontent/dcm/Nictiz/DCMPatientgegevens_V_0.91loNL.pdf [Geraadpleegd 23 februari 2015].<br/><br/>2. Implementatiehandleiding HL7v3 Basiscomponenten, Stichting HL7 Nederland [Online] Beschikbaar op <a href="http//www.hl7.nl/images/downloads/Implementatiehandleiding%20HL7v3%20Basiscomponenten%20%202.3NL_secure.pdf">http//www.hl7.nl/images/downloads/Implementatiehandleiding%20HL7v3%20Basiscomponenten%20%202.3NL_secure.pdf</a> [Geraadpleegd 23 februari 2015].</p> <p><b>Revision History</b></p> <p><u>Publicatieversie 1.0</u> (15-02-2013)<br/>-<br/><br/><u>Publicatieversie 1.1</u> (01-07-2013)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-33" target="_new">ZIB-33</a>.<br/><br/><u>Publicatieversie 2.0</u> (01-04-2015)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-62" target="_new">ZIB-62</a>, <a href="https//bits.nictiz.nl/browse/ZIB-67" target="_new">ZIB-67</a>, <a href="https//bits.nictiz.nl/browse/ZIB-96" target="_new">ZIB-96</a>, <a href="https//bits.nictiz.nl/browse/ZIB-97" target="_new">ZIB-97</a>, <a href="https//bits.nictiz.nl/browse/ZIB-98" target="_new">ZIB-98</a>, <a href="https//bits.nictiz.nl/browse/ZIB-99" target="_new">ZIB-99</a>, <a href="https//bits.nictiz.nl/browse/ZIB-100" target="_new">ZIB-100</a>, <a href="https//bits.nictiz.nl/browse/ZIB-102" target="_new">ZIB-102</a>, <a href="https//bits.nictiz.nl/browse/ZIB-121" target="_new">ZIB-121</a>, <a href="https//bits.nictiz.nl/browse/ZIB-257" target="_new">ZIB-257</a>, <a href="https//bits.nictiz.nl/browse/ZIB-258" target="_new">ZIB-258</a>, <a href="https//bits.nictiz.nl/browse/ZIB-259" target="_new">ZIB-259</a>, <a href="https//bits.nictiz.nl/browse/ZIB-260" target="_new">ZIB-260</a>, <a href="https//bits.nictiz.nl/browse/ZIB-261" target="_new">ZIB-261</a>, <a href="https//bits.nictiz.nl/browse/ZIB-262" target="_new">ZIB-262</a>, <a href="https//bits.nictiz.nl/browse/ZIB-303" target="_new">ZIB-303</a>, <a href="https//bits.nictiz.nl/browse/ZIB-308" target="_new">ZIB-308</a>, <a href="https//bits.nictiz.nl/browse/ZIB-349" target="_new">ZIB-349</a>, <a href="https//bits.nictiz.nl/browse/ZIB-350" target="_new">ZIB-350</a>, <a href="https//bits.nictiz.nl/browse/ZIB-351" target="_new">ZIB-351</a>, <a href="https//bits.nictiz.nl/browse/ZIB-353" target="_new">ZIB-353</a>.<br/><br/>Incl. algemene wijzigingsverzoeken <br/><a href="https//bits.nictiz.nl/browse/ZIB-94" target="_new">ZIB-94</a>, <a href="https//bits.nictiz.nl/browse/ZIB-154" target="_new">ZIB-154</a>, <a href="https//bits.nictiz.nl/browse/ZIB-200" target="_new">ZIB-200</a>, <a href="https//bits.nictiz.nl/browse/ZIB-201" target="_new">ZIB-201</a>, <a href="https//bits.nictiz.nl/browse/ZIB-309" target="_new">ZIB-309</a>, <a href="https//bits.nictiz.nl/browse/ZIB-324" target="_new">ZIB-324</a>, <a href="https//bits.nictiz.nl/browse/ZIB-326" target="_new">ZIB-326</a>.<br/><br/><u>Publicatieversie 2.0.1</u> (22-05-2015)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-385" target="_new">ZIB-385</a>, <a href="https//bits.nictiz.nl/browse/ZIB-374" target="_new">ZIB-374</a>.<br/><br/><u>Publicatieversie 3.0</u> (01-05-2016)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-453" target="_new">ZIB-453</a>.<br/><br/><u>Publicatieversie 3.1</u> (04-09-2017)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-429" target="_new">ZIB-429</a>, <a href="https//bits.nictiz.nl/browse/ZIB-430" target="_new">ZIB-430</a>, <a href="https//bits.nictiz.nl/browse/ZIB-442" target="_new">ZIB-442</a>, <a href="https//bits.nictiz.nl/browse/ZIB-471" target="_new">ZIB-471</a>, <a href="https//bits.nictiz.nl/browse/ZIB-491" target="_new">ZIB-491</a>, <a href="https//bits.nictiz.nl/browse/ZIB-564" target="_new">ZIB-564</a>.<br/><br/><u>Publicatieversie 3.1.1</u> (01-10-2018)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-647" target="_new">ZIB-647</a>.<br/><br/>Publicatieversie <u>3.2</u> (01-09-2020)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-961" target="_new">ZIB-961</a>, <a href="https//bits.nictiz.nl/browse/ZIB-1029" target="_new">ZIB-1029</a>, <a href="https//bits.nictiz.nl/browse/ZIB-1189" target="_new">ZIB-1189</a>.</p>
            alt_descriptions:
                - description: <p><b>Concept</b></p> <p>A person who receives medical, psychological, paramedical or nursing care. In some care settings, the term client or participant is used instead of the term patient.</p> <p><b>Purpose</b></p> <p>Recording relevant information to identify the patient for administrative purposes and process support.</p> <p><b>Evidence Base</b></p> <p>Although the term Patient is not used in all care settings, it has been decided not to change the name of the zib to Person as the overall name for Patient, Client, Participant, etc. because the concept Person is broader than the concept referred to here. Healthprofessionals and contact persons are ultimately also Persons.<br/>The name and address information is based on the information set of the Municipal Personal Records Database (GBA) and on the Dutch Implementation Guide HL7v3 Basic Components. <br/><br/>The information for the legally required verification of a social security number provided by the SBV-Z also follows GBA specifications. <br/><br/>Furthermore, the AZR (AWBZ-wide healthcare registration) data set used in AWBZ healthcare served as a base in determining the set. <br/><br/>Use of patient and personal details must follow the Personal Data Protection Act. This law prohibits processing non-essential personal data and mandates decent and reasonable processing of obtained personal data (Kohnstamm, 2006). Patient data recorded in (electronic) patient records or in digital messages must be handled in the context of the Personal Data Protection Act. Furthermore, healthcare centers must meet the Information Security NEN 7510 standard. Observance of the PDPA is monitored by the Dutch Data Protection Authority (CBP). The CBP and the Healthcare Inspectorate (IGZ) are jointly responsible for monitoring information security in healthcare (CBP, IGZ, 2008). <br/>For those reasons, some personal data, seen in some countries as administrative data, are not included in this information model but in the information models for the Social Anamnesis.<br/></p> <p><b>Example Instances</b></p> <p><img src="http//decor.nictiz.nl/decor/data/projects/zib2020bbr/zib2020bbr-images/nl.zorg.Patient-3.2-ExampleInstances-366593607-1.png" alt="nl.zorg.Patient-3.2-ExampleInstances-366593607-1.png" style="width392px; height798px;"/></p> <p><b>Instructions</b></p> <p>If both a name and an identification number are given, the name must match the name registered under that identification number, for verification purposes.</p>
                  source: Nictiz
            structured_aliases:
                - literal_form: nl.zorg.Patient
            last_updated_on: "2020-09-01T00:00:00"
            comments:
                - DatasetRoot
            slots:
                - nl_zorg_Patient_Adresgegevens
                - nl_zorg_Patient_Geslacht
                - nl_zorg_Patient_MeerlingIndicator
                - nl_zorg_Patient_OverlijdensIndicator
    imports: 
        - linkml:types
    slots:
        nl_zorg_Patient_Adresgegevens: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.0.1.4
            name: nl_zorg_Patient_Adresgegevens
            title: Adresgegevens
            structured_aliases:
                - literal_form: Adresgegevens
                - literal_form: AddressInformation
            range: NlZorgPatientAdresgegevensContainer
        nl_zorg_part_Adresgegevens_Huisnummer: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.20.5.12
            name: nl_zorg_part_Adresgegevens_Huisnummer
            title: Huisnummer
            structured_aliases:
                - literal_form: Huisnummer
                - literal_form: HouseNumber
            range: string
        nl_zorg_part_Adresgegevens_Huisnummerletter: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.20.5.11
            name: nl_zorg_part_Adresgegevens_Huisnummerletter
            title: Huisnummerletter
            structured_aliases:
                - literal_form: Huisnummerletter
                - literal_form: HouseNumberLetter
            range: string
        nl_zorg_part_Adresgegevens_Huisnummertoevoeging: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.20.5.10
            name: nl_zorg_part_Adresgegevens_Huisnummertoevoeging
            title: Huisnummertoevoeging
            structured_aliases:
                - literal_form: Huisnummertoevoeging
                - literal_form: HouseNumberAddition
            range: string
        nl_zorg_part_Adresgegevens_AanduidingBijNummer: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.20.5.9
            name: nl_zorg_part_Adresgegevens_AanduidingBijNummer
            title: AanduidingBijNummer
            structured_aliases:
                - literal_form: AanduidingBijNummer
                - literal_form: HouseNumberIndication
            values_from: 
                - AanduidingBijNummerCodelijst
        nl_zorg_part_Adresgegevens_Gemeente: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.20.5.4
            name: nl_zorg_part_Adresgegevens_Gemeente
            title: Gemeente
            structured_aliases:
                - literal_form: Gemeente
                - literal_form: Municipality
            range: string
        nl_zorg_part_Adresgegevens_Land: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.20.5.5
            name: nl_zorg_part_Adresgegevens_Land
            title: Land
            structured_aliases:
                - literal_form: Land
                - literal_form: Country
            values_from: 
                - LandGBACodelijst
                - LandISOCodelijst
        nl_zorg_Patient_Geslacht: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.0.1.9
            name: nl_zorg_Patient_Geslacht
            title: Geslacht
            structured_aliases:
                - literal_form: Geslacht
                - literal_form: Gender
            values_from: 
                - GeslachtCodelijst
        nl_zorg_Patient_MeerlingIndicator: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.0.1.31
            name: nl_zorg_Patient_MeerlingIndicator
            title: MeerlingIndicator
            structured_aliases:
                - literal_form: MeerlingIndicator
                - literal_form: MultipleBirthIndicator
            range: boolean
        nl_zorg_Patient_OverlijdensIndicator: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.0.1.32
            name: nl_zorg_Patient_OverlijdensIndicator
            title: OverlijdensIndicator
            structured_aliases:
                - literal_form: OverlijdensIndicator
                - literal_form: DeathIndicator
            range: boolean
    enums:
        AanduidingBijNummerCodelijst:
            enum_uri: 2.16.840.1.113883.2.4.3.11.60.40.2.20.5.4
            name: AanduidingBijNummerCodelijst
            last_updated_on: "2020-09-01T00:00:00"
            permissible_values: 
                Tegenover:
                    meaning: AanduidingBijHuisnummer:to
                Bij:
                    meaning: AanduidingBijHuisnummer:by
        LandISOCodelijst: 
            enum_uri: 2.16.840.1.113883.2.4.3.11.60.40.2.20.5.2
            name: LandISOCodelijst
            last_updated_on: "2020-09-01T00:00:00"
            description: ISO 3166-1 (alpha-2) - Alle waarden
            reachable_from:
                source_ontology: zib2020bbr-
                source_nodes: 
                    - urn:iso:std:iso:3166
                include_self: false
                relationship_types:
                    - rdfs:subClassOf
        GeslachtCodelijst:
            enum_uri: 2.16.840.1.113883.2.4.3.11.60.40.2.17.1.8
            name: GeslachtCodelijst
            last_updated_on: "2020-09-01T00:00:00"
            permissible_values: 
                Undifferentiated:
                    meaning: Administrative_Gender:UN
                Male:
                    meaning: Administrative_Gender:M
                Female:
                    meaning: Administrative_Gender:F
                Unknown:
                    meaning: Administrative_Gender:UNK
    types:
        count: 
            uri: xsd:integer 
            base: int
        quantity: 
            uri: xsd:integer 
            base: int
        complex: 
            uri: xsd:string 
            base: str
        identifier: 
            uri: xsd:integer 
            base: int
        blob:
            uri: xsd:string
            base: str
    ''')

@pytest.fixture(scope='session')
def yaml_3ZIB_complex():
    return yaml.safe_load('''
    id: 2.16.840.1.113883.2.4.3.11.60.121
    name: 3Zorginformatiebouwstenen_(ZIB)_2020
    structured_aliases:
        - literal_form: Zorginformatiebouwstenen (ZIB) 2020
        - literal_form: Health and Care Information Models (HCIM) 2020
    last_updated_on: "2023-07-06T18:06:20"
    prefixes:
        zib2020bbr-: https://decor.nictiz.nl/ad/#/zib2020bbr-/ 
        snomed: https://browser.ihtsdotools.org/?perspective=full&conceptId1= 
        loinc: https://loinc.org/ 
        hl7: http://terminology.hl7.org/CodeSystem/v3- 
        vektis: https://www.vektis.nl/standaardisatie/codelijsten/ 
        rdfs: http://www.w3.org/2000/01/rdf-schema# 
        linkml: https://w3id.org/linkml/ 
    default_prefix: zib2020bbr-
    default_range: string

    classes:
        NlZorgPatientAdresgegevensContainer:
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.0.1.4
            name: NlZorgPatientAdresgegevensContainer
            description: Adresgegevens van de patiënt.
            alt_descriptions:
                - description: Patients address information.
                  source: Nictiz
            structured_aliases:
                - literal_form: Adresgegevens
                - literal_form: AddressInformation
            last_updated_on: "2020-09-01T00:00:00"
            slots:
                - nl_zorg_part_Adresgegevens_Huisnummer
                - nl_zorg_part_Adresgegevens_Huisnummerletter
                - nl_zorg_part_Adresgegevens_Huisnummertoevoeging
                - nl_zorg_part_Adresgegevens_Gemeente
        Nl.zorg.Patient:
            source: 2.16.840.1.113883.2.4.3.11.60.40.3.0.1
            name: Nl.zorg.Patient
            description: <p><b>Concept</b></p> <p>Een persoon die medische, psychische, paramedische of verpleegkundige zorg ontvangt. In sommige zorgsectoren wordt in plaats van de term patient de term client of deelnemer gebruikt.</p> <p><b>Purpose</b></p> <p>Het vastleggen van de relevante gegevens ten behoeve van identificatie van de patiënt, voor administratieve doeleinden en procesondersteuning.</p> <p><b>Evidence Base</b></p> <p>Hoewel de term Patiënt niet in alle zorgsectoren gebruikt wordt, is er niet voor gekozen de naam van de zib te wijzigen in Persoon als overkoepelende aanduiding voor patiënt, cliënt, deelnemer, etc. omdat het begrip Persoon breder is dan het hier bedoelde concept. Zorgverleners en Contactpersonen zijn uiteindelijk ook personen.<br/><br/>De naam en adresgegevens zijn gebaseerd op de gegevensset van de Gemeentelijk Basis Administratie (GBA) en op de Nederlandse implementatiehandleiding HL7v3 Basiscomponenten.<br/><br/>De gegevens die bij de wettelijk verplichte verificatie van een BSN door de SBV-Z worden opgeleverd zijn eveneens conform de GBA specificatie.<br/><br/>Daarnaast is bij het vaststellen van de set gekeken naar de in de AWBZ zorg gebruikte AZR (AWBZ-brede zorgregistratie) gegevensset.<br/><br/>Gebruik van patiënt- en persoonsgegevens dient te voldoen aan de Wet Bescherming Persoonsgegevens. In deze wet wordt beschreven dat het verboden is om niet-noodzakelijke persoonsgegevens te verwerken en dat op een nadenkende en fatsoenlijke wijze met verkregen persoonsgegevens omgegaan wordt (Kohnstamm, 2006). Patiëntgegevens vastgelegd in een (elektronisch) patiëntendossier of in een elektronisch bericht dienen in de context van de Wet Bescherming Persoonsgegevens beschouwd te worden. Daarnaast dienen gezondheidszorginstellingen te voldoen aan de norm Informatiebeveiliging NEN 7510. Het toezicht op naleving van de WBP ligt bij het college Bescherming persoonsgegevens (CBP). Voor het toezicht op de informatiebeveiliging in de zorg zijn het CBP en de Inspectie voor de gezondheidszorg (IGZ) gezamenlijk verantwoordelijk (CBP, IGZ, 2008).<br/>Om die redenen zijn een aantal persoonsgegevens, die in sommige landen als administratieve gegevens beschouwd worden, niet in deze bouwsteen maar in de bouwstenen voor de Sociale Anamnese opgenomen.</p> <p><b>Example Instances</b></p> <p><img src="http//decor.nictiz.nl/decor/data/projects/zib2020bbr/zib2020bbr-images/nl.zorg.Patient-3.2-ExampleInstances-366593607-1.png" alt="nl.zorg.Patient-3.2-ExampleInstances-366593607-1.png" style="width392px; height798px;"/></p> <p><b>Instructions</b></p> <p>Indien zowel een naam als een identificatienummer wordt meegegeven, moet, voor verificatiedoeleinden, de naam overeenkomen met de naam die bij het identifcatienummer geregistreerd is.</p> <p><b>References</b></p> <p>1. DCM Patientgegevens V0.91. [Online] Beschikbaar op http//www.nictiz.nl/uploaded/FILES/htmlcontent/dcm/Nictiz/DCMPatientgegevens_V_0.91loNL.pdf [Geraadpleegd 23 februari 2015].<br/><br/>2. Implementatiehandleiding HL7v3 Basiscomponenten, Stichting HL7 Nederland [Online] Beschikbaar op <a href="http//www.hl7.nl/images/downloads/Implementatiehandleiding%20HL7v3%20Basiscomponenten%20%202.3NL_secure.pdf">http//www.hl7.nl/images/downloads/Implementatiehandleiding%20HL7v3%20Basiscomponenten%20%202.3NL_secure.pdf</a> [Geraadpleegd 23 februari 2015].</p> <p><b>Revision History</b></p> <p><u>Publicatieversie 1.0</u> (15-02-2013)<br/>-<br/><br/><u>Publicatieversie 1.1</u> (01-07-2013)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-33" target="_new">ZIB-33</a>.<br/><br/><u>Publicatieversie 2.0</u> (01-04-2015)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-62" target="_new">ZIB-62</a>, <a href="https//bits.nictiz.nl/browse/ZIB-67" target="_new">ZIB-67</a>, <a href="https//bits.nictiz.nl/browse/ZIB-96" target="_new">ZIB-96</a>, <a href="https//bits.nictiz.nl/browse/ZIB-97" target="_new">ZIB-97</a>, <a href="https//bits.nictiz.nl/browse/ZIB-98" target="_new">ZIB-98</a>, <a href="https//bits.nictiz.nl/browse/ZIB-99" target="_new">ZIB-99</a>, <a href="https//bits.nictiz.nl/browse/ZIB-100" target="_new">ZIB-100</a>, <a href="https//bits.nictiz.nl/browse/ZIB-102" target="_new">ZIB-102</a>, <a href="https//bits.nictiz.nl/browse/ZIB-121" target="_new">ZIB-121</a>, <a href="https//bits.nictiz.nl/browse/ZIB-257" target="_new">ZIB-257</a>, <a href="https//bits.nictiz.nl/browse/ZIB-258" target="_new">ZIB-258</a>, <a href="https//bits.nictiz.nl/browse/ZIB-259" target="_new">ZIB-259</a>, <a href="https//bits.nictiz.nl/browse/ZIB-260" target="_new">ZIB-260</a>, <a href="https//bits.nictiz.nl/browse/ZIB-261" target="_new">ZIB-261</a>, <a href="https//bits.nictiz.nl/browse/ZIB-262" target="_new">ZIB-262</a>, <a href="https//bits.nictiz.nl/browse/ZIB-303" target="_new">ZIB-303</a>, <a href="https//bits.nictiz.nl/browse/ZIB-308" target="_new">ZIB-308</a>, <a href="https//bits.nictiz.nl/browse/ZIB-349" target="_new">ZIB-349</a>, <a href="https//bits.nictiz.nl/browse/ZIB-350" target="_new">ZIB-350</a>, <a href="https//bits.nictiz.nl/browse/ZIB-351" target="_new">ZIB-351</a>, <a href="https//bits.nictiz.nl/browse/ZIB-353" target="_new">ZIB-353</a>.<br/><br/>Incl. algemene wijzigingsverzoeken <br/><a href="https//bits.nictiz.nl/browse/ZIB-94" target="_new">ZIB-94</a>, <a href="https//bits.nictiz.nl/browse/ZIB-154" target="_new">ZIB-154</a>, <a href="https//bits.nictiz.nl/browse/ZIB-200" target="_new">ZIB-200</a>, <a href="https//bits.nictiz.nl/browse/ZIB-201" target="_new">ZIB-201</a>, <a href="https//bits.nictiz.nl/browse/ZIB-309" target="_new">ZIB-309</a>, <a href="https//bits.nictiz.nl/browse/ZIB-324" target="_new">ZIB-324</a>, <a href="https//bits.nictiz.nl/browse/ZIB-326" target="_new">ZIB-326</a>.<br/><br/><u>Publicatieversie 2.0.1</u> (22-05-2015)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-385" target="_new">ZIB-385</a>, <a href="https//bits.nictiz.nl/browse/ZIB-374" target="_new">ZIB-374</a>.<br/><br/><u>Publicatieversie 3.0</u> (01-05-2016)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-453" target="_new">ZIB-453</a>.<br/><br/><u>Publicatieversie 3.1</u> (04-09-2017)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-429" target="_new">ZIB-429</a>, <a href="https//bits.nictiz.nl/browse/ZIB-430" target="_new">ZIB-430</a>, <a href="https//bits.nictiz.nl/browse/ZIB-442" target="_new">ZIB-442</a>, <a href="https//bits.nictiz.nl/browse/ZIB-471" target="_new">ZIB-471</a>, <a href="https//bits.nictiz.nl/browse/ZIB-491" target="_new">ZIB-491</a>, <a href="https//bits.nictiz.nl/browse/ZIB-564" target="_new">ZIB-564</a>.<br/><br/><u>Publicatieversie 3.1.1</u> (01-10-2018)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-647" target="_new">ZIB-647</a>.<br/><br/>Publicatieversie <u>3.2</u> (01-09-2020)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-961" target="_new">ZIB-961</a>, <a href="https//bits.nictiz.nl/browse/ZIB-1029" target="_new">ZIB-1029</a>, <a href="https//bits.nictiz.nl/browse/ZIB-1189" target="_new">ZIB-1189</a>.</p>
            alt_descriptions:
                - description: <p><b>Concept</b></p> <p>A person who receives medical, psychological, paramedical or nursing care. In some care settings, the term client or participant is used instead of the term patient.</p> <p><b>Purpose</b></p> <p>Recording relevant information to identify the patient for administrative purposes and process support.</p> <p><b>Evidence Base</b></p> <p>Although the term Patient is not used in all care settings, it has been decided not to change the name of the zib to Person as the overall name for Patient, Client, Participant, etc. because the concept Person is broader than the concept referred to here. Healthprofessionals and contact persons are ultimately also Persons.<br/>The name and address information is based on the information set of the Municipal Personal Records Database (GBA) and on the Dutch Implementation Guide HL7v3 Basic Components. <br/><br/>The information for the legally required verification of a social security number provided by the SBV-Z also follows GBA specifications. <br/><br/>Furthermore, the AZR (AWBZ-wide healthcare registration) data set used in AWBZ healthcare served as a base in determining the set. <br/><br/>Use of patient and personal details must follow the Personal Data Protection Act. This law prohibits processing non-essential personal data and mandates decent and reasonable processing of obtained personal data (Kohnstamm, 2006). Patient data recorded in (electronic) patient records or in digital messages must be handled in the context of the Personal Data Protection Act. Furthermore, healthcare centers must meet the Information Security NEN 7510 standard. Observance of the PDPA is monitored by the Dutch Data Protection Authority (CBP). The CBP and the Healthcare Inspectorate (IGZ) are jointly responsible for monitoring information security in healthcare (CBP, IGZ, 2008). <br/>For those reasons, some personal data, seen in some countries as administrative data, are not included in this information model but in the information models for the Social Anamnesis.<br/></p> <p><b>Example Instances</b></p> <p><img src="http//decor.nictiz.nl/decor/data/projects/zib2020bbr/zib2020bbr-images/nl.zorg.Patient-3.2-ExampleInstances-366593607-1.png" alt="nl.zorg.Patient-3.2-ExampleInstances-366593607-1.png" style="width392px; height798px;"/></p> <p><b>Instructions</b></p> <p>If both a name and an identification number are given, the name must match the name registered under that identification number, for verification purposes.</p>
                  source: Nictiz
            structured_aliases:
                - literal_form: nl.zorg.Patient
            last_updated_on: "2020-09-01T00:00:00"
            comments:
                - DatasetRoot
            slots:
                - nl_zorg_Patient_Adresgegevens
                - nl_zorg_Patient_Geslacht
                - nl_zorg_Patient_OverlijdensIndicator
        Nl.zorg.Alert:
            source: 2.16.840.1.113883.2.4.3.11.60.40.3.8.3
            name: Nl.zorg.Alert
            description: <p><b>Concept</b></p> <p>Een alert beschrijft een klinisch of administratief feit dat onder de aandacht van de gebruikers van de klinische systemen wordt gebracht, om er bij het vormen van diagnostisch en therapeutisch beleid of bij de omgang met de patiënt rekening mee te houden, meestal wegens een veiligheidsrisico. <br/>Aandoeningen, die de overgevoeligheid van het lichaam voor een stof beschrijven, zich uitend in een specifieke fysiologische reactie na blootstelling, worden allergieën genoemd. Deze worden in een aparte bouwsteen beschreven<br/>Waarschuwingen voor niet allergische aandoeningen kunnen betreffen <br/><ul><li>Een aandoening, conditie of diagnose die beschouwd kan worden als contra-indicatie voor het ondergaan van een bepaalde therapie, zoals zwangerschap of een verlengd QT-syndroom; <br/></li> <li>Verminderde functie van een orgaansysteem (hartfalen, verminder lever- of nierfunctie, verminderde afweer); <br/></li> <li>Kans op verspreiding van bepaalde micro-organismen (multiresistente bacterie, tuberkelbacterie, HIV, HBV, Ebola virus); <br/></li> <li>Andere risico’s. </li></ul></p> <p><b>Purpose</b></p> <p>Het vastleggen en doorgeven van aandoeningen of condities die aandacht behoeven, is een belangrijk onderdeel van de medische registratie. Het raakt de kern van patiëntveiligheid. In de uitvoering van onderzoek en behandeling moet veelal continu rekening worden gehouden met deze, als waarschuwing gemarkeerde, patiëntkenmerken. Ze verschaffen informatie die belangrijk is in relatie met de conditie van de patiënt en de opties die een zorgverlener heeft voor therapie. Aandoeningen die als Alert worden geregistreerd of overgedragen, kunnen ook als Probleem worden beschreven. Het verschil is hierin gelegen, dat de zorgverlener het probleem heeft aangemerkt als Alert = waarschuwing. In veel gevallen zal overdracht onderworpen zijn aan sterke privacy regels, aangezien de waarschuwing niet altijd een adequate reactie van de geïnformeerde omgeving kan uitlokken.</p> <p><b>Example Instances</b></p> <p><img src="http//decor.nictiz.nl/decor/data/projects/zib2020bbr/zib2020bbr-images/nl.zorg.Alert-4.1-ExampleInstances-202057790-1.png" alt="nl.zorg.Alert-4.1-ExampleInstances-202057790-1.png" style="width600px; height123px;"/></p> <p><b>Instructions</b></p> <p>Indien sprake is van een contra-indicatie die tevens van belang is voor de medicatieveiligheid dient deze ook via de g-standaard (Thesaurus 40) te worden vastgelegd.  Zie hiervoor de bouwsteen MedicatieContraIndicatie</p> <p><b>Revision History</b></p> <p><u>Publicatieversie 1.0</u> (01-04-2015)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-109" target="_new">ZIB-109</a>, <a href="https//bits.nictiz.nl/browse/ZIB-132" target="_new">ZIB-132</a>, <a href="https//bits.nictiz.nl/browse/ZIB-203" target="_new">ZIB-203</a>, <a href="https//bits.nictiz.nl/browse/ZIB-204" target="_new">ZIB-204</a>, <a href="https//bits.nictiz.nl/browse/ZIB-306" target="_new">ZIB-306</a>, <a href="https//bits.nictiz.nl/browse/ZIB-308" target="_new">ZIB-308</a>, <a href="https//bits.nictiz.nl/browse/ZIB-352" target="_new">ZIB-352</a>.<br/><br/>Incl. algemene wijzigingsverzoeken <br/><a href="https//bits.nictiz.nl/browse/ZIB-94" target="_new">ZIB-94</a>, <a href="https//bits.nictiz.nl/browse/ZIB-154" target="_new">ZIB-154</a>, <a href="https//bits.nictiz.nl/browse/ZIB-200" target="_new">ZIB-200</a>, <a href="https//bits.nictiz.nl/browse/ZIB-201" target="_new">ZIB-201</a>, <a href="https//bits.nictiz.nl/browse/ZIB-309" target="_new">ZIB-309</a>, <a href="https//bits.nictiz.nl/browse/ZIB-324" target="_new">ZIB-324</a>, <a href="https//bits.nictiz.nl/browse/ZIB-326" target="_new">ZIB-326</a>.<br/><br/><u>Publicatieversie 3.0</u> (01-05-2016)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-438" target="_new">ZIB-438</a>, <a href="https//bits.nictiz.nl/browse/ZIB-453" target="_new">ZIB-453</a>, <a href="https//bits.nictiz.nl/browse/ZIB-574" target="_new">ZIB-574</a>.<br/><br/><u>Publicatieversie 3.1</u> (04-09-2017)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-546" target="_new">ZIB-546</a>.<br/><br/><u>Publicatieversie 3.2</u> (31-12-2017)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-593" target="_new">ZIB-593</a>. <br/><br/><u>Publicatieversie 3.3</u> (26-02-2019)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-682" target="_new">ZIB-682</a>. <br/><br/><u>Publicatieversie 3.4</u> (06-07-2019)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-813" target="_new">ZIB-813</a>. <br/><br/><u>Publicatieversie 4.0</u> (31-01-2020)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-905" target="_new">ZIB-905</a>, <a href="https//bits.nictiz.nl/browse/ZIB-526" target="_new">ZIB-526</a>.<br/><br/>Publicatieversie <u>4.1</u> (01-09-2020)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-1160" target="_new">ZIB-1160</a>, <a href="https//bits.nictiz.nl/browse/ZIB-1209" target="_new">ZIB-1209</a>.</p>
            alt_descriptions:
                - description: <p><b>Concept</b></p> <p>An alert describes a clinical or administrative fact brought to the attention of the users of the clinical systems to be taken into account when shaping diagnostic and therapeutic policy or in dealing with the patient, usually because of a safety risk. <br/>Disorders that describe the body’s sensitivity to a substance which results in a specific physiological reaction after being exposed to that substance are referred to as allergies. These are described in a separate information model. <br/>Warnings for non-allergic disorders can concern <br/><ul><li>A disorder, condition or diagnosis which can be considered as a contraindication for undergoing a certain type of therapy, such as pregnancy or long QT syndrome; <br/></li> <li>Impaired functioning of an organ system (heart failure, impaired liver or kidney function, weakened immune system); <br/></li> <li>Risk of spreading certain microorganisms (multi-resistant bacteria, tubercle bacilli, HIV, HBV, Ebola virus); <br/></li> <li>Other risks </li></ul></p> <p><b>Purpose</b></p> <p>Documenting and entering disorders or conditions that require attention is an important part of medical registration. It concerns the core of patient safety. In the execution of research and treatment, these patient characteristics - which are marked as a warning - constantly have to be taken into account. They provide information that is important for the patient’s condition and the options a healthcare provider has for therapy. Disorders that are registered or transferred as an Alert can also be described as a Problem. The difference is in the fact that the healthcare provider considers the problem as an Alert = warning. In many cases, transfer will be subject to strict privacy rules, as the warning will not always elicit an adequate reaction in the informed environment.</p> <p><b>Example Instances</b></p> <p><img src="http//decor.nictiz.nl/decor/data/projects/zib2020bbr/zib2020bbr-images/nl.zorg.Alert-4.1-ExampleInstances-202057790-1.png" alt="nl.zorg.Alert-4.1-ExampleInstances-202057790-1.png" style="width600px; height123px;"/></p> <p><b>Instructions</b></p> <p>If there is a contraindication which is also important for medication safety, it should also be registered via the g-standard (Thesaurus 40).  See further HCIM MedicationContraIndication.</p>
                  source: Nictiz
            structured_aliases:
                - literal_form: nl.zorg.Alert
            last_updated_on: "2020-09-01T00:00:00"
            comments:
                - DatasetRoot
            slots:
                - nl_zorg_Alert_AlertNaam
                - nl_zorg_Alert_BeginDatumTijd
                - nl_zorg_Alert_AlertType
                - nl_zorg_Alert_Toelichting
        Nl.zorg.Woonsituatie:
            source: 2.16.840.1.113883.2.4.3.11.60.40.3.7.8
            name: Nl.zorg.Woonsituatie
            description: <p><b>Concept</b></p> <p>De woonsituatie is de fysieke omgeving waarin de patiënt normaliter woont, slaapt, kleding bewaart, enz.</p> <p><b>Purpose</b></p> <p>Het doel is om de huidige woonsituatie van de patiënt in kaart te brengen. Dit in verband met huidige of eventuele toekomstige problemen die de patiënt ondervindt of zou kunnen ondervinden met betrekking tot het wonen in relatie met ziekte en de (toekomstige) beperkingen van de patiënt. <br/>Het vragen naar de woonsituatie van de patiënt kent meerdere redenen. Zo kan de woonsituatie van belang zijn bij de wens zelfstandig in de eigen woning te willen blijven wonen in het geval van ziekte en/of beperkingen (WMO, 2011; CIZ, 2011). Daarnaast is de woonsituatie van belang bij het inschatten van het valrisico, met name bij alleenwonenden (CMO, richtlijn valpreventie, 2004). </p> <p><b>Example Instances</b></p> <p><img src="http//decor.nictiz.nl/decor/data/projects/zib2020bbr/zib2020bbr-images/nl.zorg.Woonsituatie-3.3-ExampleInstances-984125332-1.png" alt="nl.zorg.Woonsituatie-3.3-ExampleInstances-984125332-1.png" style="width522px; height85px;"/></p> <p><b>Revision History</b></p> <p><u>Publicatieversie 1.0</u> (15-02-2013)<br/><br/><u>Publicatieversie 1.1</u> (01-07-2013)<br/><br/><u>Publicatieversie 1.2</u> (01-04-2015)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-162" target="_new">ZIB-162</a>, <a href="https//bits.nictiz.nl/browse/ZIB-283" target="_new">ZIB-283</a>, <a href="https//bits.nictiz.nl/browse/ZIB-284" target="_new">ZIB-284</a>, <a href="https//bits.nictiz.nl/browse/ZIB-308" target="_new">ZIB-308</a>.<br/><br/>Incl. algemene wijzigingsverzoeken <br/><a href="https//bits.nictiz.nl/browse/ZIB-94" target="_new">ZIB-94</a>, <a href="https//bits.nictiz.nl/browse/ZIB-154" target="_new">ZIB-154</a>, <a href="https//bits.nictiz.nl/browse/ZIB-200" target="_new">ZIB-200</a>, <a href="https//bits.nictiz.nl/browse/ZIB-201" target="_new">ZIB-201</a>, <a href="https//bits.nictiz.nl/browse/ZIB-309" target="_new">ZIB-309</a>, <a href="https//bits.nictiz.nl/browse/ZIB-324" target="_new">ZIB-324</a>, <a href="https//bits.nictiz.nl/browse/ZIB-326" target="_new">ZIB-326</a>.<br/><br/><u>Publicatieversie 3.0</u> (01-05-2016)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-453" target="_new">ZIB-453</a>.<br/><br/><u>Publicatieversie 3.1</u> (04-09-2017)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-561" target="_new">ZIB-561</a>, <a href="https//bits.nictiz.nl/browse/ZIB-564" target="_new">ZIB-564</a>.<br/><br/><u>Publicatieversie 3.2</u> (01-10-2018)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-653" target="_new">ZIB-653</a>.<br/><br/>Publicatieversie <u>3.3</u> (01-09-2020)<br/>Bevat <a href="https//bits.nictiz.nl/browse/ZIB-694" target="_new">ZIB-694</a>, <a href="https//bits.nictiz.nl/browse/ZIB-769" target="_new">ZIB-769</a>, <a href="https//bits.nictiz.nl/browse/ZIB-810" target="_new">ZIB-810</a>.</p>
            alt_descriptions:
                - description: <p><b>Concept</b></p> <p>The living situation is the physical environment in which the patient normally lives, sleeps, keeps their clothing, etc.</p> <p><b>Purpose</b></p> <p>The goal is to take stock of the patient’s current living situation. This is in regard to any current or future problems the patient encounters or could encounter when living with the disease and the patient’s (future) constraints. <br/>There are many reasons to ask about the patient’s living situation. The living situation can be relevant in the patient’s wish to live in their own home independently in the event of disease and/or disability (WMO, 2011; CIZ, 2011). Furthermore, the living situation is important in evaluating the risks of falling, particularly among people living alone (CMO, guidelines for fall prevention, 2004).<br/></p> <p><b>Example Instances</b></p> <p><img src="http//decor.nictiz.nl/decor/data/projects/zib2020bbr/zib2020bbr-images/nl.zorg.Woonsituatie-3.3-ExampleInstances-984125332-1.png" alt="nl.zorg.Woonsituatie-3.3-ExampleInstances-984125332-1.png" style="width522px; height85px;"/></p>
                  source: Nictiz
            structured_aliases:
                - literal_form: nl.zorg.Woonsituatie
                - literal_form: nl.zorg.LivingSituation
            last_updated_on: "2020-09-01T00:00:00"
            comments:
                - DatasetRoot
            slots:
                - nl_zorg_Woonsituatie_WoningAanpassing
                - nl_zorg_Woonsituatie_WoonOmstandigheid
    imports: 
        - linkml:types
    slots:
        nl_zorg_Patient_Adresgegevens: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.0.1.4
            name: nl_zorg_Patient_Adresgegevens
            title: Adresgegevens
            structured_aliases:
                - literal_form: Adresgegevens
                - literal_form: AddressInformation
            range: NlZorgPatientAdresgegevensContainer
        nl_zorg_part_Adresgegevens_Huisnummer: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.20.5.12
            name: nl_zorg_part_Adresgegevens_Huisnummer
            title: Huisnummer
            structured_aliases:
                - literal_form: Huisnummer
                - literal_form: HouseNumber
            range: string
        nl_zorg_part_Adresgegevens_Huisnummerletter: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.20.5.11
            name: nl_zorg_part_Adresgegevens_Huisnummerletter
            title: Huisnummerletter
            structured_aliases:
                - literal_form: Huisnummerletter
                - literal_form: HouseNumberLetter
            range: string
        nl_zorg_part_Adresgegevens_Huisnummertoevoeging: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.20.5.10
            name: nl_zorg_part_Adresgegevens_Huisnummertoevoeging
            title: Huisnummertoevoeging
            structured_aliases:
                - literal_form: Huisnummertoevoeging
                - literal_form: HouseNumberAddition
            range: string
        nl_zorg_part_Adresgegevens_Gemeente: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.20.5.4
            name: nl_zorg_part_Adresgegevens_Gemeente
            title: Gemeente
            structured_aliases:
                - literal_form: Gemeente
                - literal_form: Municipality
            range: string
        nl_zorg_Patient_Geslacht: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.0.1.9
            name: nl_zorg_Patient_Geslacht
            title: Geslacht
            structured_aliases:
                - literal_form: Geslacht
                - literal_form: Gender
            values_from: 
                - GeslachtCodelijst
        nl_zorg_Patient_OverlijdensIndicator: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.0.1.32
            name: nl_zorg_Patient_OverlijdensIndicator
            title: OverlijdensIndicator
            structured_aliases:
                - literal_form: OverlijdensIndicator
                - literal_form: DeathIndicator
            range: boolean
        nl_zorg_Alert_AlertNaam: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.8.3.4
            name: nl_zorg_Alert_AlertNaam
            title: AlertNaam
            structured_aliases:
                - literal_form: AlertNaam
                - literal_form: AlertName
            values_from: 
                - AlertNaamCodelijst
        nl_zorg_Alert_BeginDatumTijd: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.8.3.5
            name: nl_zorg_Alert_BeginDatumTijd
            title: BeginDatumTijd
            structured_aliases:
                - literal_form: BeginDatumTijd
                - literal_form: StartDateTime
            range: datetime
        nl_zorg_Alert_AlertType: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.8.3.6
            name: nl_zorg_Alert_AlertType
            title: AlertType
            structured_aliases:
                - literal_form: AlertType
            values_from: 
                - AlertTypeCodelijst
        nl_zorg_Alert_Toelichting: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.8.3.7
            name: nl_zorg_Alert_Toelichting
            title: Toelichting
            structured_aliases:
                - literal_form: Toelichting
                - literal_form: Comment
            range: string
        nl_zorg_Woonsituatie_WoningAanpassing: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.7.8.5
            name: nl_zorg_Woonsituatie_WoningAanpassing
            title: WoningAanpassing
            structured_aliases:
                - literal_form: WoningAanpassing
                - literal_form: HomeAdaption
            values_from: 
                - WoningAanpassingCodelijst
        nl_zorg_Woonsituatie_WoonOmstandigheid: 
            source: 2.16.840.1.113883.2.4.3.11.60.40.1.7.8.4
            name: nl_zorg_Woonsituatie_WoonOmstandigheid
            title: WoonOmstandigheid
            structured_aliases:
                - literal_form: WoonOmstandigheid
                - literal_form: LivingCondition
            values_from: 
                - WoonOmstandigheidCodelijst
    enums:
        GeslachtCodelijst:
            enum_uri: 2.16.840.1.113883.2.4.3.11.60.40.2.17.1.8
            name: GeslachtCodelijst
            last_updated_on: "2020-09-01T00:00:00"
            permissible_values: 
                Male:
                    meaning: Administrative_Gender:M
                Female:
                    meaning: Administrative_Gender:F
        AlertNaamCodelijst:
            enum_uri: 2.16.840.1.113883.2.4.3.11.60.40.2.8.3.2
            name: AlertNaamCodelijst
            last_updated_on: "2020-09-01T00:00:00"
            permissible_values: 
                drager_van_infectie:
                    meaning: snomed:66598005
                drager_van_carbapenemresistente_Enterobacteriaceae:
                    meaning: snomed:715881003
                slachtoffer_van_kindermishandeling:
                    meaning: snomed:397940009
                Other:
                    meaning: snomed:OTH
        AlertTypeCodelijst:
            enum_uri: 2.16.840.1.113883.2.4.3.11.60.40.2.8.3.1
            name: AlertTypeCodelijst
            last_updated_on: "2020-09-01T00:00:00"
            permissible_values: 
                Alert:
                    meaning: loinc:74018-3
        WoningAanpassingCodelijst:
            enum_uri: 2.16.840.1.113883.2.4.3.11.60.40.2.7.8.2
            name: WoningAanpassingCodelijst
            last_updated_on: "2020-09-01T00:00:00"
            permissible_values: 
                badstoel_en/of_douchestoel:
                    meaning: snomed:467158009
                traplift:
                    meaning: snomed:465153004
                aangepast_toilet:
                    meaning: snomed:465302005
        WoonOmstandigheidCodelijst:
            enum_uri: 2.16.840.1.113883.2.4.3.11.60.40.2.7.8.3
            name: WoonOmstandigheidCodelijst
            last_updated_on: "2020-09-01T00:00:00"
            permissible_values: 
                huis_bevat_trap:
                    meaning: snomed:160708008
    types:
        count: 
            uri: xsd:integer 
            base: int
        quantity: 
            uri: xsd:integer 
            base: int
        complex: 
            uri: xsd:string 
            base: str
        identifier: 
            uri: xsd:integer 
            base: int
        blob:
            uri: xsd:string
            base: str


    ''')

@pytest.fixture(scope='session')
def patient_partial_form_expected():
    return '''
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>LinkML JSON schema form builder</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
</head>
<style>
    .form-text {
        font-style: italic;
        width: -webkit-fill-available;
    }

    p :not(.form-description){
        margin-bottom: 0px !important;
    }

    .form-description {
        margin-top: 0px !important;
        margin-bottom: 20px;
    }

    body {
        margin-left: 10px !important;
    }

    label {
        font-weight: normal !important;
    }

    .input-group {
        width: -webkit-fill-available !important;
        display: table !important;
    }

    .mb-3 {
        margin-bottom: 1rem !important;
    }

    .input-group-text {
        padding: .5rem .75rem;
        font-weight: 400;
        line-height: 1.5;
        color: #212529;
        text-align: center;
        white-space: nowrap;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 0.375rem;
        width: 20%;
        float: left;
        min-height: 34px;
        white-space: pre-wrap;
    }

    .form-control {
        width: 80% !important;
        height: 100%;
    }

    .input-group {
        position: relative;
        display: flex;
        flex-wrap: wrap;
        align-items: stretch;
        width: 100%;
    }

    .hideField {
        visibility: hidden;
    }

    .form-check {
        width: fit-content;
        display: inline-block;
        margin-right: 5px;
    }

    .values-from {
        font-weight: bold;
        margin-right: 5px;
    }

    .values-from-dynamic {
        font-weight: bold;
        margin-right: 5px;
        float: left;
        width: calc(20% - 5px);
    }

    h2 {
        width: 100vw;
    }
</style>
<body>
<h1>Zorginformatiebouwstenen_(ZIB)_2020 (Zorginformatiebouwstenen (ZIB) 2020 / Health and Care Information Models (HCIM) 2020)</h1>
<h2>Nl.zorg.Patient (nl.zorg.Patient)</h2>
<p class='form-description'>Form description: Concept Een persoon die medische, psychische, paramedische of verpleegkundige zorg ontvangt. In sommige zorgsectoren wordt in plaats van de term patient de term client of deelnemer gebruikt. Purpose Het vastleggen van de relevante gegevens ten behoeve van identificatie van de patiënt, voor administratieve doeleinden en procesondersteuning. Evidence Base Hoewel de term Patiënt niet in alle zorgsectoren gebruikt wordt, is er niet voor gekozen de naam van de zib te wijzigen in Persoon als overkoepelende aanduiding voor patiënt, cliënt, deelnemer, etc. omdat het begrip Persoon breder is dan het hier bedoelde concept. Zorgverleners en Contactpersonen zijn uiteindelijk ook personen.De naam en adresgegevens zijn gebaseerd op de gegevensset van de Gemeentelijk Basis Administratie (GBA) en op de Nederlandse implementatiehandleiding HL7v3 Basiscomponenten.De gegevens die bij de wettelijk verplichte verificatie van een BSN door de SBV-Z worden opgeleverd zijn eveneens conform de GBA specificatie.Daarnaast is bij het vaststellen van de set gekeken naar de in de AWBZ zorg gebruikte AZR (AWBZ-brede zorgregistratie) gegevensset.Gebruik van patiënt- en persoonsgegevens dient te voldoen aan de Wet Bescherming Persoonsgegevens. In deze wet wordt beschreven dat het verboden is om niet-noodzakelijke persoonsgegevens te verwerken en dat op een nadenkende en fatsoenlijke wijze met verkregen persoonsgegevens omgegaan wordt (Kohnstamm, 2006). Patiëntgegevens vastgelegd in een (elektronisch) patiëntendossier of in een elektronisch bericht dienen in de context van de Wet Bescherming Persoonsgegevens beschouwd te worden. Daarnaast dienen gezondheidszorginstellingen te voldoen aan de norm Informatiebeveiliging NEN 7510. Het toezicht op naleving van de WBP ligt bij het college Bescherming persoonsgegevens (CBP). Voor het toezicht op de informatiebeveiliging in de zorg zijn het CBP en de Inspectie voor de gezondheidszorg (IGZ) gezamenlijk verantwoordelijk (CBP, IGZ, 2008).Om die redenen zijn een aantal persoonsgegevens, die in sommige landen als administratieve gegevens beschouwd worden, niet in deze bouwsteen maar in de bouwstenen voor de Sociale Anamnese opgenomen. Example Instances  Instructions Indien zowel een naam als een identificatienummer wordt meegegeven, moet, voor verificatiedoeleinden, de naam overeenkomen met de naam die bij het identifcatienummer geregistreerd is. References 1. DCM Patientgegevens V0.91. [Online] Beschikbaar op http//www.nictiz.nl/uploaded/FILES/htmlcontent/dcm/Nictiz/DCMPatientgegevens_V_0.91loNL.pdf [Geraadpleegd 23 februari 2015].2. Implementatiehandleiding HL7v3 Basiscomponenten, Stichting HL7 Nederland [Online] Beschikbaar op http//www.hl7.nl/images/downloads/Implementatiehandleiding%20HL7v3%20Basiscomponenten%20%202.3NL_secure.pdf [Geraadpleegd 23 februari 2015]. Revision History Publicatieversie 1.0 (15-02-2013)-Publicatieversie 1.1 (01-07-2013)Bevat ZIB-33.Publicatieversie 2.0 (01-04-2015)Bevat ZIB-62, ZIB-67, ZIB-96, ZIB-97, ZIB-98, ZIB-99, ZIB-100, ZIB-102, ZIB-121, ZIB-257, ZIB-258, ZIB-259, ZIB-260, ZIB-261, ZIB-262, ZIB-303, ZIB-308, ZIB-349, ZIB-350, ZIB-351, ZIB-353.Incl. algemene wijzigingsverzoeken ZIB-94, ZIB-154, ZIB-200, ZIB-201, ZIB-309, ZIB-324, ZIB-326.Publicatieversie 2.0.1 (22-05-2015)Bevat ZIB-385, ZIB-374.Publicatieversie 3.0 (01-05-2016)Bevat ZIB-453.Publicatieversie 3.1 (04-09-2017)Bevat ZIB-429, ZIB-430, ZIB-442, ZIB-471, ZIB-491, ZIB-564.Publicatieversie 3.1.1 (01-10-2018)Bevat ZIB-647.Publicatieversie 3.2 (01-09-2020)Bevat ZIB-961, ZIB-1029, ZIB-1189. (Concept A person who receives medical, psychological, paramedical or nursing care. In some care settings, the term client or participant is used instead of the term patient. Purpose Recording relevant information to identify the patient for administrative purposes and process support. Evidence Base Although the term Patient is not used in all care settings, it has been decided not to change the name of the zib to Person as the overall name for Patient, Client, Participant, etc. because the concept Person is broader than the concept referred to here. Healthprofessionals and contact persons are ultimately also Persons.The name and address information is based on the information set of the Municipal Personal Records Database (GBA) and on the Dutch Implementation Guide HL7v3 Basic Components. The information for the legally required verification of a social security number provided by the SBV-Z also follows GBA specifications. Furthermore, the AZR (AWBZ-wide healthcare registration) data set used in AWBZ healthcare served as a base in determining the set. Use of patient and personal details must follow the Personal Data Protection Act. This law prohibits processing non-essential personal data and mandates decent and reasonable processing of obtained personal data (Kohnstamm, 2006). Patient data recorded in (electronic) patient records or in digital messages must be handled in the context of the Personal Data Protection Act. Furthermore, healthcare centers must meet the Information Security NEN 7510 standard. Observance of the PDPA is monitored by the Dutch Data Protection Authority (CBP). The CBP and the Healthcare Inspectorate (IGZ) are jointly responsible for monitoring information security in healthcare (CBP, IGZ, 2008). For those reasons, some personal data, seen in some countries as administrative data, are not included in this information model but in the information models for the Social Anamnesis. Example Instances  Instructions If both a name and an identification number are given, the name must match the name registered under that identification number, for verification purposes.)</p>
<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">Geslacht (Geslacht / Gender)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_Patient_Geslacht-description"></div>
<div class='answer-options'>
<span class='values-from'>GeslachtCodelijst:</span>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="GeslachtCodelijst" id="Undifferentiated" value="Undifferentiated">
                  <label class="form-check-label" for="Undifferentiated">Undifferentiated</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="GeslachtCodelijst" id="Male" value="Male">
                  <label class="form-check-label" for="Male">Male</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="GeslachtCodelijst" id="Female" value="Female">
                  <label class="form-check-label" for="Female">Female</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="GeslachtCodelijst" id="Unknown" value="Unknown">
                  <label class="form-check-label" for="Unknown">Unknown</label></div>
</div>
</div>
<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">MeerlingIndicator (MeerlingIndicator / MultipleBirthIndicator)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_Patient_MeerlingIndicator-description"></div>
<div class='answer-options'>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="nl_zorg_Patient_MeerlingIndicator" id="True" value="True">
                  <label class="form-check-label" for="True">True</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="nl_zorg_Patient_MeerlingIndicator" id="False" value="False">
                  <label class="form-check-label" for="False">False</label></div>
</div>
</div>
<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">OverlijdensIndicator (OverlijdensIndicator / DeathIndicator)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_Patient_OverlijdensIndicator-description"></div>
<div class='answer-options'>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="nl_zorg_Patient_OverlijdensIndicator" id="True" value="True">
                  <label class="form-check-label" for="True">True</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="nl_zorg_Patient_OverlijdensIndicator" id="False" value="False">
                  <label class="form-check-label" for="False">False</label></div>
</div>
</div>
<h3>NlZorgPatientAdresgegevensContainer (Adresgegevens / AddressInformation)</h3>
<p class='form-description'>Form description: Adresgegevens van de patiënt. (Patients address information.)</p>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_part_Adresgegevens_Huisnummer-addon">Huisnummer (Huisnummer / HouseNumber)</span>
      <textarea rows="6" class="form-control" id="nl_zorg_part_Adresgegevens_Huisnummer" name="nl_zorg_part_Adresgegevens_Huisnummer" aria-describedby="nl_zorg_part_Adresgegevens_Huisnummer-addon nl_zorg_part_Adresgegevens_Huisnummer-description" ></textarea>
    </div>
    <div class="form-text" id="nl_zorg_part_Adresgegevens_Huisnummer-description"></div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_part_Adresgegevens_Huisnummerletter-addon">Huisnummerletter (Huisnummerletter / HouseNumberLetter)</span>
      <textarea rows="6" class="form-control" id="nl_zorg_part_Adresgegevens_Huisnummerletter" name="nl_zorg_part_Adresgegevens_Huisnummerletter" aria-describedby="nl_zorg_part_Adresgegevens_Huisnummerletter-addon nl_zorg_part_Adresgegevens_Huisnummerletter-description" ></textarea>
    </div>
    <div class="form-text" id="nl_zorg_part_Adresgegevens_Huisnummerletter-description"></div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_part_Adresgegevens_Huisnummertoevoeging-addon">Huisnummertoevoeging (Huisnummertoevoeging / HouseNumberAddition)</span>
      <textarea rows="6" class="form-control" id="nl_zorg_part_Adresgegevens_Huisnummertoevoeging" name="nl_zorg_part_Adresgegevens_Huisnummertoevoeging" aria-describedby="nl_zorg_part_Adresgegevens_Huisnummertoevoeging-addon nl_zorg_part_Adresgegevens_Huisnummertoevoeging-description" ></textarea>
    </div>
    <div class="form-text" id="nl_zorg_part_Adresgegevens_Huisnummertoevoeging-description"></div>
  </div>
<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">AanduidingBijNummer (AanduidingBijNummer / HouseNumberIndication)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_part_Adresgegevens_AanduidingBijNummer-description"></div>
<div class='answer-options'>
<span class='values-from'>AanduidingBijNummerCodelijst:</span>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="AanduidingBijNummerCodelijst" id="Tegenover" value="Tegenover">
                  <label class="form-check-label" for="Tegenover">Tegenover</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="AanduidingBijNummerCodelijst" id="Bij" value="Bij">
                  <label class="form-check-label" for="Bij">Bij</label></div>
</div>
</div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_part_Adresgegevens_Gemeente-addon">Gemeente (Gemeente / Municipality)</span>
      <textarea rows="6" class="form-control" id="nl_zorg_part_Adresgegevens_Gemeente" name="nl_zorg_part_Adresgegevens_Gemeente" aria-describedby="nl_zorg_part_Adresgegevens_Gemeente-addon nl_zorg_part_Adresgegevens_Gemeente-description" ></textarea>
    </div>
    <div class="form-text" id="nl_zorg_part_Adresgegevens_Gemeente-description"></div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_part_Adresgegevens_Land-addon">Land (Land / Country)</span>
      <textarea rows="6" class="form-control" id="nl_zorg_part_Adresgegevens_Land" name="nl_zorg_part_Adresgegevens_Land" aria-describedby="nl_zorg_part_Adresgegevens_Land-addon nl_zorg_part_Adresgegevens_Land-description" ></textarea>
    </div>
    <div class="form-text" id="nl_zorg_part_Adresgegevens_Land-description"></div>
  </div>
</body>
</html>
'''

@pytest.fixture(scope='session')
def three_zibs_form_expected():
    return '''
    <!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>LinkML JSON schema form builder</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
</head>
<style>
    .form-text {
        font-style: italic;
        width: -webkit-fill-available;
    }

    p :not(.form-description){
        margin-bottom: 0px !important;
    }

    .form-description {
        margin-top: 0px !important;
        margin-bottom: 20px;
    }

    body {
        margin-left: 10px !important;
    }

    label {
        font-weight: normal !important;
    }

    .input-group {
        width: -webkit-fill-available !important;
        display: table !important;
    }

    .mb-3 {
        margin-bottom: 1rem !important;
    }

    .input-group-text {
        padding: .5rem .75rem;
        font-weight: 400;
        line-height: 1.5;
        color: #212529;
        text-align: center;
        white-space: nowrap;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 0.375rem;
        width: 20%;
        float: left;
        min-height: 34px;
        white-space: pre-wrap;
    }

    .form-control {
        width: 80% !important;
        height: 100%;
    }

    .input-group {
        position: relative;
        display: flex;
        flex-wrap: wrap;
        align-items: stretch;
        width: 100%;
    }

    .hideField {
        visibility: hidden;
    }

    .form-check {
        width: fit-content;
        display: inline-block;
        margin-right: 5px;
    }

    .values-from {
        font-weight: bold;
        margin-right: 5px;
    }

    .values-from-dynamic {
        font-weight: bold;
        margin-right: 5px;
        float: left;
        width: calc(20% - 5px);
    }

    h2 {
        width: 100vw;
    }
</style>
<body>
<h1>3Zorginformatiebouwstenen_(ZIB)_2020 (Zorginformatiebouwstenen (ZIB) 2020 / Health and Care Information Models (HCIM) 2020)</h1>
<h2>Nl.zorg.Patient (nl.zorg.Patient)</h2>
<p class='form-description'>Form description: Concept Een persoon die medische, psychische, paramedische of verpleegkundige zorg ontvangt. In sommige zorgsectoren wordt in plaats van de term patient de term client of deelnemer gebruikt. Purpose Het vastleggen van de relevante gegevens ten behoeve van identificatie van de patiënt, voor administratieve doeleinden en procesondersteuning. Evidence Base Hoewel de term Patiënt niet in alle zorgsectoren gebruikt wordt, is er niet voor gekozen de naam van de zib te wijzigen in Persoon als overkoepelende aanduiding voor patiënt, cliënt, deelnemer, etc. omdat het begrip Persoon breder is dan het hier bedoelde concept. Zorgverleners en Contactpersonen zijn uiteindelijk ook personen.De naam en adresgegevens zijn gebaseerd op de gegevensset van de Gemeentelijk Basis Administratie (GBA) en op de Nederlandse implementatiehandleiding HL7v3 Basiscomponenten.De gegevens die bij de wettelijk verplichte verificatie van een BSN door de SBV-Z worden opgeleverd zijn eveneens conform de GBA specificatie.Daarnaast is bij het vaststellen van de set gekeken naar de in de AWBZ zorg gebruikte AZR (AWBZ-brede zorgregistratie) gegevensset.Gebruik van patiënt- en persoonsgegevens dient te voldoen aan de Wet Bescherming Persoonsgegevens. In deze wet wordt beschreven dat het verboden is om niet-noodzakelijke persoonsgegevens te verwerken en dat op een nadenkende en fatsoenlijke wijze met verkregen persoonsgegevens omgegaan wordt (Kohnstamm, 2006). Patiëntgegevens vastgelegd in een (elektronisch) patiëntendossier of in een elektronisch bericht dienen in de context van de Wet Bescherming Persoonsgegevens beschouwd te worden. Daarnaast dienen gezondheidszorginstellingen te voldoen aan de norm Informatiebeveiliging NEN 7510. Het toezicht op naleving van de WBP ligt bij het college Bescherming persoonsgegevens (CBP). Voor het toezicht op de informatiebeveiliging in de zorg zijn het CBP en de Inspectie voor de gezondheidszorg (IGZ) gezamenlijk verantwoordelijk (CBP, IGZ, 2008).Om die redenen zijn een aantal persoonsgegevens, die in sommige landen als administratieve gegevens beschouwd worden, niet in deze bouwsteen maar in de bouwstenen voor de Sociale Anamnese opgenomen. Example Instances  Instructions Indien zowel een naam als een identificatienummer wordt meegegeven, moet, voor verificatiedoeleinden, de naam overeenkomen met de naam die bij het identifcatienummer geregistreerd is. References 1. DCM Patientgegevens V0.91. [Online] Beschikbaar op http//www.nictiz.nl/uploaded/FILES/htmlcontent/dcm/Nictiz/DCMPatientgegevens_V_0.91loNL.pdf [Geraadpleegd 23 februari 2015].2. Implementatiehandleiding HL7v3 Basiscomponenten, Stichting HL7 Nederland [Online] Beschikbaar op http//www.hl7.nl/images/downloads/Implementatiehandleiding%20HL7v3%20Basiscomponenten%20%202.3NL_secure.pdf [Geraadpleegd 23 februari 2015]. Revision History Publicatieversie 1.0 (15-02-2013)-Publicatieversie 1.1 (01-07-2013)Bevat ZIB-33.Publicatieversie 2.0 (01-04-2015)Bevat ZIB-62, ZIB-67, ZIB-96, ZIB-97, ZIB-98, ZIB-99, ZIB-100, ZIB-102, ZIB-121, ZIB-257, ZIB-258, ZIB-259, ZIB-260, ZIB-261, ZIB-262, ZIB-303, ZIB-308, ZIB-349, ZIB-350, ZIB-351, ZIB-353.Incl. algemene wijzigingsverzoeken ZIB-94, ZIB-154, ZIB-200, ZIB-201, ZIB-309, ZIB-324, ZIB-326.Publicatieversie 2.0.1 (22-05-2015)Bevat ZIB-385, ZIB-374.Publicatieversie 3.0 (01-05-2016)Bevat ZIB-453.Publicatieversie 3.1 (04-09-2017)Bevat ZIB-429, ZIB-430, ZIB-442, ZIB-471, ZIB-491, ZIB-564.Publicatieversie 3.1.1 (01-10-2018)Bevat ZIB-647.Publicatieversie 3.2 (01-09-2020)Bevat ZIB-961, ZIB-1029, ZIB-1189. (Concept A person who receives medical, psychological, paramedical or nursing care. In some care settings, the term client or participant is used instead of the term patient. Purpose Recording relevant information to identify the patient for administrative purposes and process support. Evidence Base Although the term Patient is not used in all care settings, it has been decided not to change the name of the zib to Person as the overall name for Patient, Client, Participant, etc. because the concept Person is broader than the concept referred to here. Healthprofessionals and contact persons are ultimately also Persons.The name and address information is based on the information set of the Municipal Personal Records Database (GBA) and on the Dutch Implementation Guide HL7v3 Basic Components. The information for the legally required verification of a social security number provided by the SBV-Z also follows GBA specifications. Furthermore, the AZR (AWBZ-wide healthcare registration) data set used in AWBZ healthcare served as a base in determining the set. Use of patient and personal details must follow the Personal Data Protection Act. This law prohibits processing non-essential personal data and mandates decent and reasonable processing of obtained personal data (Kohnstamm, 2006). Patient data recorded in (electronic) patient records or in digital messages must be handled in the context of the Personal Data Protection Act. Furthermore, healthcare centers must meet the Information Security NEN 7510 standard. Observance of the PDPA is monitored by the Dutch Data Protection Authority (CBP). The CBP and the Healthcare Inspectorate (IGZ) are jointly responsible for monitoring information security in healthcare (CBP, IGZ, 2008). For those reasons, some personal data, seen in some countries as administrative data, are not included in this information model but in the information models for the Social Anamnesis. Example Instances  Instructions If both a name and an identification number are given, the name must match the name registered under that identification number, for verification purposes.)</p>
<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">Geslacht (Geslacht / Gender)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_Patient_Geslacht-description"></div>
<div class='answer-options'>
<span class='values-from'>GeslachtCodelijst:</span>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="GeslachtCodelijst" id="Male" value="Male">
                  <label class="form-check-label" for="Male">Male</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="GeslachtCodelijst" id="Female" value="Female">
                  <label class="form-check-label" for="Female">Female</label></div>
</div>
</div>
<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">OverlijdensIndicator (OverlijdensIndicator / DeathIndicator)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_Patient_OverlijdensIndicator-description"></div>
<div class='answer-options'>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="nl_zorg_Patient_OverlijdensIndicator" id="True" value="True">
                  <label class="form-check-label" for="True">True</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="nl_zorg_Patient_OverlijdensIndicator" id="False" value="False">
                  <label class="form-check-label" for="False">False</label></div>
</div>
</div>
<h3>NlZorgPatientAdresgegevensContainer (Adresgegevens / AddressInformation)</h3>
<p class='form-description'>Form description: Adresgegevens van de patiënt. (Patients address information.)</p>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_part_Adresgegevens_Huisnummer-addon">Huisnummer (Huisnummer / HouseNumber)</span>
      <textarea rows="6" class="form-control" id="nl_zorg_part_Adresgegevens_Huisnummer" name="nl_zorg_part_Adresgegevens_Huisnummer" aria-describedby="nl_zorg_part_Adresgegevens_Huisnummer-addon nl_zorg_part_Adresgegevens_Huisnummer-description" ></textarea>
    </div>
    <div class="form-text" id="nl_zorg_part_Adresgegevens_Huisnummer-description"></div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_part_Adresgegevens_Huisnummerletter-addon">Huisnummerletter (Huisnummerletter / HouseNumberLetter)</span>
      <textarea rows="6" class="form-control" id="nl_zorg_part_Adresgegevens_Huisnummerletter" name="nl_zorg_part_Adresgegevens_Huisnummerletter" aria-describedby="nl_zorg_part_Adresgegevens_Huisnummerletter-addon nl_zorg_part_Adresgegevens_Huisnummerletter-description" ></textarea>
    </div>
    <div class="form-text" id="nl_zorg_part_Adresgegevens_Huisnummerletter-description"></div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_part_Adresgegevens_Huisnummertoevoeging-addon">Huisnummertoevoeging (Huisnummertoevoeging / HouseNumberAddition)</span>
      <textarea rows="6" class="form-control" id="nl_zorg_part_Adresgegevens_Huisnummertoevoeging" name="nl_zorg_part_Adresgegevens_Huisnummertoevoeging"  aria-describedby="nl_zorg_part_Adresgegevens_Huisnummertoevoeging-addon nl_zorg_part_Adresgegevens_Huisnummertoevoeging-description" ></textarea>
    </div>
    <div class="form-text" id="nl_zorg_part_Adresgegevens_Huisnummertoevoeging-description"></div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_part_Adresgegevens_Gemeente-addon">Gemeente (Gemeente / Municipality)</span>
      <textarea rows="6" class="form-control" id="nl_zorg_part_Adresgegevens_Gemeente"  name="nl_zorg_part_Adresgegevens_Gemeente" aria-describedby="nl_zorg_part_Adresgegevens_Gemeente-addon nl_zorg_part_Adresgegevens_Gemeente-description" ></textarea>
    </div>
    <div class="form-text" id="nl_zorg_part_Adresgegevens_Gemeente-description"></div>
  </div>
<h2>Nl.zorg.Alert (nl.zorg.Alert)</h2>
<p class='form-description'>Form description: Concept Een alert beschrijft een klinisch of administratief feit dat onder de aandacht van de gebruikers van de klinische systemen wordt gebracht, om er bij het vormen van diagnostisch en therapeutisch beleid of bij de omgang met de patiënt rekening mee te houden, meestal wegens een veiligheidsrisico. Aandoeningen, die de overgevoeligheid van het lichaam voor een stof beschrijven, zich uitend in een specifieke fysiologische reactie na blootstelling, worden allergieën genoemd. Deze worden in een aparte bouwsteen beschrevenWaarschuwingen voor niet allergische aandoeningen kunnen betreffen Een aandoening, conditie of diagnose die beschouwd kan worden als contra-indicatie voor het ondergaan van een bepaalde therapie, zoals zwangerschap of een verlengd QT-syndroom;  Verminderde functie van een orgaansysteem (hartfalen, verminder lever- of nierfunctie, verminderde afweer);  Kans op verspreiding van bepaalde micro-organismen (multiresistente bacterie, tuberkelbacterie, HIV, HBV, Ebola virus);  Andere risico’s.  Purpose Het vastleggen en doorgeven van aandoeningen of condities die aandacht behoeven, is een belangrijk onderdeel van de medische registratie. Het raakt de kern van patiëntveiligheid. In de uitvoering van onderzoek en behandeling moet veelal continu rekening worden gehouden met deze, als waarschuwing gemarkeerde, patiëntkenmerken. Ze verschaffen informatie die belangrijk is in relatie met de conditie van de patiënt en de opties die een zorgverlener heeft voor therapie. Aandoeningen die als Alert worden geregistreerd of overgedragen, kunnen ook als Probleem worden beschreven. Het verschil is hierin gelegen, dat de zorgverlener het probleem heeft aangemerkt als Alert = waarschuwing. In veel gevallen zal overdracht onderworpen zijn aan sterke privacy regels, aangezien de waarschuwing niet altijd een adequate reactie van de geïnformeerde omgeving kan uitlokken. Example Instances  Instructions Indien sprake is van een contra-indicatie die tevens van belang is voor de medicatieveiligheid dient deze ook via de g-standaard (Thesaurus 40) te worden vastgelegd.  Zie hiervoor de bouwsteen MedicatieContraIndicatie Revision History Publicatieversie 1.0 (01-04-2015)Bevat ZIB-109, ZIB-132, ZIB-203, ZIB-204, ZIB-306, ZIB-308, ZIB-352.Incl. algemene wijzigingsverzoeken ZIB-94, ZIB-154, ZIB-200, ZIB-201, ZIB-309, ZIB-324, ZIB-326.Publicatieversie 3.0 (01-05-2016)Bevat ZIB-438, ZIB-453, ZIB-574.Publicatieversie 3.1 (04-09-2017)Bevat ZIB-546.Publicatieversie 3.2 (31-12-2017)Bevat ZIB-593. Publicatieversie 3.3 (26-02-2019)Bevat ZIB-682. Publicatieversie 3.4 (06-07-2019)Bevat ZIB-813. Publicatieversie 4.0 (31-01-2020)Bevat ZIB-905, ZIB-526.Publicatieversie 4.1 (01-09-2020)Bevat ZIB-1160, ZIB-1209. (Concept An alert describes a clinical or administrative fact brought to the attention of the users of the clinical systems to be taken into account when shaping diagnostic and therapeutic policy or in dealing with the patient, usually because of a safety risk. Disorders that describe the body’s sensitivity to a substance which results in a specific physiological reaction after being exposed to that substance are referred to as allergies. These are described in a separate information model. Warnings for non-allergic disorders can concern A disorder, condition or diagnosis which can be considered as a contraindication for undergoing a certain type of therapy, such as pregnancy or long QT syndrome;  Impaired functioning of an organ system (heart failure, impaired liver or kidney function, weakened immune system);  Risk of spreading certain microorganisms (multi-resistant bacteria, tubercle bacilli, HIV, HBV, Ebola virus);  Other risks  Purpose Documenting and entering disorders or conditions that require attention is an important part of medical registration. It concerns the core of patient safety. In the execution of research and treatment, these patient characteristics - which are marked as a warning - constantly have to be taken into account. They provide information that is important for the patient’s condition and the options a healthcare provider has for therapy. Disorders that are registered or transferred as an Alert can also be described as a Problem. The difference is in the fact that the healthcare provider considers the problem as an Alert = warning. In many cases, transfer will be subject to strict privacy rules, as the warning will not always elicit an adequate reaction in the informed environment. Example Instances  Instructions If there is a contraindication which is also important for medication safety, it should also be registered via the g-standard (Thesaurus 40).  See further HCIM MedicationContraIndication.)</p>
<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">AlertNaam (AlertNaam / AlertName)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_Alert_AlertNaam-description"></div>
<div class='answer-options'>
<span class='values-from'>AlertNaamCodelijst:</span>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="AlertNaamCodelijst" id="drager_van_infectie" value="drager_van_infectie">
                  <label class="form-check-label" for="drager_van_infectie">Drager_van_infectie</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="AlertNaamCodelijst" id="drager_van_carbapenemresistente_Enterobacteriaceae" value="drager_van_carbapenemresistente_Enterobacteriaceae">
                  <label class="form-check-label" for="drager_van_carbapenemresistente_Enterobacteriaceae">Drager_van_carbapenemresistente_Enterobacteriaceae</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="AlertNaamCodelijst" id="slachtoffer_van_kindermishandeling" value="slachtoffer_van_kindermishandeling">
                  <label class="form-check-label" for="slachtoffer_van_kindermishandeling">Slachtoffer_van_kindermishandeling</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="AlertNaamCodelijst" id="Other" value="Other">
                  <label class="form-check-label" for="Other">Other</label></div>
</div>
</div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_Alert_BeginDatumTijd-addon">BeginDatumTijd (BeginDatumTijd / StartDateTime)</span>
      <input type="text" class="form-control" id="nl_zorg_Alert_BeginDatumTijd" name="nl_zorg_Alert_BeginDatumTijd" aria-describedby="nl_zorg_Alert_BeginDatumTijd-addon nl_zorg_Alert_BeginDatumTijd-description" >
    </div>
    <div class="form-text" id="nl_zorg_Alert_BeginDatumTijd-description"></div>
  </div>
<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">AlertType (AlertType)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_Alert_AlertType-description"></div>
<div class='answer-options'>
<span class='values-from'>AlertTypeCodelijst:</span>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="AlertTypeCodelijst" id="Alert" value="Alert">
                  <label class="form-check-label" for="Alert">Alert</label></div>
</div>
</div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="nl_zorg_Alert_Toelichting-addon">Toelichting (Toelichting / Comment)</span>
      <textarea rows="6" class="form-control" id="nl_zorg_Alert_Toelichting" name="nl_zorg_Alert_Toelichting" aria-describedby="nl_zorg_Alert_Toelichting-addon nl_zorg_Alert_Toelichting-description" ></textarea>
    </div>
    <div class="form-text" id="nl_zorg_Alert_Toelichting-description"></div>
  </div>
<h2>Nl.zorg.Woonsituatie (nl.zorg.Woonsituatie / nl.zorg.LivingSituation)</h2>
<p class='form-description'>Form description: Concept De woonsituatie is de fysieke omgeving waarin de patiënt normaliter woont, slaapt, kleding bewaart, enz. Purpose Het doel is om de huidige woonsituatie van de patiënt in kaart te brengen. Dit in verband met huidige of eventuele toekomstige problemen die de patiënt ondervindt of zou kunnen ondervinden met betrekking tot het wonen in relatie met ziekte en de (toekomstige) beperkingen van de patiënt. Het vragen naar de woonsituatie van de patiënt kent meerdere redenen. Zo kan de woonsituatie van belang zijn bij de wens zelfstandig in de eigen woning te willen blijven wonen in het geval van ziekte en/of beperkingen (WMO, 2011; CIZ, 2011). Daarnaast is de woonsituatie van belang bij het inschatten van het valrisico, met name bij alleenwonenden (CMO, richtlijn valpreventie, 2004).  Example Instances  Revision History Publicatieversie 1.0 (15-02-2013)Publicatieversie 1.1 (01-07-2013)Publicatieversie 1.2 (01-04-2015)Bevat ZIB-162, ZIB-283, ZIB-284, ZIB-308.Incl. algemene wijzigingsverzoeken ZIB-94, ZIB-154, ZIB-200, ZIB-201, ZIB-309, ZIB-324, ZIB-326.Publicatieversie 3.0 (01-05-2016)Bevat ZIB-453.Publicatieversie 3.1 (04-09-2017)Bevat ZIB-561, ZIB-564.Publicatieversie 3.2 (01-10-2018)Bevat ZIB-653.Publicatieversie 3.3 (01-09-2020)Bevat ZIB-694, ZIB-769, ZIB-810. (Concept The living situation is the physical environment in which the patient normally lives, sleeps, keeps their clothing, etc. Purpose The goal is to take stock of the patient’s current living situation. This is in regard to any current or future problems the patient encounters or could encounter when living with the disease and the patient’s (future) constraints. There are many reasons to ask about the patient’s living situation. The living situation can be relevant in the patient’s wish to live in their own home independently in the event of disease and/or disability (WMO, 2011; CIZ, 2011). Furthermore, the living situation is important in evaluating the risks of falling, particularly among people living alone (CMO, guidelines for fall prevention, 2004). Example Instances )</p>
<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">WoningAanpassing (WoningAanpassing / HomeAdaption)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_Woonsituatie_WoningAanpassing-description"></div>
<div class='answer-options'>
<span class='values-from'>WoningAanpassingCodelijst:</span>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="WoningAanpassingCodelijst" id="badstoel_en/of_douchestoel" value="badstoel_en/of_douchestoel">
                  <label class="form-check-label" for="badstoel_en/of_douchestoel">Badstoel_en/of_douchestoel</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="WoningAanpassingCodelijst" id="traplift" value="traplift">
                  <label class="form-check-label" for="traplift">Traplift</label></div>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="WoningAanpassingCodelijst" id="aangepast_toilet" value="aangepast_toilet">
                  <label class="form-check-label" for="aangepast_toilet">Aangepast_toilet</label></div>
</div>
</div>
<div class="mb-3">
            <div class="input-group">
<span class="input-group-text">WoonOmstandigheid (WoonOmstandigheid / LivingCondition)</span>
<input type="text" class="form-control hideField">
</div>
<div class="form-text" id="nl_zorg_Woonsituatie_WoonOmstandigheid-description"></div>
<div class='answer-options'>
<span class='values-from'>WoonOmstandigheidCodelijst:</span>
<div class="form-check">
                  <input class="form-check-input" type="radio" name="WoonOmstandigheidCodelijst" id="huis_bevat_trap" value="huis_bevat_trap">
                  <label class="form-check-label" for="huis_bevat_trap">Huis_bevat_trap</label></div>
</div>
</div>
</body>
</html>
    '''

@pytest.fixture(scope='session')
def default_range_yaml_integer():
    return yaml.safe_load(getDefaultRangeCode("integer"))

@pytest.fixture(scope='session')
def default_range_yaml_float():
    return yaml.safe_load(getDefaultRangeCode("float"))

@pytest.fixture(scope='session')
def default_range_yaml_string():
    return yaml.safe_load(getDefaultRangeCode("string"))

@pytest.fixture(scope='session')
def default_range_yaml_boolean():
    return yaml.safe_load(getDefaultRangeCode("boolean"))

@pytest.fixture(scope='session')
def default_range_yaml_datetime():
    return yaml.safe_load(getDefaultRangeCode("datetime"))

@pytest.fixture(scope = 'session')
def tutorial1_yaml():
    return yaml.safe_load("""
    id: https://w3id.org/linkml/examples/personinfo
    name: personinfo
    prefixes:
        linkml: https://w3id.org/linkml/
        personinfo: https://w3id.org/linkml/examples/personinfo
    imports:
        - linkml:types
    default_range: string
    default_prefix: personinfo

    classes:
        Person:
            attributes:
                id:
                full_name:
                aliases:
                phone:
                age:
""")

@pytest.fixture(scope='session')
def tutorial1_yaml_expected():
    return """
    <!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>LinkML JSON schema form builder</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
</head>
<style>
    .form-text {
        font-style: italic;
        width: -webkit-fill-available;
    }

    p :not(.form-description){
        margin-bottom: 0px !important;
    }

    .form-description {
        margin-top: 0px !important;
        margin-bottom: 20px;
    }

    body {
        margin-left: 10px !important;
    }

    label {
        font-weight: normal !important;
    }

    .input-group {
        width: -webkit-fill-available !important;
        display: table !important;
    }

    .mb-3 {
        margin-bottom: 1rem !important;
    }

    .input-group-text {
        padding: .5rem .75rem;
        font-weight: 400;
        line-height: 1.5;
        color: #212529;
        text-align: center;
        white-space: nowrap;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 0.375rem;
        width: 20%;
        float: left;
        min-height: 34px;
        white-space: pre-wrap;
    }

    .form-control {
        width: 80% !important;
        height: 100%;
    }

    .input-group {
        position: relative;
        display: flex;
        flex-wrap: wrap;
        align-items: stretch;
        width: 100%;
    }

    .hideField {
        visibility: hidden;
    }

    .form-check {
        width: fit-content;
        display: inline-block;
        margin-right: 5px;
    }

    .values-from {
        font-weight: bold;
        margin-right: 5px;
    }

    .values-from-dynamic {
        font-weight: bold;
        margin-right: 5px;
        float: left;
        width: calc(20% - 5px);
    }

    h2 {
        width: 100vw;
    }
</style>
<body>
<h1>personinfo</h1>
<h2>Person</h2>
<p class='form-description'>Form description: </p>
</body>
</html>
"""

@pytest.fixture(scope = 'session')
def tutorial1_no_name_yaml():
    return yaml.safe_load("""
    id: https://w3id.org/linkml/examples/personinfo
    prefixes:
        linkml: https://w3id.org/linkml/
        personinfo: https://w3id.org/linkml/examples/personinfo
    imports:
        - linkml:types
    default_range: string
    default_prefix: personinfo

    classes:
        Person:
            attributes:
                id:
                full_name:
                aliases:
                phone:
                age:
""")

@pytest.fixture(scope='session')
def tutorial1_no_name_yaml_expected():
    return """
    <!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>LinkML JSON schema form builder</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
</head>
<style>
    .form-text {
        font-style: italic;
        width: -webkit-fill-available;
    }

    p :not(.form-description){
        margin-bottom: 0px !important;
    }

    .form-description {
        margin-top: 0px !important;
        margin-bottom: 20px;
    }

    body {
        margin-left: 10px !important;
    }

    label {
        font-weight: normal !important;
    }

    .input-group {
        width: -webkit-fill-available !important;
        display: table !important;
    }

    .mb-3 {
        margin-bottom: 1rem !important;
    }

    .input-group-text {
        padding: .5rem .75rem;
        font-weight: 400;
        line-height: 1.5;
        color: #212529;
        text-align: center;
        white-space: nowrap;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 0.375rem;
        width: 20%;
        float: left;
        min-height: 34px;
        white-space: pre-wrap;
    }

    .form-control {
        width: 80% !important;
        height: 100%;
    }

    .input-group {
        position: relative;
        display: flex;
        flex-wrap: wrap;
        align-items: stretch;
        width: 100%;
    }

    .hideField {
        visibility: hidden;
    }

    .form-check {
        width: fit-content;
        display: inline-block;
        margin-right: 5px;
    }

    .values-from {
        font-weight: bold;
        margin-right: 5px;
    }

    .values-from-dynamic {
        font-weight: bold;
        margin-right: 5px;
        float: left;
        width: calc(20% - 5px);
    }

    h2 {
        width: 100vw;
    }
</style>
<body>
<h1>default</h1>
<h2>Person</h2>
<p class='form-description'>Form description: </p>
</body>
</html>
"""

@pytest.fixture(scope = 'session')
def tutorial5_yaml():
    return yaml.safe_load("""
    id: https://w3id.org/linkml/examples/personinfo
    name: personinfo5
    prefixes:
        linkml: https://w3id.org/linkml/
        schema: http://schema.org/
        personinfo: https://w3id.org/linkml/examples/personinfo/
        ORCID: https://orcid.org/
    imports:
        - linkml:types
    default_range: string

    classes:
        Person:
            class_uri: schema:Person
            attributes:
                id:
                    identifier: true
                full_name:
                    required: true
                    description: name of the person
                    slot_uri: schema:name
                aliases:
                    multivalued: true
                    description: other names for the person
                phone:
                    slot_uri: schema:telephone
                age:
                    range: integer
                    minimum_value: 0
                    maximum_value: 200
            id_prefixes:
                - ORCID
        Container:
            attributes:
                persons:
                    multivalued: true
                    inlined_as_list: true
                    range: Person
""")

@pytest.fixture(scope='session')
def tutorial5_yaml_expected():
    return """
    <!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>LinkML JSON schema form builder</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
</head>
<style>
    .form-text {
        font-style: italic;
        width: -webkit-fill-available;
    }

    p :not(.form-description){
        margin-bottom: 0px !important;
    }

    .form-description {
        margin-top: 0px !important;
        margin-bottom: 20px;
    }

    body {
        margin-left: 10px !important;
    }

    label {
        font-weight: normal !important;
    }

    .input-group {
        width: -webkit-fill-available !important;
        display: table !important;
    }

    .mb-3 {
        margin-bottom: 1rem !important;
    }

    .input-group-text {
        padding: .5rem .75rem;
        font-weight: 400;
        line-height: 1.5;
        color: #212529;
        text-align: center;
        white-space: nowrap;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 0.375rem;
        width: 20%;
        float: left;
        min-height: 34px;
        white-space: pre-wrap;
    }

    .form-control {
        width: 80% !important;
        height: 100%;
    }

    .input-group {
        position: relative;
        display: flex;
        flex-wrap: wrap;
        align-items: stretch;
        width: 100%;
    }

    .hideField {
        visibility: hidden;
    }

    .form-check {
        width: fit-content;
        display: inline-block;
        margin-right: 5px;
    }

    .values-from {
        font-weight: bold;
        margin-right: 5px;
    }

    .values-from-dynamic {
        font-weight: bold;
        margin-right: 5px;
        float: left;
        width: calc(20% - 5px);
    }

    h2 {
        width: 100vw;
    }
</style>
<body>
<h1>personinfo5</h1>
<h2>Person</h2>
<p class='form-description'>Form description: </p>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="id-addon">Id</span>
      <textarea rows="6" class="form-control" id="id" name="id" aria-describedby="id-addon id-description" ></textarea>
    </div><div class="form-text" id="id-description"></div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="full_name-addon">Full_name</span>
      <textarea rows="6" class="form-control" id="full_name" name="full_name" aria-describedby="full_name-addon full_name-description" required></textarea>
    </div><div class="form-text" id="full_name-description">Name of the person</div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="aliases-addon">Aliases</span>
      <textarea rows="6" class="form-control" id="aliases" name="aliases" aria-describedby="aliases-addon aliases-description" ></textarea>
    </div><div class="input-group">
      <span class="input-group-text hideField" id="aliases-addon">Aliases</span>
      <textarea rows="6" class="form-control" id="aliases2" name="aliases2" aria-describedby="aliases-addon aliases-description"></textarea>
    </div><div class="form-text" id="aliases-description">Other names for the person This field requires at least 1 value(s)</div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="phone-addon">Phone</span>
      <textarea rows="6" class="form-control" id="phone" name="phone" aria-describedby="phone-addon phone-description" ></textarea>
    </div><div class="form-text" id="phone-description"></div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="age-addon">Age</span>
      <input type="number" class="form-control" id="age" name="age" aria-describedby="age-addon age-description" >
    </div>
    <div class="form-text" id="age-description"> The value for this field should be between 0 and 200</div>
  </div>
<h2>Container</h2>
<p class='form-description'>Form description: </p>
<h3>persons</h3>
<p class='form-description'>Form description: </p>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="id-addon">Id</span>
      <textarea rows="6" class="form-control" id="id" name="id" aria-describedby="id-addon id-description" ></textarea>
    </div><div class="form-text" id="id-description"></div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="full_name-addon">Full_name</span>
      <textarea rows="6" class="form-control" id="full_name" name="full_name" aria-describedby="full_name-addon full_name-description" required></textarea>
    </div><div class="form-text" id="full_name-description">Name of the person</div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="aliases-addon">Aliases</span>
      <textarea rows="6" class="form-control" id="aliases" name="aliases" aria-describedby="aliases-addon aliases-description" ></textarea>
    </div><div class="input-group">
      <span class="input-group-text hideField" id="aliases-addon">Aliases</span>
      <textarea rows="6" class="form-control" id="aliases2" name="aliases2" aria-describedby="aliases-addon aliases-description"></textarea>
    </div><div class="form-text" id="aliases-description">Other names for the person This field requires at least 1 value(s)</div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="phone-addon">Phone</span>
      <textarea rows="6" class="form-control" id="phone" name="phone" aria-describedby="phone-addon phone-description" ></textarea>
    </div><div class="form-text" id="phone-description"></div>
  </div>
<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="age-addon">Age</span>
      <input type="number" class="form-control" id="age" name="age" aria-describedby="age-addon age-description" >
    </div>
    <div class="form-text" id="age-description"> The value for this field should be between 0 and 200</div>
  </div>
</body>
</html>
"""
