from enum import Enum

KPI_COLUMN_NAME = 'kpi'

concatenatedList = []

class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class OriginEvents(str, ExtendedEnum):
    OWN_PUCKOUT_WON = 'own po won'
    OWN_PUCKOUT_LOST = 'own po lost'
    OPP_PUCKOUT_WON = 'opp po won'
    OPP_PUCKOUT_LOST = 'opp po lost'
    OWN_SL_WON = 'own sl won'
    OWN_SL_LOST = 'own sl lost'
    OPP_SL_WON = 'opp sl won'
    OPP_SL_LOST = 'opp sl lost'
    OWN_PUCK_KICK_WON = 'own puck/kick out won'
    OWN_PUCK_KICK_LOST = 'own puck/kick out lost'


class PlayType(str, ExtendedEnum):
    FROM_PLAY = 'from play'
    FROM_PLACED = 'from placed'
    FROM_FREE = 'from free'
    FROM_65 = 'from 65'
    FROM_SL = 'from sideline'
    FROM_PENALTY = 'from penalty'
    OUT_4565 = 'from 45/65'


class Scores(str, ExtendedEnum):
    POINT = 'point'
    GOAL = 'goal'
    OPP_POINT = 'opp point'
    OPP_GOAL = 'opp goal'
    SCORE = 'score'


class Shots(str, ExtendedEnum):
    WIDE = 'wide'
    WIDE_SL = 'wide sideline'
    OPP_WIDE_SL = 'opp wide sideline'
    OPP_WIDE = 'opp wide'
    SAVED_65 = 'save out 65'
    OPP_SAVED_65 = 'opp save out 65'
    SAVED_4565 = 'saved out for 45/65'
    OPP_SAVED_4565 = 'opp saved out for 45/65'
    SHOT = 'shot'
    SAVED = 'saved'
    SHORT = 'short'
    POSTS = 'off posts'
    OUT_4565 = 'out for 45/65'


class Deadballs(str, ExtendedEnum):
    OUT_65 = '65'
    OUT_SL = 'out sl'
    OPP_OUT_65 = 'opp 65'
    OPP_OUT_SL = 'opp out sl'


class TransitionEvents(str, ExtendedEnum):
    FREE_AGAINST = 'free against'
    OPP_FREE_AGAINST = 'opp free against'
    FREE_PEN_CONCEEDED = 'free/pen conceded'
    TO_WON = 'to won'
    TO_LOST = 'opp to won'
    SHORT_FROM_PLAY = 'short from play'
    SHORT_FROM_PLACED = 'short from placed'
    SHORT_FROM_FREE = 'short from free'
    SHORT_FROM_65 = 'short from 65'
    SHORT_FROM_SL = 'short from sideline'
    TO = 'to'
    FREE = 'free'
    OPP_SHORT = 'opp short'
    OPP_SHORT_FROM_PLAY = 'opp short from play'
    OPP_SHORT_FROM_PLACE = 'opp short from placed'
    OPP_SHORT_FROM_FREE = 'opp short from free'
    OPP_SHORT_FROM_65 = 'opp short from 65'
    OPP_SHORT_FROM_SIDELINE = 'opp short from sideline'


class FreeEvents(str, ExtendedEnum):
    FREE_AGAINST = 'free against'
    OPP_FREE_AGAINST = 'opp free against'
    FREE = 'free'
    FREE_PEN_CONCEEDED = 'free/pen conceded'


class TurnoverEvents(str, ExtendedEnum):
    TO_WON = 'to won'
    TO_LOST = 'opp to won'
    TO = 'to'


class AttackEvents(str, ExtendedEnum):
    ATTACK = 'attack'
    OPP_ATTACK = 'opp attack'


class SidelineEvents(str, ExtendedEnum):
    SL = 'sl'
    OWN_SL_WON = 'own sl won'
    OWN_SL_LOST = 'own sl lost'
    OPP_SL_WON = 'opp sl won'
    OPP_SL_LOST = 'opp sl lost'


class ShortShotEvents(str, ExtendedEnum):
    SHORT_FROM_PLAY = 'short from play'
    SHORT_FROM_PLACED = 'short from placed'
    SHORT_FROM_65 = 'short from 65'
    SHORT_FROM_SL = 'short from sideline'
    SHORT = 'short'
    OPP_SHORT = 'opp short'
    OPP_SHORT_FROM_PLAY = 'opp short from play'
    OPP_SHORT_FROM_PLACE = 'opp short from placed'
    OPP_SHORT_FROM_65 = 'opp short from 65'
    OPP_SHORT_FROM_SIDELINE = 'opp short from sideline'


class MiddleEvents(str, ExtendedEnum):
    POS_POSSESSION = 'pos possession'
    NEG_POSSESSION = 'neg possession'
    POSSESSION = 'possession'
    OPP_POSSESSION = 'opp possession'
    TACKLE = 'tackle'
    ATTACK = 'attack'
    OPP_ATTACK = 'opp attack'
    POS_COACH = 'coach +'
    NEG_COACH = 'coach -'
    SHAPE_FORMATION = 'shape formation'
    GOAL_CHANCE = 'goal chance'
    OPP_GOAL_CHANCE = 'opp goal chance'
    RUCK_WON = 'ruck won'
    RUCK_LOST = 'ruck lost'
    THROW_IN = 'throw in'

    YELLOW_CARD = 'yellow card'
    RED_CARD = 'red card'

    SAVE = 'save'
    SAVE_FROM_PLAY = 'save from play'
    SAVE_FROM_PLACED = 'save from placed'
    SAVE_FROM_65 = 'save from 65'
    SAVE_FROM_SL = 'save from sideline'

    OPP_SAVE = 'opp save'
    OPP_SAVE_FROM_PLAY = 'opp save from play'
    OPP_SAVE_FROM_PLACED = 'opp save from placed'
    OPP_SAVE_FROM_65 = 'opp save from 65'
    OPP_SAVE_FROM_SL = 'opp save from sideline'

    POSTS = 'posts'
    POSTS_FROM_PLAY = 'posts from play'
    POSTS_FROM_PLACED = 'posts from placed'
    POSTS_FROM_65 = 'posts from 65'
    POSTS_FROM_SL = 'posts from sideline'

    OPP_POSTS = 'posts'
    OPP_POSTS_FROM_PLAY = 'opp posts from play'
    OPP_POSTS_FROM_PLACED = 'opp posts from placed'
    OPP_POSTS_FROM_65 = 'opp posts from 65'
    OPP_POSTS_FROM_SL = 'opp posts from sideline'


def is_origin_of_play_event(row):
    if row[KPI_COLUMN_NAME] in OriginEvents.list():
        return True

    return False


def is_outcome_of_play_event(row):
    if row[KPI_COLUMN_NAME] in get_concatenate_play_type_and_outcomes():
        return True

    return False


def is_transition_play_event(row):
    if row[KPI_COLUMN_NAME] in TransitionEvents.list():
        return True

    return False


def is_middle_play_event(row):
    if row[KPI_COLUMN_NAME] in MiddleEvents.list():
        return True

    return False


def get_outcomes_as_list():
    outcome_list = list()
    outcome_list.extend(Scores.list())
    outcome_list.extend(Shots.list())
    outcome_list.extend(Deadballs.list())

    return outcome_list


def get_concatenate_play_type_and_outcomes():
    if len(concatenatedList) == 0:
        for _, outcome in enumerate(get_outcomes_as_list()):
            concatenatedList.append(outcome)

            for _, play_type in enumerate(PlayType.list()):
                play_type_outcome = outcome + ' ' + play_type
                concatenatedList.append(play_type_outcome)

    return concatenatedList


def is_outcome_a_score(outcome):
    for score in Scores.list():
        if outcome.startswith(score):
            return True

    return False


def is_outcome_a_shot(outcome):
    for shot in Shots.list():
        if outcome.startswith(shot):
            return True

    return False


def is_outcome_a_free(outcome):
    for event in FreeEvents.list():
        if outcome.startswith(event):
            return True

    return False


def is_outcome_a_turnover(outcome):
    for event in TurnoverEvents.list():
        if event in outcome:
            return True

    return False


def is_outcome_a_sideline(outcome):
    for event in SidelineEvents.list():
        if event in outcome:
            return True

    return False


def is_outcome_short_shot(outcome):
    for event in ShortShotEvents.list():
        if event in outcome:
            return True

    return False


def transpose_outcome(outcome):
    if is_outcome_a_shot(outcome):
        return Shots.SHOT.value

    if is_outcome_a_score(outcome):
        return Scores.SCORE.value

    if is_outcome_a_free(outcome):
        return FreeEvents.FREE.value

    if is_outcome_a_turnover(outcome):
        return TurnoverEvents.TO.value

    if is_outcome_a_sideline(outcome):
        return SidelineEvents.SL.value

    if is_outcome_short_shot(outcome):
        return Shots.SHOT.value

    return outcome
