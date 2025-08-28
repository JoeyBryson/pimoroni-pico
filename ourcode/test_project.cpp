#include <string.h>
#include <math.h>
#include <vector>
#include <cstdlib>

#include "libraries/pico_display_2/pico_display_2.hpp"
#include "drivers/st7789/st7789.hpp"
#include "libraries/pico_graphics/pico_graphics.hpp"
#include "rgbled.hpp"
#include "button.hpp"

using namespace pimoroni;

ST7789 st7789(320, 240, ROTATE_0, false, get_spi_pins(BG_SPI_FRONT));
PicoGraphics_PenRGB332 graphics(st7789.width, st7789.height, nullptr);

RGBLED led(PicoDisplay2::LED_R, PicoDisplay2::LED_G, PicoDisplay2::LED_B);

int main() {
  st7789.set_backlight(255);
  uint8_t *fb = static_cast<uint8_t*>(graphics.frame_buffer);
  while(true) {
    for(size_t x = 0; x < 320; x++)
    {
      for(size_t y = 0; y < 240; y++)
      {
        size_t index = y * graphics.bounds.w + x;
        fb[index] = 0b11110011;
      }
    }
    st7789.update(&graphics);
  }

    return 0;
}
