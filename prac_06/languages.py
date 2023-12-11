from programming_language import Programming_language


def main():
    python = Programming_language("Python", "Dynamic", True, 1991)
    ruby = Programming_language("Ruby", "Dynamic", True, 1995)
    visual_basic = Programming_language("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]

    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == '__main__':
    main()