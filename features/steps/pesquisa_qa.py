import time

from behave import given, when, then

from features.steps.config import Config
from selenium.webdriver.support.ui import Select

from features.steps.page_objects.confirmacao import Confirmacao
from features.steps.page_objects.pesquisa import Pesquisa
from features.steps.page_objects.via import Via


@given('que eu acesse a página da VV Test')
def step_impl(context):
    context.web.get(Config.get_url())


@given('acesse o menu "Pesquisa - QA"')
def step_impl(context):
    context.web.find_element_by_id(Via.get_id_pesquisa_qa()).click()


@when('eu preencher todos os campos obrigatórios')
def step_impl(context):
    context.web.find_element_by_id(Pesquisa.get_id_txt_nome()).send_keys("nome")
    context.web.find_element_by_id(Pesquisa.get_id_txt_sobrenome()).send_keys("sobrenome")
    context.web.find_element_by_id(Pesquisa.get_id_txt_email()).send_keys("nome@sobrenome.com")
    context.web.find_element_by_id(Pesquisa.get_id_txt_confirm_email()).send_keys("nome@sobrenome.com")
    context.web.find_element_by_id(Pesquisa.get_id_radio_idade()).click()
    context.select = Select(context.web.find_element_by_id(Pesquisa.get_id_select_experiencia()))
    context.select.select_by_visible_text("mais de 5 anos")
    context.select = Select(context.web.find_element_by_id(Pesquisa.get_id_select_atraiu_na_area()))
    context.select.select_by_visible_text("Salário")
    context.web.find_element_by_id(Pesquisa.get_id_radio_a_melhorar()).click()
    context.web.find_element_by_id(Pesquisa.get_id_txt_linguagem_de_prog()).send_keys("ruby, python, java")
    context.web.find_element_by_id(Pesquisa.get_id_btn_enviar()).click()
    time.sleep(3)

@then('deve ser direcionado para uma página de sucesso')
def step_impl(context):
    context.label = context.web.find_element_by_id(Confirmacao.get_id_lbl_msg_confirmacao()).text
    assert context.label == "Your form has been successfully submitted."



