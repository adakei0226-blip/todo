from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser =p.chromium.launch(headless=False)
    context = browser.new_context(storage_state = "state.json")
    page = context.new_page()
    page.goto("https://lms.gakusei.kyoto-u.ac.jp/portal")
    print(page.title())

    input("確認出来たらEnter")

    # print("ログイン状態を保存")
    browser.close()