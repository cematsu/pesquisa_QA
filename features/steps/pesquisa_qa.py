from behave import given, when, then

from features.steps.config import Config
from features.steps.page_objects.via import Via


@given('que eu acesse a página da VV Test')
def step_impl(context):
    context.web.get(Config.get_url())


@given('acesse o menu "Pesquisa - QA"')
def step_impl(context):
    context.link_pesquisa = context.web.find_element_by_id(Via.get_id_pesquisa_qa())
    context.link_pesquisa.click()


@when('eu preencher todos os campos obrigatórios')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu preencher todos os campos obrigatórios')


@then('deve ser direcionado para uma página de sucesso')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then deve ser direcionado para uma página de sucesso')

