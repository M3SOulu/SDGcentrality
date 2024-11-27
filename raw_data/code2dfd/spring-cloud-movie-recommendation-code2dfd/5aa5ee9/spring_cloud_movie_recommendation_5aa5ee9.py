from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "spring-cloud-movie-recommendation_5aa5ee9"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/recommendation/movie', '/recommendation', '/recommendation/user', '/recommendation/user/{userId}', '/recommendation/movie/{movieId}', '/recommendation/dummyData', '/recommendation/recommend/user/{userId}']"})
config_service = CClass(service, "config-service", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
recommendation_client = CClass(service, "recommendation-client", stereotype_instances = [circuit_breaker, monitoring_dashboard, infrastructural, gateway, load_balancer], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Load Balancer': 'Spring Cloud', 'Endpoints': "['/api/recommendation/user/{userId}', '/user/{userId}', '/recommendation/dummyData', '/newuser', '/api/userDetails/{userId}', '/movie', '/movie/dummyData', '/api', '/user']", 'Gateway': 'Zuul'})
eureka_service = CClass(service, "eureka-service", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Service Discovery': 'Eureka'})
user_service = CClass(service, "user-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/user/{userId}', '/user']"})
movie_service = CClass(service, "movie-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/movie/{movieId}', '/movie', '/movie/list', '/movie/dummyData']"})
github_repository = CClass(external_component, "github-repository", stereotype_instances = [github_repository, entrypoint], tagged_values = {'URL': 'https://github.com/mdeket/spring-cloud-example-config-repo.git\n'})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, entrypoint, exitpoint])
add_links({github_repository: config_service}, stereotype_instances = [restful_http])
add_links({config_service: recommendation_service}, stereotype_instances = [restful_http])
add_links({config_service: recommendation_client}, stereotype_instances = [restful_http])
add_links({config_service: eureka_service}, stereotype_instances = [restful_http])
add_links({config_service: user_service}, stereotype_instances = [restful_http])
add_links({config_service: movie_service}, stereotype_instances = [restful_http])
add_links({recommendation_client: user_service}, stereotype_instances = [restful_http, circuit_breaker_link, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({recommendation_client: recommendation_service}, stereotype_instances = [restful_http, circuit_breaker_link, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({recommendation_client: movie_service}, stereotype_instances = [restful_http, circuit_breaker_link, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({user_service: eureka_service}, stereotype_instances = [restful_http])
add_links({eureka_service: recommendation_client}, stereotype_instances = [restful_http])
add_links({recommendation_service: eureka_service}, stereotype_instances = [restful_http])
add_links({movie_service: eureka_service}, stereotype_instances = [restful_http])
add_links({user: recommendation_client}, stereotype_instances = [restful_http])
add_links({recommendation_client: user}, stereotype_instances = [restful_http, circuit_breaker_link, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
model = CBundle(model_name, elements = movie_service.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()