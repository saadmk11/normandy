import pytest

from normandy.classifier.tests import BundleFactory
from normandy.classifier.serializers import BundleSerializer
from normandy.recipes.tests import RecipeFactory


@pytest.mark.django_db()
def test_bundle_serializer():
    recipe = RecipeFactory()
    bundle = BundleFactory(recipes=[recipe])
    serializer = BundleSerializer(bundle)

    assert serializer.data['recipes'] == [{'name': recipe.name, 'actions': []}]