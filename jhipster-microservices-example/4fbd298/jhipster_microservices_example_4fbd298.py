from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "jhipster-microservices-example_4fbd298"
blog = CClass(service, "blog", stereotype_instances = [local_logging, gateway, load_balancer, infrastructural, csrf_disabled], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon', 'Port': '8080 5701'})
jhipster_registry = CClass(service, "jhipster-registry", stereotype_instances = [local_logging, basic_authentication, gateway, service_discovery, load_balancer, infrastructural, csrf_disabled, configuration_server], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon', 'Port': 8761, 'Configuration Server': 'Spring Cloud Config', 'Service Discovery': 'Eureka'})
store = CClass(service, "store", stereotype_instances = [internal, local_logging, csrf_disabled], tagged_values = {'Port': 8081})
store_mongodb = CClass(service, "store-mongodb", stereotype_instances = [database], tagged_values = {'Database': 'MongoDB'})
blog_postgresql = CClass(service, "blog-postgresql", stereotype_instances = [internal])
blog_elasticsearch = CClass(service, "blog-elasticsearch", stereotype_instances = [search_engine, infrastructural], tagged_values = {'Search Engine': 'Elasticsearch'})
github_repository = CClass(external_component, "github-repository", stereotype_instances = [entrypoint, github_repository], tagged_values = {'URL': 'https://github.com/jhipster/jhipster-registry-sample-config'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({github_repository: jhipster_registry}, stereotype_instances = [restful_http])
add_links({jhipster_registry: blog}, stereotype_instances = [restful_http])
add_links({jhipster_registry: store}, stereotype_instances = [restful_http])
add_links({jhipster_registry: jhipster_registry}, stereotype_instances = [restful_http])
add_links({store: jhipster_registry}, stereotype_instances = [restful_http])
add_links({user: blog}, stereotype_instances = [restful_http])
add_links({blog: user}, stereotype_instances = [restful_http])
add_links({user: jhipster_registry}, stereotype_instances = [restful_http])
add_links({jhipster_registry: user}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = blog_elasticsearch.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()