#include <Bounce.h>

#define ARRAY_SIZE(a) (sizeof(a) / sizeof(a[0]))

// The first number corresponds to the pin number and the second number to the button number. See https://www.pjrc.com/teensy/td_joystick.html for more information.
const uint8_t buttonsMap[][2] = {
  {8, 1},   // L3
  {11, 2},  // R3
  {16, 3},  // Sqare
  {15, 4},  // Circle
  {14, 5},  // Triangle
  {13, 6},  // Cross
  {17, 7},  // R1
  {12, 8},  // R2
  {6, 9},   // L1
  {7, 10},  // L2
  {5, 11},  // SELECT
  {1, 12},  // START
  {10, 13}, // AUX1
  {23, 14}, // AUX2
};

const int buttonsMapSize = ARRAY_SIZE(buttonsMap);

Bounce* buttons[buttonsMapSize];

// Pin numbers used by the dpad
const uint8_t down = 2;
const uint8_t right = 0;
const uint8_t up = 4;
const uint8_t left = 3;

const uint8_t dpadButtons[] = { up, right, down, left };

const int dpadButtonsSize = ARRAY_SIZE(dpadButtons);

void setup() {

    // configure the joystick to manual send mode.  This gives precise
    // control over when the computer receives updates, but it does
    // require you to manually call Joystick.send_now().
    Joystick.useManualSend(true);

    for (int i = 0; i < buttonsMapSize; ++i) {
        const uint8_t pin = buttonsMap[i][0];
        buttons[i] = new Bounce(pin, 10);
        pinMode(pin, INPUT_PULLUP);
    }
    for (int i = 0; i < dpadButtonsSize; ++i) {
        pinMode(dpadButtons[i], INPUT_PULLUP);
    }
}

void loop() {
    // read 6 analog inputs and use them for the joystick axis
    Joystick.X(analogRead(2));
    // we need to invert the y axis
    Joystick.Y(1023 - analogRead(3));
    Joystick.Z(analogRead(0));
    Joystick.Zrotate(analogRead(1));

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

    uint8_t dpadValue = 0;
    for (int i = 0; i < dpadButtonsSize; ++i) {
        const int value = !digitalRead(dpadButtons[i]);
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

    Joystick.hat(angle);
    Joystick.send_now();
    delay(50);
}