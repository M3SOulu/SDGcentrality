from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "microservices-basics-spring-boot_ac0a249"
web_portal = CClass(service, "web-portal", stereotype_instances = [monitoring_server, infrastructural, monitoring_dashboard], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Monitoring Server': 'Turbine'})
user_webservice = CClass(service, "user-webservice", stereotype_instances = [authentication_scope_all_requests, resource_server, internal], tagged_values = {'Endpoints': "['/', '/{userName}']"})
api_gateway = CClass(service, "api-gateway", stereotype_instances = [gateway, load_balancer, csrf_disabled, infrastructural], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
comments_webservice = CClass(service, "comments-webservice", stereotype_instances = [resource_server, internal], tagged_values = {'Endpoints': "['/comments', '/comments/{taskId}']"})
auth_server = CClass(service, "auth-server", stereotype_instances = [authorization_server, resource_server, infrastructural], tagged_values = {'Endpoints': "['/me']", 'Authorization Server': 'Spring OAuth2'})
webservice_registry = CClass(service, "webservice-registry", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Service Discovery': 'Eureka'})
task_webservice = CClass(service, "task-webservice", stereotype_instances = [circuit_breaker, authentication_scope_all_requests, internal, load_balancer, resource_server], tagged_values = {'Load Balancer': 'Spring Cloud', 'Endpoints': "['/usertask/{userName}', '/', '/{taskId}']"})
configserver = CClass(service, "configserver", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
zipkin_tracing = CClass(service, "zipkin-tracing", stereotype_instances = [internal])
zipkinserver = CClass(service, "zipkinserver", stereotype_instances = [internal], tagged_values = {'Port': 9411})
mysqldb = CClass(service, "mysqldb", stereotype_instances = [internal], tagged_values = {'Port': 3306})
github_repository = CClass(external_component, "github-repository", stereotype_instances = [github_repository, entrypoint], tagged_values = {'URL': 'https://github.com/anilallewar/microservices-basics-cloud-config'})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, entrypoint, exitpoint])
add_links({github_repository: configserver}, stereotype_instances = [restful_http])
add_links({configserver: web_portal}, stereotype_instances = [restful_http])
add_links({configserver: user_webservice}, stereotype_instances = [restful_http])
add_links({configserver: api_gateway}, stereotype_instances = [restful_http])
add_links({configserver: comments_webservice}, stereotype_instances = [restful_http])
add_links({configserver: auth_server}, stereotype_instances = [restful_http])
add_links({configserver: webservice_registry}, stereotype_instances = [restful_http])
add_links({configserver: task_webservice}, stereotype_instances = [restful_http])
add_links({configserver: zipkin_tracing}, stereotype_instances = [restful_http])
add_links({task_webservice: comments_webservice}, stereotype_instances = [circuit_breaker_link, restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({webservice_registry: api_gateway}, stereotype_instances = [restful_http])
add_links({user_webservice: webservice_registry}, stereotype_instances = [restful_http])
add_links({auth_server: webservice_registry}, stereotype_instances = [restful_http])
add_links({comments_webservice: webservice_registry}, stereotype_instances = [restful_http])
add_links({web_portal: webservice_registry}, stereotype_instances = [restful_http])
add_links({task_webservice: webservice_registry}, stereotype_instances = [circuit_breaker_link, restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({user: api_gateway}, stereotype_instances = [restful_http])
add_links({api_gateway: user}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = mysqldb.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()