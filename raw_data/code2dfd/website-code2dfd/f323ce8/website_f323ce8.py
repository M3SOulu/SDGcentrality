from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "website_f323ce8"
authserver = CClass(service, "authserver", stereotype_instances = [resource_server, authorization_server, authentication_scope_all_requests, basic_authentication, local_logging, infrastructural], tagged_values = {'Authorization Server': 'Spring OAuth2', 'Logging Technology': 'Lombok', 'Endpoints': "['/user', '/', '/admin']", 'Port': 80})
backend = CClass(service, "backend", stereotype_instances = [local_logging, internal], tagged_values = {'Logging Technology': 'Lombok', 'Port': 80})
common = CClass(service, "common", stereotype_instances = [local_logging, internal], tagged_values = {'Logging Technology': 'Lombok'})
registry = CClass(service, "registry", stereotype_instances = [csrf_disabled, authentication_scope_all_requests, basic_authentication, service_discovery, infrastructural], tagged_values = {'Port': 8761, 'Service Discovery': 'Eureka'})
gateway = CClass(service, "gateway", stereotype_instances = [gateway, infrastructural], tagged_values = {'Gateway': 'Spring Cloud Gateway', 'Port': 443})
web_app = CClass(service, "web-app", stereotype_instances = [web_application, infrastructural], tagged_values = {'Web Application': 'Nginx'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, entrypoint, user_stereotype])
add_links({authserver: registry}, stereotype_instances = [restful_http])
add_links({backend: registry}, stereotype_instances = [restful_http])
add_links({registry: gateway}, stereotype_instances = [restful_http])
add_links({user: gateway}, stereotype_instances = [restful_http])
add_links({gateway: user}, stereotype_instances = [restful_http])
add_links({gateway: authserver}, stereotype_instances = [restful_http])
add_links({gateway: backend}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = web_app.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()