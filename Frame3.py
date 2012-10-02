#Boa:Frame:Frame2

import wx
import Dialog1
import Dialog2
import binascii

materia = ['\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']*22
mx = 0

def update(self):
    # This module reads from the ~limits list, determined by x (usually lx)
    # Data from ~limits[lx] is read, then converted into ff7_vars, each linked
    # to a particular hex character in the string.

    global materia
    
    global mx

    
    byte = 8
    materiaarray = ['']*22
    
    j = 0
    while j < 22:
        materiastring = materia[j]
            
        materiabytelist = [' ']*8
        materiabytelist2 = [' ']*8
        
        i = 0
        while i < 8:
            try:
                materiabytelist[i] = binascii.hexlify(materiastring[i*2])
                materiabytelist2[i] = int(materiabytelist[i],16)
                if (materiabytelist2[i] > 128):
                    number = int(materiabytelist2[i])
                    binary = bin(number)
                    materiabytelist2[i] = int(binary,2)-(1<<byte)
            except IndexError:
                materiabytelist[i] = 0
                materiabytelist2[i] = 0
            i = i+1
        
        #print(materiabytelist)
        materiaarray[j] = materiabytelist2
        j += 1
    #print(materiaarray)
    
    # Rellenar Tabla
    children = self.panel1.GetChildren()
    j = 0
    for child in children:
        attnumber = materiaarray[j]
        j += 1
        widget = child.GetName()
        children = child.GetChildren()
        i = 0
        for child in children:
            widget = child.GetName()
            #print widget
            child.SetValue(str(attnumber[i]))
            i += 1
    

def saver(filename,fileoffset):
    global materia
    # This module saves the file. It should be preceded in use by the updater.
    # Data is stored in limits[lx]. All we have to do is go to the file
    materiamenufile = open(filename,'r+b')
    materiamenufile.seek(fileoffset)
    
    a = 0
    while a < 22:
        b = materia[a]
        materiamenufile.write(b)
        print materia[a]
        a = a + 1
    materiamenufile.close()

def materiaLoader(filename,fileoffset):
    global materia
    # loader is a fileloader. It creates a list of limits and returns it.
    # loader goes to the offset in the chosen file, specified by filename and fileoffset
    # Then, it reads blocks of data of 28 bytes (d) length into the members of limits.
    # Reading is done in binary mode, and the file is closed at the end.
    # The returned list 'limits' will then be used by the 'updater'. offset 4900d for PSX

    materiamenufile = open(filename,'rb')
    materiamenufile.seek(fileoffset)
    
    a = 0
    while a < 22:
        materia[a] = materiamenufile.read(16)
        a = a + 1
    
    materiamenufile.close()
    #print(materia)
    return materia

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BUTTON1, wxID_FRAME2BUTTON2, wxID_FRAME2PANEL1, 
 wxID_FRAME2PANEL10, wxID_FRAME2PANEL11, wxID_FRAME2PANEL2, wxID_FRAME2PANEL3, 
 wxID_FRAME2PANEL4, wxID_FRAME2PANEL5, wxID_FRAME2PANEL6, wxID_FRAME2PANEL7, 
 wxID_FRAME2PANEL8, wxID_FRAME2PANEL9, wxID_FRAME2PANELBUTTONS, 
 wxID_FRAME2TEXTCTRL1, wxID_FRAME2TEXTCTRL10, wxID_FRAME2TEXTCTRL11, 
 wxID_FRAME2TEXTCTRL12, wxID_FRAME2TEXTCTRL13, wxID_FRAME2TEXTCTRL14, 
 wxID_FRAME2TEXTCTRL15, wxID_FRAME2TEXTCTRL16, wxID_FRAME2TEXTCTRL17, 
 wxID_FRAME2TEXTCTRL18, wxID_FRAME2TEXTCTRL19, wxID_FRAME2TEXTCTRL2, 
 wxID_FRAME2TEXTCTRL20, wxID_FRAME2TEXTCTRL21, wxID_FRAME2TEXTCTRL22, 
 wxID_FRAME2TEXTCTRL23, wxID_FRAME2TEXTCTRL24, wxID_FRAME2TEXTCTRL25, 
 wxID_FRAME2TEXTCTRL26, wxID_FRAME2TEXTCTRL27, wxID_FRAME2TEXTCTRL28, 
 wxID_FRAME2TEXTCTRL29, wxID_FRAME2TEXTCTRL3, wxID_FRAME2TEXTCTRL30, 
 wxID_FRAME2TEXTCTRL31, wxID_FRAME2TEXTCTRL32, wxID_FRAME2TEXTCTRL33, 
 wxID_FRAME2TEXTCTRL34, wxID_FRAME2TEXTCTRL35, wxID_FRAME2TEXTCTRL36, 
 wxID_FRAME2TEXTCTRL37, wxID_FRAME2TEXTCTRL38, wxID_FRAME2TEXTCTRL39, 
 wxID_FRAME2TEXTCTRL4, wxID_FRAME2TEXTCTRL40, wxID_FRAME2TEXTCTRL41, 
 wxID_FRAME2TEXTCTRL42, wxID_FRAME2TEXTCTRL43, wxID_FRAME2TEXTCTRL44, 
 wxID_FRAME2TEXTCTRL45, wxID_FRAME2TEXTCTRL46, wxID_FRAME2TEXTCTRL47, 
 wxID_FRAME2TEXTCTRL48, wxID_FRAME2TEXTCTRL49, wxID_FRAME2TEXTCTRL5, 
 wxID_FRAME2TEXTCTRL50, wxID_FRAME2TEXTCTRL51, wxID_FRAME2TEXTCTRL52, 
 wxID_FRAME2TEXTCTRL53, wxID_FRAME2TEXTCTRL54, wxID_FRAME2TEXTCTRL55, 
 wxID_FRAME2TEXTCTRL56, wxID_FRAME2TEXTCTRL57, wxID_FRAME2TEXTCTRL58, 
 wxID_FRAME2TEXTCTRL59, wxID_FRAME2TEXTCTRL6, wxID_FRAME2TEXTCTRL60, 
 wxID_FRAME2TEXTCTRL61, wxID_FRAME2TEXTCTRL62, wxID_FRAME2TEXTCTRL63, 
 wxID_FRAME2TEXTCTRL64, wxID_FRAME2TEXTCTRL65, wxID_FRAME2TEXTCTRL66, 
 wxID_FRAME2TEXTCTRL67, wxID_FRAME2TEXTCTRL68, wxID_FRAME2TEXTCTRL69, 
 wxID_FRAME2TEXTCTRL7, wxID_FRAME2TEXTCTRL70, wxID_FRAME2TEXTCTRL71, 
 wxID_FRAME2TEXTCTRL72, wxID_FRAME2TEXTCTRL73, wxID_FRAME2TEXTCTRL74, 
 wxID_FRAME2TEXTCTRL75, wxID_FRAME2TEXTCTRL76, wxID_FRAME2TEXTCTRL77, 
 wxID_FRAME2TEXTCTRL78, wxID_FRAME2TEXTCTRL79, wxID_FRAME2TEXTCTRL8, 
 wxID_FRAME2TEXTCTRL80, wxID_FRAME2TEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(95)]

class Frame2(wx.Frame):

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(385, 118), size=wx.Size(569, 500),
              style=wx.DEFAULT_FRAME_STYLE, title='Materia Attr.')
        self.SetClientSize(wx.Size(569, 500))

        self.panel1 = wx.Panel(id=wxID_FRAME2PANEL1, name='panel1', parent=self,
              pos=wx.Point(128, 16), size=wx.Size(432, 400),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_FRAME2PANEL2, name='panel2',
              parent=self.panel1, pos=wx.Point(8, 8), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel2.SetMinSize(wx.Size(200, 26))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL1, name='textCtrl1',
              parent=self.panel2, pos=wx.Point(56, 0), size=wx.Size(40, 24),
              style=0, value=u'0')
        self.textCtrl1.SetMaxLength(4)
        self.textCtrl1.SetInsertionPoint(0)
        self.textCtrl1.SetToolTipString(u'textCtrl1')
        self.textCtrl1.SetMinSize(wx.Size(40, 24))

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL2, name='textCtrl2',
              parent=self.panel2, pos=wx.Point(96, 0), size=wx.Size(40, 24),
              style=0, value=u'0')
        self.textCtrl2.SetMaxLength(4)
        self.textCtrl2.SetInsertionPoint(0)
        self.textCtrl2.SetMinSize(wx.Size(40, 24))

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL3, name='textCtrl3',
              parent=self.panel2, pos=wx.Point(136, 0), size=wx.Size(40, 24),
              style=0, value=u'0')
        self.textCtrl3.SetMaxLength(4)
        self.textCtrl3.SetInsertionPoint(0)
        self.textCtrl3.SetMinSize(wx.Size(40, 24))

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL4, name='textCtrl4',
              parent=self.panel2, pos=wx.Point(176, 0), size=wx.Size(40, 24),
              style=0, value=u'0')
        self.textCtrl4.SetMaxLength(4)
        self.textCtrl4.SetInsertionPoint(0)
        self.textCtrl4.SetMinSize(wx.Size(40, 24))

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL5, name='textCtrl5',
              parent=self.panel2, pos=wx.Point(216, 0), size=wx.Size(40, 24),
              style=0, value=u'0')
        self.textCtrl5.SetMaxLength(4)
        self.textCtrl5.SetInsertionPoint(0)
        self.textCtrl5.SetMinSize(wx.Size(40, 24))

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL6, name='textCtrl6',
              parent=self.panel2, pos=wx.Point(256, 0), size=wx.Size(40, 24),
              style=0, value=u'0')
        self.textCtrl6.SetMaxLength(4)
        self.textCtrl6.SetInsertionPoint(0)
        self.textCtrl6.SetMinSize(wx.Size(40, 24))

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL7, name='textCtrl7',
              parent=self.panel2, pos=wx.Point(296, 0), size=wx.Size(40, 24),
              style=0, value=u'0')
        self.textCtrl7.SetMaxLength(4)
        self.textCtrl7.SetInsertionPoint(0)
        self.textCtrl7.SetMinSize(wx.Size(40, 24))

        self.textCtrl8 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL8, name='textCtrl8',
              parent=self.panel2, pos=wx.Point(336, 0), size=wx.Size(40, 24),
              style=0, value=u'0')
        self.textCtrl8.SetMaxLength(4)
        self.textCtrl8.SetInsertionPoint(0)
        self.textCtrl8.SetMinSize(wx.Size(40, 24))

        self.panel3 = wx.Panel(id=wxID_FRAME2PANEL3, name='panel3',
              parent=self.panel1, pos=wx.Point(8, 32), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel3.SetMinSize(wx.Size(200, 26))

        self.textCtrl9 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL9, name='textCtrl9',
              parent=self.panel3, pos=wx.Point(56, 0), size=wx.Size(40, 24),
              style=0, value=u'0')
        self.textCtrl9.SetMaxLength(4)
        self.textCtrl9.SetInsertionPoint(0)
        self.textCtrl9.SetMinSize(wx.Size(40, 24))

        self.textCtrl10 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL10,
              name='textCtrl10', parent=self.panel3, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl10.SetMaxLength(4)
        self.textCtrl10.SetInsertionPoint(0)
        self.textCtrl10.SetMinSize(wx.Size(40, 24))

        self.textCtrl11 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL11,
              name='textCtrl11', parent=self.panel3, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl11.SetMaxLength(4)
        self.textCtrl11.SetInsertionPoint(0)
        self.textCtrl11.SetMinSize(wx.Size(40, 24))

        self.textCtrl12 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL12,
              name='textCtrl12', parent=self.panel3, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl12.SetMaxLength(4)
        self.textCtrl12.SetInsertionPoint(0)
        self.textCtrl12.SetMinSize(wx.Size(40, 24))

        self.textCtrl13 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL13,
              name='textCtrl13', parent=self.panel3, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl13.SetMaxLength(4)
        self.textCtrl13.SetInsertionPoint(0)
        self.textCtrl13.SetMinSize(wx.Size(40, 24))

        self.textCtrl14 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL14,
              name='textCtrl14', parent=self.panel3, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl14.SetMaxLength(4)
        self.textCtrl14.SetInsertionPoint(0)
        self.textCtrl14.SetMinSize(wx.Size(40, 24))

        self.textCtrl15 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL15,
              name='textCtrl15', parent=self.panel3, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl15.SetMaxLength(4)
        self.textCtrl15.SetInsertionPoint(0)
        self.textCtrl15.SetMinSize(wx.Size(40, 24))

        self.textCtrl16 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL16,
              name='textCtrl16', parent=self.panel3, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl16.SetMaxLength(4)
        self.textCtrl16.SetInsertionPoint(0)
        self.textCtrl16.SetToolTipString(u'textCtrl1')
        self.textCtrl16.SetMinSize(wx.Size(40, 24))

        self.panel4 = wx.Panel(id=wxID_FRAME2PANEL4, name='panel4',
              parent=self.panel1, pos=wx.Point(8, 56), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel4.SetMinSize(wx.Size(200, 26))

        self.textCtrl17 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL17,
              name='textCtrl17', parent=self.panel4, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl17.SetMaxLength(4)
        self.textCtrl17.SetInsertionPoint(0)
        self.textCtrl17.SetMinSize(wx.Size(40, 24))

        self.textCtrl18 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL18,
              name='textCtrl18', parent=self.panel4, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl18.SetMaxLength(4)
        self.textCtrl18.SetInsertionPoint(0)
        self.textCtrl18.SetToolTipString(u'textCtrl1')
        self.textCtrl18.SetMinSize(wx.Size(40, 24))

        self.textCtrl19 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL19,
              name='textCtrl19', parent=self.panel4, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl19.SetMaxLength(4)
        self.textCtrl19.SetInsertionPoint(0)
        self.textCtrl19.SetMinSize(wx.Size(40, 24))

        self.textCtrl20 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL20,
              name='textCtrl20', parent=self.panel4, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl20.SetMaxLength(4)
        self.textCtrl20.SetInsertionPoint(0)
        self.textCtrl20.SetMinSize(wx.Size(40, 24))

        self.textCtrl21 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL21,
              name='textCtrl21', parent=self.panel4, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl21.SetMaxLength(4)
        self.textCtrl21.SetInsertionPoint(0)
        self.textCtrl21.SetMinSize(wx.Size(40, 24))

        self.textCtrl22 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL22,
              name='textCtrl22', parent=self.panel4, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl22.SetMaxLength(4)
        self.textCtrl22.SetInsertionPoint(0)
        self.textCtrl22.SetMinSize(wx.Size(40, 24))

        self.textCtrl23 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL23,
              name='textCtrl23', parent=self.panel4, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl23.SetMaxLength(4)
        self.textCtrl23.SetInsertionPoint(0)
        self.textCtrl23.SetMinSize(wx.Size(40, 24))

        self.textCtrl24 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL24,
              name='textCtrl24', parent=self.panel4, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl24.SetMaxLength(4)
        self.textCtrl24.SetInsertionPoint(0)
        self.textCtrl24.SetMinSize(wx.Size(40, 24))

        self.panelButtons = wx.Panel(id=wxID_FRAME2PANELBUTTONS,
              name=u'panelButtons', parent=self, pos=wx.Point(8, 16),
              size=wx.Size(112, 72), style=wx.TAB_TRAVERSAL)

        self.button2 = wx.Button(id=wxID_FRAME2BUTTON2, label=u'SAVE',
              name='button2', parent=self.panelButtons, pos=wx.Point(0, 32),
              size=wx.Size(104, 32), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME2BUTTON2)

        self.button1 = wx.Button(id=wxID_FRAME2BUTTON1, label=u'LOAD',
              name='button1', parent=self.panelButtons, pos=wx.Point(0, 0),
              size=wx.Size(104, 32), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME2BUTTON1)

        self.panel5 = wx.Panel(id=wxID_FRAME2PANEL5, name=u'panel5',
              parent=self.panel1, pos=wx.Point(8, 80), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel5.SetMinSize(wx.Size(200, 26))

        self.textCtrl25 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL25,
              name='textCtrl25', parent=self.panel5, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl25.SetMaxLength(4)
        self.textCtrl25.SetInsertionPoint(0)
        self.textCtrl25.SetMinSize(wx.Size(40, 24))

        self.textCtrl26 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL26,
              name='textCtrl26', parent=self.panel5, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl26.SetMaxLength(4)
        self.textCtrl26.SetInsertionPoint(0)
        self.textCtrl26.SetMinSize(wx.Size(40, 24))

        self.textCtrl27 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL27,
              name='textCtrl27', parent=self.panel5, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl27.SetMaxLength(4)
        self.textCtrl27.SetInsertionPoint(0)
        self.textCtrl27.SetMinSize(wx.Size(40, 24))

        self.textCtrl28 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL28,
              name='textCtrl28', parent=self.panel5, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl28.SetMaxLength(4)
        self.textCtrl28.SetInsertionPoint(0)
        self.textCtrl28.SetMinSize(wx.Size(40, 24))

        self.textCtrl29 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL29,
              name='textCtrl29', parent=self.panel5, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl29.SetMaxLength(4)
        self.textCtrl29.SetInsertionPoint(0)
        self.textCtrl29.SetMinSize(wx.Size(40, 24))

        self.textCtrl30 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL30,
              name='textCtrl30', parent=self.panel5, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl30.SetMaxLength(4)
        self.textCtrl30.SetInsertionPoint(0)
        self.textCtrl30.SetMinSize(wx.Size(40, 24))

        self.textCtrl31 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL31,
              name='textCtrl31', parent=self.panel5, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl31.SetMaxLength(4)
        self.textCtrl31.SetInsertionPoint(0)
        self.textCtrl31.SetToolTipString(u'textCtrl1')
        self.textCtrl31.SetMinSize(wx.Size(40, 24))

        self.textCtrl32 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL32,
              name='textCtrl32', parent=self.panel5, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl32.SetMaxLength(4)
        self.textCtrl32.SetInsertionPoint(0)
        self.textCtrl32.SetMinSize(wx.Size(40, 24))

        self.panel6 = wx.Panel(id=wxID_FRAME2PANEL6, name='panel6',
              parent=self.panel1, pos=wx.Point(8, 104), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel6.SetMinSize(wx.Size(200, 26))

        self.textCtrl33 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL33,
              name='textCtrl33', parent=self.panel6, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl33.SetMaxLength(4)
        self.textCtrl33.SetInsertionPoint(0)
        self.textCtrl33.SetMinSize(wx.Size(40, 24))

        self.textCtrl34 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL34,
              name='textCtrl34', parent=self.panel6, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl34.SetMaxLength(4)
        self.textCtrl34.SetInsertionPoint(0)
        self.textCtrl34.SetMinSize(wx.Size(40, 24))

        self.textCtrl35 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL35,
              name='textCtrl35', parent=self.panel6, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl35.SetMaxLength(4)
        self.textCtrl35.SetInsertionPoint(0)
        self.textCtrl35.SetMinSize(wx.Size(40, 24))

        self.textCtrl36 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL36,
              name='textCtrl36', parent=self.panel6, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl36.SetMaxLength(4)
        self.textCtrl36.SetInsertionPoint(0)
        self.textCtrl36.SetMinSize(wx.Size(40, 24))

        self.textCtrl37 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL37,
              name='textCtrl37', parent=self.panel6, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl37.SetMaxLength(4)
        self.textCtrl37.SetInsertionPoint(0)
        self.textCtrl37.SetMinSize(wx.Size(40, 24))

        self.textCtrl38 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL38,
              name='textCtrl38', parent=self.panel6, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl38.SetMaxLength(4)
        self.textCtrl38.SetInsertionPoint(0)
        self.textCtrl38.SetMinSize(wx.Size(40, 24))

        self.textCtrl39 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL39,
              name='textCtrl39', parent=self.panel6, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl39.SetMaxLength(4)
        self.textCtrl39.SetInsertionPoint(0)
        self.textCtrl39.SetToolTipString(u'textCtrl1')
        self.textCtrl39.SetMinSize(wx.Size(40, 24))

        self.textCtrl40 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL40,
              name='textCtrl40', parent=self.panel6, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl40.SetMaxLength(4)
        self.textCtrl40.SetInsertionPoint(0)
        self.textCtrl40.SetMinSize(wx.Size(40, 24))

        self.panel7 = wx.Panel(id=wxID_FRAME2PANEL7, name='panel7',
              parent=self.panel1, pos=wx.Point(8, 128), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel7.SetMinSize(wx.Size(200, 26))

        self.textCtrl41 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL41,
              name='textCtrl41', parent=self.panel7, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl41.SetMaxLength(4)
        self.textCtrl41.SetInsertionPoint(0)
        self.textCtrl41.SetMinSize(wx.Size(40, 24))

        self.textCtrl42 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL42,
              name='textCtrl42', parent=self.panel7, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl42.SetMaxLength(4)
        self.textCtrl42.SetInsertionPoint(0)
        self.textCtrl42.SetMinSize(wx.Size(40, 24))

        self.textCtrl43 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL43,
              name='textCtrl43', parent=self.panel7, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl43.SetMaxLength(4)
        self.textCtrl43.SetInsertionPoint(0)
        self.textCtrl43.SetMinSize(wx.Size(40, 24))

        self.textCtrl44 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL44,
              name='textCtrl44', parent=self.panel7, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl44.SetMaxLength(4)
        self.textCtrl44.SetInsertionPoint(0)
        self.textCtrl44.SetMinSize(wx.Size(40, 24))

        self.textCtrl45 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL45,
              name='textCtrl45', parent=self.panel7, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl45.SetMaxLength(4)
        self.textCtrl45.SetInsertionPoint(0)
        self.textCtrl45.SetMinSize(wx.Size(40, 24))

        self.textCtrl46 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL46,
              name='textCtrl46', parent=self.panel7, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl46.SetMaxLength(4)
        self.textCtrl46.SetInsertionPoint(0)
        self.textCtrl46.SetMinSize(wx.Size(40, 24))

        self.textCtrl47 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL47,
              name='textCtrl47', parent=self.panel7, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl47.SetMaxLength(4)
        self.textCtrl47.SetInsertionPoint(0)
        self.textCtrl47.SetToolTipString(u'textCtrl1')
        self.textCtrl47.SetMinSize(wx.Size(40, 24))

        self.textCtrl48 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL48,
              name='textCtrl48', parent=self.panel7, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl48.SetMaxLength(4)
        self.textCtrl48.SetInsertionPoint(0)
        self.textCtrl48.SetMinSize(wx.Size(40, 24))

        self.panel8 = wx.Panel(id=wxID_FRAME2PANEL8, name='panel8',
              parent=self.panel1, pos=wx.Point(8, 152), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel8.SetMinSize(wx.Size(200, 26))

        self.textCtrl49 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL49,
              name='textCtrl49', parent=self.panel8, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl49.SetMaxLength(4)
        self.textCtrl49.SetInsertionPoint(0)
        self.textCtrl49.SetMinSize(wx.Size(40, 24))

        self.textCtrl50 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL50,
              name='textCtrl50', parent=self.panel8, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl50.SetMaxLength(4)
        self.textCtrl50.SetInsertionPoint(0)
        self.textCtrl50.SetMinSize(wx.Size(40, 24))

        self.textCtrl51 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL51,
              name='textCtrl51', parent=self.panel8, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl51.SetMaxLength(4)
        self.textCtrl51.SetInsertionPoint(0)
        self.textCtrl51.SetMinSize(wx.Size(40, 24))

        self.textCtrl52 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL52,
              name='textCtrl52', parent=self.panel8, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl52.SetMaxLength(4)
        self.textCtrl52.SetInsertionPoint(0)
        self.textCtrl52.SetMinSize(wx.Size(40, 24))

        self.textCtrl53 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL53,
              name='textCtrl53', parent=self.panel8, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl53.SetMaxLength(4)
        self.textCtrl53.SetInsertionPoint(0)
        self.textCtrl53.SetToolTipString(u'textCtrl1')
        self.textCtrl53.SetMinSize(wx.Size(40, 24))

        self.textCtrl54 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL54,
              name='textCtrl54', parent=self.panel8, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl54.SetMaxLength(4)
        self.textCtrl54.SetInsertionPoint(0)
        self.textCtrl54.SetMinSize(wx.Size(40, 24))

        self.textCtrl55 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL55,
              name='textCtrl55', parent=self.panel8, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl55.SetMaxLength(4)
        self.textCtrl55.SetInsertionPoint(0)
        self.textCtrl55.SetMinSize(wx.Size(40, 24))

        self.textCtrl56 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL56,
              name='textCtrl56', parent=self.panel8, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl56.SetMaxLength(4)
        self.textCtrl56.SetInsertionPoint(0)
        self.textCtrl56.SetMinSize(wx.Size(40, 24))

        self.panel9 = wx.Panel(id=wxID_FRAME2PANEL9, name='panel9',
              parent=self.panel1, pos=wx.Point(8, 176), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel9.SetMinSize(wx.Size(200, 26))

        self.textCtrl57 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL57,
              name='textCtrl57', parent=self.panel9, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl57.SetMaxLength(4)
        self.textCtrl57.SetInsertionPoint(0)
        self.textCtrl57.SetToolTipString(u'textCtrl1')
        self.textCtrl57.SetMinSize(wx.Size(40, 24))

        self.textCtrl58 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL58,
              name='textCtrl58', parent=self.panel9, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl58.SetMaxLength(4)
        self.textCtrl58.SetInsertionPoint(0)
        self.textCtrl58.SetMinSize(wx.Size(40, 24))

        self.textCtrl59 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL59,
              name='textCtrl59', parent=self.panel9, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl59.SetMaxLength(4)
        self.textCtrl59.SetInsertionPoint(0)
        self.textCtrl59.SetMinSize(wx.Size(40, 24))

        self.textCtrl60 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL60,
              name='textCtrl60', parent=self.panel9, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl60.SetMaxLength(4)
        self.textCtrl60.SetInsertionPoint(0)
        self.textCtrl60.SetMinSize(wx.Size(40, 24))

        self.textCtrl61 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL61,
              name='textCtrl61', parent=self.panel9, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl61.SetMaxLength(4)
        self.textCtrl61.SetInsertionPoint(0)
        self.textCtrl61.SetMinSize(wx.Size(40, 24))

        self.textCtrl62 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL62,
              name='textCtrl62', parent=self.panel9, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl62.SetMaxLength(4)
        self.textCtrl62.SetInsertionPoint(0)
        self.textCtrl62.SetMinSize(wx.Size(40, 24))

        self.textCtrl63 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL63,
              name='textCtrl63', parent=self.panel9, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl63.SetMaxLength(4)
        self.textCtrl63.SetInsertionPoint(0)
        self.textCtrl63.SetMinSize(wx.Size(40, 24))

        self.textCtrl64 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL64,
              name='textCtrl64', parent=self.panel9, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl64.SetMaxLength(4)
        self.textCtrl64.SetInsertionPoint(0)
        self.textCtrl64.SetMinSize(wx.Size(40, 24))

        self.panel10 = wx.Panel(id=wxID_FRAME2PANEL10, name='panel10',
              parent=self.panel1, pos=wx.Point(8, 200), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel10.SetMinSize(wx.Size(200, 26))

        self.textCtrl65 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL65,
              name='textCtrl65', parent=self.panel10, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl65.SetMaxLength(4)
        self.textCtrl65.SetInsertionPoint(0)
        self.textCtrl65.SetMinSize(wx.Size(40, 24))

        self.textCtrl66 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL66,
              name='textCtrl66', parent=self.panel10, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl66.SetMaxLength(4)
        self.textCtrl66.SetInsertionPoint(0)
        self.textCtrl66.SetToolTipString(u'textCtrl1')
        self.textCtrl66.SetMinSize(wx.Size(40, 24))

        self.textCtrl67 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL67,
              name='textCtrl67', parent=self.panel10, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl67.SetMaxLength(4)
        self.textCtrl67.SetInsertionPoint(0)
        self.textCtrl67.SetMinSize(wx.Size(40, 24))

        self.textCtrl68 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL68,
              name='textCtrl68', parent=self.panel10, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl68.SetMaxLength(4)
        self.textCtrl68.SetInsertionPoint(0)
        self.textCtrl68.SetMinSize(wx.Size(40, 24))

        self.textCtrl69 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL69,
              name='textCtrl69', parent=self.panel10, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl69.SetMaxLength(4)
        self.textCtrl69.SetInsertionPoint(0)
        self.textCtrl69.SetMinSize(wx.Size(40, 24))

        self.textCtrl70 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL70,
              name='textCtrl70', parent=self.panel10, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl70.SetMaxLength(4)
        self.textCtrl70.SetInsertionPoint(0)
        self.textCtrl70.SetMinSize(wx.Size(40, 24))

        self.textCtrl71 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL71,
              name='textCtrl71', parent=self.panel10, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl71.SetMaxLength(4)
        self.textCtrl71.SetInsertionPoint(0)
        self.textCtrl71.SetMinSize(wx.Size(40, 24))

        self.textCtrl72 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL72,
              name='textCtrl72', parent=self.panel10, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl72.SetMaxLength(4)
        self.textCtrl72.SetInsertionPoint(0)
        self.textCtrl72.SetMinSize(wx.Size(40, 24))

        self.panel11 = wx.Panel(id=wxID_FRAME2PANEL11, name='panel11',
              parent=self.panel1, pos=wx.Point(8, 224), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel11.SetMinSize(wx.Size(200, 26))

        self.textCtrl73 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL73,
              name='textCtrl73', parent=self.panel11, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl73.SetMaxLength(4)
        self.textCtrl73.SetInsertionPoint(0)
        self.textCtrl73.SetMinSize(wx.Size(40, 24))

        self.textCtrl74 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL74,
              name='textCtrl74', parent=self.panel11, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl74.SetMaxLength(4)
        self.textCtrl74.SetInsertionPoint(0)
        self.textCtrl74.SetMinSize(wx.Size(40, 24))

        self.textCtrl75 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL75,
              name='textCtrl75', parent=self.panel11, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl75.SetMaxLength(4)
        self.textCtrl75.SetInsertionPoint(0)
        self.textCtrl75.SetMinSize(wx.Size(40, 24))

        self.textCtrl76 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL76,
              name='textCtrl76', parent=self.panel11, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl76.SetMaxLength(4)
        self.textCtrl76.SetInsertionPoint(0)
        self.textCtrl76.SetMinSize(wx.Size(40, 24))

        self.textCtrl77 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL77,
              name='textCtrl77', parent=self.panel11, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl77.SetMaxLength(4)
        self.textCtrl77.SetInsertionPoint(0)
        self.textCtrl77.SetMinSize(wx.Size(40, 24))

        self.textCtrl78 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL78,
              name='textCtrl78', parent=self.panel11, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl78.SetMaxLength(4)
        self.textCtrl78.SetInsertionPoint(0)
        self.textCtrl78.SetToolTipString(u'textCtrl1')
        self.textCtrl78.SetMinSize(wx.Size(40, 24))

        self.textCtrl79 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL79,
              name='textCtrl79', parent=self.panel11, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl79.SetMaxLength(4)
        self.textCtrl79.SetInsertionPoint(0)
        self.textCtrl79.SetMinSize(wx.Size(40, 24))

        self.textCtrl80 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL80,
              name='textCtrl80', parent=self.panel11, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl80.SetMaxLength(4)
        self.textCtrl80.SetInsertionPoint(0)
        self.textCtrl80.SetMinSize(wx.Size(40, 24))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        dlg = wx.FileDialog(self, 'Choose a PC FF7.EXE file', '.', '', '*.exe', wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                materia = [' ']*22
                materia = materiaLoader(filename,5232840)
                global mx
                mx = 0
                update(self)
        finally:
            dlg.Destroy()
        event.Skip()

    def OnButton2Button(self, event):
        dlg = wx.FileDialog(self, 'Save to PC FF7.exe', '.', '', '*.exe', wx.SAVE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                materia=downdate(self)
                saver(filename,5232840)
                
        finally:
            dlg.Destroy()
        event.Skip()
