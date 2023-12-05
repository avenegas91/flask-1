### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

>JavaScript is a front-end, client-side, scripting language that is used alongside HTML and CSS.Python is a back-end language that uses a server to have website function the way you want.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

>The dictionary can be looped over to find the necessary hidden data that we are looking for.

- What is a unit test?

>A unit test will test one "unit" of functionallity; typically one fuction or method at a time.

- What is an integration test?

>Tests that make sure components of the code work together.  An example using Flask: "Does this URL path map to a route function?"

- What is the role of web application framework, like Flask?

>Flask acts like a web framework by: responding to certain GET and POST requests. Also has tools like the Python Standard Library, except there are more use-cases and tools available.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

>Both work equally great; however, the URL query parameter is used o handle more sensetive information and can be restricted to certain users.

- How do you collect data from a URL placeholder parameter using Flask?

> Using the @app.route() to redirect you on which placeholder you want to go to. Returns the data as a string.

- How do you collect data from the query string using Flask?

> Using the request.args in Flask and submitting a POST request.

- How do you collect data from the body of the request using Flask?

> Using the request.form and submitting a POST request.

- What is a cookie and what kinds of things are they commonly used for?

> Cookies are ways to store small bits of data on the client side (browser).  Example: Items remaing in the cart after leaving a website.

- What is the session object in Flask?

> Sessions contain info in the current browser and are "signed" so users are unable to modify the data.

- What does Flask's `jsonify()` do?

> The jsonify() object returns an object response.  Flask will parse data as JSON from an API.