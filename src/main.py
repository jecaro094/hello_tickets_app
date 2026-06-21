
from src.utils import get_logger
import src.constants as const
import asyncio
from playwright.sync_api import sync_playwright

logger = get_logger(__name__)

test_url = (
    "https://www.hellotickets.es/estados-unidos/nueva-york/excursion-2-dias-cataratas-niagara-filadelfia-washington/a/pa-6800"
)

def handle_locator():
    pass

def run(test_url):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(test_url)
        logger.info(f"Título de la página: {page.title()}")

        # Datepicker
        date_picker = page.locator(".datepicker-input")
        if date_picker.count() == 1:
            logger.info("Datepicker exists; clicking")
            date_picker.click()
        else:
            logger.info("Datepicker does not exist...")

        day_text = "30"
        day = page.locator(".calendar__day-number", has_text=day_text)

        number_of_days = day.count()
        if number_of_days > 0:
            logger.info(f"Found {number_of_days} days in the calendar with text {day_text}")
            day.first.click()
            page.wait_for_timeout(3000)
        else:
            logger.info("Not found dates in datepicker...")

        select_button = page.locator(".custom-button.check-availability__btn.custom-button--default")
        if select_button.count() > 0:
            logger.info("Select button exists! Clicking...")

            # Esperar a la petición AJAX que carga las opciones
            with page.expect_response(lambda r: "availability" in r.url):
                select_button.click()

            logger.info("AJAX response received")

        else:
            logger.info("Not found select button in page...")

        options = page.locator(".tour-grades-options.tour-grades-list-item__options")

        if options.count() > 0:
            logger.info(f"{options.count()} options available!")
            page.wait_for_timeout(3000)
        else:
            logger.info("No options available after date selection...")

        count = options.count()
        for i in range(count):
            text = options.nth(i).inner_text()
            logger.info(text)

        browser.close()

    logger.info(f"url: {test_url}")


if __name__ == "__main__":
    asyncio.run(run(test_url))

