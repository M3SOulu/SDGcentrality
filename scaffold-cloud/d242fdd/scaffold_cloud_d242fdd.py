from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "scaffold-cloud_d242fdd"
scaffold_txmanager = CClass(service, "scaffold-txmanager", stereotype_instances = [internal])
scaffold_core_code = CClass(service, "scaffold-core-code", stereotype_instances = [internal, local_logging], tagged_values = {'Logging Technology': 'Lombok'})
scaffold_core_common = CClass(service, "scaffold-core-common", stereotype_instances = [internal, local_logging])
scaffold_core_plugin = CClass(service, "scaffold-core-plugin", stereotype_instances = [internal, local_logging], tagged_values = {'Logging Technology': 'Lombok'})
scaffold_business_thirdparty_service = CClass(service, "scaffold-business-thirdparty-service", stereotype_instances = [internal, local_logging], tagged_values = {'Logging Technology': 'Lombok'})
scaffold_business_job_service = CClass(service, "scaffold-business-job-service", stereotype_instances = [internal, local_logging])
scaffold_business_sys_service = CClass(service, "scaffold-business-sys-service", stereotype_instances = [internal, local_logging], tagged_values = {'Logging Technology': 'Lombok'})
scaffold_zuul = CClass(service, "scaffold-zuul", stereotype_instances = [gateway, infrastructural, load_balancer], tagged_values = {'Load Balancer': 'Ribbon', 'Gateway': 'Zuul'})
demo = CClass(service, "demo", stereotype_instances = [internal])
scaffold_config_server = CClass(service, "scaffold-config-server", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Configuration Server': 'Spring Cloud Config'})
scaffold_eureka = CClass(service, "scaffold-eureka", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Service Discovery': 'Eureka'})
scaffold_business_thirdparty_api = CClass(service, "scaffold-business-thirdparty-api", stereotype_instances = [internal])
scaffold_business_sys_api = CClass(service, "scaffold-business-sys-api", stereotype_instances = [internal])
scaffold_feign_sys = CClass(service, "scaffold-feign-sys", stereotype_instances = [internal])
scaffold_feign_thirdparty = CClass(service, "scaffold-feign-thirdparty", stereotype_instances = [internal])
scaffold_route_openapi = CClass(service, "scaffold-route-openapi", stereotype_instances = [internal, circuit_breaker], tagged_values = {'Circuit Breaker': 'Hystrix'})
scaffold_route_app = CClass(service, "scaffold-route-app", stereotype_instances = [internal])
scaffold_route_operate = CClass(service, "scaffold-route-operate", stereotype_instances = [internal, local_logging, circuit_breaker], tagged_values = {'Circuit Breaker': 'Hystrix', 'Logging Technology': 'Lombok'})
mysql = CClass(service, "mysql", stereotype_instances = [database], tagged_values = {'Database': 'MySQL', 'Port': 3306})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, exitpoint, user_stereotype])
add_links({scaffold_config_server: demo}, stereotype_instances = [restful_http])
add_links({scaffold_route_app: scaffold_eureka}, stereotype_instances = [restful_http])
add_links({scaffold_route_operate: scaffold_eureka}, stereotype_instances = [restful_http])
add_links({scaffold_route_openapi: scaffold_eureka}, stereotype_instances = [restful_http])
add_links({demo: scaffold_eureka}, stereotype_instances = [restful_http])
add_links({scaffold_eureka: scaffold_zuul}, stereotype_instances = [restful_http])
add_links({scaffold_business_thirdparty_service: scaffold_eureka}, stereotype_instances = [restful_http])
add_links({scaffold_business_job_service: scaffold_eureka}, stereotype_instances = [restful_http])
add_links({scaffold_txmanager: scaffold_eureka}, stereotype_instances = [restful_http])
add_links({scaffold_business_sys_service: scaffold_eureka}, stereotype_instances = [restful_http])
add_links({scaffold_config_server: scaffold_eureka}, stereotype_instances = [restful_http])
add_links({user: scaffold_zuul}, stereotype_instances = [restful_http])
add_links({scaffold_zuul: user}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = mysql.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()