import pytest
from users.models import User


@pytest.mark.django_db
# @pytest.mark.run
def test_create_user():
    """
    Ensure we can create a new user.
    """
    user = User.objects.create_user(email="example@mail.com", password="S_t_r_o_n_g")
    assert user.email == "example@mail.com"


@pytest.mark.django_db
# @pytest.mark.run
def test_create_user_is_admin_false():
    """
    Ensure created user isn't admin.
    """
    user = User.objects.create_user(email="example@mail.com", password="S_t_r_o_n_g")
    assert user.is_admin == False


@pytest.mark.django_db
# @pytest.mark.run
def test_create_user_is_staff_false():
    """
    Ensure created user isn't staff.
    """
    user = User.objects.create_user(email="example@mail.com", password="S_t_r_o_n_g")
    assert user.is_staff == False


@pytest.mark.django_db
# @pytest.mark.run
@pytest.mark.xfail(raises=ValueError)
def test_create_user_fail():
    """
    Ensure we can't create user without email.
    """
    User.objects.create_user(email=None, password="S_t_r_o_n_g")


@pytest.mark.django_db
@pytest.mark.run
def test_create_superuser():
    """
    Ensure we can create superuser.
    """
    user = User.objects.create_superuser(email="example@mail.com", password="S_t_r_o_n_g")
    assert user.email == "example@mail.com"


@pytest.mark.django_db
@pytest.mark.run
@pytest.mark.xfail(raises=ValueError)
def test_create_superuser_fail():
    """
    Ensure we can't create superuser without email.
    """
    user = User.objects.create_superuser(email=None, password="S_t_r_o_n_g")


@pytest.mark.django_db
@pytest.mark.run
def test_create_superuser_is_admin_true():
    """
    Ensure created superuser is admin.
    """
    user = User.objects.create_superuser(email="example@mail.com", password="S_t_r_o_n_g")
    assert user.is_admin == True


@pytest.mark.django_db
@pytest.mark.run
def test_create_superuser_is_staff_true():
    """
    Ensure created superuser is staff.
    """
    user = User.objects.create_superuser(email="example@mail.com", password="S_t_r_o_n_g")
    assert user.is_staff == True
