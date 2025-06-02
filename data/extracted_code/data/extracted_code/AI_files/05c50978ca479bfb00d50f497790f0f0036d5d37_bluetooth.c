void main() {

    TRISD = 0x00; // Output for motors
    TRISC = 0b10000000; // RC7 input (RX), RC6 output (TX)
    UART1_Init(9600);
    Delay_ms(100);

    while (1) {
        if (UART1_Data_Ready()) {
            data0 = UART1_Read();

            switch (data0) {
            case 'F':
                forward();
                break;
            case 'B':
                backward();
                break;
            case 'L':
                left();
                break;
            case 'R':
                right();
                break;
            case 'S':
                stop();
                break;
            case 'O':
                servo_pulse(0);
                break; // 0°
            case 'H':
                servo_pulse(1000);
                break; // 90°
            case 'Z':
                servo_pulse(2000);
                break; // 180°
            }
        }
    }
}