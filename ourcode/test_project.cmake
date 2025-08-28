add_executable(
  test_project
  test_project.cpp
)

# Pull in pico libraries that we need
target_link_libraries(test_project pico_stdlib hardware_spi hardware_pwm hardware_dma rgbled button pico_display_2 st7789 pico_graphics)

# create map/bin/hex file etc.
pico_add_extra_outputs(test_project)
