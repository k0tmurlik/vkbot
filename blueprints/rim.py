from vkbottle.bot import Blueprint

bp = Blueprint("RimNumber")
bp.labeler.vbml_ignore_case = True
 

@bp.on.message(text='рим <number:int>')
async def rim(_, number: int):

    if number > 5000:
        return "❓ Укажите число менее 5.000."

    base = "I" * int(number)
    
    base = base.replace("I" * 5, "V")
    base = base.replace("V" * 2, "X")
    base = base.replace("X" * 5, "L")
    base = base.replace("L" * 2, "C")

    base = base.replace("C" * 5, "D")
    base = base.replace("D" * 2, "M")
    base = base.replace("DCCCC", "CM")
    base = base.replace("CCCC", "CD")

    base = base.replace("LXXXX", "XC")
    base = base.replace("XXXX", "XL")
    base = base.replace("VIIII", "IX")
    base = base.replace("IIII", "IV")

    return f'✏ Ваше число: {number}\n📝 В римких числах: {base}'
