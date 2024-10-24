from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "spring-petclinic-microservices_636d71f"
config_server = CClass(service, "config-server", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
discovery_server = CClass(service, "discovery-server", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Service Discovery': 'Eureka'})
hystrix_dashboard = CClass(service, "hystrix-dashboard", stereotype_instances = [monitoring_dashboard, infrastructural], tagged_values = {'Endpoints': "['/']", 'Monitoring Dashboard': 'Hystrix'})
admin_server = CClass(service, "admin-server", stereotype_instances = [administration_server, infrastructural], tagged_values = {'Administration Server': 'Spring Boot Admin'})
vets_service = CClass(service, "vets-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/vets']"})
api_gateway = CClass(service, "api-gateway", stereotype_instances = [load_balancer, gateway, circuit_breaker, infrastructural], tagged_values = {'Endpoints': "['/api/gatewayowners/{ownerId}', '/api/gateway']", 'Gateway': 'Spring Cloud Gateway', 'Circuit Breaker': 'Hystrix', 'Load Balancer': 'Spring Cloud'})
customers_service = CClass(service, "customers-service", stereotype_instances = [local_logging, internal], tagged_values = {'Logging Technology': 'Lombok', 'Endpoints': "['/owners/{ownerId}', '/owners']"})
visits_service = CClass(service, "visits-service", stereotype_instances = [local_logging, internal], tagged_values = {'Logging Technology': 'Lombok'})
grafana_server = CClass(service, "grafana-server", stereotype_instances = [internal], tagged_values = {'Port': 3000})
tracing_server = CClass(service, "tracing-server", stereotype_instances = [infrastructural, tracing_server], tagged_values = {'Tracing Server': 'Zipkin', 'Port': 9411})
prometheus_server = CClass(service, "prometheus-server", stereotype_instances = [internal], tagged_values = {'Port': 9091})
prometheus_server = CClass(service, "prometheus_server", stereotype_instances = [infrastructural, metrics_server], tagged_values = {'Metrics Server': 'Prometheus'})
github_repository = CClass(external_component, "github-repository", stereotype_instances = [entrypoint, github_repository], tagged_values = {'URL': 'file:///${GIT_REPO}'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, entrypoint, user_stereotype])
add_links({github_repository: config_server}, stereotype_instances = [restful_http])
add_links({config_server: discovery_server}, stereotype_instances = [restful_http])
add_links({config_server: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({config_server: admin_server}, stereotype_instances = [restful_http])
add_links({config_server: vets_service}, stereotype_instances = [restful_http])
add_links({config_server: api_gateway}, stereotype_instances = [restful_http])
add_links({config_server: customers_service}, stereotype_instances = [restful_http])
add_links({config_server: visits_service}, stereotype_instances = [restful_http])
add_links({admin_server: discovery_server}, stereotype_instances = [restful_http])
add_links({visits_service: discovery_server}, stereotype_instances = [restful_http])
add_links({hystrix_dashboard: discovery_server}, stereotype_instances = [restful_http])
add_links({customers_service: discovery_server}, stereotype_instances = [restful_http])
add_links({discovery_server: api_gateway}, stereotype_instances = [restful_http])
add_links({vets_service: discovery_server}, stereotype_instances = [restful_http])
add_links({user: api_gateway}, stereotype_instances = [restful_http])
add_links({api_gateway: user}, stereotype_instances = [circuit_breaker_link, restful_http, load_balanced_link], tagged_values = {'Circuit Breaker': 'Hystrix', 'Load Balancer': 'Spring Cloud'})
add_links({api_gateway: visits_service}, stereotype_instances = [circuit_breaker_link, restful_http, load_balanced_link], tagged_values = {'Circuit Breaker': 'Hystrix', 'Load Balancer': 'Spring Cloud'})
add_links({api_gateway: vets_service}, stereotype_instances = [circuit_breaker_link, restful_http, load_balanced_link], tagged_values = {'Circuit Breaker': 'Hystrix', 'Load Balancer': 'Spring Cloud'})
add_links({api_gateway: customers_service}, stereotype_instances = [circuit_breaker_link, restful_http, load_balanced_link], tagged_values = {'Circuit Breaker': 'Hystrix', 'Load Balancer': 'Spring Cloud'})
add_links({api_gateway: prometheus_server}, stereotype_instances = [circuit_breaker_link, restful_http, load_balanced_link], tagged_values = {'Circuit Breaker': 'Hystrix', 'Load Balancer': 'Spring Cloud'})
add_links({customers_service: prometheus_server}, stereotype_instances = [restful_http])
add_links({visits_service: prometheus_server}, stereotype_instances = [restful_http])
add_links({vets_service: prometheus_server}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = prometheus_server.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()