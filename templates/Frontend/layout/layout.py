{% extends 'Frontend/base/portfolio-base.html' %}
    <!-- Start Home
    ===================================-->
    {% block home %}
    {% include "Frontend/partials/home.py" %}
    {% endblock home %}
    <!-- End Home ==================-->

    <!-- Start About Me
   ===================================-->
    {% block aboutme %}
    {% include "Frontend/partials/aboutme.html" %}
    {% endblock aboutme %}
    <!-- End About Me ==================-->

    <!-- Start portfolio
    ===================================-->
    {% block portfolio %}
    {% include "Frontend/partials/portfolio.html" %}
    {% endblock portfolio %}
        
    <!-- End portfolio ================-->

    <!-- Start Resume
    ===================================-->
    {% block resume %}
    {% include "Frontend/partials/resume.html" %}
    {% endblock resume %}
    <!-- End REsume ===================-->


    <!-- Start Contact
    ===================================-->
    {% block contact %}
    {% include "Frontend/partials/contact.html" %}
    {% endblock contact %}
    <!-- End Contact ==================-->

    <!-- Start Loading
    ===================================-->
    {% block loading %}
    {% include "Frontend/partials/loading.html" %}
    {% endblock loading %}
    <!-- End Loading ==================-->

<!-- start the script -->
{% block script %}
{% include "Frontend/partials/script.py" %}
{% endblock script %}
<!-- end the script -->