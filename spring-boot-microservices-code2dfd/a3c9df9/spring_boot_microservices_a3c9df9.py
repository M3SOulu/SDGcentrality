from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "spring-boot-microservices_a3c9df9"
web_portal = CClass(service, "web-portal", stereotype_instances = [internal])
user_webservice = CClass(service, "user-webservice", stereotype_instances = [resource_server, internal, authentication_scope_all_requests], tagged_values = {'Endpoints': "['/', '/{userName}']"})
api_gateway = CClass(service, "api-gateway", stereotype_instances = [gateway, load_balancer, infrastructural], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
comments_webservice = CClass(service, "comments-webservice", stereotype_instances = [resource_server, internal, authentication_scope_all_requests], tagged_values = {'Endpoints': "['/comments/{taskId}', '/comments']"})
auth_server = CClass(service, "auth-server", stereotype_instances = [resource_server, authorization_server, infrastructural], tagged_values = {'Endpoints': "['/', '/me']", 'Authorization Server': 'Spring OAuth2'})
webservice_registry = CClass(service, "webservice-registry", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Service Discovery': 'Eureka'})
task_webservice = CClass(service, "task-webservice", stereotype_instances = [circuit_breaker, internal, resource_server, authentication_scope_all_requests], tagged_values = {'Endpoints': "['/', '/usertask/{userName}', '/{taskId}']"})
configserver = CClass(service, "configserver", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
github_repository = CClass(external_component, "github-repository", stereotype_instances = [entrypoint, github_repository], tagged_values = {'URL': 'https://github.com/anilallewar/sample-config'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({github_repository: configserver}, stereotype_instances = [restful_http])
add_links({configserver: web_portal}, stereotype_instances = [restful_http])
add_links({configserver: user_webservice}, stereotype_instances = [restful_http])
add_links({configserver: api_gateway}, stereotype_instances = [restful_http])
add_links({configserver: comments_webservice}, stereotype_instances = [restful_http])
add_links({configserver: auth_server}, stereotype_instances = [restful_http])
add_links({configserver: webservice_registry}, stereotype_instances = [restful_http])
add_links({configserver: task_webservice}, stereotype_instances = [restful_http])
add_links({task_webservice: comments_webservice}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({auth_server: webservice_registry}, stereotype_instances = [restful_http])
add_links({web_portal: webservice_registry}, stereotype_instances = [restful_http])
add_links({comments_webservice: webservice_registry}, stereotype_instances = [restful_http])
add_links({webservice_registry: api_gateway}, stereotype_instances = [restful_http])
add_links({task_webservice: webservice_registry}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({user_webservice: webservice_registry}, stereotype_instances = [restful_http])
add_links({user: api_gateway}, stereotype_instances = [restful_http])
add_links({api_gateway: user}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = configserver.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()