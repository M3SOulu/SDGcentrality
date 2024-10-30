from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "micro_webshop_6667ecf"
zuul = CClass(service, "zuul", stereotype_instances = [infrastructural, load_balancer, gateway], tagged_values = {'Port': 8081, 'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
eureka = CClass(service, "eureka", stereotype_instances = [service_discovery, monitoring_dashboard, infrastructural], tagged_values = {'Port': 8761, 'Monitoring Dashboard': 'Hystrix', 'Service Discovery': 'Eureka'})
user_proxy = CClass(service, "user-proxy", stereotype_instances = [circuit_breaker, internal, load_balancer], tagged_values = {'Circuit Breaker': 'Hystrix', 'Port': 8088, 'Endpoints': "['/users/{userId}', '/users']", 'Load Balancer': 'Ribbon'})
product_service = CClass(service, "product-service", stereotype_instances = [internal], tagged_values = {'Port': 8092, 'Endpoints': "['/', '/products/{productId}', '/products', '/products/{categoryId}']"})
category_service = CClass(service, "category-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/categories/byname/{name}', '/', '/status', '/categories/{id}', '/categories']", 'Port': 8091})
security_service = CClass(service, "security-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/', '/users', '/users/{username}', '/roles/{rolelevel}']", 'Port': 8093})
product_proxy = CClass(service, "product-proxy", stereotype_instances = [resource_server, circuit_breaker, internal, load_balancer], tagged_values = {'Circuit Breaker': 'Hystrix', 'Endpoints': "['/', '/products/{productId}', '/categories', '/products']", 'Port': 8089, 'Load Balancer': 'Ribbon'})
auth_server = CClass(service, "auth-server", stereotype_instances = [authorization_server, resource_server, in_memory_authentication, infrastructural], tagged_values = {'Port': 8010, 'Authorization Server': 'Spring OAuth2', 'Username': 'user', 'Password': 'password', 'Endpoints': "['/user']"})
database_product_service = CClass(external_component, "database-product-service", stereotype_instances = [entrypoint, external_database, plaintext_credentials, exitpoint], tagged_values = {'Port': 3306, 'Username': 'admin', 'Password': '', 'Database': 'MySQL'})
database_category_service = CClass(external_component, "database-category-service", stereotype_instances = [entrypoint, external_database, plaintext_credentials, exitpoint], tagged_values = {'Port': 3306, 'Username': 'admin', 'Password': '', 'Database': 'MySQL'})
database_security_service = CClass(external_component, "database-security-service", stereotype_instances = [entrypoint, external_database, plaintext_credentials, exitpoint], tagged_values = {'Port': 3306, 'Username': 'admin', 'Password': '', 'Database': 'MySQL'})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, entrypoint, exitpoint])
add_links({user_proxy: security_service}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({product_proxy: category_service}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({product_proxy: product_service}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({database_product_service: product_service}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Password': '', 'Username': 'admin'})
add_links({database_category_service: category_service}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Password': '', 'Username': 'admin'})
add_links({database_security_service: security_service}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Password': '', 'Username': 'admin'})
add_links({category_service: eureka}, stereotype_instances = [restful_http])
add_links({security_service: eureka}, stereotype_instances = [restful_http])
add_links({user_proxy: eureka}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({auth_server: eureka}, stereotype_instances = [restful_http])
add_links({product_service: eureka}, stereotype_instances = [restful_http])
add_links({product_proxy: eureka}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({eureka: zuul}, stereotype_instances = [restful_http])
add_links({user: zuul}, stereotype_instances = [restful_http])
add_links({zuul: user}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = auth_server.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()