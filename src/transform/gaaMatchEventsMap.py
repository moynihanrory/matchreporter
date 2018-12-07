
GMA_KPI_GOAL = 'goal'
GMA_KPI_POINT = 'point'
GMA_KPI_WIDE = 'wide'
GMA_KPI_SAVED_OUT_65 = 'saved / out for 45/65'
GMA_KPI_OFF_POSTS = 'off posts'
GMA_KPI_SAVED = 'saved'
GMA_KPI_SHORT = 'short'
GMA_KPI_OUTCOMES = [GMA_KPI_GOAL, GMA_KPI_POINT, GMA_KPI_WIDE, GMA_KPI_SAVED_OUT_65,
                    GMA_KPI_OFF_POSTS, GMA_KPI_SAVED, GMA_KPI_SHORT]

GMA_KPI_SOURCE_PLAY = 'from play'
GMA_KPI_SOURCE_FREE = 'from free'
GMA_KPI_SOURCE_PEN = 'from penalty'
GMA_KPI_SOURCE_65 = 'from 45/65'
GMA_KPI_SOURCE_SL = 'from sideline'
GMA_KPI_SOURCES = [GMA_KPI_SOURCE_PLAY, GMA_KPI_SOURCE_FREE, GMA_KPI_SOURCE_PEN,
                   GMA_KPI_SOURCE_65, GMA_KPI_SOURCE_SL]



GMA_KPI_PUCKOUT_WON = 'own puckout won'
GMA_KPI_PUCKOUT_LOST = 'own puckout lost'
GMA_KPI_FREE_CONCEDED = 'free/pen conceded'
GMA_KPI_CARD_BLACK = 'black card'
GMA_KPI_CARD_YELLOW = 'yellow card'
GMA_KPI_CARD_RED = 'red card'
GMA_KPI_PUCKOUT_WON_ANDROID = 'own puck/kick out won'
GMA_KPI_PUCKOUT_LOST_ANDROID = 'own puck/kick out lost'
GMA_OUTFOR4565_ANDROID = 'out for 45/65'
GMA_SAVED_ANDROID = 'saved'
GMA_SAVED_OUTFOR4565_ANDROID = 'saved out for 45/65'
GMA_OTHER_EVENTS = [GMA_KPI_PUCKOUT_WON, GMA_KPI_PUCKOUT_LOST, GMA_KPI_CARD_BLACK,
                    GMA_KPI_CARD_YELLOW, GMA_KPI_CARD_RED, GMA_KPI_FREE_CONCEDED,
                    GMA_KPI_SAVED_OUT_65, GMA_KPI_PUCKOUT_WON_ANDROID, GMA_KPI_PUCKOUT_LOST_ANDROID,
                    GMA_OUTFOR4565_ANDROID, GMA_SAVED_ANDROID, GMA_SAVED_OUTFOR4565_ANDROID]

def createGmaKpiAndSourcesList():
    kpiAndSources = []

    for i, kpi in enumerate(GMA_KPI_OUTCOMES):
        kpi = GMA_KPI_OUTCOMES[i]

        for j, source in enumerate(GMA_KPI_SOURCES):
            source = GMA_KPI_SOURCES[j]

            kpiAndSource = '{0} {1}'.format(kpi, source)

            kpiAndSources.append(kpiAndSource)

    return kpiAndSources


def createEventLookupTable():
    keys = createGmaKpiAndSourcesList()

    for i, kpi in enumerate(GMA_OTHER_EVENTS):
        keys.append(kpi)

    values = range(0, len(keys))

    dictionary = {k: v for k, v in zip(keys, values)}

    return dictionary