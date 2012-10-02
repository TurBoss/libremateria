#Boa:Frame:Frame2

import wx
import array
import binascii

import Dialog1
import Dialog2

materia = ['\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']*22
mx = 0

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

def update(self):
    # This module reads from the ~limits list, determined by x (usually lx)
    # Data from ~limits[lx] is read, then converted into ff7_vars, each linked
    # to a particular hex character in the string.

    global materia
    
    global mx

    
    byte = 8
    materiaarray = ['\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']*22
    
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

def downdate(self):
    # This module does the opposite of update. It polls the gui controls
    # for data, which it turns into decimal data in a datalist list.
    # This is then parsed into a hex string, limitstring,
    # before being pushed into limits[lx].
    global materia
    global mx
    
    materiaData = ['\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']*22
    
    # Leer Tabla
    children = self.panel1.GetChildren()
    j = 0
    for child in children:
        widget = child.GetName()
        children = child.GetChildren()
        
        attnumber = ['']*8
        materiaAtt = ['']*16
        materiaLol = ['']*16

        i = 0
        for child in children:
            widget = child.GetName()
            attnumber[i] = int(child.GetValue())
            #print(attnumber[i])
            if (attnumber[i] >= 0)&(attnumber[i] <= 128):
                materiaAtt[i*2] = attnumber[i]
                materiaAtt[i*2+1] = 0
            else:
                
                number = int(attnumber[i])
                number += 256
                
                materiaAtt[i*2] = number
                materiaAtt[i*2+1] = 255
                
            
            i += 1
        
        #print(materiaAtt)
        materiaData[j] = array.array('B', materiaAtt).tostring()
        
        #materiaData[j] = materiaAtt
        
        #materiaData[j] = ''.join(materiaAtt)
        #print("JOIN")
        #print(materiaData[j])
        #materiaData[j] = materiaData[j].split()
        #materiaData[i] = array.array('B', materiaAtt[i]).tostring()
        #materiaData[i*2] = array.array('B', materiaAtt[i*2]).tostring()
            
        j += 1
    
    
    #print('############')
    #print(materiaData)
    #print('############')
    
    
    materia = materiaData
        
    return materia

def saver(filename,fileoffset):
    #print("~~~~~~~~~~~~~~~~~~~~~~~")
    global materia
    # This module saves the file. It should be preceded in use by the updater.
    # Data is stored in limits[lx]. All we have to do is go to the file
    materiamenufile = open(filename,'r+b')
    materiamenufile.seek(fileoffset)
    
    a = 0
    while a < 22:
        b = str(materia[a])
        materiamenufile.write(b)
        a +=1
    materiamenufile.close()
    #print("SAVED")

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BUTTON1, wxID_FRAME2BUTTON2, wxID_FRAME2PANEL1, 
 wxID_FRAME2PANEL10, wxID_FRAME2PANEL11, wxID_FRAME2PANEL12, 
 wxID_FRAME2PANEL13, wxID_FRAME2PANEL14, wxID_FRAME2PANEL15, 
 wxID_FRAME2PANEL16, wxID_FRAME2PANEL17, wxID_FRAME2PANEL18, 
 wxID_FRAME2PANEL19, wxID_FRAME2PANEL2, wxID_FRAME2PANEL20, 
 wxID_FRAME2PANEL21, wxID_FRAME2PANEL22, wxID_FRAME2PANEL23, 
 wxID_FRAME2PANEL24, wxID_FRAME2PANEL3, wxID_FRAME2PANEL4, wxID_FRAME2PANEL5, 
 wxID_FRAME2PANEL6, wxID_FRAME2PANEL7, wxID_FRAME2PANEL8, wxID_FRAME2PANEL9, 
 wxID_FRAME2PANELBUTTONS, wxID_FRAME2STATICTEXT8, wxID_FRAME2TEXTCTRL1, 
 wxID_FRAME2TEXTCTRL10, wxID_FRAME2TEXTCTRL100, wxID_FRAME2TEXTCTRL101, 
 wxID_FRAME2TEXTCTRL102, wxID_FRAME2TEXTCTRL103, wxID_FRAME2TEXTCTRL104, 
 wxID_FRAME2TEXTCTRL105, wxID_FRAME2TEXTCTRL106, wxID_FRAME2TEXTCTRL107, 
 wxID_FRAME2TEXTCTRL108, wxID_FRAME2TEXTCTRL109, wxID_FRAME2TEXTCTRL11, 
 wxID_FRAME2TEXTCTRL110, wxID_FRAME2TEXTCTRL111, wxID_FRAME2TEXTCTRL112, 
 wxID_FRAME2TEXTCTRL113, wxID_FRAME2TEXTCTRL114, wxID_FRAME2TEXTCTRL115, 
 wxID_FRAME2TEXTCTRL116, wxID_FRAME2TEXTCTRL117, wxID_FRAME2TEXTCTRL118, 
 wxID_FRAME2TEXTCTRL119, wxID_FRAME2TEXTCTRL12, wxID_FRAME2TEXTCTRL120, 
 wxID_FRAME2TEXTCTRL121, wxID_FRAME2TEXTCTRL122, wxID_FRAME2TEXTCTRL123, 
 wxID_FRAME2TEXTCTRL124, wxID_FRAME2TEXTCTRL125, wxID_FRAME2TEXTCTRL126, 
 wxID_FRAME2TEXTCTRL127, wxID_FRAME2TEXTCTRL128, wxID_FRAME2TEXTCTRL129, 
 wxID_FRAME2TEXTCTRL13, wxID_FRAME2TEXTCTRL130, wxID_FRAME2TEXTCTRL131, 
 wxID_FRAME2TEXTCTRL132, wxID_FRAME2TEXTCTRL133, wxID_FRAME2TEXTCTRL134, 
 wxID_FRAME2TEXTCTRL135, wxID_FRAME2TEXTCTRL136, wxID_FRAME2TEXTCTRL137, 
 wxID_FRAME2TEXTCTRL138, wxID_FRAME2TEXTCTRL139, wxID_FRAME2TEXTCTRL14, 
 wxID_FRAME2TEXTCTRL140, wxID_FRAME2TEXTCTRL141, wxID_FRAME2TEXTCTRL142, 
 wxID_FRAME2TEXTCTRL143, wxID_FRAME2TEXTCTRL144, wxID_FRAME2TEXTCTRL145, 
 wxID_FRAME2TEXTCTRL146, wxID_FRAME2TEXTCTRL147, wxID_FRAME2TEXTCTRL148, 
 wxID_FRAME2TEXTCTRL149, wxID_FRAME2TEXTCTRL15, wxID_FRAME2TEXTCTRL150, 
 wxID_FRAME2TEXTCTRL151, wxID_FRAME2TEXTCTRL152, wxID_FRAME2TEXTCTRL153, 
 wxID_FRAME2TEXTCTRL154, wxID_FRAME2TEXTCTRL155, wxID_FRAME2TEXTCTRL156, 
 wxID_FRAME2TEXTCTRL157, wxID_FRAME2TEXTCTRL158, wxID_FRAME2TEXTCTRL159, 
 wxID_FRAME2TEXTCTRL16, wxID_FRAME2TEXTCTRL160, wxID_FRAME2TEXTCTRL161, 
 wxID_FRAME2TEXTCTRL162, wxID_FRAME2TEXTCTRL163, wxID_FRAME2TEXTCTRL164, 
 wxID_FRAME2TEXTCTRL165, wxID_FRAME2TEXTCTRL166, wxID_FRAME2TEXTCTRL167, 
 wxID_FRAME2TEXTCTRL168, wxID_FRAME2TEXTCTRL169, wxID_FRAME2TEXTCTRL17, 
 wxID_FRAME2TEXTCTRL170, wxID_FRAME2TEXTCTRL171, wxID_FRAME2TEXTCTRL172, 
 wxID_FRAME2TEXTCTRL173, wxID_FRAME2TEXTCTRL174, wxID_FRAME2TEXTCTRL175, 
 wxID_FRAME2TEXTCTRL176, wxID_FRAME2TEXTCTRL18, wxID_FRAME2TEXTCTRL19, 
 wxID_FRAME2TEXTCTRL2, wxID_FRAME2TEXTCTRL20, wxID_FRAME2TEXTCTRL21, 
 wxID_FRAME2TEXTCTRL22, wxID_FRAME2TEXTCTRL23, wxID_FRAME2TEXTCTRL24, 
 wxID_FRAME2TEXTCTRL25, wxID_FRAME2TEXTCTRL26, wxID_FRAME2TEXTCTRL27, 
 wxID_FRAME2TEXTCTRL28, wxID_FRAME2TEXTCTRL29, wxID_FRAME2TEXTCTRL3, 
 wxID_FRAME2TEXTCTRL30, wxID_FRAME2TEXTCTRL31, wxID_FRAME2TEXTCTRL32, 
 wxID_FRAME2TEXTCTRL33, wxID_FRAME2TEXTCTRL34, wxID_FRAME2TEXTCTRL35, 
 wxID_FRAME2TEXTCTRL36, wxID_FRAME2TEXTCTRL37, wxID_FRAME2TEXTCTRL38, 
 wxID_FRAME2TEXTCTRL39, wxID_FRAME2TEXTCTRL4, wxID_FRAME2TEXTCTRL40, 
 wxID_FRAME2TEXTCTRL41, wxID_FRAME2TEXTCTRL42, wxID_FRAME2TEXTCTRL43, 
 wxID_FRAME2TEXTCTRL44, wxID_FRAME2TEXTCTRL45, wxID_FRAME2TEXTCTRL46, 
 wxID_FRAME2TEXTCTRL47, wxID_FRAME2TEXTCTRL48, wxID_FRAME2TEXTCTRL49, 
 wxID_FRAME2TEXTCTRL5, wxID_FRAME2TEXTCTRL50, wxID_FRAME2TEXTCTRL51, 
 wxID_FRAME2TEXTCTRL52, wxID_FRAME2TEXTCTRL53, wxID_FRAME2TEXTCTRL54, 
 wxID_FRAME2TEXTCTRL55, wxID_FRAME2TEXTCTRL56, wxID_FRAME2TEXTCTRL57, 
 wxID_FRAME2TEXTCTRL58, wxID_FRAME2TEXTCTRL59, wxID_FRAME2TEXTCTRL6, 
 wxID_FRAME2TEXTCTRL60, wxID_FRAME2TEXTCTRL61, wxID_FRAME2TEXTCTRL62, 
 wxID_FRAME2TEXTCTRL63, wxID_FRAME2TEXTCTRL64, wxID_FRAME2TEXTCTRL65, 
 wxID_FRAME2TEXTCTRL66, wxID_FRAME2TEXTCTRL67, wxID_FRAME2TEXTCTRL68, 
 wxID_FRAME2TEXTCTRL69, wxID_FRAME2TEXTCTRL7, wxID_FRAME2TEXTCTRL70, 
 wxID_FRAME2TEXTCTRL71, wxID_FRAME2TEXTCTRL72, wxID_FRAME2TEXTCTRL73, 
 wxID_FRAME2TEXTCTRL74, wxID_FRAME2TEXTCTRL75, wxID_FRAME2TEXTCTRL76, 
 wxID_FRAME2TEXTCTRL77, wxID_FRAME2TEXTCTRL78, wxID_FRAME2TEXTCTRL79, 
 wxID_FRAME2TEXTCTRL8, wxID_FRAME2TEXTCTRL80, wxID_FRAME2TEXTCTRL81, 
 wxID_FRAME2TEXTCTRL82, wxID_FRAME2TEXTCTRL83, wxID_FRAME2TEXTCTRL84, 
 wxID_FRAME2TEXTCTRL85, wxID_FRAME2TEXTCTRL86, wxID_FRAME2TEXTCTRL87, 
 wxID_FRAME2TEXTCTRL88, wxID_FRAME2TEXTCTRL89, wxID_FRAME2TEXTCTRL9, 
 wxID_FRAME2TEXTCTRL90, wxID_FRAME2TEXTCTRL91, wxID_FRAME2TEXTCTRL92, 
 wxID_FRAME2TEXTCTRL93, wxID_FRAME2TEXTCTRL94, wxID_FRAME2TEXTCTRL95, 
 wxID_FRAME2TEXTCTRL96, wxID_FRAME2TEXTCTRL97, wxID_FRAME2TEXTCTRL98, 
 wxID_FRAME2TEXTCTRL99, 
] = [wx.NewId() for _init_ctrls in range(205)]

class Frame2(wx.Frame):

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(545, 89), size=wx.Size(523, 594),
              style=wx.DEFAULT_FRAME_STYLE, title='Materia Attr.')
        self.SetClientSize(wx.Size(523, 594))

        self.panel1 = wx.Panel(id=wxID_FRAME2PANEL1, name='panel1', parent=self,
              pos=wx.Point(136, 24), size=wx.Size(432, 544),
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
              size=wx.Size(112, 416), style=wx.TAB_TRAVERSAL)

        self.button2 = wx.Button(id=wxID_FRAME2BUTTON2, label=u'Save',
              name='button2', parent=self.panelButtons, pos=wx.Point(0, 56),
              size=wx.Size(104, 40), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME2BUTTON2)

        self.button1 = wx.Button(id=wxID_FRAME2BUTTON1, label=u'Load',
              name='button1', parent=self.panelButtons, pos=wx.Point(0, 0),
              size=wx.Size(104, 40), style=0)
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

        self.panel12 = wx.Panel(id=wxID_FRAME2PANEL12, name='panel12',
              parent=self.panel1, pos=wx.Point(8, 248), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel12.SetMinSize(wx.Size(200, 26))

        self.textCtrl81 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL81,
              name='textCtrl81', parent=self.panel12, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl81.SetMaxLength(4)
        self.textCtrl81.SetInsertionPoint(0)
        self.textCtrl81.SetMinSize(wx.Size(40, 24))

        self.textCtrl82 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL82,
              name='textCtrl82', parent=self.panel12, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl82.SetMaxLength(4)
        self.textCtrl82.SetInsertionPoint(0)
        self.textCtrl82.SetMinSize(wx.Size(40, 24))

        self.textCtrl83 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL83,
              name='textCtrl83', parent=self.panel12, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl83.SetMaxLength(4)
        self.textCtrl83.SetInsertionPoint(0)
        self.textCtrl83.SetMinSize(wx.Size(40, 24))

        self.textCtrl84 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL84,
              name='textCtrl84', parent=self.panel12, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl84.SetMaxLength(4)
        self.textCtrl84.SetInsertionPoint(0)
        self.textCtrl84.SetMinSize(wx.Size(40, 24))

        self.textCtrl85 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL85,
              name='textCtrl85', parent=self.panel12, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl85.SetMaxLength(4)
        self.textCtrl85.SetInsertionPoint(0)
        self.textCtrl85.SetMinSize(wx.Size(40, 24))

        self.textCtrl86 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL86,
              name='textCtrl86', parent=self.panel12, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl86.SetMaxLength(4)
        self.textCtrl86.SetInsertionPoint(0)
        self.textCtrl86.SetToolTipString(u'textCtrl1')
        self.textCtrl86.SetMinSize(wx.Size(40, 24))

        self.textCtrl87 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL87,
              name='textCtrl87', parent=self.panel12, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl87.SetMaxLength(4)
        self.textCtrl87.SetInsertionPoint(0)
        self.textCtrl87.SetMinSize(wx.Size(40, 24))

        self.textCtrl88 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL88,
              name='textCtrl88', parent=self.panel12, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl88.SetMaxLength(4)
        self.textCtrl88.SetInsertionPoint(0)
        self.textCtrl88.SetMinSize(wx.Size(40, 24))

        self.panel13 = wx.Panel(id=wxID_FRAME2PANEL13, name='panel13',
              parent=self.panel1, pos=wx.Point(8, 272), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel13.SetMinSize(wx.Size(200, 26))

        self.textCtrl89 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL89,
              name='textCtrl89', parent=self.panel13, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl89.SetMaxLength(4)
        self.textCtrl89.SetInsertionPoint(0)
        self.textCtrl89.SetMinSize(wx.Size(40, 24))

        self.textCtrl90 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL90,
              name='textCtrl90', parent=self.panel13, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl90.SetMaxLength(4)
        self.textCtrl90.SetInsertionPoint(0)
        self.textCtrl90.SetToolTipString(u'textCtrl1')
        self.textCtrl90.SetMinSize(wx.Size(40, 24))

        self.textCtrl91 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL91,
              name='textCtrl91', parent=self.panel13, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl91.SetMaxLength(4)
        self.textCtrl91.SetInsertionPoint(0)
        self.textCtrl91.SetMinSize(wx.Size(40, 24))

        self.textCtrl92 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL92,
              name='textCtrl92', parent=self.panel13, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl92.SetMaxLength(4)
        self.textCtrl92.SetInsertionPoint(0)
        self.textCtrl92.SetMinSize(wx.Size(40, 24))

        self.textCtrl93 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL93,
              name='textCtrl93', parent=self.panel13, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl93.SetMaxLength(4)
        self.textCtrl93.SetInsertionPoint(0)
        self.textCtrl93.SetMinSize(wx.Size(40, 24))

        self.textCtrl94 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL94,
              name='textCtrl94', parent=self.panel13, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl94.SetMaxLength(4)
        self.textCtrl94.SetInsertionPoint(0)
        self.textCtrl94.SetMinSize(wx.Size(40, 24))

        self.textCtrl95 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL95,
              name='textCtrl95', parent=self.panel13, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl95.SetMaxLength(4)
        self.textCtrl95.SetInsertionPoint(0)
        self.textCtrl95.SetMinSize(wx.Size(40, 24))

        self.textCtrl96 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL96,
              name='textCtrl96', parent=self.panel13, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl96.SetMaxLength(4)
        self.textCtrl96.SetInsertionPoint(0)
        self.textCtrl96.SetMinSize(wx.Size(40, 24))

        self.panel14 = wx.Panel(id=wxID_FRAME2PANEL14, name='panel14',
              parent=self.panel1, pos=wx.Point(8, 296), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel14.SetMinSize(wx.Size(200, 26))

        self.textCtrl97 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL97,
              name='textCtrl97', parent=self.panel14, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl97.SetMaxLength(4)
        self.textCtrl97.SetInsertionPoint(0)
        self.textCtrl97.SetMinSize(wx.Size(40, 24))

        self.textCtrl98 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL98,
              name='textCtrl98', parent=self.panel14, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl98.SetMaxLength(4)
        self.textCtrl98.SetInsertionPoint(0)
        self.textCtrl98.SetMinSize(wx.Size(40, 24))

        self.textCtrl99 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL99,
              name='textCtrl99', parent=self.panel14, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl99.SetMaxLength(4)
        self.textCtrl99.SetInsertionPoint(0)
        self.textCtrl99.SetMinSize(wx.Size(40, 24))

        self.textCtrl100 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL100,
              name='textCtrl100', parent=self.panel14, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl100.SetMaxLength(4)
        self.textCtrl100.SetInsertionPoint(0)
        self.textCtrl100.SetMinSize(wx.Size(40, 24))

        self.textCtrl101 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL101,
              name='textCtrl101', parent=self.panel14, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl101.SetMaxLength(4)
        self.textCtrl101.SetInsertionPoint(0)
        self.textCtrl101.SetMinSize(wx.Size(40, 24))

        self.textCtrl102 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL102,
              name='textCtrl102', parent=self.panel14, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl102.SetMaxLength(4)
        self.textCtrl102.SetInsertionPoint(0)
        self.textCtrl102.SetToolTipString(u'textCtrl1')
        self.textCtrl102.SetMinSize(wx.Size(40, 24))

        self.textCtrl103 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL103,
              name='textCtrl103', parent=self.panel14, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl103.SetMaxLength(4)
        self.textCtrl103.SetInsertionPoint(0)
        self.textCtrl103.SetMinSize(wx.Size(40, 24))

        self.textCtrl104 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL104,
              name='textCtrl104', parent=self.panel14, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl104.SetMaxLength(4)
        self.textCtrl104.SetInsertionPoint(0)
        self.textCtrl104.SetMinSize(wx.Size(40, 24))

        self.panel15 = wx.Panel(id=wxID_FRAME2PANEL15, name='panel15',
              parent=self.panel1, pos=wx.Point(8, 320), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel15.SetMinSize(wx.Size(200, 26))

        self.textCtrl105 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL105,
              name='textCtrl105', parent=self.panel15, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl105.SetMaxLength(4)
        self.textCtrl105.SetInsertionPoint(0)
        self.textCtrl105.SetMinSize(wx.Size(40, 24))

        self.textCtrl106 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL106,
              name='textCtrl106', parent=self.panel15, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl106.SetMaxLength(4)
        self.textCtrl106.SetInsertionPoint(0)
        self.textCtrl106.SetMinSize(wx.Size(40, 24))

        self.textCtrl107 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL107,
              name='textCtrl107', parent=self.panel15, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl107.SetMaxLength(4)
        self.textCtrl107.SetInsertionPoint(0)
        self.textCtrl107.SetMinSize(wx.Size(40, 24))

        self.textCtrl108 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL108,
              name='textCtrl108', parent=self.panel15, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl108.SetMaxLength(4)
        self.textCtrl108.SetInsertionPoint(0)
        self.textCtrl108.SetMinSize(wx.Size(40, 24))

        self.textCtrl109 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL109,
              name='textCtrl109', parent=self.panel15, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl109.SetMaxLength(4)
        self.textCtrl109.SetInsertionPoint(0)
        self.textCtrl109.SetMinSize(wx.Size(40, 24))

        self.textCtrl110 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL110,
              name='textCtrl110', parent=self.panel15, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl110.SetMaxLength(4)
        self.textCtrl110.SetInsertionPoint(0)
        self.textCtrl110.SetMinSize(wx.Size(40, 24))

        self.textCtrl111 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL111,
              name='textCtrl111', parent=self.panel15, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl111.SetMaxLength(4)
        self.textCtrl111.SetInsertionPoint(0)
        self.textCtrl111.SetToolTipString(u'textCtrl1')
        self.textCtrl111.SetMinSize(wx.Size(40, 24))

        self.textCtrl112 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL112,
              name='textCtrl112', parent=self.panel15, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl112.SetMaxLength(4)
        self.textCtrl112.SetInsertionPoint(0)
        self.textCtrl112.SetMinSize(wx.Size(40, 24))

        self.panel16 = wx.Panel(id=wxID_FRAME2PANEL16, name='panel16',
              parent=self.panel1, pos=wx.Point(8, 344), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel16.SetMinSize(wx.Size(200, 26))

        self.textCtrl113 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL113,
              name='textCtrl113', parent=self.panel16, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl113.SetMaxLength(4)
        self.textCtrl113.SetInsertionPoint(0)
        self.textCtrl113.SetMinSize(wx.Size(40, 24))

        self.textCtrl114 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL114,
              name='textCtrl114', parent=self.panel16, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl114.SetMaxLength(4)
        self.textCtrl114.SetInsertionPoint(0)
        self.textCtrl114.SetMinSize(wx.Size(40, 24))

        self.textCtrl115 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL115,
              name='textCtrl115', parent=self.panel16, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl115.SetMaxLength(4)
        self.textCtrl115.SetInsertionPoint(0)
        self.textCtrl115.SetMinSize(wx.Size(40, 24))

        self.textCtrl116 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL116,
              name='textCtrl116', parent=self.panel16, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl116.SetMaxLength(4)
        self.textCtrl116.SetInsertionPoint(0)
        self.textCtrl116.SetMinSize(wx.Size(40, 24))

        self.textCtrl117 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL117,
              name='textCtrl117', parent=self.panel16, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl117.SetMaxLength(4)
        self.textCtrl117.SetInsertionPoint(0)
        self.textCtrl117.SetMinSize(wx.Size(40, 24))

        self.textCtrl118 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL118,
              name='textCtrl118', parent=self.panel16, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl118.SetMaxLength(4)
        self.textCtrl118.SetInsertionPoint(0)
        self.textCtrl118.SetToolTipString(u'textCtrl1')
        self.textCtrl118.SetMinSize(wx.Size(40, 24))

        self.textCtrl119 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL119,
              name='textCtrl119', parent=self.panel16, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl119.SetMaxLength(4)
        self.textCtrl119.SetInsertionPoint(0)
        self.textCtrl119.SetMinSize(wx.Size(40, 24))

        self.textCtrl120 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL120,
              name='textCtrl120', parent=self.panel16, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl120.SetMaxLength(4)
        self.textCtrl120.SetInsertionPoint(0)
        self.textCtrl120.SetMinSize(wx.Size(40, 24))

        self.panel17 = wx.Panel(id=wxID_FRAME2PANEL17, name='panel17',
              parent=self.panel1, pos=wx.Point(8, 368), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel17.SetMinSize(wx.Size(200, 26))

        self.textCtrl121 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL121,
              name='textCtrl121', parent=self.panel17, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl121.SetMaxLength(4)
        self.textCtrl121.SetInsertionPoint(0)
        self.textCtrl121.SetMinSize(wx.Size(40, 24))

        self.textCtrl122 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL122,
              name='textCtrl122', parent=self.panel17, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl122.SetMaxLength(4)
        self.textCtrl122.SetInsertionPoint(0)
        self.textCtrl122.SetMinSize(wx.Size(40, 24))

        self.textCtrl123 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL123,
              name='textCtrl123', parent=self.panel17, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl123.SetMaxLength(4)
        self.textCtrl123.SetInsertionPoint(0)
        self.textCtrl123.SetMinSize(wx.Size(40, 24))

        self.textCtrl124 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL124,
              name='textCtrl124', parent=self.panel17, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl124.SetMaxLength(4)
        self.textCtrl124.SetInsertionPoint(0)
        self.textCtrl124.SetMinSize(wx.Size(40, 24))

        self.textCtrl125 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL125,
              name='textCtrl125', parent=self.panel17, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl125.SetMaxLength(4)
        self.textCtrl125.SetInsertionPoint(0)
        self.textCtrl125.SetToolTipString(u'textCtrl1')
        self.textCtrl125.SetMinSize(wx.Size(40, 24))

        self.textCtrl126 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL126,
              name='textCtrl126', parent=self.panel17, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl126.SetMaxLength(4)
        self.textCtrl126.SetInsertionPoint(0)
        self.textCtrl126.SetMinSize(wx.Size(40, 24))

        self.textCtrl127 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL127,
              name='textCtrl127', parent=self.panel17, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl127.SetMaxLength(4)
        self.textCtrl127.SetInsertionPoint(0)
        self.textCtrl127.SetMinSize(wx.Size(40, 24))

        self.textCtrl128 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL128,
              name='textCtrl128', parent=self.panel17, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl128.SetMaxLength(4)
        self.textCtrl128.SetInsertionPoint(0)
        self.textCtrl128.SetMinSize(wx.Size(40, 24))

        self.panel18 = wx.Panel(id=wxID_FRAME2PANEL18, name='panel18',
              parent=self.panel1, pos=wx.Point(8, 392), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel18.SetMinSize(wx.Size(200, 26))

        self.textCtrl129 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL129,
              name='textCtrl129', parent=self.panel18, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl129.SetMaxLength(4)
        self.textCtrl129.SetInsertionPoint(0)
        self.textCtrl129.SetMinSize(wx.Size(40, 24))

        self.textCtrl130 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL130,
              name='textCtrl130', parent=self.panel18, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl130.SetMaxLength(4)
        self.textCtrl130.SetInsertionPoint(0)
        self.textCtrl130.SetMinSize(wx.Size(40, 24))

        self.textCtrl131 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL131,
              name='textCtrl131', parent=self.panel18, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl131.SetMaxLength(4)
        self.textCtrl131.SetInsertionPoint(0)
        self.textCtrl131.SetMinSize(wx.Size(40, 24))

        self.textCtrl132 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL132,
              name='textCtrl132', parent=self.panel18, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl132.SetMaxLength(4)
        self.textCtrl132.SetInsertionPoint(0)
        self.textCtrl132.SetMinSize(wx.Size(40, 24))

        self.textCtrl133 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL133,
              name='textCtrl133', parent=self.panel18, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl133.SetMaxLength(4)
        self.textCtrl133.SetInsertionPoint(0)
        self.textCtrl133.SetMinSize(wx.Size(40, 24))

        self.textCtrl134 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL134,
              name='textCtrl134', parent=self.panel18, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl134.SetMaxLength(4)
        self.textCtrl134.SetInsertionPoint(0)
        self.textCtrl134.SetMinSize(wx.Size(40, 24))

        self.textCtrl135 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL135,
              name='textCtrl135', parent=self.panel18, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl135.SetMaxLength(4)
        self.textCtrl135.SetInsertionPoint(0)
        self.textCtrl135.SetToolTipString(u'textCtrl1')
        self.textCtrl135.SetMinSize(wx.Size(40, 24))

        self.textCtrl136 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL136,
              name='textCtrl136', parent=self.panel18, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl136.SetMaxLength(4)
        self.textCtrl136.SetInsertionPoint(0)
        self.textCtrl136.SetMinSize(wx.Size(40, 24))

        self.panel19 = wx.Panel(id=wxID_FRAME2PANEL19, name='panel19',
              parent=self.panel1, pos=wx.Point(8, 416), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel19.SetMinSize(wx.Size(200, 26))

        self.textCtrl137 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL137,
              name='textCtrl137', parent=self.panel19, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl137.SetMaxLength(4)
        self.textCtrl137.SetInsertionPoint(0)
        self.textCtrl137.SetMinSize(wx.Size(40, 24))
        self.textCtrl137.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.textCtrl137.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl138 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL138,
              name='textCtrl138', parent=self.panel19, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl138.SetMaxLength(4)
        self.textCtrl138.SetInsertionPoint(0)
        self.textCtrl138.SetMinSize(wx.Size(40, 24))
        self.textCtrl138.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl139 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL139,
              name='textCtrl139', parent=self.panel19, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl139.SetMaxLength(4)
        self.textCtrl139.SetInsertionPoint(0)
        self.textCtrl139.SetMinSize(wx.Size(40, 24))
        self.textCtrl139.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl140 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL140,
              name='textCtrl140', parent=self.panel19, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl140.SetMaxLength(4)
        self.textCtrl140.SetInsertionPoint(0)
        self.textCtrl140.SetMinSize(wx.Size(40, 24))
        self.textCtrl140.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl141 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL141,
              name='textCtrl141', parent=self.panel19, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl141.SetMaxLength(4)
        self.textCtrl141.SetInsertionPoint(0)
        self.textCtrl141.SetMinSize(wx.Size(40, 24))
        self.textCtrl141.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl142 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL142,
              name='textCtrl142', parent=self.panel19, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl142.SetMaxLength(4)
        self.textCtrl142.SetInsertionPoint(0)
        self.textCtrl142.SetMinSize(wx.Size(40, 24))
        self.textCtrl142.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl143 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL143,
              name='textCtrl143', parent=self.panel19, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl143.SetMaxLength(4)
        self.textCtrl143.SetInsertionPoint(0)
        self.textCtrl143.SetToolTipString(u'textCtrl1')
        self.textCtrl143.SetMinSize(wx.Size(40, 24))
        self.textCtrl143.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl144 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL144,
              name='textCtrl144', parent=self.panel19, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl144.SetMaxLength(4)
        self.textCtrl144.SetInsertionPoint(0)
        self.textCtrl144.SetMinSize(wx.Size(40, 24))
        self.textCtrl144.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.panel20 = wx.Panel(id=wxID_FRAME2PANEL20, name='panel20',
              parent=self.panel1, pos=wx.Point(8, 440), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel20.SetMinSize(wx.Size(200, 26))

        self.textCtrl145 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL145,
              name='textCtrl145', parent=self.panel20, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl145.SetMaxLength(4)
        self.textCtrl145.SetInsertionPoint(0)
        self.textCtrl145.SetMinSize(wx.Size(40, 24))
        self.textCtrl145.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl146 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL146,
              name='textCtrl146', parent=self.panel20, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl146.SetMaxLength(4)
        self.textCtrl146.SetInsertionPoint(0)
        self.textCtrl146.SetMinSize(wx.Size(40, 24))
        self.textCtrl146.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl147 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL147,
              name='textCtrl147', parent=self.panel20, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl147.SetMaxLength(4)
        self.textCtrl147.SetInsertionPoint(0)
        self.textCtrl147.SetMinSize(wx.Size(40, 24))
        self.textCtrl147.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl148 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL148,
              name='textCtrl148', parent=self.panel20, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl148.SetMaxLength(4)
        self.textCtrl148.SetInsertionPoint(0)
        self.textCtrl148.SetToolTipString(u'textCtrl1')
        self.textCtrl148.SetMinSize(wx.Size(40, 24))
        self.textCtrl148.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl149 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL149,
              name='textCtrl149', parent=self.panel20, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl149.SetMaxLength(4)
        self.textCtrl149.SetInsertionPoint(0)
        self.textCtrl149.SetMinSize(wx.Size(40, 24))
        self.textCtrl149.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl150 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL150,
              name='textCtrl150', parent=self.panel20, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl150.SetMaxLength(4)
        self.textCtrl150.SetInsertionPoint(0)
        self.textCtrl150.SetMinSize(wx.Size(40, 24))
        self.textCtrl150.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl151 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL151,
              name='textCtrl151', parent=self.panel20, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl151.SetMaxLength(4)
        self.textCtrl151.SetInsertionPoint(0)
        self.textCtrl151.SetMinSize(wx.Size(40, 24))
        self.textCtrl151.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl152 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL152,
              name='textCtrl152', parent=self.panel20, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl152.SetMaxLength(4)
        self.textCtrl152.SetInsertionPoint(0)
        self.textCtrl152.SetMinSize(wx.Size(40, 24))
        self.textCtrl152.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.textCtrl152.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.panel21 = wx.Panel(id=wxID_FRAME2PANEL21, name='panel21',
              parent=self.panel1, pos=wx.Point(8, 464), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel21.SetMinSize(wx.Size(200, 26))

        self.textCtrl153 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL153,
              name='textCtrl153', parent=self.panel21, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl153.SetMaxLength(4)
        self.textCtrl153.SetInsertionPoint(0)
        self.textCtrl153.SetMinSize(wx.Size(40, 24))
        self.textCtrl153.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl154 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL154,
              name='textCtrl154', parent=self.panel21, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl154.SetMaxLength(4)
        self.textCtrl154.SetInsertionPoint(0)
        self.textCtrl154.SetMinSize(wx.Size(40, 24))
        self.textCtrl154.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl155 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL155,
              name='textCtrl155', parent=self.panel21, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl155.SetMaxLength(4)
        self.textCtrl155.SetInsertionPoint(0)
        self.textCtrl155.SetMinSize(wx.Size(40, 24))
        self.textCtrl155.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl156 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL156,
              name='textCtrl156', parent=self.panel21, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl156.SetMaxLength(4)
        self.textCtrl156.SetInsertionPoint(0)
        self.textCtrl156.SetToolTipString(u'textCtrl1')
        self.textCtrl156.SetMinSize(wx.Size(40, 24))
        self.textCtrl156.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl157 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL157,
              name='textCtrl157', parent=self.panel21, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl157.SetMaxLength(4)
        self.textCtrl157.SetInsertionPoint(0)
        self.textCtrl157.SetMinSize(wx.Size(40, 24))
        self.textCtrl157.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl158 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL158,
              name='textCtrl158', parent=self.panel21, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl158.SetMaxLength(4)
        self.textCtrl158.SetInsertionPoint(0)
        self.textCtrl158.SetMinSize(wx.Size(40, 24))
        self.textCtrl158.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl159 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL159,
              name='textCtrl159', parent=self.panel21, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl159.SetMaxLength(4)
        self.textCtrl159.SetInsertionPoint(0)
        self.textCtrl159.SetMinSize(wx.Size(40, 24))
        self.textCtrl159.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl160 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL160,
              name='textCtrl160', parent=self.panel21, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl160.SetMaxLength(4)
        self.textCtrl160.SetInsertionPoint(0)
        self.textCtrl160.SetMinSize(wx.Size(40, 24))
        self.textCtrl160.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.textCtrl160.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.panel22 = wx.Panel(id=wxID_FRAME2PANEL22, name='panel22',
              parent=self.panel1, pos=wx.Point(8, 488), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel22.SetMinSize(wx.Size(200, 26))

        self.textCtrl161 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL161,
              name='textCtrl161', parent=self.panel22, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl161.SetMaxLength(4)
        self.textCtrl161.SetInsertionPoint(0)
        self.textCtrl161.SetToolTipString(u'textCtrl1')
        self.textCtrl161.SetMinSize(wx.Size(40, 24))
        self.textCtrl161.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl162 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL162,
              name='textCtrl162', parent=self.panel22, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl162.SetMaxLength(4)
        self.textCtrl162.SetInsertionPoint(0)
        self.textCtrl162.SetMinSize(wx.Size(40, 24))
        self.textCtrl162.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl163 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL163,
              name='textCtrl163', parent=self.panel22, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl163.SetMaxLength(4)
        self.textCtrl163.SetInsertionPoint(0)
        self.textCtrl163.SetMinSize(wx.Size(40, 24))
        self.textCtrl163.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.textCtrl163.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl164 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL164,
              name='textCtrl164', parent=self.panel22, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl164.SetMaxLength(4)
        self.textCtrl164.SetInsertionPoint(0)
        self.textCtrl164.SetMinSize(wx.Size(40, 24))
        self.textCtrl164.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl165 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL165,
              name='textCtrl165', parent=self.panel22, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl165.SetMaxLength(4)
        self.textCtrl165.SetInsertionPoint(0)
        self.textCtrl165.SetMinSize(wx.Size(40, 24))
        self.textCtrl165.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl166 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL166,
              name='textCtrl166', parent=self.panel22, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl166.SetMaxLength(4)
        self.textCtrl166.SetInsertionPoint(0)
        self.textCtrl166.SetMinSize(wx.Size(40, 24))
        self.textCtrl166.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl167 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL167,
              name='textCtrl167', parent=self.panel22, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl167.SetMaxLength(4)
        self.textCtrl167.SetInsertionPoint(0)
        self.textCtrl167.SetMinSize(wx.Size(40, 24))
        self.textCtrl167.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.textCtrl168 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL168,
              name='textCtrl168', parent=self.panel22, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl168.SetMaxLength(4)
        self.textCtrl168.SetInsertionPoint(0)
        self.textCtrl168.SetMinSize(wx.Size(40, 24))
        self.textCtrl168.SetBackgroundColour(wx.Colour(255, 217, 34))

        self.panel23 = wx.Panel(id=wxID_FRAME2PANEL23, name='panel23',
              parent=self.panel1, pos=wx.Point(8, 512), size=wx.Size(376, 26),
              style=wx.TAB_TRAVERSAL)
        self.panel23.SetMinSize(wx.Size(200, 26))

        self.textCtrl169 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL169,
              name='textCtrl169', parent=self.panel23, pos=wx.Point(56, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl169.SetMaxLength(4)
        self.textCtrl169.SetInsertionPoint(0)
        self.textCtrl169.SetMinSize(wx.Size(40, 24))
        self.textCtrl169.SetBackgroundColour(wx.Colour(255, 0, 0))

        self.textCtrl170 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL170,
              name='textCtrl170', parent=self.panel23, pos=wx.Point(96, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl170.SetMaxLength(4)
        self.textCtrl170.SetInsertionPoint(0)
        self.textCtrl170.SetToolTipString(u'textCtrl1')
        self.textCtrl170.SetMinSize(wx.Size(40, 24))
        self.textCtrl170.SetBackgroundColour(wx.Colour(255, 0, 0))

        self.textCtrl171 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL171,
              name='textCtrl171', parent=self.panel23, pos=wx.Point(136, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl171.SetMaxLength(4)
        self.textCtrl171.SetInsertionPoint(0)
        self.textCtrl171.SetMinSize(wx.Size(40, 24))
        self.textCtrl171.SetBackgroundColour(wx.Colour(255, 0, 0))

        self.textCtrl172 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL172,
              name='textCtrl172', parent=self.panel23, pos=wx.Point(176, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl172.SetMaxLength(4)
        self.textCtrl172.SetInsertionPoint(0)
        self.textCtrl172.SetMinSize(wx.Size(40, 24))
        self.textCtrl172.SetBackgroundColour(wx.Colour(255, 0, 0))

        self.textCtrl173 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL173,
              name='textCtrl173', parent=self.panel23, pos=wx.Point(216, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl173.SetMaxLength(4)
        self.textCtrl173.SetInsertionPoint(0)
        self.textCtrl173.SetMinSize(wx.Size(40, 24))
        self.textCtrl173.SetBackgroundColour(wx.Colour(255, 0, 0))

        self.textCtrl174 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL174,
              name='textCtrl174', parent=self.panel23, pos=wx.Point(256, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl174.SetMaxLength(4)
        self.textCtrl174.SetInsertionPoint(0)
        self.textCtrl174.SetMinSize(wx.Size(40, 24))
        self.textCtrl174.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.textCtrl174.SetBackgroundColour(wx.Colour(255, 0, 0))

        self.textCtrl175 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL175,
              name='textCtrl175', parent=self.panel23, pos=wx.Point(296, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl175.SetMaxLength(4)
        self.textCtrl175.SetInsertionPoint(0)
        self.textCtrl175.SetMinSize(wx.Size(40, 24))
        self.textCtrl175.SetBackgroundColour(wx.Colour(255, 0, 0))

        self.textCtrl176 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL176,
              name='textCtrl176', parent=self.panel23, pos=wx.Point(336, 0),
              size=wx.Size(40, 24), style=0, value=u'0')
        self.textCtrl176.SetMaxLength(4)
        self.textCtrl176.SetInsertionPoint(0)
        self.textCtrl176.SetMinSize(wx.Size(40, 24))
        self.textCtrl176.SetBackgroundColour(wx.Colour(255, 0, 0))

        self.panel24 = wx.Panel(id=wxID_FRAME2PANEL24, name='panel24',
              parent=self, pos=wx.Point(168, 0), size=wx.Size(376, 30),
              style=wx.TAB_TRAVERSAL)
        self.panel24.SetMinSize(wx.Size(200, 30))

        self.staticText8 = wx.StaticText(id=wxID_FRAME2STATICTEXT8,
              label=u'STR   VIT   DEF MDEF DEX  LCK  HP% MP%',
              name='staticText8', parent=self.panel24, pos=wx.Point(32, 8),
              size=wx.Size(385, 17), style=0)
        self.staticText8.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Sans Serif'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        event.Skip()
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

    def OnButton2Button(self, event):
        event.Skip()
        dlg = wx.FileDialog(self, 'Save to PC FF7.exe', '.', '', '*.exe', wx.SAVE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                materia=downdate(self)
                #print(materia)
                saver(filename,5232840)
                
        finally:
            dlg.Destroy()

    def OnButton3Button(self, event):
        event.Skip()
