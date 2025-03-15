from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
# Ждем появления поля поиска
wait = WebDriverWait(browser, 10)  # Максимальное время ожидания - 10 секунд
search_box = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))

# Отправляем текст в поле поиска и нажимаем Enter
search_box.send_keys(input("Введите ваш запрос: "))
search_box.send_keys(Keys.RETURN)

# Ожидание загрузки результатов поиска
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))  # Ожидаем появления ссылок

# Шаг 3: Даем пользователю возможность выбирать дальнейшие действия
def scroll_paragraphs(driver):
    """
    Функция для постраничного вывода параграфов статьи.
    :param driver: экземпляр веб-драйвера Selenium.
    """
    # Находим все параграфы на странице
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')

    # Проходим по каждому параграфу и выводим его текст
    for i, paragraph in enumerate(paragraphs):
        print(f"{i + 1}. {paragraph.text}")  # Выводим номер параграфа и его текст
        input("Нажмите Enter для продолжения...")  # Ожидаем ввода пользователя перед показом следующего параграфа

while True:
    print("\nТекущая страница:", browser.title)

    # Шаг 4: Выбор действия
    choice = input("""
Выберите действие:
1. Листать параграфы текущей статьи
2. Перейти на одну из связанных страниц
3. Выйти из программы
Ваш выбор: """)

    if choice == '1':
        # Листание параграфов
        scroll_paragraphs(browser)

    elif choice == '2':
        # Выбор ссылки для перехода
        link_text = input("Введите название связанной страницы: ").strip()
        try:
            # Поиск всех ссылок на странице
            all_links = browser.find_elements(By.PARTIAL_LINK_TEXT, link_text)
            if not all_links:
                print("Не найдено ссылок с таким названием.")
            else:
                # Переход по первой подходящей ссылке
                all_links[0].click()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    elif choice == '3':
        break

    else:
        print("Неверный ввод. Попробуйте ещё раз.")

# Функция для листания параграфов
def scroll_paragraphs(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    for i, paragraph in enumerate(paragraphs):
        print(f"{i + 1}. {paragraph.text}")
        input("Нажмите Enter для продолжения...")

# Закрытие браузера после завершения работы
browser.quit()
