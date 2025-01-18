import Модуль10.module_10_4 as obj

def  introspection_info(object_for_introspect) -> None:
	attribute_list = dir(object_for_introspect)
	#[print(element) for element in attribute_list]
	print(attribute_list)

introspection_info(obj.Cafe)
