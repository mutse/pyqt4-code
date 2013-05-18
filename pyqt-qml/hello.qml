import QtQuick 1.0

Rectangle {  
	id: page  
	width: 500; height: 200  
	color: "lightgray" 
	Text {  
		id: helloText  
		text: "Hello QML & PyQt4"  
		font.pointSize: 24; font.bold: true  
		anchors.centerIn: parent; color: "blue" 
	}
}

