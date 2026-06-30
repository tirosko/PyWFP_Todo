import os

FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                done_str, text = line.split(";", 1)
                done = (done_str == "1")
                tasks.append({"text": text, "done": done})
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for task in tasks:
            done_str = "1" if task["done"] else "0"
            f.write(f"{done_str};{task['text']}\n")


def show_tasks(tasks):
    if not tasks:
        print("Nemáš žiadne úlohy.")
        return
    print("\nTvoje úlohy:")
    for i, task in enumerate(tasks, start=1):
        status = "[X]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['text']}")
    print()


def add_task(tasks):
    text = input("Zadaj text úlohy: ").strip()
    if text:
        tasks.append({"text": text, "done": False})
        print("Úloha pridaná.\n")
    else:
        print("Prázdna úloha sa nepridala.\n")


def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Číslo úlohy na označenie ako splnenú: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Úloha označená ako splnená.\n")
        else:
            print("Neplatné číslo.\n")
    except ValueError:
        print("Zadaj číslo.\n")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Číslo úlohy na vymazanie: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Úloha '{removed['text']}' vymazaná.\n")
        else:
            print("Neplatné číslo.\n")
    except ValueError:
        print("Zadaj číslo.\n")


def main():
    tasks = load_tasks()

    while True:
        print("=== MINI TO-DO ===")
        print("1 – Zobraziť úlohy")
        print("2 – Pridať úlohu")
        print("3 – Označiť úlohu ako splnenú")
        print("4 – Vymazať úlohu")
        print("5 – Ukončiť")
        choice = input("Vyber možnosť: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Ukončujem program. Ahoj!")
            break
        else:
            print("Neplatná voľba.\n")


if __name__ == "__main__":
    main()
