from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "microservice-consul_08b0190"
customer = CClass(service, "customer", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/form.html', '/list.html', '/{id}.html']", 'Port': 8080})
order = CClass(service, "order", stereotype_instances = [local_logging, load_balancer, internal], tagged_values = {'Load Balancer': 'Ribbon', 'Endpoints': "['/form.html', '/{id}', '/', '/line']", 'Port': 8080})
catalog = CClass(service, "catalog", stereotype_instances = [internal], tagged_values = {'Endpoints': '[\'/"catalog\']', 'Port': 8080})
apache = CClass(service, "apache", stereotype_instances = [web_server, infrastructural], tagged_values = {'Web Server': 'Apache httpd', 'Port': 8080})
consul = CClass(service, "consul", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Service Discovery': 'Consul', 'Port': 8500})
prometheus_server = CClass(service, "prometheus_server", stereotype_instances = [metrics_server, infrastructural], tagged_values = {'Metrics Server': 'Prometheus'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({order: catalog}, stereotype_instances = [restful_http])
add_links({order: customer}, stereotype_instances = [restful_http])
add_links({apache: customer}, stereotype_instances = [restful_http])
add_links({apache: catalog}, stereotype_instances = [restful_http])
add_links({apache: order}, stereotype_instances = [restful_http])
add_links({order: order}, stereotype_instances = [restful_http])
add_links({customer: consul}, stereotype_instances = [restful_http])
add_links({catalog: consul}, stereotype_instances = [restful_http])
add_links({order: consul}, stereotype_instances = [restful_http])
add_links({apache: consul}, stereotype_instances = [restful_http])
add_links({user: apache}, stereotype_instances = [restful_http])
add_links({apache: user}, stereotype_instances = [restful_http])
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