from typing import List
from typing import Union

from pyrogram import filters

# --- حركة الإنقاذ لعام 2026 ---
# بنعرف 'edited' يدوي عشان أي ملف يطلبها يلاقيها وميعملش كراش
if not hasattr(filters, "edited"):
    filters.edited = filters.create(lambda _, __, ___: False)

from VCPlayBot.config import COMMAND_PREFIXES

# تم حذف filters.edited للتوافق مع تحديثات pyrogram 2.0+
other_filters = filters.group & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
