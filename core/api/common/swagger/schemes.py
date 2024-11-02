from collections import defaultdict
from drf_yasg.generators import OpenAPISchemaGenerator


class APISchemeGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self):
        return {
            'Bearer': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization',
                'description': 'JWT Token in the format "Bearer <token>"',
            }
        }

    def get_schema(self, request=None, public=True):
        schema = super().get_schema(request, public)

        # Add tags in the desired order for Swagger Schema
        model_tags = [
        ]

        # Add tags for other models (Default Alphabetic Sorting)
        other_tags = [
        ]

        desired_order = [*model_tags, *sorted(other_tags)]

        operations_by_tags = defaultdict(list)
        other_operations = []

        for path, path_item in schema.paths.items():
            for method, operation in path_item.operations:
                operation_handled = False
                for tag in operation.tags:
                    if tag in desired_order:
                        operations_by_tags[tag].append((path, method, operation))
                        operation_handled = True
                        break
                if not operation_handled:
                    other_operations.append((path, method, operation))

        new_paths = {}

        for tag in desired_order:
            if tag in operations_by_tags:
                for path, method, operation in operations_by_tags[tag]:
                    if path not in new_paths:
                        new_paths[path] = schema.paths[path]

                    new_paths[path].operations = [
                        (method, operation)
                        for method, operation in new_paths[path].operations
                        if (method, operation) not in operations_by_tags[tag]
                    ] + [(method, operation)]

        for path, method, operation in other_operations:
            if path not in new_paths:
                new_paths[path] = schema.paths[path]
            new_paths[path].operations.append((method, operation))

        schema.paths = new_paths

        return schema
