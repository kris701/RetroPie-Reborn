#pragma once

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

// Pin numbers used by the dpad
const uint8_t down = 2;
const uint8_t right = 0;
const uint8_t up = 4;
const uint8_t left = 3;
const uint8_t dpadMap[] = { up, right, down, left };

// Analogs
const uint8_t axisXPlus = 2;
const uint8_t axisXMinus = 3;
const uint8_t axisYPlus = 0;
const uint8_t axisYMinus = 1;
const uint8_t analogMap[] = { axisXPlus, axisXMinus, axisYPlus, axisYMinus };
