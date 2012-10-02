#Boa:Dialog:Dialog2

import wx

def create(parent):
    return Dialog2(parent)

[wxID_DIALOG2, wxID_DIALOG2TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(2)]

try:
    hf = open('librehelp.txt','r')
    helptext = hf.read()
except:
    helptext = "If you can read this, Libre didn't successfully open librehelp.txt"

class Dialog2(wx.Dialog):
    def _init_ctrls(self, prnt):
        
             
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG2, name='', parent=prnt,
              pos=wx.Point(352, 180), size=wx.Size(474, 321),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Libre Help File')
        self.SetClientSize(wx.Size(474, 321))

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG2TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(8, 8), size=wx.Size(456, 304),
              style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_LINEWRAP | wx.VSCROLL,
              value= helptext)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
