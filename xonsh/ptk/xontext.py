from prompt_toolkit.filters import Filter, IsMultiline, HasFocus, IsDone
from prompt_toolkit.layout.controls import BufferControl
from prompt_toolkit.layout.lexers import SimpleLexer
from prompt_toolkit.buffer import Buffer, AcceptAction
from prompt_toolkit.token import Token
from prompt_toolkit.layout.processors import BeforeInput
from prompt_toolkit.layout.containers import ConditionalContainer, Window
from prompt_toolkit.layout.screen import Char
from prompt_toolkit.layout.dimension import LayoutDimension

XONTEXT_BUFFER = Buffer(accept_action=AcceptAction.IGNORE)
has_xontext = HasFocus('XONTEXT_BUFFER')

class XontextToolbarControl(BufferControl):
    def __init__(self):
        token = Token.Toolbar.System

        super(XontextToolbarControl, self).__init__(
            buffer_name='XONTEXT_BUFFER',
            default_char=Char(token=token),
            lexer=SimpleLexer(default_token=token.Text),
            input_processors=[BeforeInput.static('Xontext: ', token)],)


class XontextToolbar(ConditionalContainer):
    def __init__(self):
        super(XontextToolbar, self).__init__(
            content=Window(
                XontextToolbarControl(),
                height=LayoutDimension.exact(1)),
            filter=HasFocus('XONTEXT_BUFFER') & ~IsDone())


