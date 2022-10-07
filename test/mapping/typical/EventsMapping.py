import dateutil.parser
from datetime import datetime
from typing import Set, Any, Generic

from main.mapping.Field import Field
from main.Asgn import Asgn

from main.mapping.ObjectMapper import ObjectMapper
from test.mapping.typical.DistinguishedNameSerializer import DistinguishedNameSerializer
from test.mapping.typical.Exchange import Exchange
from test.mapping.typical.ExchangeFormatter import ExchangeFormatter

from typing import TypeVar

from test.mapping.typical.TimeSerializer import TimeSerializer

OF = TypeVar('OF')
RF = TypeVar('RF')



"""
 Context of batch translation.
 """


class BatchContext:
    """
     * Creates instance.
     :param exchangeFormatter: Formatter used to dump exchange that is being processed.
     :param exchange: Exchange that is being processed.
     """

    def __init__(self, exchangeFormatter: ExchangeFormatter,
                 exchange: Exchange):
        self.exchange = exchange
        self.exchangeFormatter = exchangeFormatter

    def __str__(self) -> str:
        return f"{{exchange={self.exchangeFormatter.format(self.exchange)}}}"


"""
 * Custom context that caches data from field to field while translating an event.
 """


# @ToString(includeNames = True, includePackage = False, ignoreNulls = False)
class EventContext:
    """
     * Context of a batch.

     * Name of the mapping table being used to map fields of event.

     * Creates instance.
     :param batchContext: Context of a batch.
     :param mappingTableName: Name of the mapping table being used to map the event.
     """

    def __init__(self, batchContext: BatchContext, mappingTableName: str):
        self.batchContext = batchContext
        self.mappingTableName = mappingTableName


"""
 * A field with pre-set types of original and result objects for real time and resync channels.
 * OF - Type of original field.
 * RF - Type of result field.
 """


class F(Generic[OF, RF], Field[dict[str, object], dict[str, object], OF, RF, EventContext]):
    pass


# Translates notifications.

class EventsMapping:

    def __init__(self):
        '''
         * Value of agentEntity specified in configuration.
         *
         * Remove this when coding for real EMS and it provides agentEntity.
         * Otherwise, keep the parameter but remove this comment.
        '''

        self.configuredAgentEntity: str

        """
         * Mapping between probable causes sent by EMS and standard TMB probable causes.
         """

        self.probableCauses: dict[str, str]

        """
         * Mapping between alarm types sent by EMS and standard TMB alarm types.
         """

        self.alarmTypes: dict[str, str]

        """
         * Mapping between severities sent by EMS and standard TMB severities.
         """

        self.severities: dict[str, str]

        """
         * Fields used to translate objectInstance in real time notifications.
         """

        self.rtObjectInstanceFields: Set[str] = set(('in_CLASS_1', 'in_CLASS_2', 'in_objectInstance'))

        """
         * Serializes distinguished name that will be sent to the bus.
         """

        self.distinguishedNameSerializer: DistinguishedNameSerializer

        """
         * Converter for dates.
         """

        self.timeSerializer: TimeSerializer

        """
         * Mapper to be used to map events.
         """

        self.mapper: ObjectMapper[dict[str, object], dict[str, object], EventContext]
        # Mapping table for raise alarm notifications.
        self.notifyNewAlarm: dict[Field[dict[str, object], dict[str, object], Any, Any, EventContext], bool] = {
            F[None, str](
                withId='notificationType'
                , withDefaulter=(lambda d, it: 'notifyNewAlarm')
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_notificationType', it))): True,
            F[None, str](
                withId='agentEntity'
                , withDefaulter=(lambda d, it: self.configuredAgentEntity)
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_agentEntity', it))): True,
            F[str, str](
                withId='alarmId'
                , withGetter=(lambda d, it: str(it['in_alarmId']))
                , withValidator=(lambda d, it: it)
                , withTranslator=(lambda d, it: it)
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_alarmId', it))): True,
            F[str, str](
                withId='alarmType'
                , withGetter=(lambda d, it: str(it['in_alarmType']))
                , withValidator=(lambda d, it: it in self.alarmTypes)
                , withTranslator=(lambda d, it: self.alarmTypes[it])
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_alarmType', it))): True,
            F[str, str](
                withId='objectClass'
                , withGetter=(lambda d, it: str(it['in_objectClass']))
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_objectClass', it))): False,
            F[dict[str, object], str](
                withId='objectInstance'
                , withGetter=(lambda d, it: {key: it[key] for key in self.rtObjectInstanceFields if key in it.keys()})
                , withValidator=(lambda d, it: ('in_CLASS_2' in it and 'in_CLASS_1' in it) or 'in_objectInstance' in it)
                , withTranslator=(lambda d, it: it['in_objectInstance'])
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_objectInstance', it))): True,
            F[int, int](
                withId='notificationId'
                , withGetter=(lambda d, it: int(it['in_notificationId']))
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_notificationId', it))): False,
            F[list[int], list[int]](
                withId='correlatedNotifications'
                , withGetter=(lambda d, it: it.get('in_correlatedNotifications', None))
                , withValidator=(lambda d, it: it)
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_correlatedNotifications', it))): False,
            F[str, str](
                withId='eventTime'
                , withGetter=(lambda d, it: str(it['in_eventTime']))
                , withValidator=(lambda d, it: dateutil.parser.parse(it) is not None)
                , withDefaulter=(lambda d, it: datetime.now())
                , withTranslator=(lambda d, it: dateutil.parser.parse(it).isoformat(sep='T') )
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_eventTime', it))): True,
            F[str, str](
                withId='systemDN'
                , withGetter=(lambda d, it: str(it['in_systemDN']))
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_systemDN', it))): False,
            F[str, str](
                withId='probableCause'
                , withGetter=(lambda d, it: str(it['in_probableCause']))
                , withValidator=(lambda d, it: it in self.probableCauses)
                , withDefaulter=(lambda d, it: 'indeterminate')
                , withTranslator=(lambda d, it: self.probableCauses[it])
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_probableCause', it))): True,
            F[str, str](
                withId='perceivedSeverity'
                , withGetter=(lambda d, it: str(it['in_perceivedSeverity']))
                , withValidator=(lambda d, it: it in self.severities)
                , withDefaulter=(lambda d, it: 'Indeterminate')
                , withTranslator=(lambda d, it: self.severities[it])
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_perceivedSeverity', it))): True,
            F[list[str], list[str]](
                withId='specificProblem'
                , withGetter=(lambda d, it: it['in_specificProblem'])
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_specificProblem', it))): False,
            F[str, str](
                withId='additionalText'
                , withGetter=(lambda d, it: str(it['in_additionalText']))
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_additionalText', it))): False,
            F[str, str](
                withId='siteLocation'
                , withGetter=(lambda d, it: str(it['in_siteLocation']))
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_siteLocation', it))): False,
            F[str, str](
                withId='regionLocation'
                , withGetter=(lambda d, it: str(it['in_regionLocation']))
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_regionLocation', it))): False,
            F[str, str](
                withId='vendorName'
                , withGetter=(lambda d, it: str(it['in_vendorName']))
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_vendorName', it))): False,
            F[str, str](
                withId='technologyDomain'
                , withGetter=(lambda d, it: str(it['in_technologyDomain']))
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_technologyDomain', it))): False,
            F[str, str](
                withId='equipmentModel'
                , withGetter=(lambda d, it: str(it['in_equipmentModel']))
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_equipmentModel', it))): False,
            F[bool, bool](
                withId='plannedOutageIndication'
                , withGetter=(lambda d, it: bool(it['in_plannedOutageIndication']))
                , withSetter=(lambda d, it: Asgn(d.resultObject, 'out_plannedOutageIndication', it))): False
        }


    """
     * Maps single real time event.
     *
     :param raw: Incoming event.
     :param batchContext: Mapping context.
     * @return list of outgoing mapped events.
     """

    def mapEvent(self, raw: dict[str, object], batchContext: BatchContext) -> list[dict[str, object]]:
        notificationType: str = 'notifyNewAlarm'
        eventContext: EventContext = EventContext(batchContext, notificationType)
        event = dict()
        event = self.mapper.mapAllFields(raw, event, self.notifyNewAlarm, eventContext)
        result: list[dict[str, object]] = [event]
        return result
