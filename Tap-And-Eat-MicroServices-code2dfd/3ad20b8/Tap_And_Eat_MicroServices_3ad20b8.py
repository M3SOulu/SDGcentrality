from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "Tap-And-Eat-MicroServices_3ad20b8"
account_service = CClass(service, "account-service", stereotype_instances = [internal], tagged_values = {'Port': 8000, 'Endpoints': "['/accounts']"})
config_service = CClass(service, "config-service", stereotype_instances = [infrastructural, configuration_server], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8167})
foodtray_service = CClass(service, "foodtray-service", stereotype_instances = [infrastructural, monitoring_dashboard, circuit_breaker], tagged_values = {'Port': 8005, 'Circuit Breaker': 'Hystrix', 'Monitoring Dashboard': 'Hystrix'})
discovery_service = CClass(service, "discovery-service", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Port': 8002, 'Service Discovery': 'Eureka'})
price_service = CClass(service, "price-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/prices']", 'Port': 8002})
store_service = CClass(service, "store-service", stereotype_instances = [internal], tagged_values = {'Port': 8003, 'Endpoints': "['/stores']"})
customer_service = CClass(service, "customer-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/customers']", 'Port': 8002})
item_service = CClass(service, "item-service", stereotype_instances = [internal], tagged_values = {'Port': 8004, 'Endpoints': "['/items']"})
github_repository = CClass(external_component, "github-repository", stereotype_instances = [github_repository, entrypoint], tagged_values = {'URL': 'https://github.com/jferrater/ConfigData'})
add_links({github_repository: config_service}, stereotype_instances = [restful_http])
add_links({config_service: account_service}, stereotype_instances = [restful_http])
add_links({config_service: foodtray_service}, stereotype_instances = [restful_http])
add_links({config_service: price_service}, stereotype_instances = [restful_http])
add_links({config_service: store_service}, stereotype_instances = [restful_http])
add_links({config_service: customer_service}, stereotype_instances = [restful_http])
add_links({config_service: item_service}, stereotype_instances = [restful_http])
add_links({foodtray_service: item_service}, stereotype_instances = [restful_http, feign_connection, circuit_breaker_link, load_balanced_link], tagged_values = {'Load Balancer': 'Ribbon'})
add_links({foodtray_service: price_service}, stereotype_instances = [restful_http, feign_connection, circuit_breaker_link, load_balanced_link], tagged_values = {'Load Balancer': 'Ribbon'})
add_links({foodtray_service: discovery_service}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({customer_service: discovery_service}, stereotype_instances = [restful_http])
add_links({account_service: discovery_service}, stereotype_instances = [restful_http])
add_links({store_service: discovery_service}, stereotype_instances = [restful_http])
add_links({config_service: discovery_service}, stereotype_instances = [restful_http])
add_links({price_service: discovery_service}, stereotype_instances = [restful_http])
add_links({item_service: discovery_service}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = item_service.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()