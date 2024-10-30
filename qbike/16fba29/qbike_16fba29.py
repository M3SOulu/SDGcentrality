from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "qbike_16fba29"
qbike_order = CClass(service, "qbike-order", stereotype_instances = [local_logging, internal, load_balancer], tagged_values = {'Port': 8002, 'Load Balancer': 'Spring Cloud'})
qbike_intention = CClass(service, "qbike-intention", stereotype_instances = [circuit_breaker, local_logging, internal, load_balancer], tagged_values = {'Port': 8001, 'Load Balancer': 'Spring Cloud'})
microservice_api_gateway = CClass(service, "microservice-api-gateway", stereotype_instances = [gateway, infrastructural, load_balancer], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon', 'Port': 8050})
qbike_trip = CClass(service, "qbike-trip", stereotype_instances = [circuit_breaker, local_logging, internal, load_balancer], tagged_values = {'Port': 8003, 'Load Balancer': 'Spring Cloud'})
eureka = CClass(service, "eureka", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Port': 8761, 'Service Discovery': 'Eureka'})
qbike_uc = CClass(service, "qbike-uc", stereotype_instances = [internal], tagged_values = {'Endpoints': '[\'/"users\']', 'Port': 8000})
testclient = CClass(service, "testclient", stereotype_instances = [internal])
zipkin_server = CClass(service, "zipkin-server", stereotype_instances = [internal], tagged_values = {'Port': 9411})
mysql = CClass(service, "mysql", stereotype_instances = [internal], tagged_values = {'Port': 13306})
rabbit = CClass(service, "rabbit", stereotype_instances = [message_broker, infrastructural], tagged_values = {'Message Broker': 'RabbitMQ', 'Port': 15672})
database_qbike_order = CClass(external_component, "database-qbike-order", stereotype_instances = [entrypoint, plaintext_credentials, exitpoint, external_database], tagged_values = {'Username': 'root', 'Database': 'MySQL'})
database_qbike_intention = CClass(external_component, "database-qbike-intention", stereotype_instances = [entrypoint, plaintext_credentials, exitpoint, external_database], tagged_values = {'Username': 'root', 'Database': 'MySQL'})
database_qbike_trip = CClass(external_component, "database-qbike-trip", stereotype_instances = [entrypoint, plaintext_credentials, exitpoint, external_database], tagged_values = {'Username': 'root', 'Database': 'MySQL'})
database_qbike_uc = CClass(external_component, "database-qbike-uc", stereotype_instances = [entrypoint, plaintext_credentials, exitpoint, external_database], tagged_values = {'Username': 'root', 'Database': 'MySQL'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, user_stereotype, entrypoint])
add_links({rabbit: qbike_order}, stereotype_instances = [message_consumer_rabbitmq, restful_http], tagged_values = {'Queue': 'intention'})
add_links({qbike_intention: qbike_trip}, stereotype_instances = [load_balanced_link, restful_http, circuit_breaker_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({database_qbike_order: qbike_order}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Username': 'root'})
add_links({database_qbike_intention: qbike_intention}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Username': 'root'})
add_links({database_qbike_trip: qbike_trip}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Username': 'root'})
add_links({database_qbike_uc: qbike_uc}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Username': 'root'})
add_links({uc: mysql}, stereotype_instances = [restful_http])
add_links({uc: rabbit}, stereotype_instances = [restful_http])
add_links({intention: mysql}, stereotype_instances = [restful_http])
add_links({intention: rabbit}, stereotype_instances = [restful_http])
add_links({position: mysql}, stereotype_instances = [restful_http])
add_links({position: rabbit}, stereotype_instances = [restful_http])
add_links({order: mysql}, stereotype_instances = [restful_http])
add_links({order: rabbit}, stereotype_instances = [restful_http])
add_links({api_gateway: rabbit}, stereotype_instances = [restful_http])
add_links({zipkin: rabbit}, stereotype_instances = [restful_http])
add_links({qbike_uc: eureka}, stereotype_instances = [restful_http])
add_links({qbike_trip: eureka}, stereotype_instances = [load_balanced_link, restful_http, circuit_breaker_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({qbike_intention: eureka}, stereotype_instances = [load_balanced_link, restful_http, circuit_breaker_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({qbike_order: eureka}, stereotype_instances = [load_balanced_link, restful_http], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({eureka: microservice_api_gateway}, stereotype_instances = [restful_http])
add_links({user: microservice_api_gateway}, stereotype_instances = [restful_http])
add_links({microservice_api_gateway: user}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = rabbit.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()