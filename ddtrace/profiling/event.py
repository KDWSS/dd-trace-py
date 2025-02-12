import typing

import attr

from ddtrace import span as ddspan
from ddtrace.internal import compat


_T = typing.TypeVar("_T")


def event_class(
        klass  # type: typing.Type[_T]
):
    # type: (...) -> typing.Type[_T]
    return attr.s(slots=True)(klass)


@event_class
class Event(object):
    """An event happening at a point in time."""

    timestamp = attr.ib(factory=compat.time_ns)

    @property
    def name(self):
        # type: (...) -> str
        """Name of the event."""
        return self.__class__.__name__


@event_class
class TimedEvent(Event):
    """An event that has a duration."""

    duration = attr.ib(default=None)


@event_class
class SampleEvent(Event):
    """An event representing a sample gathered from the system."""

    sampling_period = attr.ib(default=None)


@event_class
class StackBasedEvent(SampleEvent):
    thread_id = attr.ib(default=None)
    thread_name = attr.ib(default=None)
    thread_native_id = attr.ib(default=None)
    task_id = attr.ib(default=None)
    task_name = attr.ib(default=None)
    frames = attr.ib(default=None)
    nframes = attr.ib(default=None)
    local_root_span_id = attr.ib(default=None, type=typing.Optional[int])
    span_id = attr.ib(default=None, type=typing.Optional[int])
    trace_type = attr.ib(default=None, type=typing.Optional[str])
    trace_resource_container = attr.ib(default=None)

    def set_trace_info(
        self,
        span,  # type: typing.Optional[ddspan.Span]
        endpoint_collection_enabled,  # type: bool
    ):
        if span:
            self.span_id = span.span_id
            if span._local_root is not None:
                self.local_root_span_id = span._local_root.span_id
                self.trace_type = span._local_root._span_type
                if endpoint_collection_enabled:
                    self.trace_resource_container = span._local_root._resource
