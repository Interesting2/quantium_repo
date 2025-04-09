import pytest
from visualise_data import app 
from selenium.webdriver.chrome.webdriver import WebDriver
from dash import testing as dcct

@pytest.mark.usefixtures("dash_duo")
def test_check_header(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None
    assert header.text == "Pink Morsel Sales [2018-2022]" 

def test_check_visualisation(dash_duo):
    dash_duo.start_server(app)

    visualization = dash_duo.find_element("#Pink-Morsel-Sales")
    assert visualization is not None

def test_check_region_picker(dash_duo):
    dash_duo.start_server(app)

    region_picker = dash_duo.find_element("#radio-region")
    assert region_picker is not None
