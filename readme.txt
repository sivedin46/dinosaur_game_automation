My solution is based on the difference between background image and images of bird and cactus detecting areas.
It has no problem detecting obstacles. Day and night does not cause any problems.
However, it is not possible to smoothly adjust the timing of the reaction to obstacles as the game speed changes
with this solution. Also juöping height can not be set. As a complement to this, it is possible to adjust the jumping
and bending by checking the game speed from the Selenium related libraries. It can be solved with a small function like
 detect_Speed before each jump or bend. However, it was not possible with my laptop :). Some products are based on pixel
color, but this approach should change to the opposite color at night.
Also i used pyautogui.screenshot(region=(160, 100, 310, 1)).convert("1") mode “1” for speedy process
