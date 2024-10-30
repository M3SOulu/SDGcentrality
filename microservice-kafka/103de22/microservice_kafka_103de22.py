from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "microservice-kafka_103de22"
invoicing = CClass(service, "invoicing", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080})
order = CClass(service, "order", stereotype_instances = [internal], tagged_values = {'Endpoints': '[\'/"order\']', 'Port': 8080})
shipping = CClass(service, "shipping", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080})
zookeeper = CClass(service, "zookeeper", stereotype_instances = [infrastructural, configuration_server], tagged_values = {'Configuration Server': 'ZooKeeper'})
kafka = CClass(service, "kafka", stereotype_instances = [infrastructural, message_broker], tagged_values = {'Message Broker': 'Kafka'})
apache = CClass(service, "apache", stereotype_instances = [infrastructural, web_server], tagged_values = {'Web Server': 'Apache httpd', 'Port': 8080})
postgres = CClass(service, "postgres", stereotype_instances = [database, plaintext_credentials], tagged_values = {'Database': 'PostgreSQL', 'Username': 'dbuser', 'Password': 'dbpass'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({kafka: shipping}, stereotype_instances = [restful_http, message_consumer_kafka], tagged_values = {'Consumer Topic': 'order'})
add_links({kafka: invoicing}, stereotype_instances = [restful_http, message_consumer_kafka], tagged_values = {'Consumer Topic': 'order'})
add_links({order: kafka}, stereotype_instances = [message_producer_kafka, restful_http], tagged_values = {'Producer Topic': 'order'})
add_links({postgres: invoicing}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Username': 'dbuser', 'Password': 'dbpass'})
add_links({postgres: order}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Username': 'dbuser', 'Password': 'dbpass'})
add_links({postgres: shipping}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Username': 'dbuser', 'Password': 'dbpass'})
add_links({order: order}, stereotype_instances = [restful_http])
add_links({apache: order}, stereotype_instances = [restful_http])
add_links({apache: shipping}, stereotype_instances = [restful_http])
add_links({apache: invoicing}, stereotype_instances = [restful_http])
add_links({shipping: kafka}, stereotype_instances = [restful_http])
add_links({invoicing: kafka}, stereotype_instances = [restful_http])
add_links({zookeeper: kafka}, stereotype_instances = [restful_http])
add_links({user: apache}, stereotype_instances = [restful_http])
add_links({apache: user}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = postgres.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()