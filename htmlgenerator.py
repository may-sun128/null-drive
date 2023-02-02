import jinja2
import os

class HTMLGenerator:
    def __init__(self):
        self.jinja_html: str = """
        <html>
            <head>
                <title>{{ Test }}</title>
                <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
                <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-colors-flat.css">
            </head>
            <body>
                {# Banner #}
                <div class="w3-container w3-flat-midnight-blue">
                    <h2>Null Drive</h2>
                    <p>Support Local.</p>
                </div>
                {# Populate with directory contents#}
                {% for item in items %}
                    <div class="w3-container">
                        {# Images #}
                        {% if item.endswith('.jpg') or item.endswith('.jpeg') or item.endswith('.png') %}
                        <h2>{{ item }}</h2>
                        <div class="w3-card-4" style="width:50%">
                            <img src="{{ item }}" style="width:100%">
                            <div class="w3-container w3-center">
                                <p>{{ item }}</p>
                            </div>
                        </div>
                        {% endif %}
                    </div>
                {% endfor %}
            </body>
        </html>"""
        self.jin_env = jinja2.Environment()
        self.template = self.jin_env.from_string(self.jinja_html)

    def render_output(self, path: str) -> str:
        files = os.listdir(path)
        output = self.template.render(items=files)
        return output