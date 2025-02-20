import requests

def insert_data(last_name_input, flow_rate_input, flow_rate_GA, volume_input, volume_GA, length_dataset):
    URL = "http://127.0.0.1:3030/teapot_project/update"

    query_insert = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX teapot: <http://www.semanticweb.org/sfoss/ontologies/2023/10/teapot_project#>

    INSERT DATA {{
    # Inserting a new customer with a name
    teapot:{last_name_input} rdf:type teapot:Customer;
        teapot:hasLastName "{last_name_input}".
    
    # Inserting a new teapot ordered by the new customer
    teapot:Teapot{length_dataset} rdf:type teapot:Teapot;
        teapot:hasFlowRate {flow_rate_input};
        teapot:hasVolume {volume_input};
        teapot:hasFlowRateGA {flow_rate_GA};
        teapot:hasVolumeGA {volume_GA}.

    teapot:{last_name_input} teapot:ordersTeapot teapot:Teapot{length_dataset}.
    }}
    """

    # defining a query params
    PARAMS = {'update': query_insert}

    # sending post request and saving the response as response object
    r = requests.post(url=URL, data=PARAMS)

    if r.status_code == 200:
        print("Data inserted successfully.")
    else:
        print("Error:", r.status_code)
        print("Response text:", r.text)