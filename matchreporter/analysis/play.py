from matchreporter.analysis.events import AttackEvents

ROW_TEAM = 'team'
ROW_KPI = 'kpi'
ROW_TIME = 'time'

PLAY_ID = 0

def get_play():
    global PLAY_ID
    play = Play(PLAY_ID)
    PLAY_ID = PLAY_ID + 1
    return play


class Play:
    def __init__(self, playid):
        self.starttime = ''
        self.endtime = ''
        self.events = []
        self.origin = ''
        self.outcome = ''
        self.origin_team = ''
        self.outcome_team = ''
        self.origin_attacks = 0
        self.outcome_attacks = 0
        self.playid = playid
        self.previous = playid - 1
        self.next = playid + 1

    def add_event(self, event):
        self.events.append(event)


    def add_origin_event(self, origin_event):
        if self.has_origin_event() is not True:
            self.add_event(origin_event)
            self.starttime = origin_event[ROW_TIME]
            self.origin = origin_event[ROW_KPI]
            self.origin_team = origin_event[ROW_TEAM]
        else:
            raise Exception('Cannot set origin - play has events')


    def add_outcome_event(self, outcome_event):
        self.add_event(outcome_event)
        self.endtime = outcome_event[ROW_TIME]
        self.outcome = outcome_event[ROW_KPI]
        self.outcome_team = outcome_event[ROW_TEAM]
        self._compute_attack_events()


    def has_origin_event(self):
        if len(self.events) > 0:
            return True

        return False


    def _is_attack_event(self, event):
        if event in AttackEvents.list():
            return True

        return False


    def _compute_attack_events(self):
        for _, event in enumerate(self.events):
            if (self.origin_team == event[ROW_TEAM]) and (self._is_attack_event(event[ROW_KPI])):
                self.origin_attacks = self.origin_attacks + 1
            elif (self.outcome_team == event[ROW_TEAM]) and (self._is_attack_event(event[ROW_KPI])):
                self.outcome_attacks = self.outcome_attacks + 1


