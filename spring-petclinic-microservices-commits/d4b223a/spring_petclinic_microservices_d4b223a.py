from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "spring-petclinic-microservices_d4b223a"
tracing_server = CClass(service, "tracing-server", stereotype_instances = [internal], tagged_values = {'Port': 8081})
config_server = CClass(service, "config-server", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
discovery_server = CClass(service, "discovery-server", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Port': 8761, 'Service Discovery': 'Eureka'})
admin_server = CClass(service, "admin-server", stereotype_instances = [administration_server, infrastructural], tagged_values = {'Administration Server': 'Spring Boot Admin', 'Port': 9090})
vets_service = CClass(service, "vets-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/vets']", 'Port': 8081})
api_gateway = CClass(service, "api-gateway", stereotype_instances = [infrastructural, gateway, load_balancer], tagged_values = {'Port': 8081, 'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
customers_service = CClass(service, "customers-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/owners', '/owners/{ownerId}']", 'Port': 8081, 'Logging Technology': 'Lombok'})
visits_service = CClass(service, "visits-service", stereotype_instances = [internal, local_logging], tagged_values = {'Logging Technology': 'Lombok', 'Port': 8081})
spring_petclinic_monitoring = CClass(service, "spring-petclinic-monitoring", stereotype_instances = [internal])
github_repository = CClass(external_component, "github-repository", stereotype_instances = [github_repository, entrypoint], tagged_values = {'URL': 'https://github.com/spring-petclinic/spring-petclinic-microservices-config'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, entrypoint, user_stereotype])
add_links({github_repository: config_server}, stereotype_instances = [restful_http])
add_links({config_server: tracing_server}, stereotype_instances = [restful_http])
add_links({config_server: discovery_server}, stereotype_instances = [restful_http])
add_links({config_server: admin_server}, stereotype_instances = [restful_http])
add_links({config_server: vets_service}, stereotype_instances = [restful_http])
add_links({config_server: api_gateway}, stereotype_instances = [restful_http])
add_links({config_server: customers_service}, stereotype_instances = [restful_http])
add_links({config_server: visits_service}, stereotype_instances = [restful_http])
add_links({customers_service: tracing_server}, stereotype_instances = [restful_http])
add_links({visits_service: tracing_server}, stereotype_instances = [restful_http])
add_links({vets_service: tracing_server}, stereotype_instances = [restful_http])
add_links({api_gateway: customers_service}, stereotype_instances = [load_balanced_link, restful_http], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({api_gateway: visits_service}, stereotype_instances = [load_balanced_link, restful_http], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({api_gateway: vets_service}, stereotype_instances = [load_balanced_link, restful_http], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({api_gateway: tracing_server}, stereotype_instances = [load_balanced_link, restful_http], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({vets_service: discovery_server}, stereotype_instances = [restful_http])
add_links({discovery_server: api_gateway}, stereotype_instances = [restful_http])
add_links({admin_server: discovery_server}, stereotype_instances = [restful_http])
add_links({visits_service: discovery_server}, stereotype_instances = [restful_http])
add_links({tracing_server: discovery_server}, stereotype_instances = [restful_http])
add_links({customers_service: discovery_server}, stereotype_instances = [restful_http])
add_links({user: api_gateway}, stereotype_instances = [restful_http])
add_links({api_gateway: user}, stereotype_instances = [load_balanced_link, restful_http], tagged_values = {'Load Balancer': 'Spring Cloud'})
model = CBundle(model_name, elements = spring_petclinic_monitoring.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()