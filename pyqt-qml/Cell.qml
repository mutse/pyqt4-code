import QtQuick 1.0

Item {
	id: container
	property alias cellColor: rectangle.color
	signal clicked(color cellCorlor)

	width: 40; height: 25

	Rectangle {
		id: rectangle
		border.color: "white"
		anchors.fill: parent
	}

	MouseArea {
		anchors.fill: parent
		onClicked: container.clicked(container.cellColor)
	}
}

