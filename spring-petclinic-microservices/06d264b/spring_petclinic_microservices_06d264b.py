from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "spring-petclinic-microservices_06d264b"
spring_petclinic_config_server = CClass(service, "spring-petclinic-config-server", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
discovery_server = CClass(service, "discovery-server", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Service Discovery': 'Eureka'})
vets_service = CClass(service, "vets-service", stereotype_instances = [internal])
api_gateway = CClass(service, "api-gateway", stereotype_instances = [gateway, infrastructural, load_balancer], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
spring_petclinic_ui = CClass(service, "spring-petclinic-ui", stereotype_instances = [internal])
customers_service = CClass(service, "customers-service", stereotype_instances = [internal])
visits_service = CClass(service, "visits-service", stereotype_instances = [internal])
spring_petclinic_monitoring = CClass(service, "spring-petclinic-monitoring", stereotype_instances = [internal])
github_repository = CClass(external_component, "github-repository", stereotype_instances = [entrypoint, github_repository], tagged_values = {'URL': 'https://github.com/spring-petclinic/spring-petclinic-microservices-config'})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, exitpoint, entrypoint])
add_links({github_repository: spring_petclinic_config_server}, stereotype_instances = [restful_http])
add_links({spring_petclinic_config_server: discovery_server}, stereotype_instances = [restful_http])
add_links({spring_petclinic_config_server: vets_service}, stereotype_instances = [restful_http])
add_links({spring_petclinic_config_server: api_gateway}, stereotype_instances = [restful_http])
add_links({spring_petclinic_config_server: customers_service}, stereotype_instances = [restful_http])
add_links({spring_petclinic_config_server: visits_service}, stereotype_instances = [restful_http])
add_links({vets_service: discovery_server}, stereotype_instances = [restful_http])
add_links({visits_service: discovery_server}, stereotype_instances = [restful_http])
add_links({discovery_server: api_gateway}, stereotype_instances = [restful_http])
add_links({customers_service: discovery_server}, stereotype_instances = [restful_http])
add_links({user: api_gateway}, stereotype_instances = [restful_http])
add_links({api_gateway: user}, stereotype_instances = [restful_http])
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