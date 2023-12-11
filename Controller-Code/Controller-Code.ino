#include <Bounce.h>
#include "defaultController.h"

#define ARRAY_SIZE(a) (sizeof(a) / sizeof(a[0]))
const int buttonsMapSize = ARRAY_SIZE(buttonsMap);
const int dpadButtonsSize = ARRAY_SIZE(dpadMap);
Bounce* buttons[buttonsMapSize];
Bounce* dpadButtons[dpadButtonsSize];

void setup() {
    Joystick.useManualSend(true);

    for (int i = 0; i < buttonsMapSize; ++i) {
        const uint8_t pin = buttonsMap[i][0];
        buttons[i] = new Bounce(pin, 10);
        pinMode(pin, INPUT_PULLUP);
    }
    for (int i = 0; i < dpadButtonsSize; ++i) {
        const uint8_t pin = dpadMap[i];
        dpadButtons[i] = new Bounce(pin, 10);
        pinMode(pin, INPUT_PULLUP);
    }
}

void loop() {
    handleAnalog();
    handleButtons();
    Joystick.hat(handleDpad());
    Joystick.send_now();
    delay(50);
}

void handleAnalog() {
    // read 6 analog inputs and use them for the joystick axis
    Joystick.X(analogRead(axisXPlus));
    // we need to invert the y axis
    Joystick.Y(1023 - analogRead(axisXMinus));
    Joystick.Z(analogRead(axisYPlus));
    Joystick.Zrotate(analogRead(axisYMinus));
}

void handleButtons() {
    // read digital pins and use them for the buttons
    for (int i = 0; i < buttonsMapSize; ++i) {
        const uint8_t* buttonMapping = buttonsMap[i];
        buttons[i]->update();

        if (buttons[i]->fallingEdge()) {
            Joystick.button(buttonMapping[1], 1);
        }

        if (buttons[i]->risingEdge()) {
            Joystick.button(buttonMapping[1], 0);
        }
    }
}

int handleDpad() {
    uint8_t dpadValue = 0;
    for (int i = 0; i < dpadButtonsSize; ++i) {
        dpadButtons[i]->update();
        int value = 0;
        if (dpadButtons[i]->fallingEdge())
            value = 1;
        dpadValue |= value << i;
    }

    int angle = 0;
    switch (dpadValue) {
    case 0x0:
        // no button pressed, return to the rest position
        angle = -1;
        break;
    case 0x1:
        angle = 0;
        break;
    case 0x2:
        angle = 90;
        break;
    case 0x3:
        angle = 45;
        break;
    case 0x4:
        angle = 180;
        break;
    case 0x6:
        angle = 135;
        break;
    case 0x8:
        angle = 270;
        break;
    case 0xC:
        angle = 225;
        break;
    case 0x9:
        angle = 315;
        break;
    }
    return angle;
}