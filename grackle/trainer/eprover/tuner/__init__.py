from .base import BaseTuner
from .glob import GlobalTuner
from .order import OrderTuner
from .sine import SineTuner
from .fine import FineTuner

from .wpo import WpoOrderTuner, WpoFakeOrderTuner, OnlyWpoTuner, OnlyWpoFakeTuner

BASE  = lambda nick: BaseTuner(True, 1, nick)
GLOBAL = lambda nick: GlobalTuner(True, 1, nick)
ORDER = lambda nick: OrderTuner(True, 1, nick)
SINE = lambda nick: SineTuner(True, 1, nick)
FINE  = lambda nick: FineTuner(True, 1, nick)

WPO_ORDER = lambda nick: WpoOrderTuner(True, 1, nick)
WPO_FAKE_ORDER = lambda nick: WpoFakeOrderTuner(True, 1, nick)
WPO_ONLY = lambda nick: OnlyWpoTuner(True, 1, nick)
WPO_FAKE_ONLY = lambda nick: OnlyWpoFakeTuner(True, 1, nick)

