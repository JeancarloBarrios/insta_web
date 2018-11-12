import graphene
import graphql_jwt

from post import schema as post_schema
from users import schema as user_schema


class Query(
    post_schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    post_schema.Mutation,
    user_schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)