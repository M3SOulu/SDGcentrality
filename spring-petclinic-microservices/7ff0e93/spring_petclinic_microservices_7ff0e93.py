from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "spring-petclinic-microservices_7ff0e93"
tracing_server = CClass(service, "tracing-server", stereotype_instances = [internal])
config_server = CClass(service, "config-server", stereotype_instances = [infrastructural, configuration_server], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
discovery_server = CClass(service, "discovery-server", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Service Discovery': 'Eureka'})
admin_server = CClass(service, "admin-server", stereotype_instances = [infrastructural, administration_server], tagged_values = {'Administration Server': 'Spring Boot Admin'})
vets_service = CClass(service, "vets-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/vets']"})
api_gateway = CClass(service, "api-gateway", stereotype_instances = [infrastructural, load_balancer, gateway], tagged_values = {'Load Balancer': 'Ribbon', 'Gateway': 'Zuul'})
customers_service = CClass(service, "customers-service", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/owners/{ownerId}', '/owners']", 'Logging Technology': 'Lombok'})
visits_service = CClass(service, "visits-service", stereotype_instances = [local_logging, internal], tagged_values = {'Logging Technology': 'Lombok'})
github_repository = CClass(external_component, "github-repository", stereotype_instances = [entrypoint, github_repository], tagged_values = {'URL': 'https://github.com/spring-petclinic/spring-petclinic-microservices-config'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, exitpoint, user_stereotype])
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
add_links({api_gateway: customers_service}, stereotype_instances = [restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({api_gateway: visits_service}, stereotype_instances = [restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({api_gateway: vets_service}, stereotype_instances = [restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({api_gateway: tracing_server}, stereotype_instances = [restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({discovery_server: api_gateway}, stereotype_instances = [restful_http])
add_links({vets_service: discovery_server}, stereotype_instances = [restful_http])
add_links({visits_service: discovery_server}, stereotype_instances = [restful_http])
add_links({tracing_server: discovery_server}, stereotype_instances = [restful_http])
add_links({customers_service: discovery_server}, stereotype_instances = [restful_http])
add_links({admin_server: discovery_server}, stereotype_instances = [restful_http])
add_links({user: api_gateway}, stereotype_instances = [restful_http])
add_links({api_gateway: user}, stereotype_instances = [restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
model = CBundle(model_name, elements = visits_service.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()