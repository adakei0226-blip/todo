#主な機能：①タスクの内容　②タスクの期限設定　③タスクの追加削除　④タスクの系統ごとに分類
#task_id INTEGER, task_title TEXT, task_limit TEXT, task_type TEXT, checked INTEGER

#設計図: dbを作成、取得, db内の情報操作（内容編集や期限設定）


import sqlite3

def init_db(database):
    conn = sqlite3.connect(database)
    sql = """
    CREATE TABLE IF NOT EXISTS tasks(
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_title TEXT,
    task_limit TEXT,
    task_type TEXT,
    checked INTEGER DEFAULT 0
    )
    """
    conn.execute(sql)
    conn.commit()
    return conn

def add_task(conn,  task_title, task_limit, task_type):
    sql = """
    INSERT INTO tasks( task_title, task_limit, task_type)
    VALUES (?,?,?)
    """
    conn.execute(sql, ( task_title, task_limit, task_type))
    conn.commit()

def list_tasks(conn):
    rows = conn.execute("SELECT * FROM tasks ORDER BY task_limit").fetchall()
    for row in rows:
        print(row)

def toggle_task(conn, task_id):
    sql = """
    UPDATE tasks SET checked = 1 - checked WHERE task_id = ?
    """
    conn.execute(sql, (task_id, ))
    conn.commit()

def delete_task(conn, task_id):
    sql = """
    DELETE FROM tasks WHERE task_id = ?
    """
    conn.execute(sql, (task_id, ))
    conn.commit()

def delete_completed(conn):
    sql = """
    DELETE FROM tasks WHERE checked = 1
    """
    conn.execute(sql)
    conn.commit()

def main():
    conn = init_db("todo.db")
    while True:
        print("5:完了済みを一括削除  4:個別削除  3:タスクの完了/未完了  2:一覧  1:タスク追加  0:終了")
        choice = input("番号を入力してください > ")
        if choice == "5":
            delete_completed(conn)
        elif choice == "4":
            choice_delete = int(input("削除するタスク番号を入力してください > "))
            delete_task(conn, choice_delete)
        elif choice == "3":
            choice_complete = int(input("完了/未完了にするタスクを選んでください > "))
            toggle_task(conn, choice_complete)
        elif choice == "2":
            list_tasks(conn)
        elif choice == "1":
            title = input("タスクのタイトルを入力してください > ")
            limit = input("タスクの期限を入力してください > ")
            task_type = input("タスクの種類を入力してください > ")
            add_task(conn, title, limit, task_type)
        elif choice == "0":
            print("終了します")
            break
        else:
            print("その番号はありません")



# delete_task(conn, 5)
# # complete_task(conn, 1)
# list_tasks(conn)
# add_task(conn, "レポート提出", "2026-12-01 23:59", "授業")
# add_task(conn, "レポート提出", "2026-11-01 23:59", "授業")
# list_tasks(conn)

if __name__ == "__main__":
    main()
