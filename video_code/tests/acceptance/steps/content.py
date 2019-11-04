from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    # title_tag = context.driver.find_element(*HomePageLocators.TITLE)  # this can be more flexible # 1st steps
    # however it cd be expressed as well as this --> title_tag = context.driver.find_element_by_id(id)
    # Asterick is use to deconstruct the tuple and parse individual args
    assert page.title.is_displayed()


@step('The title tag has content "(.*)"')  # used @step since it's a repeated step'
def step_impl(context, content):

    # title_tag = context.driver.find_element(*HomePageLocators.TITLE)
    # title_tag = context.driver.find_element(By.TAG_NAME, 'h1') --> original
    page = BasePage(context.driver)
    assert page.title.text == content


@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)

    assert page.posts_section.is_displayed()


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]

    assert len(posts_with_title) > 0
    assert all([post.is_displayed() for post in posts_with_title])
