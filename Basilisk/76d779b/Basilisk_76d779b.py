from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "Basilisk_76d779b"
benchmark_service = CClass(service, "benchmark-service", stereotype_instances = [local_logging, internal], tagged_values = {'Logging Technology': 'Lombok', 'Endpoints': "['/benchmarkService', '/benchmarkService//stop', '/benchmarkService//status', '/benchmarkService//joblist', '/benchmarkService//start']", 'Port': 8082})
commons = CClass(service, "commons", stereotype_instances = [internal])
repository_service = CClass(service, "repository-service", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Logging Technology': 'Lombok', 'Endpoints': "['/pending', '/docker', '/repos/docker/{id}', '/repos/git', '/repos/git/{id}', '/continuousChecking//stop', '/repos/docker', '/continuousChecking', '/manualStart', '/git', '/abort/{id}', '/repos/git/release', '/repos/git/pullRequest', '/', '/continuousChecking//start', '/{id}', '/delete/{id}', '/repos/git/branch', '/continuousChecking//status']"})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [message_broker, plaintext_credentials, infrastructural], tagged_values = {'Port': 5672, 'Username': 'guest', 'Password': 'guest', 'Message Broker': 'RabbitMQ'})
database_benchmark_service = CClass(external_component, "database-benchmark-service", stereotype_instances = [entrypoint, external_database, plaintext_credentials, exitpoint], tagged_values = {'Username': 'basilisk', 'Password': 'password'})
database_repository_service = CClass(external_component, "database-repository-service", stereotype_instances = [entrypoint, external_database, plaintext_credentials, exitpoint], tagged_values = {'Username': 'basilisk', 'Password': 'password'})
add_links({rabbitmq: repository_service}, stereotype_instances = [message_consumer_rabbitmq, restful_http], tagged_values = {'Queue': '${rabbitmq.benchmarks.resultQueue}'})
add_links({rabbitmq: benchmark_service}, stereotype_instances = [message_consumer_rabbitmq, restful_http], tagged_values = {'Queue': '${rabbitmq.benchmarks.jobQueue}'})
add_links({benchmark_service: rabbitmq}, stereotype_instances = [restful_http, message_producer_rabbitmq, plaintext_credentials_link], tagged_values = {'Routing Key': 'None', 'Producer Exchange': 'None'})
add_links({repository_service: rabbitmq}, stereotype_instances = [restful_http, message_producer_rabbitmq, plaintext_credentials_link], tagged_values = {'Routing Key': 'None', 'Producer Exchange': 'None'})
add_links({database_benchmark_service: benchmark_service}, stereotype_instances = [jdbc, plaintext_credentials_link], tagged_values = {'Username': 'basilisk', 'Password': 'password'})
add_links({database_repository_service: repository_service}, stereotype_instances = [jdbc, plaintext_credentials_link], tagged_values = {'Username': 'basilisk', 'Password': 'password'})
model = CBundle(model_name, elements = rabbitmq.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()