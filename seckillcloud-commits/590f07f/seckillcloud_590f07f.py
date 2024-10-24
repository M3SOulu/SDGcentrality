from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "seckillcloud_590f07f"
cloud_uaa = CClass(service, "cloud-uaa", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8088, 'Logging Technology': 'Lombok'})
cloud_gateway = CClass(service, "cloud-gateway", stereotype_instances = [local_logging, infrastructural, gateway], tagged_values = {'Gateway': 'Spring Cloud Gateway', 'Logging Technology': 'Lombok', 'Port': 8205})
cloud_mission = CClass(service, "cloud-mission", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8888, 'Logging Technology': 'Lombok'})
cloud_common = CClass(service, "cloud-common", stereotype_instances = [local_logging, internal], tagged_values = {'Logging Technology': 'Lombok'})
cloud_manage = CClass(service, "cloud-manage", stereotype_instances = [local_logging, pre_authorized_endpoints, internal, csrf_disabled, encryption], tagged_values = {'Pre-authorized Endpoints': "['/{id}']", 'Logging Technology': 'Lombok', 'Port': 8070})
cloud_monitor = CClass(service, "cloud-monitor", stereotype_instances = [administration_server, infrastructural, basic_authentication], tagged_values = {'Port': 8890, 'Administration Server': 'Spring Boot Admin'})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [plaintext_credentials, infrastructural, message_broker], tagged_values = {'Username': 'guest', 'Message Broker': 'RabbitMQ', 'Port': 5672, 'Password': 'guest'})
mysql = CClass(service, "mysql", stereotype_instances = [internal], tagged_values = {'Port': 3305})
database_cloud_manage = CClass(external_component, "database-cloud-manage", stereotype_instances = [entrypoint, exitpoint, external_database], tagged_values = {'Database': 'MySQL'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, exitpoint, user_stereotype])
add_links({rabbitmq: cloud_mission}, stereotype_instances = [message_consumer_rabbitmq, restful_http], tagged_values = {'Queue': 'None'})
add_links({cloud_mission: rabbitmq}, stereotype_instances = [message_producer_rabbitmq, plaintext_credentials_link, restful_http], tagged_values = {'Producer Exchange': 'None', 'Routing Key': 'None'})
add_links({database_cloud_manage: cloud_manage}, stereotype_instances = [jdbc])
add_links({user: cloud_gateway}, stereotype_instances = [restful_http])
add_links({cloud_gateway: user}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_monitor}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_manage}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_uaa}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_mission}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = mysql.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()