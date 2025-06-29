# 7-Segment Display Counter

This Arduino project controls a **7-segment display** using **8 digital pins** to show numbers from 0 to 9 with a 1-second interval between each.

## 🔧 Hardware Used

* Arduino Uno (or compatible board)
* 7-Segment display (common cathode)
* 8 x 220-ohm resistors (one per segment)
* Jumper wires
* Breadboard

## ⚙️ Pin Configuration

Each segment of the 7-segment display is connected to one digital pin on the Arduino:

| Segment | Arduino Pin |
| ------- | ----------- |
| A       | 13          |
| B       | 12          |
| C       | 11          |
| D       | 10          |
| E       | 9           |
| F       | 8           |
| G       | 7           |
| H (DP)  | 6           |

> Note: Segment H (Decimal Point) is unused for counting.

## 🧠 Functionality

* Each number (0 to 9) is represented using specific segments lit up.
* The `loop()` function calls each number function (`zero()` to `nine()`) with a 1-second delay.
* Segment control is done using `digitalWrite()` calls.

## 🧾 Code Summary

* `setup()` initializes all pins as `OUTPUT`.
* Each digit from 0-9 has its own function (`zero()`, `one()`, ..., `nine()`) that turns on/off the required segments.
* The display loops through numbers 0-9 indefinitely.

## 📦 How to Use

1. Connect each segment pin of the 7-segment display to the corresponding Arduino digital pin using resistors.
2. Upload the `.ino` code to your Arduino board.
3. Open the Serial Monitor (optional) to confirm the board is working.
4. Watch the display count from 0 to 9 repeatedly.

## 📚 Learning Outcome

* Understand how a 7-segment display works.
* Learn pin control using `digitalWrite()`.
* Practice basic timing with `delay()`.
* Understand how to break code into functions for readability.

