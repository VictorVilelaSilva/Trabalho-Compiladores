1. Download RabbitMQ Installer: Go to the official RabbitMQ website (www.rabbitmq.com) and download the Windows installer suitable for your system architecture (32-bit or 64-bit).

2. Run Installer: Once the installer is downloaded, double-click on it to run the installation wizard.

3. Install RabbitMQ: Follow the installation wizard steps to install RabbitMQ on your Windows 11 system. You can choose the installation directory and other configurations during the process.

3.1 rabbitmq-plugins enable rabbitmq_management


4. Start RabbitMQ Service: After the installation is complete, open the Windows Services Manager by searching for "Services" in the Start menu. Find the "RabbitMQ" service in the list, right-click on it, and select "Start" to start the RabbitMQ service.

5. Access RabbitMQ Management Interface: Open your web browser and go to http://localhost:15672/. This will take you to the RabbitMQ Management Interface.

6. Log in: Log in to the RabbitMQ Management Interface using the default credentials (username: "guest" and password: "guest"). It is essential to change the default password for security reasons.

7. Create Queues and Exchanges: In the RabbitMQ Management Interface, you can create queues, exchanges, and bindings to facilitate communication between applications.


user: guest
password: guest