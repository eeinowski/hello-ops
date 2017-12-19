import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings</title>
            </head>
            <body>
                <h1>Greetings</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)