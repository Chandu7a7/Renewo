<h1 align="center">Renewo eCommerce</h1>
<p align="center">A full-stack eCommerce web application built with Django, providing a seamless shopping experience for users and an admin dashboard for easy management of products and orders.</p>

<p align="center"> <b>Description:</b> Renewo is an innovative eCommerce platform developed to promote sustainability by facilitating the purchase and resale of recycled and upcycled products. Created as a submission for the hackathon organized by SVP Polytechnic College Bhopal, Renewo addresses the pressing issue of waste management and environmental conservation.</p>

<p align="center"> <b>Purpose:</b>  The main aim of Renewo is to allow consumers to buy and sell items made from recycled materials, such as plastic, shoes, and bottles, which would otherwise contribute to waste. By offering these products, Renewo encourages sustainable choices and supports the circular economy, where materials are continually repurposed and reused.
</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
</ul>

<h2 id="features">Features</h2>
<h3>User</h3>
<ul>
    <li>User registration and authentication (sign up, login, logout)</li>
    <li>Browse products with search and filter functionality</li>
    <li>Add products to cart and manage cart items</li>
    <li>Place orders with order summary and checkout process</li>
    <li>Track order status and view order history</li>
    <li>Profile management (view and edit profile information)</li>
</ul>

<h3>Admin</h3>
<ul>
    <li>Add, edit, and delete products</li>
    <li>Manage orders and update order status</li>
    <li>View user details and order history</li>
</ul>

<h2 id="tech-stack">Tech Stack</h2>
<ul>
    <li><strong>Backend:</strong> Django, Django Rest Framework</li>
    <li><strong>Frontend:</strong> HTML, CSS, JavaScript, Bootstrap</li>
    <li><strong>Database:</strong> SQLite (development), PostgreSQL/MySQL (production)</li>
    <li><strong>Authentication:</strong> Django’s built-in authentication system</li>
    <li><strong>Payment Integration:</strong> (Optional, e.g., cash on delevery)</li>
</ul>

<h2 id="installation">Installation</h2>

<h3>Prerequisites</h3>
<ul>
    <li>Python 3.8+</li>
    <li>Django 3.2+</li>
    <li>Optional: Virtual environment tool like <code>venv</code></li>
</ul>

<h3>Steps</h3>
<ol>
    <li><strong>Clone the Repository</strong>
        <pre><code>git clone https://github.com/Chandu7a7/renewo-ecommerce.git
cd renewo-ecommerce</code></pre>
    </li>
    <li><strong>Set up a Virtual Environment</strong>
        <pre><code>python -m venv env
source env/bin/activate      # On Windows use `env\Scripts\activate`</code></pre>
    </li>
    <li><strong>Install Dependencies</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Run Migrations</strong>
        <pre><code>python manage.py migrate</code></pre>
    </li>
    <li><strong>Create a Superuser (for admin access)</strong>
        <pre><code>python manage.py createsuperuser</code></pre>
    </li>
    <li><strong>Run the Development Server</strong>
        <pre><code>python manage.py runserver</code></pre>
    </li>
</ol>

<p>Access the site at <code>http://127.0.0.1:8000/</code> and the admin panel at <code>http://127.0.0.1:8000/admin</code>.</p>

<h2 id="usage">Usage</h2>
<h3>Adding Products</h3>
<ol>
    <li>Log in to the admin panel (<code>http://127.0.0.1:8000/admin</code>).</li>
    <li>Use the admin interface to add new products, manage orders, and update inventory.</li>
</ol>

<h3>User Functions</h3>
<ul>
    <li>Register or log in to access all features.</li>
    <li>Browse products, add them to the cart, and place orders.</li>
    <li>Check order history and track statuses.</li>
</ul>

<h2 id="project-structure">Project Structure</h2>
<pre>
renewo-ecommerce/
├── renewo/                     # Main Django project folder
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Project URLs
│   └── wsgi.py                 # WSGI for deployment
├── store/                      # Core app (e.g., for products, cart, orders)
│   ├── models.py               # Database models for the store
│   ├── views.py                # Views for handling requests
│   ├── urls.py                 # URLs specific to the store app
│   └── templates/              # HTML templates
│       └── store/              # Templates specific to store app
├── static/                     # Static files (CSS, JS)
├── media/                      # Media files (uploaded product images)
├── templates/                  # Project-wide templates
├── manage.py                   # Django management script
└── requirements.txt            # Project dependencies
</pre>

<h2 id="contributing">Contributing</h2>
<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch with a descriptive name.</li>
    <li>Make your changes and commit them.</li>
    <li>Push your changes to your branch.</li>
    <li>Open a pull request to the <code>main</code> branch.</li>
</ol>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contact</h2>
<p>For further questions, please reach out via <a href="https://github.com/Chandu7a7">GitHub</a>.</p>
