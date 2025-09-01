include(test_project.cmake)

target_link_libraries(test_project pico_stdlib)

pico_enable_stdio_usb(test_project 1)
pico_enable_stdio_uart(test_project 0)


