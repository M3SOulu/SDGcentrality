from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_1681bdb"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/recommendation', '/set-processing-time']"})
product_service = CClass(service, "product-service", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/set-processing-time', '/product/{productId}']"})
review_service = CClass(service, "review-service", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/review', '/set-processing-time']"})
composite_service = CClass(service, "composite-service", stereotype_instances = [local_logging, internal, load_balancer, resource_server, circuit_breaker], tagged_values = {'Endpoints': "['/{productId}', '/']", 'Load Balancer': 'Spring Cloud'})
monitor_dashboard = CClass(service, "monitor-dashboard", stereotype_instances = [monitoring_dashboard, local_logging, infrastructural], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Endpoints': "['/']"})
auth_server = CClass(service, "auth-server", stereotype_instances = [infrastructural, authorization_server, resource_server, local_logging], tagged_values = {'Authorization Server': 'Spring OAuth2', 'Endpoints': "['/user']"})
config_server = CClass(service, "config-server", stereotype_instances = [infrastructural, local_logging, configuration_server], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
turbine_server = CClass(service, "turbine-server", stereotype_instances = [infrastructural, local_logging, monitoring_server], tagged_values = {'Monitoring Server': 'Turbine', 'Port': 8989})
zipkin_server = CClass(service, "zipkin-server", stereotype_instances = [internal], tagged_values = {'Port': 9411})
edge_server = CClass(service, "edge-server", stereotype_instances = [infrastructural, local_logging, gateway, load_balancer, resource_server], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
discovery_server = CClass(service, "discovery-server", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Port': 8762, 'Service Discovery': 'Eureka'})
elasticsearch = CClass(service, "elasticsearch", stereotype_instances = [infrastructural, search_engine], tagged_values = {'Search Engine': 'Elasticsearch', 'Port': 9200})
kibana = CClass(service, "kibana", stereotype_instances = [monitoring_dashboard, infrastructural], tagged_values = {'Monitoring Dashboard': 'Kibana', 'Port': 5601})
zipkin = CClass(service, "zipkin", stereotype_instances = [internal], tagged_values = {'Port': 9411})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [infrastructural, message_broker], tagged_values = {'Port': 15672, 'Message Broker': 'RabbitMQ'})
logstash = CClass(service, "logstash", stereotype_instances = [logging_server, infrastructural], tagged_values = {'Port': 25826, 'Logging Server': 'Logstash'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, exitpoint, user_stereotype])
add_links({config_server: recommendation_service}, stereotype_instances = [restful_http])
add_links({config_server: product_service}, stereotype_instances = [restful_http])
add_links({config_server: review_service}, stereotype_instances = [restful_http])
add_links({config_server: composite_service}, stereotype_instances = [restful_http])
add_links({config_server: monitor_dashboard}, stereotype_instances = [restful_http])
add_links({config_server: auth_server}, stereotype_instances = [restful_http])
add_links({config_server: turbine_server}, stereotype_instances = [restful_http])
add_links({config_server: edge_server}, stereotype_instances = [restful_http])
add_links({product_service: discovery_server}, stereotype_instances = [restful_http])
add_links({composite_service: discovery_server}, stereotype_instances = [restful_http, circuit_breaker_link, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({turbine_server: discovery_server}, stereotype_instances = [restful_http])
add_links({config_server: discovery_server}, stereotype_instances = [restful_http])
add_links({recommendation_service: discovery_server}, stereotype_instances = [restful_http])
add_links({review_service: discovery_server}, stereotype_instances = [restful_http])
add_links({user: edge_server}, stereotype_instances = [restful_http])
add_links({edge_server: user}, stereotype_instances = [restful_http])
add_links({turbine_server: monitor_dashboard}, stereotype_instances = [restful_http])
add_links({elasticsearch: kibana}, stereotype_instances = [restful_http])
add_links({logstash: elasticsearch}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = logstash.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()