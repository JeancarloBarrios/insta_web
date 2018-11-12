import graphene
from graphene_django import DjangoObjectType

from . import models


class PostType(DjangoObjectType):
    class Meta:
        model = models.Post


class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag


class Query(graphene.ObjectType):
    tags = graphene.List(TagType)
    posts = graphene.List(PostType)
    # tags_from_post = graphene.List(TagType, graphene.Int)

    def resolve_tags(self, info, **kwargs):
        return models.Tag.objects.all()

    def resolve_posts(self, info, **kwargs):
        return models.Post.objects.all()

    # def resolve_tags_from_post(self, info, **kwargs):
    #     return models.Tag.objects.filter(tagpost__post=post_id)


class CreateTag(graphene.Mutation):
    id = graphene.Int()
    tag = graphene.String()

    class Arguments:
        tag = graphene.String()

    def mutate(self, info, tag):
        tag = models.Tag(tag=tag)
        tag.save()

        return CreateTag(
            id=tag.id,
            tag=tag.tag
        )


class CreatePost(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()

    class Arguments:
        title = graphene.String()

    def mutate(self, info, title):
        post = models.Post(title=title)
        post.save()

        return CreatePost(
            id=post.pk,
            tittle=post.title
        )


class Mutation(graphene.ObjectType):
    create_tag = CreateTag.Field()
    create_post = CreatePost.Field()
