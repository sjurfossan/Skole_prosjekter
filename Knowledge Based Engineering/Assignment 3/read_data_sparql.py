# importing the requests library - MAKING REQUEST TO FUSEKI example.
import requests
from insert_data_sparql import insert_data
from GA.ga_flow import GeneticAlgorithmFlow
from GA.ga_volume import GeneticAlgorithmVolume


battle_bot = 7
start_motor = 3
engage_weapon = 5
turn_on_shield = 1


filePath = 'C:\\Users\\sfoss\\OneDrive - NTNU\\Skole\\Knowledge-based Engineering\\Assignments\\Assignment 3\\tmm4270_assignment3'

def read_dataset(last_name_input, flow_rate_input, volume_input):
    URL = "http://127.0.0.1:3030/teapot_project/query"

    query_read = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX teapot: <http://www.semanticweb.org/sfoss/ontologies/2023/10/teapot_project#>

    SELECT ?lastName ?teapot ?flowRate ?flowrateGA ?volume ?volumeGA
    WHERE {
        ?lastName teapot:ordersTeapot ?teapot.
        ?teapot rdf:type teapot:Teapot;
            teapot:hasFlowRate ?flowRate;
            teapot:hasVolume ?volume;
            teapot:hasFlowRateGA ?flowrateGA;
            teapot:hasVolumeGA ?volumeGA.
    }
    """

    # defining a query params 
    PARAMS = {'query': query_read}

    # sending get request and saving the response as response object 
    r = requests.get(url=URL, params=PARAMS)

    if r.status_code == 200:
        data = r.json()
        bindings = data['results']['bindings']
        order_list = []

        for binding in bindings:
            last_name = binding['lastName']['value'][binding['lastName']['value'].find('#')+1:]
            teapot = binding['teapot']['value'][binding['lastName']['value'].find('#')+1:]
            flow_rate = binding['flowRate']['value']
            flow_rate_ga = binding['flowrateGA']['value']
            volume = binding['volume']['value']
            volume_ga = binding['volumeGA']['value']

            order_list.append([last_name, teapot, flow_rate, flow_rate_ga, volume, volume_ga])

    else:
        print("Error:", r.status_code)

    if_flow, if_volume = False, False
    for orders in order_list:
        if(orders[2] == flow_rate_input):
            flow_rate_GA_generated = orders[3]
            if_flow = True

        if(orders[4] == volume_input):
            volume_GA_generated = orders[5]
            if_volume = True

        

    if(if_flow == False):
        flow_rate_GA_generated = str(GeneticAlgorithmFlow(float(flow_rate_input), 100, 0.15).calculate_flow(GeneticAlgorithmFlow(float(flow_rate_input), 100, 0.15).best_radius))
    if(if_volume == False):
        volume_GA_generated = str(GeneticAlgorithmVolume(float(volume_input), 100, 0.15).calculate_volume(GeneticAlgorithmVolume(float(volume_input), 100, 0.15).best_radius))

    insert_data(last_name_input, flow_rate_input, flow_rate_GA_generated, volume_input, volume_GA_generated, len(order_list)+1)


    #Open the template file
    f = open(filePath + "\\template\\test_html_server.py", "r")
    txt = f.read()

    # Replacing and writing the file to correct location
    #Not the best way to solve this, since the genetic algorithm is being called even though the data might be in the dataset
    #But the alternative involves a lot more coding than this. This is just to show that the appliction is working
    txt = txt.replace("<LAST_NAME>", last_name_input)
    txt = txt.replace("<VOLUME_RADIUS>", str(GeneticAlgorithmVolume(float(volume_input), 100, 0.15).best_radius))
    txt = txt.replace("<SPOUT_RADIUS>", str(GeneticAlgorithmFlow(float(flow_rate_input), 100, 0.15).best_radius))
    f.close()

    #Writing to the correct location
    f = open(filePath + "\\test_html_server.py", "w")
    f.write(txt)
    f.close()


    return flow_rate_GA_generated, volume_GA_generated