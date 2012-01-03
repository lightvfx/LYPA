def setStyleSheet(main):
		main.setStyleSheet("""


QMainWindow,QWidget 
{background-color: rgb(60,60,60);color: rgb(240,240,240);}
QDialog{background-color: rgb(50,50,50);}
QMainWindow::separator {
     background: rgb(50,50,50);
     width: 10px; /* when vertical */
     height: 10px; /* when horizontal */
 }

QMainWindow::separator:hover {
     background: rgb(75,75,75);
 }
QSlider::groove:horizontal {
border: 1px solid rgb(30,30,30);
background: rgb(50,50,50);
height: 8px;
border-radius: 1px;
}
QSlider::handle:horizontal {
background:rgb(75,75,75) ;
border: 1px solid rgb(30,30,30);
width: 16px;
border-radius: 1px;


}



 
QTabWidget::tab-bar {background-color: rgb(30,30,30);


 }
QTabBar::tab {
  background: rgb(50,50,50);
  color: rgb(150,150,150);
  border-radius: 4px;
  height : 20px;
  width:80px;
 }
 QTabBar::tab:selected {
  background: orange;
  color: rgb(30,30,30);
  border: 1px solid rgb(180,180,180);
 }
QLabel{color: rgb(240,240,240);}
QLabel[mandatory="true"] { 
				color: red; 
				}

QLineEdit {border: 1px solid orange;
				color: rgb(240,240,240);
				background: rgb(100,100,100);
				selection-color: rgb(240,240,240);
				selection-background-color: orange;}

QLineEdit:read-only {border: 1px solid rgb(30,30,30);
				color: rgb(200,200,200);
				background: rgb(100,100,100);
				selection-color: rgb(240,240,240);
				selection-background-color: solid rgb(30,30,30);}				

QDoubleSpinBox {color: rgb(240,240,240);
				background-color:orange;
				background: rgb(75,75,75);
				selection-color: rgb(240,240,240);
				selection-background-color: orange;}
QDoubleSpinBox::up-button {
     subcontrol-origin: border;
     subcontrol-position: top right; /* position at the top right corner */

     width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */
     border-image: url(:/images/spinup.png) 1;
     border-width: 1px;
 }

 QDoubleSpinBox::up-button:hover {
    
 }

 QDoubleSpinBox::up-button:pressed {
     
 }

 QDoubleSpinBox::up-arrow {
     
     width: 7px;
     height: 7px;
 }

 QDoubleSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */
    
 }

 QDoubleSpinBox::down-button {
     subcontrol-origin: border;
     subcontrol-position: bottom right; /* position at bottom right corner */

     width: 16px;
    
     border-width: 1px;
     border-top-width: 0;
 }

 QDoubleSpinBox::down-button:hover {
   
 }

 QDoubleSpinBox::down-button:pressed {
  
 }

 QDoubleSpinBox::down-arrow {
   
     width: 7px;
     height: 7px;
 }

QTextEdit {border: 1px solid orange;
				color: rgb(30, 30, 30);
				background: rgb(92, 95, 100);
				selection-color: rgb(92, 102, 115);
				selection-background-color: rgb(200, 205, 210);}
QGroupBox{border: 1px solid rgb(30,30,30);border-radius: 5px;margin: 2px 0px 0px 2px;color: rgb(150,150,150);padding: 20px 0px 20px 0px}



QCheckBox {color: rgb(240,240,240);
				background-color:orange;
				background: rgb(50,50,50);
				selection-color: rgb(240,240,240);
				selection-background-color: orange;}
QTabWidget::pane { 
     border-top: 2px rgb(30,30,30);
 }







QComboBox{color: rgb(220,220,220);
				background-color: rgb(100,100,100);
                               
    
     }
	
QMessageBox{background: rgb(50,50,50);}
QTreeWidget {background: rgb(100,100,100);
				color: rgb(240,240,240);
				selection-color: white;
				selection-background-color: orange;
				alternate-background-color: rgb(90,90,90);
				border: 1px solid orange;}
QTreeWidget QHeaderView:section {background: rgb(75,75,75);
				color: rgb(240,240,240);
                                height: 20px;
				selection-color: rgb(240,240,240);
				selection-background-color: black;
				alternate-background-color: rgb(60,60,60);
				border: 1px solid rgb(50,50,50);}
QListWidget {background: rgb(100,100,100);
				color: rgb(240,240,240);
				selection-color: rgb(240,240,240);
				selection-background-color: orange;
				alternate-background-color: rgb(90,90,90);
				border: 1px solid orange;}
				
QCalendar {background: rgb(100,100,100);
				color: rgb(240,240,240);
				selection-color: rgb(240,240,240);
				selection-background-color: orange;
				alternate-background-color: rgb(90,90,90);
				border: 1px solid orange;}
				
QTableWidget {background: rgb(100,100,100);
				color: rgb(240,240,240);
				selection-color: rgb(240,240,240);
				selection-background-color: orange;
				alternate-background-color: rgb(90,90,90);
				border: 1px solid orange;}
QProgressBar{color: rgb(240,240,240);
				background-color: rgb(75,75,75);
				selection-color: black;
				border-style: outset;
				border-width: 1px;
				border-color: black;
				selection-background-color: orange;
				text-align: center;}



QPushButton{color: rgb(200,200,200);
				background-color: rgb(85,85,85);
				
				border-style: outset;
                                border-radius: 4px;
                                border: 10px solid black;
				border-width: 1px;
                                font:  10px;
                                min-width: 4em;
                                padding: 2px;
				border-color: black;}
				
QTabWidget {background: rgb(50,50,50);
				color: rgb(240,240,240);
				selection-color: rgb(240,240,240);
				selection-background-color: orange;
				
                                background-color: rgb(30,30,30);
				border: 1px solid orange;}


QPushButton:pressed {
 background-color: rgb(30, 30, 30);}



QScrollBar:horizontal {
      
      background: rgb(60, 60, 60);
      border: 2px rgb(30, 30, 30);
      height: 18px;
      margin: 22px 0 22px 0;
  }
QScrollBar::handle:horizontal {
      background:rgb(75, 75, 75);
      min-width: 10px;
     
  }
QScrollBar::add-line:horizontal {
      border: 1px solid rgb(50, 50, 50);
      background: rgb(50, 50, 50);
      width: 20px;
      subcontrol-position:right;
      subcontrol-origin: margin;

      
  }

QScrollBar::sub-line:horizontal {
      border: 1px solid black;
      background: rgb(50, 50, 50);
      width: 20px;
      subcontrol-position: left;
      subcontrol-origin: margin;
  }
  QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
      border: 2px solid black;
      width: 3px;
      height: 3px;
      background: rgb(50, 50, 50);
  }

  QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
      background: none;
  }
  
QScrollBar:vertical {
      
      background: rgb(50, 50, 50);
      border: 1px solid rgb(30, 30, 30);
      width: 18px;
      margin: 22px 0 22px 0;
  }
QScrollBar::handle:vertical {
      background:rgb(90, 90, 90);
      min-height: 10px;
      border: 1px solid rgb(30, 30, 30);
  }
QScrollBar::add-line:vertical {
      border: 1px solid rgb(50, 50, 50);
      background: rgb(95, 95, 95);
      height: 20px;
      subcontrol-position: bottom;
      subcontrol-origin: margin;
  }

QScrollBar::sub-line:vertical {
      border: 1px solid rgb(50, 50, 50);
      background: rgb(95, 95, 95);
      height: 20px;
      subcontrol-position: top;
      subcontrol-origin: margin;
  }
  QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
      
      width: 7px;
      height: 7px;
      background: rgb(200, 200, 200);
  }

  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
      background: rgb(85, 85, 85);
      
  }
mainFrame {
border: 1px solid  rgb(50, 50, 50);
border-radius:0px;
background: rgb(50, 50, 50);
}

QToolBar {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                     stop: 0 rgb(110, 110, 110),
                                    stop: 1.0 rgb(90, 90, 90));
                border-radius: 1px;

             
         height: 10px;
         spacing: 0px; /* spacing between items in the tool bar */
     }

     QToolBar::handle {
         image: url(handle.png);
     }
      QMenuBar {
     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                       stop:0 lightgray, stop:1 darkgray);
 }

 QMenuBar::item {
     spacing: 3px; /* spacing between menu bar items */
     padding: 1px 4px;
     background: transparent;
     border-radius: 4px;
     color:rgb(30, 30, 30);
 }

 QMenuBar::item:selected { /* when selected using mouse or keyboard */
     background: #a8a8a8;
 }

 QMenuBar::item:pressed {
     background: #888888;
 }
 

 """)
                



