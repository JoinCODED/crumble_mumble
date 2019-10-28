import graphene

from graphene_django.types import DjangoObjectType

from .models import Category, Ingredient, Recipe

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_recipes = graphene.List(RecipeType)
    recipe = graphene.Field(RecipeType, id=graphene.Int(), slug=graphene.String())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_recipes(self, info, **kwargs):
        return Recipe.objects.all()

    def resolve_recipe(self, info, **kwargs):
    	slug = kwargs.get('slug')
    	id = kwargs.get('id')

    	if id is not None:
    		return Recipe.objects.get(id=id)

    	if slug is not None:
    		return Recipe.objects.get(slug=slug)


    	return None