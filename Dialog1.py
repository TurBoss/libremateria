#Boa:Dialog:Dialog1

import wx
import wx.lib.hyperlink

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(3)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(444, 321), size=wx.Size(392, 101),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'A little about Libre')
        self.SetClientSize(wx.Size(384, 67))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label=u'LIBRE - LImit BReak Editor for Final Fantasy 7, PSX',
              name='staticText1', parent=self, pos=wx.Point(65, 8),
              size=wx.Size(247, 17), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label=u'Version 0.2 - Copyright Jimmy Breck-McKye, March 2010',
              name='staticText2', parent=self, pos=wx.Point(48, 40),
              size=wx.Size(280, 17), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
