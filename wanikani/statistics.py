from aqt import mw # main window
from aqt.utils import showInfo
from aqt.qt import *

def getLevel():
    """Get WaniKani level which is the highest level vocabulary in the
    learning stage. This definition differs from WaniKani by
    encouraging users to level up by completing vocab, rather than
    rushing through radicals and kanji while letting vocabulary
    lessons pile up.
    """
    model = mw.col.models.byName('WaniKani Vocabulary')
    notes = mw.col.findNotes('is:learn mid:%d' % model['id'])
    if not notes:
        notes = mw.col.findNotes('is:review mid:%d' % model['id'])
    notes = [mw.col.getNote(id) for id in notes]
    m = max(notes, key=lambda x: int(x.fields[-1]))
    level = int(m.fields[-1])
    return level

def showStatistics():
    showInfo('WaniKani Level: %d' % getLevel())

action = QAction('WaniKani statistics', mw)
action.triggered.connect(showStatistics)
mw.form.menuTools.addAction(action)
