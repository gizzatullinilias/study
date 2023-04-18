def wrap_in_p(func):
    def wrapper(text):
        return f"<p>{func(text)}</p>"
    return wrapper
@wrap_in_p
def render_input(field):
    return f'<input id="id_{field}" name="{field}">'
username = render_input('username')
print(username)
