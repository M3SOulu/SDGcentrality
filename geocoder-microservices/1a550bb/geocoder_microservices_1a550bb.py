from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "geocoder-microservices_1a550bb"
geocoderlocal_service = CClass(service, "geocoderlocal-service", stereotype_instances = [internal, circuit_breaker, resource_server], tagged_values = {'Port': 9001, 'Circuit Breaker': 'Hystrix', 'Endpoints': "['/geocoder']"})
zuul_gateway = CClass(service, "zuul-gateway", stereotype_instances = [gateway, local_logging, infrastructural, load_balancer], tagged_values = {'Gateway': 'Zuul', 'Port': 4000, 'Load Balancer': 'Ribbon'})
geocoderremote_service = CClass(service, "geocoderremote-service", stereotype_instances = [internal, circuit_breaker, resource_server], tagged_values = {'Port': 9002, 'Circuit Breaker': 'Hystrix', 'Endpoints': "['/geocoder']"})
hystrix_dashboard = CClass(service, "hystrix-dashboard", stereotype_instances = [monitoring_server, infrastructural, monitoring_dashboard], tagged_values = {'Port': 7979, 'Monitoring Server': 'Turbine', 'Monitoring Dashboard': 'Hystrix'})
eureka_discovery = CClass(service, "eureka-discovery", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Service Discovery': 'Eureka', 'Port': 8761})
configurator = CClass(service, "configurator", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
auth_service = CClass(service, "auth-service", stereotype_instances = [authorization_server, local_logging, resource_server, infrastructural, encryption, token_server], tagged_values = {'Port': 5000, 'Authorization Server': 'Spring OAuth2', 'Endpoints': "['/users', '/users/current']"})
mongodb = CClass(service, "mongodb", stereotype_instances = [plaintext_credentials, database], tagged_values = {'Database': 'MongoDB', 'Password': 'pwd', 'Port': 25000, 'Username': 'user'})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, exitpoint, entrypoint])
add_links({configurator: geocoderlocal_service}, stereotype_instances = [restful_http])
add_links({configurator: zuul_gateway}, stereotype_instances = [restful_http])
add_links({configurator: geocoderremote_service}, stereotype_instances = [restful_http])
add_links({configurator: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({configurator: eureka_discovery}, stereotype_instances = [restful_http])
add_links({configurator: auth_service}, stereotype_instances = [restful_http])
add_links({mongodb: geocoderremote_service}, stereotype_instances = [jdbc, plaintext_credentials_link], tagged_values = {'Password': 'pwd', 'Username': 'user'})
add_links({mongodb: auth_service}, stereotype_instances = [jdbc, plaintext_credentials_link], tagged_values = {'Password': 'pwd', 'Username': 'user'})
add_links({geocoderremote_service: eureka_discovery}, stereotype_instances = [restful_http])
add_links({eureka_discovery: zuul_gateway}, stereotype_instances = [restful_http])
add_links({auth_service: eureka_discovery}, stereotype_instances = [restful_http])
add_links({geocoderlocal_service: eureka_discovery}, stereotype_instances = [restful_http])
add_links({user: zuul_gateway}, stereotype_instances = [restful_http])
add_links({zuul_gateway: user}, stereotype_instances = [restful_http])
add_links({zuul_gateway: auth_service}, stereotype_instances = [circuit_breaker_link, load_balanced_link, restful_http], tagged_values = {'Load Balancer': 'Ribbon', 'Circuit Breaker': 'Hystrix'})
add_links({auth_service: geocoderlocal_service}, stereotype_instances = [auth_provider, authentication_with_plaintext_credentials, restful_http, plaintext_credentials_link], tagged_values = {'Password': 'geocoderLocal-pwd'})
add_links({auth_service: geocoderremote_service}, stereotype_instances = [auth_provider, authentication_with_plaintext_credentials, restful_http, plaintext_credentials_link], tagged_values = {'Password': 'pwd1'})
add_links({hystrix_dashboard: hystrix_dashboard}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = mongodb.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()