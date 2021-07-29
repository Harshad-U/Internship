from pydispatch import Dispatcher


class MyEmitter(Dispatcher):
    # Events are defined in classes and subclasses with the '_events_' attribute
    _events_ = ['on_state', 'new_data']

    def do_some_stuff(self, data=None):
        # do stuff that makes new data
        self.get_some_data()
        # Then emit the change with optional positional and keyword arguments
        self.emit('new_data', data=data)

    def get_some_data(self):
        pass


# An observer - could inherit from Dispatcher or any other class
def on_emitter_state():
    print('emitter state changed')


def on_new_data(**kwargs):
    data = kwargs.get('data')
    print('I got data: {}'.format(data))


class MyListener(object):
    pass


emitter = MyEmitter()
listener = MyListener()

emitter.bind(on_state=on_emitter_state)
emitter.bind(new_data=on_new_data)

emitter.do_some_stuff()
# >>> I got data: ...

emitter.emit('on_state')
# >>> emitter state changed
