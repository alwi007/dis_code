from flask_restful import Resource, Api
from SPARQLWrapper import GET, JSON, JSONLD, POST, TURTLE, SPARQLWrapper
import json
from flask import Flask, render_template, make_response, request, jsonify
import sparql_dataframe
from pandas.io.json import json_normalize
import pandas as pd
import datetime
import uuid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
from io import BytesIO
import base64


# Flask
app = Flask(__name__)
api = Api(app)


# Method for General Select SPARQL Query
@app.route('/query', methods=['GET', 'POST'])
def query():
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST")

        sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
        SELECT * WHERE  { ?s ?p ?o} limit 100
        """)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        result = result['results']['bindings']
        result = json.dumps(result)
        return result


# Method for Insert SPARQL Query
@app.route('/result', methods=['GET', 'POST'])
def result():
    json=request.get_json()
    json_new=json
    MAC=json.get('MAC')
    Temperature=json.get('Temp')
    Humidity=json.get('humidity')
    Oxidised=json.get('Oxidised')
    Reduced=json.get('Reduced')
    NH3=json.get('NH3')
    PM25=json.get('PM25')
    PM10=json.get('PM10')
    O3 = json.get('O3')
    CO = json.get('CO')
    eCO2 = json.get('eCO2')
    NO = json.get('NO')
    Timestamp = json.get('Timestamp')
    TVOC=json.get('TVOC')
    LPG=json.get('LPG')
    Propane=json.get('PROPANE')
    Smoke=json.get('SMOKE')
    CH4=json.get('CH4')
    H2=json.get('H2')
    postcode=json.get('POSTCODE')


    print(json)

    # Defining Universal Unique Identifier(UUID)
    def new_uuid():
        id1 = str(uuid.uuid4())
        return id1
    if Oxidised is None:
        print("No Oxidised reading")
    else:
        id=str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+"""  UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+"""  UNIAQ:pollutant UNIAQ:Oxidised.
            UNIAQ:"""+id+"""  UNIAQ:unit UNIAQ:KOhm.
            UNIAQ:"""+id+"""  UNIAQ:value """ + Oxidised + """.
            } """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if Reduced is None:
        print("No Reduced reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:Reduced.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:KOhm.
            UNIAQ:"""+id+""" UNIAQ:value """ + Reduced + """.
            }  """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if NH3 is None:
        print("No NH3 reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:NH3.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:KOhm.
            UNIAQ:"""+id+""" UNIAQ:value """ + NH3 + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if PM25 is None:
        print("No PM25 reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:PM25.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:ugm-3.
            UNIAQ:"""+id+""" UNIAQ:value """ + PM25 + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if PM10 is None:
        print("No PM10 reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:PM10.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:ugm-3.
            UNIAQ:"""+id+""" UNIAQ:value """ + PM10 + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if O3 is None:
        print("No O3 reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
             PREFIX owl: <http://www.w3.org/2002/07/owl#>
             PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
             PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
             PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
             PREFIX foaf: <http://xmlns.com/foaf/0.1/>
             PREFIX dc: <http://purl.org/dc/elements/1.1/>
             PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
             PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
             INSERT DATA {
             UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
             UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
             UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
             UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
             UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
             UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:O3.
             UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:ppm.
             UNIAQ:"""+id+""" UNIAQ:value """ + O3 + """.
             }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if CO is None:
        print("No CO reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:CO.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:KOhm.
            UNIAQ:"""+id+""" UNIAQ:value """ + CO + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if eCO2 is None:
        print("No eCO2 reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:eCO2.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:ppm.
            UNIAQ:"""+id+""" UNIAQ:value """ + eCO2 + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if NO is None:
        print("No NO reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:NO.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:KOhm.
            UNIAQ:"""+id+""" UNIAQ:value """ + NO + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if Temperature is None:
        print("No Temperature reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:Temperature.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:C.
            UNIAQ:"""+id+""" UNIAQ:value """ + Temperature + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()


    if Humidity is None:
        print("No Humidity reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:Humidity.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:Perc.
            UNIAQ:"""+id+""" UNIAQ:value """ + Humidity + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if TVOC is None:
        print("No TVOC reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:TVOC.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:Ohm.
            UNIAQ:"""+id+""" UNIAQ:value """ + TVOC + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if LPG is None:
        print("No LPG reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:LPG.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:ppm.
            UNIAQ:"""+id+""" UNIAQ:value """ + LPG + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if Propane is None:
        print("No Propane reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:Propane.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:ppm.            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            UNIAQ:"""+id+""" UNIAQ:value """ + Propane + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()


    if Smoke is None:
        print("No Smoke reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>

            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:Smoke.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:ppm.
            UNIAQ:"""+id+""" UNIAQ:value """ + Smoke + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if CH4 is None:
        print("No CH4 reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:CH4.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:ppm.
            UNIAQ:"""+id+""" UNIAQ:value """ + CH4 + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if H2 is None:
        print("No H2 reading")
    else:
        id = str(new_uuid())
        sparql = SPARQLWrapper("http://<ip address>/repositories/INDOOR_TEST/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            INSERT DATA {
            UNIAQ:MAC_ID""" + MAC + """ rdf:type UNIAQ:Sensor.
            UNIAQ:"""+id+""" rdf:type UNIAQ:Observation.
            UNIAQ:""" + MAC + """  UNIAQ:observes UNIAQ:"""+id+""".
            UNIAQ:""" + MAC + """ UNIAQ:postcode \""""+postcode+"""\".
            UNIAQ:"""+id+""" UNIAQ:timestamp """+Timestamp+"""^^xsd:dateTime.
            UNIAQ:"""+id+""" UNIAQ:pollutant UNIAQ:H2.
            UNIAQ:"""+id+""" UNIAQ:unit UNIAQ:ppm.
            UNIAQ:"""+id+""" UNIAQ:value """ + H2 + """.
            }         """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    return 'ok'

# Method for Air Quality Check
@app.route('/aqcheckindoor', methods=['GET', 'POST'])
def aqcheckindoor():
    endpoint = ("http://<ip address>/repositories/UNIAQ")
    if request.method == "POST":
        post_code = request.form["postcodeID"]
        pollutant = request.form["pollutantID"]
        fromdate = request.form["fromdateID"]
        todate = request.form["todateID"]
        reading_limit = request.form["limitID"]
        q = ("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
            PREFIX : <http://score-bradford.com/ontologies/UNIAQ.owl#>
            select ?obs ?val ?uni ?time where { 
            ?s UNIAQ:postcode \"""" + post_code + """\".
            ?s UNIAQ:observes ?obs.
	        ?obs rdf:type UNIAQ:Observation.
            ?obs UNIAQ:pollutant UNIAQ:""" + pollutant + """.
            ?obs UNIAQ:value ?val.
            ?obs UNIAQ:unit ?uni.
            ?obs UNIAQ:timestamp ?time
            FILTER ((?time> \"""" + fromdate + """:00\"^^xsd:dateTime)&&(?time< \"""" + todate + """:00\"^^xsd:dateTime))
            } limit """ + reading_limit + """
            """)

        # Converting Results into Dataframes
        result = sparql_dataframe.get(endpoint, q, post=True)

        # Standard Deviation
        sdv = str(result.loc[:, "val"].std())

        # Average
        avg = str(result.loc[:, "val"].mean())

        # Count
        cnt = str(result.loc[:, "val"].count())

        # Passing Value to HTML page for Display
        return render_template('result.html', value1=sdv, value2=avg, value3=cnt, value4=pollutant)

    # Front End form to get the variable entries from user
    return render_template('post_code.html')

# Method for Plot
@app.route('/plot', methods=['GET', 'POST'])
def plot():
    endpoint = ("http://<ip address>/repositories/INDOOR_TEST")
    if request.method == "POST":
        post_code = request.form["postcodeID"]
        pollutant = request.form["pollutantID"]
        fromdate = request.form["fromdateID"]
        todate = request.form["todateID"]
        reading_limit = request.form["limitID"]
        q = ("""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
                PREFIX : <http://score-bradford.com/ontologies/UNIAQ.owl#>
                select ?val ?time where { 
                ?s UNIAQ:postcode \"""" + post_code + """\".
                ?s UNIAQ:observes ?obs.
    	        ?obs rdf:type UNIAQ:Observation.
                ?obs UNIAQ:pollutant UNIAQ:""" + pollutant + """.
                ?obs UNIAQ:value ?val.
                ?obs UNIAQ:unit ?uni.
                ?obs UNIAQ:timestamp ?time
                FILTER ((?time> \""""+fromdate+""":00\"^^xsd:dateTime)&&(?time< \""""+todate+""":00\"^^xsd:dateTime))
                } limit """ + reading_limit + """
                """)
        result = sparql_dataframe.get(endpoint, q, post=True)
        img = BytesIO()

        y = result['val']
        x = result['time']

        plt.plot(y)

        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        print(y)

        return render_template('aqplot.html', plot_url=plot_url)

    # Front End form to get the variable entries from user
    return render_template('post_code.html')


#Method for Finding Single day Average of Pollutants

@app.route('/dayaverage', methods=['GET', 'POST'])

def dayaverage():
    if request.method == "POST":
        post_code = request.form["postcodeID"]
        from_date = request.form["fromdateID"]

        #Defining for Mean Value Calculation
        def mean(dataframe):
            Y = dataframe["val"]
            result_mean = Y.mean()
            return result_mean

        def queryMe(query):
            # print(query)
            endpoint = "http://<ip address>/repositories/INDOOR_TEST"
            df = sparql_dataframe.get(endpoint, query, post=True)
            meanvalue = mean(df)
            return meanvalue

        def calculateMean(t1, t2):
            from_date = t2
            current_date = t1
            q1 = """
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
                PREFIX : <http://score-bradford.com/ontologies/UNIAQ.owl#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                SELECT ?val ?time where { 
                     ?s UNIAQ:postcode	\""""+post_code+"""\".
                     ?s UNIAQ:observes ?obs.
                     ?obs rdf:type UNIAQ:Observation.
                     ?obs UNIAQ:pollutant UNIAQ:NH3.
                     ?obs UNIAQ:value ?val.
                     ?obs UNIAQ:unit ?uni.
                ?obs UNIAQ:timestamp ?time
                FILTER ((?time >\"""" + from_date + """\"^^xsd:dateTime)&&(?time<\"""" + current_date + """\"^^xsd:dateTime))
                  }
                """
            df1 = queryMe(q1)

            q2 = """
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
                PREFIX : <http://score-bradford.com/ontologies/UNIAQ.owl#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                SELECT ?val ?time where { 
                     ?s UNIAQ:postcode	\""""+post_code+"""\".
                     ?s UNIAQ:observes ?obs.
                     ?obs rdf:type UNIAQ:Observation.
                     ?obs UNIAQ:pollutant UNIAQ:PM25.
                     ?obs UNIAQ:value ?val.
                     ?obs UNIAQ:unit ?uni.
                ?obs UNIAQ:timestamp ?time
                FILTER ((?time >\"""" + from_date + """\"^^xsd:dateTime)&&(?time<\"""" + current_date + """\"^^xsd:dateTime))
                  }
                """
            df2 = queryMe(q2)

            q3 = """
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
                PREFIX : <http://score-bradford.com/ontologies/UNIAQ.owl#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                SELECT ?val ?time where { 
                     ?s UNIAQ:postcode	\""""+post_code+"""\".
                     ?s UNIAQ:observes ?obs.
                     ?obs rdf:type UNIAQ:Observation.
                     ?obs UNIAQ:pollutant UNIAQ:PM10.
                     ?obs UNIAQ:value ?val.
                     ?obs UNIAQ:unit ?uni.
                ?obs UNIAQ:timestamp ?time
                FILTER ((?time >\"""" + from_date + """\"^^xsd:dateTime)&&(?time<\"""" + current_date + """\"^^xsd:dateTime))
                  }
                """
            df3 = queryMe(q3)

            q4 = """
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
                    PREFIX : <http://score-bradford.com/ontologies/UNIAQ.owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    SELECT ?val ?time where { 
                         ?s UNIAQ:postcode	\""""+post_code+"""\".
                         ?s UNIAQ:observes ?obs.
                         ?obs rdf:type UNIAQ:Observation.
                         ?obs UNIAQ:pollutant UNIAQ:CO.
                         ?obs UNIAQ:value ?val.
                         ?obs UNIAQ:unit ?uni.
                    ?obs UNIAQ:timestamp ?time
                    FILTER ((?time >\"""" + from_date + """\"^^xsd:dateTime)&&(?time<\"""" + current_date + """\"^^xsd:dateTime))
                      }
                    """

            df4 = queryMe(q4)

            q5 = """
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
                    PREFIX : <http://score-bradford.com/ontologies/UNIAQ.owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    SELECT ?val ?time where { 
                         ?s UNIAQ:postcode	\""""+post_code+"""\".
                         ?s UNIAQ:observes ?obs.
                         ?obs rdf:type UNIAQ:Observation.
                         ?obs UNIAQ:pollutant UNIAQ:SMOKE.
                         ?obs UNIAQ:value ?val.
                         ?obs UNIAQ:unit ?uni.
                    ?obs UNIAQ:timestamp ?time
                    FILTER ((?time >\"""" + from_date + """\"^^xsd:dateTime)&&(?time<\"""" + current_date + """\"^^xsd:dateTime))
                      }
                    """

            df5 = queryMe(q5)

            return [df1, df2, df3, df4, df5]

        t1 = datetime.datetime.now()
        today_date = t1.strftime("%Y-%m-%dT%H:%M:%S")
        t2 = t1 - datetime.timedelta(hours=24, minutes=0)  # 1 day Average
        first_date = t2.strftime("%Y-%m-%dT%H:%M:%S")

        [NH3, PM10, PM25, CO, SMOKE] = calculateMean(today_date, first_date)

        df = pd.DataFrame({'Day': ['NH3', 'PM10', 'PM25', 'CO', 'SMOKE'], 'Average_of_pollutants': [NH3, PM10, PM25, CO, SMOKE]})

        img = BytesIO()
        #fig = plt.figure()
        fig = df.plot(kind='bar', x='Day', y='Average_of_pollutants')
        #plt.plot(df.Day, df.Average)
        plt.ylabel('Values', fontsize=12)
        # fig.savefig('test.jpg')
        plt.savefig(img, format='png')
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        plt.close()
        img.seek(0)
        #plt.show()
        return render_template('aqplot.html', plot_url=plot_url)


    return render_template('dayaverage.html')


#Method for Finding Week Average of Pollutants
@app.route('/weekaverage', methods=['GET', 'POST'])

def weekaverage():
    if request.method == "POST":
        post_code = request.form["postcodeID"]
        pollutant = request.form["pollutantID"]




        #Defining for Mean Value Calculation
        def mean(dataframe):
            Y = dataframe["val"]
            result_mean = Y.mean()
            return result_mean

        def queryMe(query):
            # print(query)
            endpoint = "http://<ip address>/repositories/INDOOR_TEST"
            df = sparql_dataframe.get(endpoint, query, post=True)
            meanvalue = mean(df)
            return meanvalue

        def calculateMean(t1, t2):
            from_date = t2
            current_date = t1
            q1 = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
                            PREFIX : <http://score-bradford.com/ontologies/UNIAQ.owl#>
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                            SELECT ?val ?time where { 
                                 ?s UNIAQ:postcode	\"""" + post_code + """\".
                                 ?s UNIAQ:observes ?obs.
                                 ?obs rdf:type UNIAQ:Observation.
                                 ?obs UNIAQ:pollutant UNIAQ:"""+pollutant+""".
                                 ?obs UNIAQ:value ?val.
                                 ?obs UNIAQ:unit ?uni.
                            ?obs UNIAQ:timestamp ?time
                            FILTER ((?time >\"""" + from_date + """\"^^xsd:dateTime)&&(?time<\"""" + current_date + """\"^^xsd:dateTime))
                              }
                            """

            df1 = queryMe(q1)
            return df1

        t1 = datetime.datetime.now()
        today_date = t1.strftime("%Y-%m-%dT%H:%M:%S")
        t2 = t1 - datetime.timedelta(hours=24, minutes=0)  # 1 day Average
        first_date = t2.strftime("%Y-%m-%dT%H:%M:%S")
        t3 = t1 - datetime.timedelta(hours=48, minutes=0)
        second_date = t3.strftime("%Y-%m-%dT%H:%M:%S")
        t4 = t1 - datetime.timedelta(hours=72, minutes=0)
        third_date = t4.strftime("%Y-%m-%dT%H:%M:%S")
        t5 = t1 - datetime.timedelta(hours=96, minutes=0)
        fourth_date = t5.strftime("%Y-%m-%dT%H:%M:%S")
        t6 = t1 - datetime.timedelta(hours=120, minutes=0)
        fifth_date = t6.strftime("%Y-%m-%dT%H:%M:%S")
        t7 = t1 - datetime.timedelta(hours=144, minutes=0)
        sixth_date = t7.strftime("%Y-%m-%dT%H:%M:%S")
        t8 = t1 - datetime.timedelta(hours=168, minutes=0)
        seventh_date = t8.strftime("%Y-%m-%dT%H:%M:%S")

        Day1 = calculateMean(today_date, first_date)
        Day2 = calculateMean(first_date, second_date)
        Day3 = calculateMean(second_date, third_date)
        Day4 = calculateMean(third_date, fourth_date)
        Day5 = calculateMean(fourth_date, fifth_date)
        Day6 = calculateMean(fifth_date, sixth_date)
        Day7 = calculateMean(sixth_date, seventh_date)

        # Converting Data into dataframes
        df = pd.DataFrame(
            {'Day': ['1', '2', '3', '4', '5', '6', '7'], 'Average': [Day1, Day2, Day3, Day4, Day5, Day6, Day7]})

        # Ploting the Exposure Value
        img = BytesIO()
        fig = plt.figure()
        plt.plot(df.Day, df.Average)
        fig.suptitle('Week average of '"" + pollutant + "", fontsize=20)
        plt.xlabel('Day', fontsize=12)
        plt.ylabel(""+pollutant+"", fontsize=12)
        # fig.savefig('test.jpg')
        plt.savefig(img, format='png')
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        plt.close()
        img.seek(0)

        return render_template('aqplot.html', plot_url=plot_url)
        # return render_template('exposure.html', value1=Day1, value2=Day2, value3=Day3, value4=Day4)

    return render_template('7dayaverage.html')



#Method for finding Exposure Value

@app.route('/exposure', methods=['GET', 'POST'])

def exposure():
    if request.method == "POST":
        post_code = request.form["postcodeID"]
        pollutant = request.form["pollutantID"]
        hours = float(request.form["hoursID"])


#Defining for Mean Value Calculation
        def mean(dataframe):
            Y = dataframe["val"]
            result_mean = Y.mean()
            return result_mean

        def queryMe(query):
            # print(query)
            endpoint = "http://<ip address>/repositories/INDOOR_TEST"
            df = sparql_dataframe.get(endpoint, query, post=True)
            meanvalue = mean(df)
            return meanvalue

        def calculateMean(t1, t2):
            from_date = t2
            current_date = t1
            q1 = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                            PREFIX UNIAQ: <http://score-bradford.com/ontologies/UNIAQ.owl#>
                            PREFIX : <http://score-bradford.com/ontologies/UNIAQ.owl#>
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                            SELECT ?val ?time where { 
                                 ?s UNIAQ:postcode	\"""" + post_code + """\".
                                 ?s UNIAQ:observes ?obs.
                                 ?obs rdf:type UNIAQ:Observation.
                                 ?obs UNIAQ:pollutant UNIAQ:""" + pollutant + """.
                                 ?obs UNIAQ:value ?val.
                                 ?obs UNIAQ:unit ?uni.
                            ?obs UNIAQ:timestamp ?time
                            FILTER ((?time >\"""" + from_date + """\"^^xsd:dateTime)&&(?time<\"""" + current_date + """\"^^xsd:dateTime))
                              }
                            """

            df1 = queryMe(q1)
            return (df1)

        # Current time - t1
        t1 = datetime.datetime.now()
        today_date = t1.strftime("%Y-%m-%dT%H:%M:%S")
        t2 = t1 - datetime.timedelta(hours=24, minutes=0)  # 1 day Average
        first_date = t2.strftime("%Y-%m-%dT%H:%M:%S")
        t3 = t1 - datetime.timedelta(hours=48, minutes=0)
        second_date = t3.strftime("%Y-%m-%dT%H:%M:%S")
        t4 = t1 - datetime.timedelta(hours=72, minutes=0)
        third_date = t4.strftime("%Y-%m-%dT%H:%M:%S")
        t5 = t1 - datetime.timedelta(hours=96, minutes=0)
        fourth_date = t5.strftime("%Y-%m-%dT%H:%M:%S")
        t6 = t1 - datetime.timedelta(hours=120, minutes=0)
        fifth_date = t6.strftime("%Y-%m-%dT%H:%M:%S")
        t7 = t1 - datetime.timedelta(hours=144, minutes=0)
        sixth_date = t7.strftime("%Y-%m-%dT%H:%M:%S")
        t8 = t1 - datetime.timedelta(hours=168, minutes=0)
        seventh_date = t8.strftime("%Y-%m-%dT%H:%M:%S")


        #Mean Calculation
        Day1 = calculateMean(today_date, first_date)
        Day2 = calculateMean(first_date, second_date)
        Day3 = calculateMean(second_date, third_date)
        Day4 = calculateMean(third_date, fourth_date)
        Day5 = calculateMean(fourth_date, fifth_date)
        Day6 = calculateMean(fifth_date, sixth_date)
        Day7 = calculateMean(sixth_date, seventh_date)

        #Exposure value = Mean of pollutant * Number of hours spend indoor
        exp1 = Day1 * hours
        exp2 = Day2 * hours
        exp3 = Day3 * hours
        exp4 = Day4 * hours
        exp5 = Day5 * hours
        exp6 = Day6 * hours
        exp7 = Day7 * hours

        #Converting Data into dataframes
        df = pd.DataFrame({'Day': ['1', '2', '3', '4', '5', '6', '7'], 'Exposure': [exp1, exp2, exp3, exp4, exp5, exp6, exp7]})

        #Ploting the Exposure Value
        img = BytesIO()
        fig = plt.figure()
        plt.plot(df.Day, df.Exposure)
        fig.suptitle('Plot of Exposure value for '""+pollutant+"", fontsize=20)
        plt.xlabel('Day', fontsize=12)
        plt.ylabel('Exposure value', fontsize=12)
        #fig.savefig('test.jpg')
        plt.savefig(img,format='png')
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        plt.close()
        img.seek(0)


        return render_template('aqplot.html', plot_url=plot_url)
        #return render_template('exposure.html', value1=Day1, value2=Day2, value3=Day3, value4=Day4)


    return render_template('exp_postcode.html')
        # val = df["val"]

        # print("Mean of NH3:", df)




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='<port id>', threaded=True)
