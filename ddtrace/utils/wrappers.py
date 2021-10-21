from ..internal.utils.deprecation import deprecation
from ..internal.utils.wrappers import F  # noqa
from ..internal.utils.wrappers import iswrapped  # noqa
from ..internal.utils.wrappers import safe_patch  # noqa
from ..internal.utils.wrappers import unwrap  # noqa


deprecation(
    name="ddtrace.utils.wrappers",
    message="Use `ddtrace.internal.utils.wrappers` module instead",
    version="1.0.0",
)
