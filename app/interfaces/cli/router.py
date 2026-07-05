from app.interfaces.cli.screens import (
    main_screen,
    vfd_main_screen,
    ab_menu_screen,
    ab_pf525_screen,
    ab_pf40_screen,
    ab_pf753_screen,
    ab_pf160_screen,
    spare_parts_screen,
    search_spare_parts_bm_screen,
)


SCREENS = {
    "main": main_screen,
    "vfd_main": vfd_main_screen,
    "ab_menu": ab_menu_screen,

    "ab_pf525_menu": ab_pf525_screen,
    "ab_pf40_menu": ab_pf40_screen,
    "ab_pf753_menu": ab_pf753_screen,
    "ab_pf160_menu": ab_pf160_screen,

    "spare_parts_menu": spare_parts_screen,
    "search_spare_parts_bm": search_spare_parts_bm_screen,
}