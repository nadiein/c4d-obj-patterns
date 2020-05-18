import c4d

def main():
    def tool():
        return plugins.FindPlugin(doc.GetAction(), c4d.PLUGINTYPE_TOOL)

    def object(i=0):
        return doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN | c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)

    def tag():
        return doc.GetActiveTag()

    def renderdata():
        return doc.GetActiveRenderData()

    def prefs(id):
        return plugins.FindPlugin(id, c4d.PLUGINTYPE_PREFS)

    for i in range(10, 200, 10):
        obj = c4d.BaseObject(c4d.Odisc)
        obj.SetRelPos(c4d.Vector(0))
        obj()[c4d.PRIM_DISC_IRAD] = i - 6
        obj()[c4d.PRIM_DISC_ORAD] = i
        obj()[c4d.PRIM_DISC_CSUB] = 30
        obj()[c4d.PRIM_DISC_SEG] = 300
        obj()[c4d.PRIM_AXIS] = 4
        doc.InsertObject(obj)           # Insert object in document
        c4d.EventAdd()

    # for i in xrange(len(object())):
    #     doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, object()[i])
        # object()[0][c4d.PRIM_DISC_IRAD] = 6
        # object()[0][c4d.PRIM_DISC_ORAD] = 7
        # object()[0][c4d.PRIM_DISC_CSUB] = 30
        # object()[0][c4d.PRIM_DISC_SEG] = 300
        # object()[0][c4d.PRIM_AXIS] = 4
    #     object()[i].Message(c4d.MSG_UPDATE)

if __name__ == '__main__':
    main()
    c4d.EventAdd()