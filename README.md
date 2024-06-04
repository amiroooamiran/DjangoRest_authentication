<h1>Authentication Project <img src="https://img.shields.io/badge/License-GNU%20v3-blue.svg"> </h1>

<p align="center">Welcome to the Authentication project! This <b>Django REST Framework </b> project offers a comprehensive set of features for user authentication, user profiles, and security measures. It empowers users to handle account creation, email verification, signin, password reset, and manage their profiles efficiently. Moreover, the project integrates various security options to ensure data integrity and user authentication.</p>

<p align="center">
    <img src="https://img.shields.io/badge/Django-v5.0.4-blue.svg?logo=django&logoColor=white">
    <img src="https://img.shields.io/badge/Python-v3.11.8-blue.svg?logo=python&logoColor=white">
    <a href="#Contribution" title="Contributions are welcome"><img src="https://img.shields.io/badge/contributions-welcome-green.svg"></a>
</p>

<h2>Features</h2>

<h3>Authentication</h3>
<ul>
  <li><strong>Signup</strong>: Enables users to register new accounts securely. ✅</li>
  <li><strong>Email Verification</strong>: Verifies the authenticity of user emails to enhance security. ✅</li>
  <li><strong>Signin</strong>: Provides a secure login mechanism for registered users. ✅</li>
  <li><strong>Password Reset</strong>: Offers a secure process for users to reset their passwords. ✅</li>
  <li><strong>Social Media Authentication</strong>: Allows users to authenticate using their social media accounts.</li>
</ul>

<h3>User Profile</h3>
<ul>
  <li><strong>Profile Image</strong>: Allows users to upload and update their profile images effortlessly. ✅</li>
  <li><strong>Bio</strong>: Enables users to add, modify, or delete their biography information. ✅</li>
  <li><strong>Username</strong>: Provides the flexibility for users to change their usernames as needed. ✅</li>
  <li><strong>Remove Full Account</strong>: Users can remove all their data from the database from their account.</li>
</ul>

<h3>Security Options</h3>
<ul>
  <li><strong>Attribute-based Authorization</strong>: Controls access to resources based on user attributes. ✅</li>
  <li><strong>Django-cryptography</strong>: Utilizes cryptographic functionalities to ensure data security.</li>
  <li><strong>Django-honeypot</strong>: Implements honeypot techniques for threat detection and mitigation.</li>
  <li><strong>Input Validation and Output Encoding</strong>: Protects against common web vulnerabilities by validating user inputs and encoding outputs securely.</li>
  <li><strong>Multi-factor Authentication</strong>: Enhances security by requiring users to authenticate through multiple methods.</li>
</ul>

<h2>Startup project</h2>

<h3>Config DataBase</h3>

<p>Before starting the project, ensure PostgreSQL is installed on your system. You can follow the instructions below to set up PostgreSQL and create a database:</p>

<h4>For Linux:</h4>

<p><b>Install PostgreSQL: <img src="https://img.shields.io/badge/PostgreSQL-v16.3-blue.svg?logo=postgresql&logoColor=white" alt="PostgreSQL Badge"></b></p>

<span>Arch Linux:</span>

```
sudo pacman -S postgresql
```
<span>Debian Linux:</span>

```
sudo apt-get install postgresql
```
<p>Start and enable PostgreSQL:</p>
<pre><code>sudo systemctl start postgresql
sudo systemctl enable postgresql
</code></pre>

<h4>Create Database User and Password</h4>

<p>To create a database user and password in PostgreSQL, follow these steps:</p>

<ol>
  <li><strong>Log in to the PostgreSQL database server with the <code>postgres</code> user:</strong></li>
  <pre><code>sudo -u postgres psql</code></pre>

  <li><strong>Create a new database user with a password. Replace <code>&lt;username&gt;</code> with the desired username and <code>&lt;password&gt;</code> with the desired password:</strong></li>
  <pre><code>CREATE USER &lt;username&gt; WITH PASSWORD '&lt;password&gt;';</code></pre>

  <li><strong>Grant the user privileges on the database. Replace <code>&lt;database&gt;</code> with the name of your database and <code>&lt;username&gt;</code> with the username you just created:</strong></li>
  <pre><code>GRANT ALL PRIVILEGES ON DATABASE &lt;database&gt; TO &lt;username&gt;;</code></pre>

  <li><strong>Exit the PostgreSQL prompt:</strong></li>
  <pre><code>\q</code></pre>
</ol>

<p>Here's an example:</p>

<pre><code>sudo -u postgres psql
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE authenticat TO myuser;
\q
</code></pre>

<p>Replace <code>myuser</code> with your desired username and <code>mypassword</code> with your desired password. Also, replace <code>authenticat</code> with the name of your database.</p>


<h4>For Windows:</h4>
<p>You can download and install PostgreSQL from the official website: <a href="https://www.postgresql.org/download/windows/">PostgreSQL Official Website</a>.</p>

<h2><strong>Install Kafka: <img src="https://img.shields.io/badge/Apache%20Kafka-v3.7.0-red.svg?logo=apache-kafka&logoColor=white" alt="Apache Kafka Badge">
</strong></h2>
<p>Before installing Kafka on your Linux system, you need to install Java, specifically JDK. You can use the following commands to install JDK on your Linux distribution:</p>
<p><span>For Arch Linux:</span></p>
<pre><code>sudo pacman -S jdk-openjdk
</code></pre>
<p><span>For Debian Linux:</span></p>
<pre><code>sudo apt install openjdk-17-jdk
</code></pre>
<p>After installing Java, you can verify the installation by running:</p>
<pre><code>java --version
</code></pre>
<p>In the next step, you should install Kafka. You can download your desired version from <a href="https://kafka.apache.org/downloads">this link</a> and then configure it for your project:</p>
<p><strong>Extract:</strong></p>
<pre><code>tar -xzf kafka_2.13–3.5.0.tgz
cd kafka_2.13–3.5.0
</code></pre>
<p><strong>Start:</strong></p>
<ul>
<li>Generate a Cluster UUID:
<pre><code>KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
</code></pre>
</li>
<li>Format Log Directories:
<pre><code>bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
</code></pre>
</li>
<li>Start the Kafka Server:
<pre><code>bin/kafka-server-start.sh config/kraft/server.properties
</code></pre>
</li>
<li>Create a topic:
<pre><code>bin/kafka-console-consumer.sh --topic topic_user_created --bootstrap-server localhost:9092 --from-beginning
</code></pre>
</li>
</ul>

<h3>Config Email App Password</h3>

<p>To configure the email app password, please follow the instructions provided by Google at the following link: <a href="https://support.google.com/mail/answer/185833?hl=en">Google Support</a>.</p>

<h3>Migrations and Run Server</h3>

<p>After configuring the database and email app password, you can proceed with migrations and running the server:</p>

<p>Run migrations:</p>
<pre><code>python manage.py makemigrations
python manage.py migrate
</code></pre>

<p>Run the server:</p>
<pre><code>python manage.py runserver
</code></pre>


<h2>Docker Support</h2>

<p>The project includes a Dockerfile, facilitating the deployment of the application within Docker containers. This simplifies the deployment process and ensures consistent behavior across various environments.</p>

<h3>Run</h3>
<p>Before running the application with Docker, ensure that Docker and docker-compose are installed on your system. If not, you can install them by following the <a href="https://docs.docker.com/manuals/">official documentation</a>.</p>

<p>To start Docker, use the following commands:</p>

```
sudo systemctl start docker
sudo systemctl enable docker
```
<p>after install Docker and Run docker on your ststem, move in project directory and up docker-compose file:</p>

```
sudo docker-compose up
```
<h2>How to Connect to Frontend:</h2>
<p>To connect to the frontend, you can follow these steps:</p>

<ol>
  <li><strong>Clone the Frontend Repository:</strong></li>
  <p>You can clone the frontend from the <a href="https://github.com/amiroooamiran/Vue.js_authentication">Vue.js_authentication</a> repository.</p>

  <li><strong>Guidance for Setting Up the Frontend:</strong></li>
  <p>Refer to the instructions provided in the frontend repository to set up and configure the frontend application.</p>

  <li><strong>Startup Project:</strong></li>
  <p>Once the frontend is set up and configured, you can integrate it with the backend authentication project and start both projects simultaneously.</p>
</ol>


<h2>Thank You!</h2>

<p>Thank you for choosing the Authentication project! Should you have any inquiries or require further assistance, please do not hesitate to contact us. We're committed to providing support and ensuring your experience with our project is smooth and successful.</p>
