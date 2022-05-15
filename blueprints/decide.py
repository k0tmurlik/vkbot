from vkbottle.bot import Blueprint
from simpleeval import simple_eval

bp = Blueprint("EvalCalc")
bp.labeler.vbml_ignore_case = False


@bp.on.message(text='реши <text>')
async def eval_text(_, text):

    try:
        return f"😎 Решил твой пример.\n>> Результат: {simple_eval(text)}"

    except:
        return f"🤨 Произошла ошибка. Проверьте пример, и введите его заново."
