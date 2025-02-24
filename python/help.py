from audio import playSoundByFilename
from speech_synthesizer import text_to_speech

help_dict = {
    -1: "Для этого раздела пока не составлены подсказки",
    "main": "Вы находитесь в главном меню приложений. Джойстик вниз или вверх: переключение между приложениями. Джойстик вправо: запустить приложение. Если вы хотите начать набирать заметку, просто начните вводить текст с помощью клавиатуры.",
    "units_tests": "Вы находитесь в меню уроков и тестов. Джойстик вниз: перейти к следующему занятию. Вверх: к предыдущему занятию. Влево: выйти в главное меню. Вправо: начать выбранное занятие.",
    "unit": "Вы находитесь внутри урока. Урок разделён на шаги. Перейти к следующему шагу: джойстик вправо, к предыдущему: влево, повторить текущий: вверхх, выйти в меню уроков: вниз",
    "test": "",
    "notes": "Вы находитесь в приложении Заметки. Джойстик вниз: перейти к следующей заметке. Вверх: к предыдущей заметке. Влево: выйти в главное меню. Вправо: прочитать заметку, а при выборе Новая заметка — создать заметку.",
    "alphabet": "Вы находитесь в приложении Азбука. Джойстик вниз: озвучить и вывести следующую букву. Вверх: предыдущую букву. Влево: выйти в главное меню. Вправо: повторить букву ещё раз.",
    "clock": "Вы находитесь в приложении Часы. Джойстик влево: выйти в главное меню.",
    "blitzModes": "Вы находитесь в меню приложения блиц-опрос на знание азбуки Брайля. Джойстик вверх или вниз: переключение между режимами. Джойстик вправо: начать раунд с выбранным режимом. Джойстик влево: возврат в главное меню. В каждом раунде нужно распознать букву, выведенную на ячейку Брайля. В режиме чтения букву нужно произнести вслух в микрофон. В режиме ввода с клавиатуры - набрать на шестиклавишной клавиатуре.",
    "calculator": "Вы находитесь в приложении Калькулятор. Для ввода +,-,*,/ используйте первые буквы соответствующих операций (сложение, вычитание, умножение, деление). Джойстик вниз: скобка открывается. Вверх: скобка закрывается. Джойстик влево: выйти в главное меню. Вправо: вывести результат.",
    "pushkin":"Приложение для чтения отрывков из цикла повестей 'Маленькие трагедии'. Джойстик вверх или вниз - переключение между отрывками. Джойстик вправо - читать отрывок далее. Джойстик влево - выйти в главное меню",
    "pushkin_line":"Приложение для чтения отрывков из цикла повестей 'Маленькие трагедии'. Джойстик влево или вниз - выход назад в меню отрывков. Джойстик вправо - читать отрывок далее, вверх - повторить строчку. Джойстик влево - выйти в главное меню",
}


def instantHelp(menuID):
    text_to_speech(help_dict[menuID])
