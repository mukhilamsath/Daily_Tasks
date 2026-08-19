
When a user types `www.google.com` into a web browser and presses Enter, a series of processes take place between the user's computer, the Internet, and the web server before the webpage is displayed. This entire process is known as the **web lifecycle**.

## 1. URL Entry

The process begins when the user enters:

`www.google.com`

into the browser and presses Enter. The browser identifies the domain name and determines where the request needs to be sent.

## 2. DNS Lookup

The browser needs the IP address of the server associated with `www.google.com`. Since humans use domain names while computers communicate using IP addresses, the browser performs a **DNS (Domain Name System) lookup**.

DNS converts the domain name into an appropriate IP address.

`www.google.com → DNS → IP Address`

The browser or operating system may first check its DNS cache. If the required information is not available, a DNS lookup is performed to obtain the IP address.

## 3. Establishing a Connection

After obtaining the IP address, the browser establishes a network connection with the destination server. For traditional HTTPS communication over TCP, a TCP connection is established.

The TCP connection provides reliable communication between the client and server.

## 4. TLS Handshake

Since the website is accessed using HTTPS, secure communication is required. The browser and server perform a **TLS (Transport Layer Security) handshake**.

TLS helps provide:

* Encryption of communication
* Server authentication
* Protection against tampering

After the TLS process is completed, the browser and server can communicate securely.

## 5. HTTP Request

The browser now sends an HTTP request to the server. For example, a simplified request may look like:

`GET / HTTP/1.1`

`Host: www.google.com`

The `GET` method indicates that the browser wants to retrieve a resource from the server.

An HTTP request can contain:

* HTTP method
* URL/path
* Headers
* Request body, when required

## 6. Server Processes the Request

The request reaches the server infrastructure. The server examines the request and processes it.

Depending on the application, the server may:

* Execute backend logic
* Access a database
* Communicate with other services
* Retrieve required information
* Generate the required response

The server then prepares an HTTP response for the browser.

## 7. HTTP Response

The server sends an HTTP response back to the browser.

A simplified response may contain:

`HTTP/1.1 200 OK`

`Content-Type: text/html`

The response generally contains:

* **Status code** – indicates whether the request succeeded or failed
* **Headers** – provide additional information about the response
* **Response body** – contains the requested content or data

For example, `200 OK` indicates that the request was successfully processed.

## 8. Browser Receives the Response

The browser receives the HTTP response and begins processing the returned content.

If the response contains HTML, the browser parses the HTML to understand the structure of the webpage.

The HTML may contain references to additional resources such as:

* CSS files
* JavaScript files
* Images
* Fonts
* Other resources

## 9. Additional Requests

The browser may send additional HTTP requests to retrieve these resources.

For example:

`HTML → CSS`

`HTML → JavaScript`

`HTML → Images`

Therefore, loading a webpage usually involves multiple requests rather than a single request.

## 10. Browser Renders the Webpage

After receiving and processing the required resources, the browser combines the HTML, CSS, JavaScript, images, and other resources.

The browser's rendering process then produces the final webpage that the user sees on the screen.

## Complete Web Lifecycle

The complete simplified process can be represented as:

`User enters URL`
→ `DNS Lookup`
→ `IP Address`
→ `TCP Connection`
→ `TLS Handshake`
→ `HTTP Request`
→ `Server Processing`
→ `HTTP Response`
→ `Additional Resource Requests`
→ `Browser Rendering`
→ `Webpage Displayed`

## Conclusion

When a user enters `www.google.com` and presses Enter, the browser does much more than simply open a webpage. It first resolves the domain name through DNS, establishes a network connection, secures the communication using TLS, sends an HTTP request, and waits for the server's response. The browser then processes the returned content and any additional resources before finally rendering the webpage. This process demonstrates the fundamental **client-server communication model** used by modern web applications.
