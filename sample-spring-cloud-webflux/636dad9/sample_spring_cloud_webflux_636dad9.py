from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "sample-spring-cloud-webflux_636dad9"
account_service = CClass(service, "account-service", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 2222})
gateway_service = CClass(service, "gateway-service", stereotype_instances = [infrastructural, gateway], tagged_values = {'Port': 8090, 'Gateway': 'Spring Cloud Gateway'})
customer_service = CClass(service, "customer-service", stereotype_instances = [internal, load_balancer, local_logging], tagged_values = {'Port': 3333, 'Load Balancer': 'Spring Cloud'})
discovery_service = CClass(service, "discovery-service", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Port': 8761, 'Service Discovery': 'Eureka'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({discovery_service: gateway_service}, stereotype_instances = [restful_http])
add_links({account_service: discovery_service}, stereotype_instances = [restful_http])
add_links({customer_service: discovery_service}, stereotype_instances = [load_balanced_link, restful_http], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({user: gateway_service}, stereotype_instances = [restful_http])
add_links({gateway_service: user}, stereotype_instances = [restful_http])
add_links({gateway_service: account_service}, stereotype_instances = [restful_http])
add_links({gateway_service: customer_service}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = discovery_service.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()