from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')  # allows our steps receive steps from the scenarios


@given('I am on the homepage')
def step_impl(context):

    context.driver = webdriver.Chrome()
    # launches a new chrome window and gives you access to it programatically
    page = HomePage(context.driver)

    context.driver.get(page.url)  # navigates to that given site


@given('I am on the blog page')
def step_impl(context):

    context.driver = webdriver.Chrome()
    # launches a new chrome window and gives you access to it programatically
    page = BlogPage(context.driver)

    context.driver.get(page.url)  # navigates to that given site


@given('I am on the new post page')
def step_impl(context):

    context.driver = webdriver.Chrome()
    # launches a new chrome window and gives you access to it programatically
    page = NewPostPage(context.driver)

    context.driver.get(page.url)  # navigates to that given site


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url
