from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "spring-boot-microservices-workshop_8b01c6d"
movie_info_service = CClass(service, "movie-info-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/movies', '/movies/{movieId}']", 'Port': 8082})
ratings_data_service = CClass(service, "ratings-data-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/ratingsdata', '/ratingsdata/user/{userId}', '/ratingsdata/movies/{movieId}']", 'Port': 8083})
movie_catalog_service = CClass(service, "movie-catalog-service", stereotype_instances = [internal, load_balancer], tagged_values = {'Port': 8081, 'Endpoints': "['/catalog', '/catalog/{userId}']", 'Load Balancer': 'Spring Cloud'})
discovery_server = CClass(service, "discovery-server", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Port': 8761, 'Service Discovery': 'Eureka'})
add_links({movie_catalog_service: ratings_data_service}, stereotype_instances = [restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({movie_catalog_service: movie_info_service}, stereotype_instances = [restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({movie_catalog_service: discovery_server}, stereotype_instances = [restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({ratings_data_service: discovery_server}, stereotype_instances = [restful_http])
add_links({movie_info_service: discovery_server}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = discovery_server.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()