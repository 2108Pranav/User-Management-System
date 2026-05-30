from views import CreateAndRetrievesUserResource

def all_route(api):
    api.add_resource(CreateAndRetrievesUserResource, "/user/create")