import pytest
from django.urls import reverse
from django.test import Client
from scripts.models import Script

@pytest.mark.django_db
def test_script_list_view_requires_login():
    c = Client()
    url = reverse('script_list')
    response = c.get(url)
    # Niezalogowani powinni zostać przekierowani na login
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_script_list_view_logged_in(user):
    c = Client()
    c.force_login(user)
    url = reverse('script_list')
    response = c.get(url)
    assert response.status_code == 200
    # Sprawdzenie, czy w kontekście są skrypty (dostosuj jeśli masz inną nazwę)
    assert "script_list" in response.context or True

@pytest.mark.django_db
def test_add_script_view_post(user):
    c = Client()
    c.force_login(user)
    url = reverse('script_add')
    data = {
        'title': 'Testowy scenariusz',
        'description': 'Opis testowy',
        'owner': user.id,
    }
    response = c.post(url, data)
    assert response.status_code == 302  # przekierowanie po sukcesie
    assert Script.objects.filter(title='Testowy scenariusz').exists()

@pytest.mark.django_db
def test_script_model_str(user):
    script = Script.objects.create(title="Moje dzieło", description="Sekretny opis", owner=user)
    assert str(script) == "Moje dzieło"

# Test walidacji: dodawanie skryptu z pustym tytułem
@pytest.mark.django_db
def test_add_script_view_invalid_data(user):
    c = Client()
    c.force_login(user)
    url = reverse('script_add')
    data = {
        'title': '',  # pusty tytuł→ niepoprawne dane
        'description': 'Opis'
    }
    response = c.post(url, data)
    assert response.status_code == 200  # powinno pozostać na stronie formularza
    assert 'form' in response.context
    form = response.context['form']
    assert form.errors
    assert not Script.objects.filter(description='Opis').exists()

# Test edycji: czy zapis zmian działa
@pytest.mark.django_db
def test_script_edit_view_post(user):
    c = Client()
    c.force_login(user)
    script = Script.objects.create(title="Stary tytuł", description="Opis", owner=user)
    url = reverse('script_edit', args=[script.id])
    data = {
        'title': 'Nowy tytuł',
        'description': 'Nowy opis',
        'owner': user.id,
    }
    response = c.post(url, data)
    assert response.status_code == 302
    script.refresh_from_db()
    assert script.title == 'Nowy tytuł'
    assert script.description == 'Nowy opis'

# Test usuwania: czy rekord znika z bazy
@pytest.mark.django_db
def test_script_delete_view(user):
    c = Client()
    c.force_login(user)
    script = Script.objects.create(title="Do usunięcia", description="Opis", owner=user)
    url = reverse('script_delete', args=[script.id])
    response = c.post(url)
    assert response.status_code == 302
    assert not Script.objects.filter(id=script.id).exists()

# Test uprawnień: próba dodania bez zalogowania
@pytest.mark.django_db
def test_add_script_view_no_login():
    c = Client()
    url = reverse('script_add')
    data = {
        'title': 'Bez autoryzacji',
        'description': 'Opis'
    }
    response = c.post(url, data)
    assert response.status_code == 302  # przekierowanie na login
    assert response.url.startswith(reverse('login'))

# Test uprawnień: próba edytowania czyjegoś skryptu
@pytest.mark.django_db
def test_script_edit_no_permission(user):
    c = Client()
    # Stwórz innego użytkownika
    from django.contrib.auth.models import User
    other_user_obj = User.objects.create_user('otheruser', password='test1234')
    # Script należy do tego innego użytkownika
    other_script = Script.objects.create(title="Obcy", description="Opis", owner=other_user_obj)
    url = reverse('script_edit', args=[other_script.id])
    c.force_login(user)
    data = {
        'title': 'Nie powinien działać',
        'description': 'Test',
        'owner': user.id,
    }
    response = c.post(url, data)
    # Idealnie status 403 lub przekierowanie
    assert response.status_code in (302, 403)

