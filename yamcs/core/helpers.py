import logging
from collections import OrderedDict
from datetime import datetime


def parse_isostring(isostring):
    """
    Parse the ISO String to a native ``datetime``.
    """
    return datetime.strptime(isostring.replace('Z', 'GMT'),
                             '%Y-%m-%dT%H:%M:%S.%f%Z')


def parse_value(proto):
    """
    Convers a Protobuf `Value` from the API into a python native value
    """
    if proto.HasField('floatValue'):
        return proto.floatValue
    elif proto.HasField('doubleValue'):
        return proto.doubleValue
    elif proto.HasField('sint32Value'):
        return proto.sint32Value
    elif proto.HasField('uint32Value'):
        return proto.uint32Value
    elif proto.HasField('binaryValue'):
        return proto.binaryValue
    elif proto.HasField('timestampValue'):
        # Don't use the actual 'timestampValue' field, it contains a number
        # that is difficult to interpret on the client. Instead parse from
        # the ISO String also set by Yamcs.
        return parse_isostring(proto.stringValue)
    elif proto.HasField('stringValue'):
        return proto.stringValue
    elif proto.HasField('uint64Value'):
        return proto.uint64Value
    elif proto.HasField('sint64Value'):
        return proto.sint64Value
    elif proto.HasField('booleanValue'):
        return proto.booleanValue
    elif proto.HasField('arrayValue'):
        return [parse_value(v) for v in proto.arrayValue]
    elif proto.HasField('aggregateValue'):
        return OrderedDict(zip(proto.aggregateValue.name, proto.aggregateValue.value))
    else:
        logging.warn('Unrecognized value type for update %s', proto)
        return None
