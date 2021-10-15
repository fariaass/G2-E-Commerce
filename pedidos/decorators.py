from django.shortcuts import redirect

def confere_session(func):
    def wrapper(arg, *args, **kwargs):
        if not arg.session.get('pedido', False):
            return redirect("/carrinho/")
        return func(arg, *args, **kwargs)
    return wrapper