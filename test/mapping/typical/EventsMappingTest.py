import json
from typing import TypeVar, Any

import pytest

from main.mapping.impl.SimpleObjectMapper import SimpleObjectMapper
from test.mapping.typical.DistinguishedNameSerializer import DistinguishedNameSerializer
from mock import Mock

from test.mapping.typical.EventsMapping import EventsMapping, BatchContext
from test.mapping.typical.Exchange import Exchange
from test.mapping.typical.ExchangeFormatter import ExchangeFormatter
from test.mapping.typical.TimeSerializer import TimeSerializer

OO = TypeVar('OO')
RO = TypeVar('RO')
OF = TypeVar('OF')
RF = TypeVar('RF')
P = TypeVar('P')

class EventsMappingTest:

    def __init__(self):
        rawEvent: dict[str, Any]
        exchange:Exchange = Mock()
        exchangeFormatter:ExchangeFormatter = Mock()

        self.batchContext: BatchContext = BatchContext(
                exchangeFormatter,
                exchange)



        mapping: EventsMapping = EventsMapping()
        mapping.configuredAgentEntity = 'configuredAgentEntity'
        mapping.probableCauses = {
                'a-bis to bts interface failure': 'a-bis to bts interface failure',
                'a-bis to trx interface failure': 'a-bis to trx interface failure',
                'adapter error'                 : 'adapter error',
                'air compressor failure'        : 'air compressor failure',
                'fire'                          : 'fire',
                'fire detector failure'         : 'fire detector failure',
        }
        mapping.alarmTypes = {
                "CommunicationsAlarm"  : 'CommunicationsAlarm',
                "ProcessingErrorAlarm" : 'ProcessingErrorAlarm',
                "EnvironmentalAlarm"   : 'EnvironmentalAlarm',
                "QualityOfServiceAlarm": 'QualityOfServiceAlarm',
                "EquipmentAlarm"       : 'EquipmentAlarm',
        }
        mapping.severities = {
                "Cleared"      : 'Cleared',
                "Indeterminate": 'Indeterminate',
                "Critical"     : 'Critical',
                "Major"        : 'Major',
                "Minor"        : 'Minor',
                "Warning"      : 'Warning',
        }
        mapping.mapper = SimpleObjectMapper[str, str, str]()
        mapping.timeSerializer = Mock(TimeSerializer)
        mapping.distinguishedNameSerializer = Mock(DistinguishedNameSerializer)
        self.eventsMapping = mapping

    def notifyNewAlarm(self):
        #@given:
        rawEvent = json.loads("""
{
  "in_notificationType": "notifyNewAlarm",
  "in_alarmType": "CommunicationsAlarm",
  "in_objectClass": "PHYSICAL_TERMINATION_POINT",
  "in_objectInstance": "IRPNetwork=ABCNetwork,Subnet=TN2,BSS=B5C0100",
  "in_notificationId": 123,
  "in_correlatedNotifications": [
    1,
    2
  ],
  "in_eventTime": "1937-01-01T12:00:27.87+00:20",
  "in_systemDN": "DC=www.some_example.org, SubNetwork=1, ManagementNode=1, IRPAgent=1",
  "in_alarmId": "ABC:5654",
  "in_agentEntity": "ems_south",
  "in_probableCause": "fire",
  "in_perceivedSeverity": "Critical",
  "in_specificProblem": [
    "example specific problem 1"
  ],
  "in_additionalText": "Everything is on fire!",
  "in_siteLocation": "Lindau",
  "in_regionLocation": "Bavaria",
  "in_vendorName": "Some Company",
  "in_technologyDomain": "Mobile",
  "in_equipmentModel": "MNM 3000",
  "in_plannedOutageIndication": false,
  "in_customStringAttribute": "custom string value",
  "in_customListAttribute": [
    "custom value 1",
    "custom value 2",
    "custom value 3"
  ]
}
""")
        #when:
        result: list[dict[str, object]] = self.eventsMapping.mapEvent(rawEvent, self.batchContext)
        #then:
        '''
        1 * eventsMapping.timeSerializer.serialize(_) ]] { Instant parsedTime -> parsedTime.toString() }
        0 * eventsMapping.distinguishedNameSerializer.serialize(_) ]] { dict[str, ?] dn ->
            dn.collect { k, v -> "$k=$v" }.join(',')
        '''
        assert result.size() == 1
        event = result[0]
        assert event['out_notificationType'] == 'notifyNewAlarm'
        assert event['out_alarmType'] == 'CommunicationsAlarm'
        assert event['out_objectClass'] == 'PHYSICAL_TERMINATION_POINT'
        assert event['out_objectInstance'] == "IRPNetwork=ABCNetwork,Subnet=TN2,BSS=B5C0100"
        assert event['out_notificationId'] == 123
        assert event['out_correlatedNotifications'] == [1, 2]
        #Instant.from(DateTimeFormatter.ISO_DATE_TIME.parse(event['out_eventTime'] as str)) ==
        #        Instant.from(DateTimeFormatter.ISO_DATE_TIME.parse("1937-01-01T12:00:27.87+00:20"))
        assert event['out_systemDN'] == "DC=www.some_example.org, SubNetwork=1, ManagementNode=1, IRPAgent=1"
        assert event['out_alarmId'] == "ABC:5654"
        assert event['out_agentEntity'] == 'configuredAgentEntity'
        assert event['out_probableCause'] == 'fire'
        assert event['out_perceivedSeverity'] == 'Critical'
        assert event['out_specificProblem'] == ["example specific problem 1"]
        assert event['out_additionalText'] == "Everything is on fire!"
        assert event['out_siteLocation'] == 'Lindau'
        assert event['out_regionLocation'] == 'Bavaria'
        assert event['out_vendorName'] == "Some Company"
        assert event['out_technologyDomain'] == 'Mobile'
        assert event['out_equipmentModel'] == "MNM 3000"
        assert event['out_plannedOutageIndication'] == False
        assert event['out_proposedRepairActions'] is None
        assert event['out_ackTime'] is None
        assert event['out_ackUserId'] is None
        assert event['out_ackState'] is None
        assert event['out_comments'] is None
    


e = EventsMappingTest()
e.notifyNewAlarm()
