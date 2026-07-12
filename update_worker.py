import json
import os

html_path = "manual.html"
worker_path = "worker.js"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Properly escape the HTML content as a JS string
escaped_html = json.dumps(html_content)

js_code = f"""export default {{
  async fetch(request, env, ctx) {{
    const html = {escaped_html};
    return new Response(html, {{
      headers: {{ "content-type": "text/html;charset=UTF-8" }},
    }});
  }},
}};
"""

with open(worker_path, "w", encoding="utf-8") as f:
    f.write(js_code)
print("Successfully updated worker.js with the latest manual.html content.")
