from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "spring-petclinic-microservices_66de0d4"
api_gateway = CClass(service, "api-gateway", stereotype_instances = [gateway, infrastructural, load_balancer], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
clients_service = CClass(service, "clients-service", stereotype_instances = [internal])
spring_petclinic_client = CClass(service, "spring-petclinic-client", stereotype_instances = [internal])
visits_service = CClass(service, "visits-service", stereotype_instances = [internal])
discovery_server = CClass(service, "discovery-server", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Service Discovery': 'Eureka'})
petclinic_config_server = CClass(service, "petclinic-config-server", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
petclinic = CClass(service, "petclinic", stereotype_instances = [internal])
vets_service = CClass(service, "vets-service", stereotype_instances = [internal])
github_repository = CClass(external_component, "github-repository", stereotype_instances = [github_repository, entrypoint], tagged_values = {'URL': 'file:///${GIT_REPO}'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, user_stereotype, entrypoint])
add_links({github_repository: petclinic_config_server}, stereotype_instances = [restful_http])
add_links({petclinic_config_server: api_gateway}, stereotype_instances = [restful_http])
add_links({petclinic_config_server: clients_service}, stereotype_instances = [restful_http])
add_links({petclinic_config_server: visits_service}, stereotype_instances = [restful_http])
add_links({petclinic_config_server: discovery_server}, stereotype_instances = [restful_http])
add_links({petclinic_config_server: vets_service}, stereotype_instances = [restful_http])
add_links({discovery_server: api_gateway}, stereotype_instances = [restful_http])
add_links({visits_service: discovery_server}, stereotype_instances = [restful_http])
add_links({clients_service: discovery_server}, stereotype_instances = [restful_http])
add_links({vets_service: discovery_server}, stereotype_instances = [restful_http])
add_links({user: api_gateway}, stereotype_instances = [restful_http])
add_links({api_gateway: user}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = vets_service.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()