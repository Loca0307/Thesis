
#ifdef HAL_IWDG_MODULE_ENABLED
    Watchdog::check_reset_flag();
    Watchdog::start();
#endif