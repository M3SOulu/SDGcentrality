from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "springcloudmicroservices_77a0429"
serviceregistry = CClass(service, "serviceregistry", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Port': 8762, 'Service Discovery': 'Eureka'})
user_service = CClass(service, "user-service", stereotype_instances = [internal, local_logging, load_balancer], tagged_values = {'Port': 8081, 'Endpoints': "['/users', '/users/{userId}']", 'Load Balancer': 'Spring Cloud'})
rating_service = CClass(service, "rating-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/ratings', '/ratings/users/{userId}', '/ratings/hotels/{hotelId}']", 'Port': 8083})
hotel_service = CClass(service, "hotel-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/hotels', '/hotels/{hotelId}']", 'Port': 8082})
api_gateway = CClass(service, "api-gateway", stereotype_instances = [infrastructural, gateway], tagged_values = {'Gateway': 'Spring Cloud Gateway', 'Port': 8084})
database_user_service = CClass(external_component, "database-user-service", stereotype_instances = [entrypoint, exitpoint, external_database, plaintext_credentials], tagged_values = {'Database': 'MySQL', 'Port': 3306, 'Username': 'root'})
database_hotel_service = CClass(external_component, "database-hotel-service", stereotype_instances = [entrypoint, exitpoint, external_database, plaintext_credentials], tagged_values = {'Database': 'MySQL', 'Port': 3306, 'Username': 'root'})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, entrypoint, exitpoint])
add_links({user_service: rating_service}, stereotype_instances = [restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({database_user_service: user_service}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Username': 'root'})
add_links({database_hotel_service: hotel_service}, stereotype_instances = [plaintext_credentials_link, jdbc], tagged_values = {'Username': 'root'})
add_links({serviceregistry: api_gateway}, stereotype_instances = [restful_http])
add_links({user_service: serviceregistry}, stereotype_instances = [restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({rating_service: serviceregistry}, stereotype_instances = [restful_http])
add_links({hotel_service: serviceregistry}, stereotype_instances = [restful_http])
add_links({user: api_gateway}, stereotype_instances = [restful_http])
add_links({api_gateway: user}, stereotype_instances = [restful_http])
add_links({api_gateway: hotel_service}, stereotype_instances = [restful_http])
add_links({api_gateway: user_service}, stereotype_instances = [restful_http])
add_links({api_gateway: rating_service}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = api_gateway.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()