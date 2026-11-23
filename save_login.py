from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser =p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://lms.gakusei.kyoto-u.ac.jp/portal")

    input("ブラウザでログインが終わったらEnter")

    context.storage_state(path="state.json")
    print("ログイン状態を保存")
    browser.close()