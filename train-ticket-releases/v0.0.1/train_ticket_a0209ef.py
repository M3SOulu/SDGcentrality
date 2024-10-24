from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "train-ticket_a0209ef"
ts_contacts_service = CClass(service, "ts-contacts-service", stereotype_instances = [internal], tagged_values = {'Port': 12347, 'Endpoints': "['/contacts/deleteContacts', '/contacts/update', '/contacts/findAll', '/welcome', '/contacts/admincreate', '/contacts/create', '/contacts/delete', '/contacts/getContactsById', '/contacts/modifyContacts', '/contacts/findContacts']"})
ts_admin_user_service = CClass(service, "ts-admin-user-service", stereotype_instances = [internal], tagged_values = {'Port': 16115, 'Endpoints': "['/adminuser/deleteUser', '/adminuser/findAll/{id}', '/adminuser/updateUser', '/adminuser/addUser', '/welcome']"})
ts_food_map_service = CClass(service, "ts-food-map-service", stereotype_instances = [internal], tagged_values = {'Port': 18855, 'Endpoints': "['/foodmap/getFoodStoresOfStation', '/welcome', '/foodmap/getAllFoodStores', '/foodmap/getAllTrainFood', '/foodmap/getTrainFoodOfTrip']"})
ts_notification_service = CClass(service, "ts-notification-service", stereotype_instances = [internal], tagged_values = {'Port': 17853, 'Endpoints': "['/notification/order_cancel_success', '/notification/order_changed_success', '/notification/order_create_success', '/notification/preserve_success', '/welcome']"})
ts_login_service = CClass(service, "ts-login-service", stereotype_instances = [internal], tagged_values = {'Port': 12342, 'Endpoints': "['/welcome', '/login', '/logout']"})
ts_cancel_service = CClass(service, "ts-cancel-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/cancelCalculateRefund', '/welcome', '/cancelOrder']", 'Port': 18885})
ts_config_service = CClass(service, "ts-config-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/config/create', '/config/update', '/config/retrieve', '/config/query', '/config/delete', '/welcome', '/config/queryAll']", 'Port': 15679})
ts_assurance_service = CClass(service, "ts-assurance-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/assurance/getAssuranceById', '/assurance/create', '/assurance/findAll', '/assurance/deleteAssuranceByOrderId', '/assurance/modifyAssurance', '/assurance/getAllAssuranceType', '/assurance/deleteAssurance', '/assurance/findAssuranceByOrderId', '/welcome']", 'Port': 18888})
ts_order_other_service = CClass(service, "ts-order-other-service", stereotype_instances = [internal], tagged_values = {'Port': 12032, 'Endpoints': "['/orderOther/payOrder', '/orderOther/findAll', '/orderOther/getById', '/orderOther/price', '/getOrderOtherInfoForSecurity', '/orderOther/getTicketListByDateAndTripId', '/orderOther/calculate', '/orderOther/create', '/welcome', '/orderOther/query', '/orderOther/queryForRefresh', '/orderOther/adminUpdate', '/orderOther/delete', '/orderOther/update', '/orderOther/adminAddOrder', '/orderOther/modifyOrderStatus']"})
ts_route_service = CClass(service, "ts-route-service", stereotype_instances = [internal], tagged_values = {'Port': 11178, 'Endpoints': "['/route/queryAll', '/route/createAndModify', '/route/queryById/{routeId}', '/route/delete', '/route/queryByStartAndTerminal', '/welcome']"})
ts_price_service = CClass(service, "ts-price-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/price/update', '/price/create', '/price/delete', '/price/queryAll', '/welcome', '/price/query']", 'Port': 16579})
ts_preserve_service = CClass(service, "ts-preserve-service", stereotype_instances = [internal], tagged_values = {'Port': 14568, 'Endpoints': "['/preserve', '/welcome']"})
micro_service_monitoring_core = CClass(service, "micro-service-monitoring-core", stereotype_instances = [internal, local_logging])
ts_security_service = CClass(service, "ts-security-service", stereotype_instances = [internal], tagged_values = {'Port': 11188, 'Endpoints': "['/securityConfig/findAll', '/security/check', '/securityConfig/create', '/welcome', '/securityConfig/delete', '/securityConfig/update']"})
ts_consign_service = CClass(service, "ts-consign-service", stereotype_instances = [internal], tagged_values = {'Port': 16111, 'Endpoints': "['/consign/insertConsign', '/consign/findByAccountId/{id}', '/consign/updateConsign', '/welcome', '/consign/findByConsignee']"})
ts_train_service = CClass(service, "ts-train-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/train/delete', '/train/retrieve', '/train/update', '/train/create', '/welcome', '/train/query']", 'Port': 14567})
ts_order_service = CClass(service, "ts-order-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/order/adminUpdate', '/order/update', '/order/delete', '/order/findAll', '/order/price', '/order/create', '/order/payOrder', '/order/adminAddOrder', '/order/modifyOrderStatus', '/getOrderInfoForSecurity', '/order/calculate', '/order/getById', '/order/queryForRefresh', '/order/getTicketListByDateAndTripId', '/welcome', '/order/query']", 'Port': 12031})
ts_verification_code_service = CClass(service, "ts-verification-code-service", stereotype_instances = [internal], tagged_values = {'Port': 15678, 'Endpoints': "['/verification/generate', '/verification/verify', '/error']"})
ts_food_service = CClass(service, "ts-food-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/food/findFoodOrderByOrderId', '/food/createFoodOrder', '/food/updateFoodOrder', '/food/cancelFoodOrder', '/welcome', '/food/findAllFoodOrder', '/food/getFood']", 'Port': 18856})
ts_rebook_service = CClass(service, "ts-rebook-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/welcome', '/rebook/payDifference', '/rebook/rebook']", 'Port': 18886})
rest_service_5 = CClass(service, "rest-service-5", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/hello5', '/monitor']", 'Port': 16005})
rest_service_2 = CClass(service, "rest-service-2", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/hello2', '/hello']", 'Port': 16002})
rest_service_collector = CClass(service, "rest-service-collector", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 16001, 'Endpoints': "['/api/v1/spans', '/api/**', '/**']"})
rest_service_3 = CClass(service, "rest-service-3", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 16003, 'Endpoints': "['/hello3', '/hello']"})
rest_service_4 = CClass(service, "rest-service-4", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 16004, 'Endpoints': "['/getdata', '/hello4', '/getdata1']"})
rest_service_1 = CClass(service, "rest-service-1", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/hello1', '/hello']", 'Port': 16001})
rest_service_6 = CClass(service, "rest-service-6", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/hello6', '/hello6_1']", 'Port': 16006})
rest_service_end = CClass(service, "rest-service-end", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/greeting', '/test']", 'Port': 16000})
ts_ui_test = CClass(service, "ts-ui-test", stereotype_instances = [internal])
ts_register_service = CClass(service, "ts-register-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/welcome', '/register']", 'Port': 12344})
spring_transaction_consumer = CClass(service, "spring-transaction-consumer", stereotype_instances = [internal])
ts_admin_basic_info_service = CClass(service, "ts-admin-basic-info-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/adminbasic/getAllContacts/{id}', '/adminbasic/modifyContacts', '/adminbasic/deleteConfig', '/adminbasic/getAllPrices/{id}', '/adminbasic/deletePrice', '/adminbasic/modifyConfig', '/welcome', '/adminbasic/addStation', '/adminbasic/getAllTrains/{id}', '/adminbasic/addConfig', '/adminbasic/deleteTrain', '/adminbasic/modifyStation', '/adminbasic/deleteStation', '/adminbasic/getAllStations/{id}', '/adminbasic/addPrice', '/adminbasic/deleteContacts', '/adminbasic/addTrain', '/adminbasic/modifyPrice', '/adminbasic/addContacts', '/adminbasic/modifyTrain', '/adminbasic/getAllConfigs/{id}']", 'Port': 18767})
ts_consign_price_service = CClass(service, "ts-consign-price-service", stereotype_instances = [internal], tagged_values = {'Port': 16110, 'Endpoints': "['/consignPrice/getPriceInfo', '/consignPrice/getPriceConfig', '/consignPrice/modifyPriceConfig', '/welcome', '/consignPrice/getPrice']"})
ts_basic_service = CClass(service, "ts-basic-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/welcome', '/basic/queryForStationId', '/basic/queryForTravel']", 'Port': 15680})
ts_preserve_other_service = CClass(service, "ts-preserve-other-service", stereotype_instances = [internal], tagged_values = {'Port': 14569, 'Endpoints': "['/welcome', '/preserveOther']"})
ts_station_service = CClass(service, "ts-station-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/station/queryForIdBatch', '/station/queryForId', '/station/create', '/station/queryById', '/station/delete', '/station/queryByIdBatch', '/station/query', '/station/update', '/welcome', '/station/queryByIdForName', '/station/exist']", 'Port': 12345})
ts_route_plan_service = CClass(service, "ts-route-plan-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/routePlan/minStopStations', '/welcome', '/routePlan/quickestRoute', '/routePlan/cheapestRoute']", 'Port': 14578})
ts_ticketinfo_service = CClass(service, "ts-ticketinfo-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/welcome', '/ticketinfo/queryForStationId', '/ticketinfo/queryForTravel']", 'Port': 15681})
spring_transaction_producer = CClass(service, "spring-transaction-producer", stereotype_instances = [internal])
ts_payment_service = CClass(service, "ts-payment-service", stereotype_instances = [internal], tagged_values = {'Port': 19001, 'Endpoints': "['/payment/query', '/welcome', '/payment/pay', '/payment/addMoney']"})
ts_inside_payment_service = CClass(service, "ts-inside-payment-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/inside_payment/queryAddMoney', '/inside_payment/createAccount', '/inside_payment/queryPayment', '/inside_payment/pay', '/inside_payment/drawBack', '/hello1_callback', '/inside_payment/addMoney', '/inside_payment/queryAccount', '/welcome', '/inside_payment/payDifference']", 'Port': 18673})
rest_travel.service_update = CClass(service, "rest-travel.service-update", stereotype_instances = [internal], tagged_values = {'Port': 15100, 'Endpoints': "['/greeting']"})
sample_test_1 = CClass(service, "sample-test-1", stereotype_instances = [internal])
ts_seat_service = CClass(service, "ts-seat-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/welcome', '/seat/getSeat', '/seat/getLeftTicketOfInterval']", 'Port': 18898})
ts_execute_service = CClass(service, "ts-execute-service", stereotype_instances = [internal], tagged_values = {'Port': 12386, 'Endpoints': "['/execute/collected', '/welcome', '/execute/execute']"})
ts_travel_plan_service = CClass(service, "ts-travel-plan-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/travelPlan/getCheapest', '/travelPlan/getMinStation', '/travelPlan/getQuickest', '/travelPlan/getTransferResult', '/welcome']", 'Port': 14322})
ts_travel2_service = CClass(service, "ts-travel2-service", stereotype_instances = [internal], tagged_values = {'Port': 16346, 'Endpoints': "['/travel2/getRouteByTripId/{tripId}', '/travel2/adminQueryAll', '/travel2/queryWithPackage', '/travel2/getTripAllDetailInfo', '/travel2/queryAll', '/travel2/delete', '/travel2/getTrainTypeByTripId/{tripId}', '/travel2/getTripsByRouteId', '/travel2/retrieve', '/travel2/create', '/welcome', '/travel2/update', '/travel2/query']"})
ts_travel_service = CClass(service, "ts-travel-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/travel/getTrainTypeByTripId/{tripId}', '/travel/getTripAllDetailInfo', '/travel/queryWithPackage', '/travel/create', '/travel/retrieve', '/travel/queryAll', '/travel/adminQueryAll', '/travel/getRouteByTripId/{tripId}', '/travel/query', '/travel/getTripsByRouteId', '/travel/update', '/welcome', '/travel/delete']", 'Port': 12346})
ts_admin_order_service = CClass(service, "ts-admin-order-service", stereotype_instances = [internal], tagged_values = {'Port': 16112, 'Endpoints': "['/adminorder/addOrder', '/adminorder/updateOrder', '/adminorder/findAll/{id}', '/welcome', '/adminorder/deleteOrder']"})
ts_admin_travel_service = CClass(service, "ts-admin-travel-service", stereotype_instances = [internal], tagged_values = {'Port': 16114, 'Endpoints': "['/admintravel/addTravel', '/admintravel/findAll/{id}', '/admintravel/deleteTravel', '/admintravel/updateTravel', '/welcome']"})
ts_sso_service = CClass(service, "ts-sso-service", stereotype_instances = [internal], tagged_values = {'Port': 12349, 'Endpoints': "['/account/findAll', '/account/register', '/account/modify', '/account/findAllLogin', '/verifyLoginToken/{token}', '/account/findById', '/account/login', '/account/adminlogin', '/account/admindelete', '/welcome', '/logout']"})
ts_admin_route_service = CClass(service, "ts-admin-route-service", stereotype_instances = [internal], tagged_values = {'Port': 16113, 'Endpoints': "['/adminroute/findAll/{id}', '/welcome', '/adminroute/createAndModifyRoute', '/adminroute/deleteRoute']"})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [message_broker, infrastructural], tagged_values = {'Message Broker': 'RabbitMQ', 'Port': 5672})
zipkin = CClass(service, "zipkin", stereotype_instances = [tracing_server, infrastructural], tagged_values = {'Port': 9411, 'Tracing Server': 'Zipkin'})
mongodb = CClass(service, "mongodb", stereotype_instances = [internal], tagged_values = {'Port': 27017})
kafka = CClass(service, "kafka", stereotype_instances = [message_broker, infrastructural, tracing_server], tagged_values = {'Tracing Server': 'Zipkin', 'Message Broker': 'Kafka', 'Port': 2181})
mail_server = CClass(external_component, "mail-server", stereotype_instances = [entrypoint, mail_server, plaintext_credentials, exitpoint], tagged_values = {'Password': 'fdse1234', 'Username': 'fdse_microservices@163.com', 'Host': 'smtp.163.com'})
add_links({rabbitmq: spring_transaction_consumer}, stereotype_instances = [message_consumer_rabbitmq, restful_http], tagged_values = {'Queue': 'async'})
add_links({kafka: rest_service_collector}, stereotype_instances = [message_consumer_kafka, restful_http], tagged_values = {'Consumer Topic': 'None'})
add_links({rest_service_collector: kafka}, stereotype_instances = [message_producer_kafka, restful_http], tagged_values = {'Producer Topic': 'app_log'})
add_links({ts_contacts_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_admin_user_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_login_service: ts_verification_code_service}, stereotype_instances = [restful_http])
add_links({ts_login_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_cancel_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_cancel_service: ts_notification_service}, stereotype_instances = [restful_http])
add_links({ts_cancel_service: ts_order_other_service}, stereotype_instances = [restful_http])
add_links({ts_cancel_service: ts_inside_payment_service}, stereotype_instances = [restful_http])
add_links({ts_cancel_service: ts_order_service}, stereotype_instances = [restful_http])
add_links({ts_assurance_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_order_other_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_order_other_service: ts_station_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_ticketinfo_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_seat_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_notification_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_assurance_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_station_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_security_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_travel_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_contacts_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_order_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_food_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_service: ts_consign_service}, stereotype_instances = [restful_http])
add_links({ts_security_service: ts_order_service}, stereotype_instances = [restful_http])
add_links({ts_security_service: ts_order_other_service}, stereotype_instances = [restful_http])
add_links({ts_consign_service: ts_consign_price_service}, stereotype_instances = [restful_http])
add_links({ts_order_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_order_service: ts_station_service}, stereotype_instances = [restful_http])
add_links({ts_food_service: ts_food_map_service}, stereotype_instances = [restful_http])
add_links({ts_food_service: ts_travel_service}, stereotype_instances = [restful_http])
add_links({ts_food_service: ts_station_service}, stereotype_instances = [restful_http])
add_links({ts_rebook_service: ts_seat_service}, stereotype_instances = [restful_http])
add_links({ts_rebook_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_rebook_service: ts_travel_service}, stereotype_instances = [restful_http])
add_links({ts_rebook_service: ts_travel2_service}, stereotype_instances = [restful_http])
add_links({ts_rebook_service: ts_order_service}, stereotype_instances = [restful_http])
add_links({ts_rebook_service: ts_order_other_service}, stereotype_instances = [restful_http])
add_links({ts_rebook_service: ts_station_service}, stereotype_instances = [restful_http])
add_links({ts_rebook_service: ts_inside_payment_service}, stereotype_instances = [restful_http])
add_links({ts_register_service: ts_verification_code_service}, stereotype_instances = [restful_http])
add_links({ts_register_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_register_service: ts_inside_payment_service}, stereotype_instances = [restful_http])
add_links({ts_admin_basic_info_service: ts_contacts_service}, stereotype_instances = [restful_http])
add_links({ts_admin_basic_info_service: ts_station_service}, stereotype_instances = [restful_http])
add_links({ts_admin_basic_info_service: ts_train_service}, stereotype_instances = [restful_http])
add_links({ts_admin_basic_info_service: ts_config_service}, stereotype_instances = [restful_http])
add_links({ts_admin_basic_info_service: ts_price_service}, stereotype_instances = [restful_http])
add_links({ts_basic_service: ts_station_service}, stereotype_instances = [restful_http])
add_links({ts_basic_service: ts_train_service}, stereotype_instances = [restful_http])
add_links({ts_basic_service: ts_route_service}, stereotype_instances = [restful_http])
add_links({ts_basic_service: ts_price_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_ticketinfo_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_seat_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_notification_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_sso_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_assurance_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_station_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_security_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_travel2_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_contacts_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_order_other_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_food_service}, stereotype_instances = [restful_http])
add_links({ts_preserve_other_service: ts_consign_service}, stereotype_instances = [restful_http])
add_links({ts_route_plan_service: ts_route_service}, stereotype_instances = [restful_http])
add_links({ts_route_plan_service: ts_travel_service}, stereotype_instances = [restful_http])
add_links({ts_route_plan_service: ts_travel2_service}, stereotype_instances = [restful_http])
add_links({ts_route_plan_service: ts_station_service}, stereotype_instances = [restful_http])
add_links({ts_ticketinfo_service: ts_basic_service}, stereotype_instances = [restful_http])
add_links({ts_ticketinfo_service: ts_price_service}, stereotype_instances = [restful_http])
add_links({ts_inside_payment_service: ts_order_service}, stereotype_instances = [restful_http])
add_links({ts_inside_payment_service: ts_order_other_service}, stereotype_instances = [restful_http])
add_links({ts_inside_payment_service: ts_payment_service}, stereotype_instances = [restful_http])
add_links({ts_seat_service: ts_travel_service}, stereotype_instances = [restful_http])
add_links({ts_seat_service: ts_order_service}, stereotype_instances = [restful_http])
add_links({ts_seat_service: ts_travel2_service}, stereotype_instances = [restful_http])
add_links({ts_seat_service: ts_order_other_service}, stereotype_instances = [restful_http])
add_links({ts_seat_service: ts_config_service}, stereotype_instances = [restful_http])
add_links({ts_execute_service: ts_order_service}, stereotype_instances = [restful_http])
add_links({ts_execute_service: ts_order_other_service}, stereotype_instances = [restful_http])
add_links({ts_travel_plan_service: ts_seat_service}, stereotype_instances = [restful_http])
add_links({ts_travel_plan_service: ts_route_plan_service}, stereotype_instances = [restful_http])
add_links({ts_travel_plan_service: ts_travel_service}, stereotype_instances = [restful_http])
add_links({ts_travel_plan_service: ts_travel2_service}, stereotype_instances = [restful_http])
add_links({ts_travel_plan_service: ts_ticketinfo_service}, stereotype_instances = [restful_http])
add_links({ts_travel_plan_service: ts_station_service}, stereotype_instances = [restful_http])
add_links({ts_travel2_service: ts_ticketinfo_service}, stereotype_instances = [restful_http])
add_links({ts_travel2_service: ts_order_other_service}, stereotype_instances = [restful_http])
add_links({ts_travel2_service: ts_train_service}, stereotype_instances = [restful_http])
add_links({ts_travel2_service: ts_route_service}, stereotype_instances = [restful_http])
add_links({ts_travel2_service: ts_seat_service}, stereotype_instances = [restful_http])
add_links({ts_travel_service: ts_ticketinfo_service}, stereotype_instances = [restful_http])
add_links({ts_travel_service: ts_order_service}, stereotype_instances = [restful_http])
add_links({ts_travel_service: ts_train_service}, stereotype_instances = [restful_http])
add_links({ts_travel_service: ts_route_service}, stereotype_instances = [restful_http])
add_links({ts_travel_service: ts_seat_service}, stereotype_instances = [restful_http])
add_links({ts_admin_order_service: ts_order_service}, stereotype_instances = [restful_http])
add_links({ts_admin_order_service: ts_order_other_service}, stereotype_instances = [restful_http])
add_links({ts_admin_travel_service: ts_travel_service}, stereotype_instances = [restful_http])
add_links({ts_admin_travel_service: ts_travel2_service}, stereotype_instances = [restful_http])
add_links({ts_admin_route_service: ts_route_service}, stereotype_instances = [restful_http])
add_links({rest_service_5: rest_service_4}, stereotype_instances = [restful_http])
add_links({rest_service_2: rest_service_1}, stereotype_instances = [restful_http])
add_links({rest_service_3: rest_service_2}, stereotype_instances = [restful_http])
add_links({rest_service_3: rest_service_1}, stereotype_instances = [restful_http])
add_links({rest_service_3: rest_service_end}, stereotype_instances = [restful_http])
add_links({rest_service_3: rest_service_6}, stereotype_instances = [restful_http])
add_links({rest_service_4: rest_service_3}, stereotype_instances = [restful_http])
add_links({rest_service_6: rest_service_5}, stereotype_instances = [restful_http])
add_links({rest_service_6: rest_service_4}, stereotype_instances = [restful_http])
add_links({rest_service_6: rest_service_3}, stereotype_instances = [restful_http])
add_links({rest_service_1: rest_service_2}, stereotype_instances = [restful_http])
add_links({rest_service_5: rest_service_collector}, stereotype_instances = [restful_http])
add_links({rest_service_2: zipkin}, stereotype_instances = [restful_http])
add_links({rest_service_3: zipkin}, stereotype_instances = [restful_http])
add_links({rest_service_4: rest_service_collector}, stereotype_instances = [restful_http])
add_links({rest_service_1: zipkin}, stereotype_instances = [restful_http])
add_links({rest_service_6: rest_service_collector}, stereotype_instances = [restful_http])
add_links({rest_service_end: zipkin}, stereotype_instances = [restful_http])
add_links({ts_notification_service: mail_server}, stereotype_instances = [plaintext_credentials_link, restful_http])
model = CBundle(model_name, elements = kafka.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()