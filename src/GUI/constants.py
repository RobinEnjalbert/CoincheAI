RES_WIDTH = 1280
RES_HEIGHT = 720
SCREEN_RES = (RES_WIDTH, RES_HEIGHT)
CARD_WIDTH = RES_WIDTH // 12
CARD_HEIGHT = RES_WIDTH // 8
CARD_SIZE = (CARD_WIDTH, CARD_HEIGHT)
FPS = 30

SERVER = ("localhost", 6804)
RECV_BUFF_SIZE = 512

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WHITE = (255, 255, 255)
LIGHTGREY = (191, 191, 191)
GREY = (127, 127, 127)
DARKGREY = (63, 63, 63)
BLACK = (0, 0, 0)

CARD_VALUES = ('7', '8', '9', '10', 'J', 'Q', 'K', 'A')
CARD_COLORS = ('C', 'D', 'S', 'H')

margin = 10
CARD_POSITIONS = {0: {'pair': ((10*i, 0 + margin) for i in range(8)),
                      'impair': ()},
                  1: {'pair': ((10*i, 50 + margin) for i in range(8)),
                      'impair': ()},
                  2: {'pair': ((10*i, 100 + margin) for i in range(8)),
                      'impair': ()},
                  3: {'pair': ((10*i, 150 + margin) for i in range(8)),
                      'impair': ()}}
