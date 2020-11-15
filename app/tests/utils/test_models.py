import pytest
from utils.models import AbstractTableMeta


@pytest.mark.django_db
@pytest.mark.skip(reason="docker should be fixed")
def test_create_dummy_object(dummy_model, create_valid_user):
    """
    Ensure we can create a new object.
    """
    dummy_obj = dummy_model.objects.create(
        created_by=create_valid_user, modified_by=create_valid_user
    )
    assert issubclass(dummy_model, AbstractTableMeta)
    assert isinstance(dummy_obj, AbstractTableMeta)
